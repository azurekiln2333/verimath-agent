"""上下文管理：滚动摘要 + token 预算截断的单元测试。

覆盖 sessions.estimate_tokens / set_summary / pop_oldest_turns / append_turn 软硬上限，
以及 main._history_as_messages 的 summary 首条 + token 截断、maybe_summarize_context 旁路压缩。
模仿 test_context.py 的风格：用 main.sessions 全局 + monkeypatch 隔离临时 SessionStore。
"""
from __future__ import annotations

import asyncio

from app import main
from app.main import _fire_and_forget_summary, _history_as_messages, maybe_summarize_context
from app.sessions import SessionStore, estimate_tokens


# ---- estimate_tokens ----

def test_estimate_tokens_empty_and_monotonic():
    assert estimate_tokens("") == 0
    assert estimate_tokens("abc") >= 1
    # 中文每字 3 字节 ×0.4 ≈ 1.2 token，必然 >0
    assert estimate_tokens("统") > 0
    assert estimate_tokens("统计学习") > estimate_tokens("统计")


# ---- sessions: summary 持久化 ----

def test_summary_persists_across_store_instances(tmp_path):
    store = SessionStore(max_history_turns=4, db_path=tmp_path / "s.db")
    store.set_summary("s1", "学生问过正态分布")
    # 新实例从同一 DB 加载，验证 summary 落库
    store2 = SessionStore(max_history_turns=4, db_path=tmp_path / "s.db")
    state = store2.get_or_create("s1")
    assert state.summary == "学生问过正态分布"


# ---- sessions: pop_oldest_turns ----

def test_pop_oldest_turns_removes_head_and_syncs_db(tmp_path):
    db = tmp_path / "p.db"
    store = SessionStore(max_history_turns=4, db_path=db)
    store.append_turn("p1", "user", "Q1")
    store.append_turn("p1", "assistant", "A1")
    store.append_turn("p1", "user", "Q2")
    popped = store.pop_oldest_turns("p1", 2)
    assert [t["content"] for t in popped] == ["Q1", "A1"]
    state = store.get_or_create("p1")
    assert [t["content"] for t in state.history] == ["Q2"]
    # DB 同步：新实例加载，被 pop 的不复活
    store2 = SessionStore(max_history_turns=4, db_path=db)
    state2 = store2.get_or_create("p1")
    assert [t["content"] for t in state2.history] == ["Q2"]


def test_pop_oldest_turns_zero_count_noop(tmp_path):
    store = SessionStore(max_history_turns=4, db_path=tmp_path / "z.db")
    store.append_turn("z1", "user", "Q1")
    assert store.pop_oldest_turns("z1", 0) == []
    assert len(store.get_or_create("z1").history) == 1


# ---- sessions: append_turn 软硬上限 ----

def test_append_turn_keeps_below_hard_cap(tmp_path):
    # max_history_turns=1 → 软上限2、硬上限4。append 5 条应截断到 4
    store = SessionStore(max_history_turns=1, db_path=tmp_path / "h.db")
    for i in range(5):
        store.append_turn("h1", "user", f"Q{i}")
    state = store.get_or_create("h1")
    assert len(state.history) == 4
    assert state.history[0]["content"] == "Q1"  # Q0 被硬上限丢弃


def test_append_turn_under_soft_cap_not_dropped(tmp_path):
    # max_history_turns=2 → 软上限4、硬上限8。append 3 条 < 软上限，不立即丢
    store = SessionStore(max_history_turns=2, db_path=tmp_path / "soft.db")
    for i in range(3):
        store.append_turn("soft1", "user", f"Q{i}")
    state = store.get_or_create("soft1")
    assert len(state.history) == 3  # 软上限内不立即压缩，留给 maybe_summarize


# ---- main: _history_as_messages summary 首条 + token 截断 ----

def test_history_as_messages_prepends_summary():
    main.sessions.clear_context("sum-head")
    main.sessions.set_summary("sum-head", "学生之前问过假设检验")
    main.sessions.append_turn("sum-head", "user", "新问题")
    msgs = _history_as_messages("sum-head")
    assert msgs[0].role == "system"
    assert "假设检验" in msgs[0].content
    assert [m.role for m in msgs[1:]] == ["user"]


def test_history_as_messages_truncates_old_turns_by_budget(monkeypatch):
    main.sessions.clear_context("trunc")
    main.sessions.append_turn("trunc", "user", "旧问题")
    main.sessions.append_turn("trunc", "assistant", "旧回答")
    main.sessions.append_turn("trunc", "user", "新问题")
    # 每条 3000 token，budget=4000：只容得下最近 1 条
    monkeypatch.setattr(main, "estimate_tokens", lambda _t: 3000)
    msgs = _history_as_messages("trunc")
    assert len(msgs) == 1
    assert msgs[0].content == "新问题"


def test_history_as_messages_keeps_summary_even_when_budget_tight(monkeypatch):
    main.sessions.clear_context("sum-tight")
    main.sessions.set_summary("sum-tight", "已压缩的旧摘要")
    main.sessions.append_turn("sum-tight", "user", "新问题")
    # summary 本身就超预算，但 summary 必须保留；history 全部被截断
    monkeypatch.setattr(main, "estimate_tokens", lambda _t: 99999)
    msgs = _history_as_messages("sum-tight")
    assert len(msgs) == 1
    assert msgs[0].role == "system"
    assert "旧摘要" in msgs[0].content


# ---- main: maybe_summarize_context 旁路压缩 ----

class _FakeModelClient:
    def __init__(self, *, enabled: bool = True, reply: str = "压缩摘要文本"):
        self.enabled = enabled
        self._reply = reply
        self.calls = 0

    async def complete(self, messages, response_format=None):
        self.calls += 1
        return self._reply


def test_maybe_summarize_context_compresses_old_turns(monkeypatch, tmp_path):
    store = SessionStore(max_history_turns=1, db_path=tmp_path / "m.db")
    monkeypatch.setattr(main, "sessions", store)
    fake = _FakeModelClient(reply="学生问过正态分布的均值")
    monkeypatch.setattr(main, "model_client", fake)
    # 软上限2，硬上限4。append 3 条 → 超 soft_cap(2)，最旧 1 条待摘要
    store.append_turn("m1", "user", "旧问题")
    store.append_turn("m1", "assistant", "旧回答")
    store.append_turn("m1", "user", "新问题")
    asyncio.run(maybe_summarize_context("m1"))
    state = store.get_or_create("m1")
    assert fake.calls == 1
    assert state.summary == "学生问过正态分布的均值"
    # 旧轮次被 pop，只剩最近 soft_cap=2 条
    assert [t["content"] for t in state.history] == ["旧回答", "新问题"]


def test_maybe_summarize_context_noop_when_model_disabled(monkeypatch, tmp_path):
    store = SessionStore(max_history_turns=1, db_path=tmp_path / "d.db")
    monkeypatch.setattr(main, "sessions", store)

    class _Disabled:
        enabled = False

        async def complete(self, *a, **k):  # pragma: no cover - 不应被调用
            raise AssertionError("model disabled, complete 不应被调用")

    monkeypatch.setattr(main, "model_client", _Disabled())
    for c in ("x", "y", "z"):
        store.append_turn("d1", "user", c)
    asyncio.run(maybe_summarize_context("d1"))
    state = store.get_or_create("d1")
    assert state.summary == ""
    assert len(state.history) == 3  # 未压缩


def test_maybe_summarize_context_noop_under_soft_cap(monkeypatch, tmp_path):
    store = SessionStore(max_history_turns=2, db_path=tmp_path / "u.db")
    monkeypatch.setattr(main, "sessions", store)
    fake = _FakeModelClient()
    monkeypatch.setattr(main, "model_client", fake)
    # 软上限4，append 2 条 < 软上限，不触发摘要
    store.append_turn("u1", "user", "Q1")
    store.append_turn("u1", "assistant", "A1")
    asyncio.run(maybe_summarize_context("u1"))
    assert fake.calls == 0
    assert store.get_or_create("u1").summary == ""


def test_fire_and_forget_summary_safe_without_event_loop():
    # 同步上下文（无运行中的事件循环）下不应抛异常
    _fire_and_forget_summary("no-such-session")
