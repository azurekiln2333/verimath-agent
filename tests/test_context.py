from fastapi.testclient import TestClient

from app import main
from app.main import app, build_model_messages, _history_as_messages
from app.model_client import ModelMessage
from app.agents.router import AgentResponse


client = TestClient(app)


def test_history_interleaved_into_prompt():
    main.sessions.clear_context("ctx-unit")
    main.sessions.append_turn("ctx-unit", "user", "什么是中心极限定理？")
    main.sessions.append_turn("ctx-unit", "assistant", "样本均值标准化后趋近正态。")
    history = _history_as_messages("ctx-unit")
    resp = AgentResponse(route="concept", text="骨架", sources=[])
    msgs = build_model_messages("它的适用条件是什么？", resp, "rigorous", history)
    assert [m.role for m in msgs] == ["system", "user", "assistant", "user"]
    assert any("中心极限定理" in m.content for m in msgs)
    assert "它的适用条件" in msgs[-1].content


def test_history_excludes_non_dialogue_roles():
    main.sessions.clear_context("ctx-roles")
    main.sessions.append_turn("ctx-roles", "user", "hi")
    main.sessions.append_turn("ctx-roles", "system", "should be ignored")
    msgs = _history_as_messages("ctx-roles")
    assert all(m.role in {"user", "assistant"} for m in msgs)
    assert len(msgs) == 1


def test_panel_chat_accumulates_and_clears_context():
    sid = "panel-test-ctx"
    main.sessions.clear_context(sid)
    r1 = client.post(
        "/api/panel/chat",
        json={"query": "中心极限定理是什么？", "use_model": False, "session_id": sid},
    )
    assert r1.status_code == 200
    # 第一轮后会话应有 user+assistant 两条
    assert len(_history_as_messages(sid)) == 2

    r2 = client.post(
        "/api/panel/chat",
        json={"query": "它的适用条件？", "use_model": False, "session_id": sid},
    )
    assert r2.status_code == 200
    assert len(_history_as_messages(sid)) == 4

    cleared = client.post("/api/panel/clear-context", json={"session_id": sid})
    assert cleared.status_code == 200
    assert _history_as_messages(sid) == []
