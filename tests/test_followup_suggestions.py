"""Async, model-authored recommendations belong to the answer that requested them."""
import asyncio
import json
from types import SimpleNamespace
from unittest.mock import AsyncMock

import pytest

from app.artifact_jobs import ArtifactService, _answer_anchors, _followups, _reviewed_followups
from app.panel_store import PanelStore


def seed(store, sid="one", task="first"):
    mid = store.begin_turn(sid, task, "圆的切线和积分怎么求？", {"route": "concept"})
    store.finish_turn(mid, "切线为 x=1，积分为3π/2。", "completed", {"route": "concept", "sources": ["keep"]})
    return mid


def proposal(label="为什么梯度给出法向方向？", query="本题P处的梯度(2,0)为什么垂直于切线？", **changes):
    return {"label": label, "query": query, "anchor_id": "a1", "target": "梯度与法向量",
            "kind": "bridge", "reason": "回答给出了切线结果，但没有解释梯度与切线方向的连接。",
            "priority": 3, "already_answered": False, **changes}


def test_recommendations_are_background_persisted_and_preserve_existing_canvas(tmp_path):
    store = PanelStore(tmp_path / "panel.sqlite")

    async def run():
        gate = asyncio.Event()
        calls = []
        async def complete(messages, **kwargs):
            calls.extend(messages)
            await gate.wait()
            if "候选问题" in json.loads(messages[-1].content):
                assert "thinking" not in kwargs  # Respect the configured reasoning setting for review.
                payload = json.loads(messages[-1].content)
                assert "本轮回答片段" not in payload
                assert "本轮完整回答" in payload
                assert "priority" not in payload["候选问题"][0]
                assert "anchor_id" not in payload["候选问题"][0]
                return json.dumps({"decisions": [{"id": "q1", "action": "keep", "priority": 3,
                                                  "reason": "梯度到切线方向的关键依据没有解释。"}]})
            return json.dumps({"suitable": False, "followups": [
                proposal(label="梯度为什么垂直切线？")]})
        service = ArtifactService(store, SimpleNamespace(enabled=True, complete=complete))
        mid = seed(store)
        offer = store.add_offer("one", mid, {"tier": "canvas", "title": "圆与梯度"})
        service.discover("one", mid)
        assert store.message("one", mid)["visualization_state"] == "ready"
        assert store.artifact_state("one")["suggestions_checking"] == [mid]
        next_mid = seed(store, task="next")
        gate.set()
        await asyncio.gather(*service.discoveries.values())
        restored = PanelStore(store.path).message("one", mid)
        assert restored["followups"][0]["label"] == "梯度为什么垂直切线？"
        assert restored["sources"] == ["keep"] and restored["followups_state"] == "completed"
        assert restored["followups_version"] == 2
        assert restored["followups_reviewed"] is True
        assert restored["followups"][0]["anchor"] == "切线为 x=1，积分为3π/2。"
        assert not store.message("one", next_mid).get("followups")
        assert store.offers("one") == [offer]
        assert not store.artifact_state("one")["pending"]
        assert not store.artifact_state("other")["suggestions"]
        assert "圆的切线和积分" in calls[-1].content
        await service.stop()
    asyncio.run(run())


@pytest.mark.parametrize("raw", ["[]", "not json", '{"followups":null,"suitable":false}'])
def test_invalid_recommendations_never_leave_infinite_polling(tmp_path, raw):
    store = PanelStore(tmp_path / "panel.sqlite")
    async def run():
        mid = seed(store)
        service = ArtifactService(store, SimpleNamespace(enabled=True, complete=AsyncMock(return_value=raw)))
        service.discover("one", mid)
        await asyncio.gather(*service.discoveries.values())
        assert not store.artifact_state("one")["pending"]
        assert not store.message("one", mid).get("followups")
        await service.stop()
    asyncio.run(run())


def test_restart_clears_pending_recommendations_without_erasing_metadata(tmp_path):
    store = PanelStore(tmp_path / "panel.sqlite")
    mid = seed(store)
    store.patch_metadata("one", mid, {"followups_state": "checking"})
    store.recover()
    assert store.message("one", mid)["followups_state"] == "interrupted"
    assert store.message("one", mid)["sources"] == ["keep"]
    assert not store.artifact_state("one")["pending"]


def test_recommendation_parsing_is_bounded_and_deduplicated():
    items = _followups([None, {}, {"label": 1, "query": "x"}, {"label": "A", "query": "a"},
        {"label": "B", "query": "a"}, {"label": "A", "query": "b"},
        {"label": "<img src=x onerror=alert(1)>", "query": "safe text"},
        *({"label": str(i), "query": str(i)} for i in range(10))])
    assert len(items) == 4 and items[0] == {"label": "A", "query": "a"}
    assert items[1]["label"].startswith("<img")  # Displayed with textContent, not interpreted as HTML.


def test_critical_questions_are_grounded_ranked_and_deduplicate_the_same_gap():
    answer = "切线为 x=1，积分为3π/2。"
    candidates = [
        proposal(label="可以推广到几维？", query="能推广到任意维吗？", priority=1),
        proposal(label="为什么积分是这个值？", query="积分怎么检验？",
                 target="积分结果检验", kind="check", priority=2),
        proposal(),
        proposal(label="梯度与切线是什么关系？", query="为什么梯度与切线垂直？"),
    ]
    selected = _followups(candidates, answer=answer)
    assert [item["target"] for item in selected] == ["梯度与法向量", "积分结果检验"]
    assert [item["priority"] for item in selected] == [3, 2]


@pytest.mark.parametrize("changes", [
    {"anchor_id": "a999"}, {"anchor_id": ""}, {"anchor_id": 12},
    {"already_answered": True}, {"already_answered": "false"},
    {"priority": 1}, {"priority": True}, {"priority": "3"},
    {"kind": "unrelated"}, {"kind": []}, {"target": ""}, {"target": {}},
    {"reason": ""}, {"reason": None}, {"query": "过长的问题" * 200},
])
def test_unsubstantiated_answered_or_malformed_candidates_are_not_recommended(changes):
    assert _followups([proposal(**changes)], answer="切线为 x=1。") == []


def test_exact_earlier_questions_are_not_recommended_again():
    question = "本题P处的梯度(2,0)为什么垂直于切线？"
    assert _followups([proposal()], answer="切线为 x=1。", asked=[question.replace("？", "?")]) == []


def test_math_anchors_preserve_original_notation_instead_of_model_transcriptions():
    answer = "梯度为 \\(\\nabla F(P)=(2,0)\\)。\n故切线是 \\(x=1\\)。"
    anchors = _answer_anchors(answer)
    assert anchors == {"a1": "梯度为 \\(\\nabla F(P)=(2,0)\\)。", "a2": "故切线是 \\(x=1\\)。"}
    selected = _followups([proposal(anchor_id="a2")], answer=answer)
    assert selected[0]["anchor"] == anchors["a2"]


def test_independent_review_drops_repeats_and_revises_misleading_wording():
    candidates = _followups([proposal(), proposal(label="是不是圆上任意点？", query="为什么圆上点都满足？",
                                                 target="测试点的取值范围", priority=2)], answer="切线为 x=1。")
    result = {"decisions": [
        {"id": "q1", "action": "drop", "priority": 1, "reason": "前面已解释法向与切向关系。"},
        {"id": "q2", "action": "revise", "priority": 3, "label": "Q一定要在圆上吗？",
         "query": "切线方程中的测试点Q一定要在圆上吗？", "reason": "需澄清任意测试点与圆上点的区别。"},
        {"id": "q999", "action": "keep", "priority": 3, "reason": "不存在的候选不能进入显示。"},
    ]}
    selected = _reviewed_followups(candidates, result, answer="切线为 x=1。", asked=[])
    assert [item["label"] for item in selected] == ["Q一定要在圆上吗？"]
    assert selected[0]["target"] == "测试点的取值范围"


@pytest.mark.parametrize("replacement_names", [False, True])
def test_model_review_replacement_field_variants_are_normalized(replacement_names):
    candidate = _followups([proposal()], answer="切线为 x=1。")
    prefix = "new_" if replacement_names else ""
    decision = {"id": "q1", "action": "revise", "priority": 3,
                prefix + "label": "梯度为何给出法向？", prefix + "query": "梯度为何是切线的法向量？",
                prefix + "reason": "尚未解释梯度与切线方向的几何联系。"}
    selected = _reviewed_followups(candidate, {"decisions": [decision]}, answer="切线为 x=1。", asked=[])
    assert selected[0]["label"] == "梯度为何给出法向？"
    assert selected[0]["query"] == "梯度为何是切线的法向量？"


@pytest.mark.parametrize("result", [None, [], {}, {"decisions": None}])
def test_missing_review_never_silently_passes_unreviewed_drafts(result):
    with pytest.raises(ValueError):
        _reviewed_followups([proposal()], result, answer="切线为 x=1。", asked=[])


def test_internal_reference_ids_do_not_leak_but_real_variable_names_are_preserved():
    candidate = _followups([proposal()], answer="切线为 x=1。")
    decision = {"id": "q1", "action": "revise", "priority": 3,
                "label": "这一步为什么？", "query": "a5说的这一步为什么？", "reason": "这一步缺少法向与切线的联系。"}
    assert _reviewed_followups(candidate, {"decisions": [decision]}, answer="切线为 x=1。", asked=[]) == []
    decision["query"] = "数列首项a1为什么是1？"
    selected = _reviewed_followups(candidate, {"decisions": [decision]}, answer="切线为 x=1。", asked=["数列a1=1"])
    assert selected[0]["query"] == decision["query"]


def test_review_failure_preserves_canvas_and_stops_polling(tmp_path):
    store = PanelStore(tmp_path / "panel.sqlite")
    async def run():
        mid = seed(store)
        client = SimpleNamespace(enabled=True, complete=AsyncMock(side_effect=[
            json.dumps({"suitable": True, "title": "梯度与切线", "followups": [proposal()]}),
            TimeoutError("review timed out"),
        ]))
        service = ArtifactService(store, client)
        service.discover("one", mid)
        await asyncio.gather(*service.discoveries.values())
        assert store.message("one", mid)["followups_state"] == "failed"
        assert not store.message("one", mid).get("followups")
        assert store.offers("one")[0]["title"] == "梯度与切线"
        assert client.complete.await_count == 2
        assert not store.artifact_state("one")["pending"]
        await service.stop()
    asyncio.run(run())


def test_context_keeps_opening_problem_without_other_sessions_or_future_turns(tmp_path):
    store = PanelStore(tmp_path / "panel.sqlite")
    first = store.begin_turn("one", "original", "原题给出了区域D与点P", {})
    store.finish_turn(first, "最初解答", "completed", {})
    for index in range(7):
        mid = store.begin_turn("one", f"question-{index}", f"第{index}个追问", {})
        store.finish_turn(mid, f"第{index}个解释", "completed", {})
    unrelated = store.begin_turn("other", "unrelated", "另一会话的私密问题", {})
    store.finish_turn(unrelated, "不要读取", "completed", {})
    store.begin_turn("one", "future", "后来的新问题", {})
    context = store.recommendation_context("one", mid)
    assert context["opening_question"] == "原题给出了区域D与点P"
    assert len(context["recent"]) == 8
    assert context["recent"][-1]["content"] == "第6个追问"
    assert "另一会话" not in json.dumps(context, ensure_ascii=False)
    assert "后来的新问题" not in json.dumps(context, ensure_ascii=False)
    assert store.recommendation_context("other", mid) == {"opening_question": "", "recent": []}


def test_bad_followups_do_not_discard_a_valid_visualization_proposal(tmp_path):
    store = PanelStore(tmp_path / "panel.sqlite")
    async def run():
        mid = seed(store)
        client = SimpleNamespace(enabled=True, complete=AsyncMock(return_value=json.dumps({
            "suitable": True, "title": "梯度与切线", "focus": "比较法向和切向方向",
            "followups": [proposal(anchor_id="a999")],
        })))
        service = ArtifactService(store, client)
        service.discover("one", mid)
        await asyncio.gather(*service.discoveries.values())
        assert store.message("one", mid)["followups"] == []
        assert store.message("one", mid)["followups_state"] == "completed"
        assert store.offers("one")[0]["title"] == "梯度与切线"
        assert client.complete.await_count == 1
        assert not store.artifact_state("one")["pending"]
        await service.stop()
    asyncio.run(run())


def test_canvas_generation_retains_model_proposal_and_context(tmp_path, monkeypatch):
    store = PanelStore(tmp_path / "panel.sqlite")
    mid = seed(store)
    service = ArtifactService(store, SimpleNamespace(enabled=True))
    offer = service.collect_offers("one", mid, "该处没有有限斜率。", "concept", [{
        "tier": "canvas", "title": "位移与点积", "query": "拖动Q，显示P到Q的位移与梯度点积",
        "context_hint": "学生把点坐标误当位移；P=(1,1)，法向量=(2,0)。"}])[0]
    build = AsyncMock(return_value={"kind": "html_canvas", "title": "位移", "html": "<html><body>图</body></html>", "height": 300})
    monkeypatch.setattr("app.skills.canvas_builder.build", build)
    asyncio.run(service._generate({"session_id": "one", "message_id": mid, "offer_id": offer["offer_id"]}))
    query, context, _ = build.call_args.args
    assert "拖动Q" in query and "点坐标误当位移" in context
