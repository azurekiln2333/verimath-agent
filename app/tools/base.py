"""工具包：把现有能力（绘图/出题/选方法/查库/生成 HTML 组件）封装为
模型可调用的工具，是 Agent「技能/hooking」的载体。

设计借鉴 MathModelAgent 的 Tool 协议：每个工具暴露 name + schema() + run()。
"""
from __future__ import annotations

from dataclasses import dataclass, field
from typing import Any, Protocol, runtime_checkable


@dataclass(frozen=True)
class ToolResult:
    """工具执行结果。
    - content：回填给模型的字符串（模型据此继续推理/生成）
    - summary：结构化摘要，供 SSE tool_result 事件与 trace
    - artifact_offer：若工具产出了可视化组件，携带 {tier, spec?, query, route, title, caption}
    """
    content: str
    summary: dict[str, Any] = field(default_factory=dict)
    artifact_offer: dict[str, Any] | None = None


@runtime_checkable
class Tool(Protocol):
    """工具协议：name + schema() + async run(**kwargs)。"""
    name: str

    def schema(self) -> dict[str, Any]:
        """返回 OpenAI function-calling 的工具 schema。"""
        ...

    async def run(self, **kwargs: Any) -> ToolResult:
        ...
