from app.agents.router import AgentResponse
from app.main import build_model_messages


def test_model_prompt_requires_latex_delimiters_and_rigorous_style():
    messages = build_model_messages(
        "样本方差为什么除以 n-1？",
        AgentResponse(route="concept", text="骨架答案"),
        "rigorous",
    )
    joined = "\n".join(message.content for message in messages)
    assert "行内公式用 \\(...\\)" in joined
    assert "独立公式用 \\[...\\]" in joined
    assert "不要把公式放进反引号代码块" in joined
    assert "严谨优先" in joined


def test_model_prompt_supports_concise_style():
    messages = build_model_messages(
        "什么是 p 值？",
        AgentResponse(route="concept", text="骨架答案"),
        "concise",
    )
    assert "节省时间" in messages[-1].content
