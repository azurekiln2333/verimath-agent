"""学习画像注入 build_model_messages 的单元测试。"""
from __future__ import annotations

from app.agents.router import AgentResponse
from app.main import build_model_messages, format_profile_for_prompt


def test_format_profile_empty_returns_empty():
    assert format_profile_for_prompt(None) == ""
    assert format_profile_for_prompt({}) == ""
    assert format_profile_for_prompt({"turn_count": 0, "topics": [], "route_counts": {}}) == ""


def test_format_profile_includes_turns_topics_routes():
    profile = {
        "turn_count": 5,
        "topics": ["正态分布", "假设检验", "中心极限定理"],
        "route_counts": {"concept": 3, "exercise": 2, "derive": 1},
    }
    text = format_profile_for_prompt(profile)
    assert "5 轮" in text
    assert "正态分布" in text
    assert "假设检验" in text
    # 突出最常用能力
    assert "concept" in text
    assert text.startswith("学生学习画像")


def test_format_profile_truncates_long_topics():
    profile = {"turn_count": 1, "topics": [f"主题{i}" for i in range(10)], "route_counts": {}}
    text = format_profile_for_prompt(profile)
    # 最多列 6 个，超出用“等共 N 个”概括
    assert "主题0" in text
    assert "等共 10 个" in text


def test_build_model_messages_without_profile_has_no_profile_marker():
    resp = AgentResponse(route="concept", text="骨架", sources=[])
    msgs = build_model_messages("什么是方差？", resp, "rigorous", None, None)
    assert msgs[0].role == "system"
    assert "学生学习画像" not in msgs[0].content


def test_build_model_messages_with_profile_appends_to_system():
    resp = AgentResponse(route="concept", text="骨架", sources=[])
    profile_text = "学生学习画像（供个性化参考，勿生硬复述）：已累计交互 3 轮。"
    msgs = build_model_messages("什么是方差？", resp, "rigorous", None, profile_text)
    assert msgs[0].role == "system"
    assert "学生学习画像" in msgs[0].content
    assert "已累计交互 3 轮" in msgs[0].content
    # 原始 system 指令仍保留
    assert "统计学本科生" in msgs[0].content
