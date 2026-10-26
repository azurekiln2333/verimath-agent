from fastapi.testclient import TestClient

from app.main import app
from app.settings import settings
from app.test_records import TestRecordStore


client = TestClient(app)


def test_dashboard_serves_panel_html():
    """静态拆分后：HTML 骨架走 /dashboard，脚本与样式走 /static。"""
    response = client.get("/dashboard")
    assert response.status_code == 200
    assert "数学与统计学习导师" in response.text
    assert 'rel="icon" href="data:,"' in response.text
    assert "/static/vendor/katex.min.js" in response.text
    assert "/static/vendor/markdown-it.min.js" in response.text
    assert "/static/vendor/purify.min.js" in response.text
    # 静态资源带内容指纹（?v=<hash>）以便改完立即生效，断言只要求前缀匹配
    assert 'src="/static/panel.js' in response.text
    assert 'href="/static/panel.css' in response.text
    js = client.get("/static/panel.js")
    assert js.status_code == 200
    assert "/api/panel/chat" in js.text
    assert "function renderMarkdown" in js.text
    assert "renderMathInElement" in js.text
    assert "MathJax" not in js.text
    assert "styleSelector" in js.text
    assert "historyList" in js.text
    assert "testRunList" in js.text
    assert "protectMathDelimiters" in js.text
    assert "restoreMathDelimiters" in js.text
    css = client.get("/static/panel.css")
    assert css.status_code == 200
    assert ".markdown table" in css.text


def test_panel_status_masks_key_material():
    response = client.get("/api/panel/status")
    assert response.status_code == 200
    data = response.json()
    assert data["status"] == "ok"
    assert "model" in data
    assert "model_api_key" not in data
    assert "DEEPSEEK_API_KEY" not in response.text


def test_panel_chat_can_skip_model_call():
    query = "中心极限定理是什么？"
    response = client.post(
        "/api/panel/chat",
        json={"query": query, "use_model": False, "answer_style": "concise"},
    )
    assert response.status_code == 200
    data = response.json()
    assert data["route"] == "concept"
    assert "中心极限定理" in data["content"]
    assert data["flags"].get("model_used") is None
    assert data["flags"]["answer_style"] == "concise"

    history = client.get("/api/panel/history?limit=5")
    assert history.status_code == 200
    assert any(item["query"] == query for item in history.json()["items"])


def test_panel_chat_stream_emits_sse_sequence():
    with client.stream(
        "POST",
        "/api/panel/chat/stream",
        json={"query": "中心极限定理是什么？", "use_model": False, "session_id": "stream-seq"},
    ) as response:
        assert response.status_code == 200
        body = "\n".join(response.iter_lines())
    assert "event: meta" in body
    assert "event: delta" in body
    assert "event: final" in body
    assert "中心极限定理" in body


def test_panel_stream_empty_query_returns_final():
    with client.stream(
        "POST", "/api/panel/chat/stream", json={"query": "  ", "use_model": False}
    ) as response:
        body = "\n".join(response.iter_lines())
    assert "event: final" in body
    assert "请输入" in body


def test_panel_test_runs_returns_saved_eval_record():
    TestRecordStore(settings.data_dir).append_eval_run(
        {"total": 1, "source_hit_rate": 1.0, "route_counts": {"concept": 1}},
        input_path="tests",
        limit=1,
    )
    response = client.get("/api/panel/test-runs?limit=5")
    assert response.status_code == 200
    assert any(item["report"]["total"] == 1 for item in response.json()["items"])
