from fastapi.testclient import TestClient

from app.main import app


client = TestClient(app)


def test_healthz():
    response = client.get("/healthz")
    assert response.status_code == 200
    assert response.json()["status"] == "ok"


def test_initialize_and_clear_context():
    init = client.post(
        "/a2a",
        json={"jsonrpc": "2.0", "id": "init", "method": "initialize", "params": {}},
    )
    assert init.status_code == 200
    session_id = init.headers["agent-session-id"]
    assert init.json()["result"]["sessionId"] == session_id

    clear = client.post(
        "/a2a",
        headers={"agent-session-id": session_id},
        json={"jsonrpc": "2.0", "id": "clear", "method": "clearContext", "params": {}},
    )
    assert clear.status_code == 200
    assert clear.json()["result"]["ok"] is True


def test_message_stream_returns_final_event():
    response = client.post(
        "/a2a",
        json={
            "jsonrpc": "2.0",
            "id": "msg",
            "method": "message/stream",
            "params": {
                "taskId": "test-stream",
                "message": {"content": "两组成绩比较用什么检验？"},
            },
        },
    )
    assert response.status_code == 200
    assert response.headers["content-type"].startswith("text/event-stream")
    text = response.text
    assert "event: final" in text
    assert "method_selection" in text
    assert "因变量" in text


def test_message_stream_can_skip_model_for_local_load_tests():
    response = client.post(
        "/a2a",
        json={
            "jsonrpc": "2.0",
            "id": "msg-offline",
            "method": "message/stream",
            "params": {
                "taskId": "test-stream-offline",
                "useModel": False,
                "message": {"content": "中心极限定理是什么？"},
            },
        },
    )
    assert response.status_code == 200
    text = response.text
    assert "event: final" in text
    assert "中心极限定理" in text
    assert "model_used" not in text


def test_cancel_task_rpc():
    response = client.post(
        "/a2a",
        json={
            "jsonrpc": "2.0",
            "id": "cancel",
            "method": "tasks/cancel",
            "params": {"taskId": "task-1", "sessionId": "session-1"},
        },
    )
    assert response.status_code == 200
    assert response.json()["result"]["taskId"] == "task-1"


def test_unknown_method_returns_jsonrpc_error():
    response = client.post(
        "/a2a",
        json={"jsonrpc": "2.0", "id": "bad", "method": "unknown/method", "params": {}},
    )
    assert response.status_code == 404
    assert response.json()["error"]["code"] == -32601
