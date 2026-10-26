from app.agents.router import AgentResponse
from app.main import build_agent_messages, build_model_messages
from app.coach import CoachDecision, level_instruction


def test_model_prompt_requires_latex_delimiters_and_rigorous_style():
    messages = build_model_messages(
        "样本方差为什么除以 n-1？",
        AgentResponse(route="concept", text="骨架答案"),
        "rigorous",
    )
    joined = "\n".join(message.content for message in messages)
    # 现行契约（KaTeX 面板）：行内 \(...\)，独立块 $$...$$，禁入代码块
    assert "行内公式用 \\(...\\)" in joined
    assert "$$...$$" in joined
    assert "不要把公式放进反引号代码块" in joined
    assert "严谨优先" in joined


def test_model_prompt_supports_concise_style():
    messages = build_model_messages(
        "什么是 p 值？",
        AgentResponse(route="concept", text="骨架答案"),
        "concise",
    )
    assert "节省时间" in messages[-1].content


def test_chat_prompts_preserve_reasoning_flow_without_forced_sections():
    for builder in (build_agent_messages, build_model_messages):
        messages = builder("还是不懂，能换个例子吗？", AgentResponse(route="concept", text="无关的固定骨架"))
        joined = "\n".join(m.content or "" for m in messages)
        assert "承接上一轮" in joined
        assert "短段落" in joined
        assert "用 Markdown 二级标题" not in joined
        assert "无关的固定骨架" not in joined


def test_coach_level_is_guidance_not_a_fixed_reply_lock():
    instruction = level_instruction(CoachDecision(level=0, level_name="复述与确认", reason="测试"))
    assert "硬约束" not in instruction
    assert "重新" in instruction and "上下文" in instruction
