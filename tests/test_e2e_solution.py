# -*- coding: utf-8 -*-
"""端到端全流程测试：HTTP 通道 → 路由 → 离线内核直答 → SSE 事件序列。

验证主产品 A 的离线交付路径（无模型、无密钥）：
学生贴题（带矩阵字面量）→ /a2a message/stream → route=solution →
逐步解答 + SymPy 复算凭证出现在 final 事件。
"""
from fastapi.testclient import TestClient

from app.main import app

client = TestClient(app)


def _post_stream(content: str, task_id: str) -> str:
    response = client.post(
        "/a2a",
        json={
            "jsonrpc": "2.0",
            "id": "e2e",
            "method": "message/stream",
            "params": {
                "taskId": task_id,
                "useModel": False,
                "message": {"content": content},
            },
        },
    )
    assert response.status_code == 200
    return response.text


def test_e2e_det_solution_offline():
    text = _post_stream("求 [[2,1],[1,3]] 的行列式", "e2e-det")
    assert '"route":"solution"' in text
    assert "复算" in text          # 验算凭证在场
    assert "第 1 步" in text       # 逐步展示


def test_e2e_inverse_solution_offline():
    text = _post_stream("求 [[4,7],[2,6]] 的逆", "e2e-inv")
    assert '"route":"solution"' in text
    assert "frac" in text          # 分数逆矩阵


def test_e2e_guide_when_no_matrix():
    text = _post_stream("这道题求特征值，矩阵我等下发", "e2e-guide")
    assert '"route":"solution"' in text
    assert "逐步" in text or "格式" in text


def test_e2e_courseware_skeleton_offline():
    text = _post_stream("帮我准备一份中心极限定理的课件", "e2e-cw")
    assert '"route":"courseware"' in text


def test_e2e_panel_stream_solution():
    with TestClient(app) as c:
        with c.stream(
            "POST",
            "/api/panel/chat/stream",
            json={"query": "求 [[3,1],[0,2]] 的行列式", "use_model": False},
        ) as response:
            body = "".join(chunk for chunk in response.iter_text())
    assert "event: meta" in body
    assert '"route":"solution"' in body
    assert "event: final" in body
    assert "复算" in body
