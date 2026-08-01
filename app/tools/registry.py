"""工具注册与调度中心。"""
from __future__ import annotations

from typing import Any

from app.tools.base import Tool, ToolResult


class ToolRegistry:
    """管理一组工具：注册、转 OpenAI schema、按名分发。"""

    def __init__(self, tools: list[Tool] | None = None) -> None:
        self._tools: dict[str, Tool] = {}
        for t in tools or []:
            self.register(t)

    def register(self, tool: Tool) -> None:
        self._tools[tool.name] = tool

    def get(self, name: str) -> Tool | None:
        return self._tools.get(name)

    def names(self) -> list[str]:
        return list(self._tools.keys())

    def to_openai_schema(self) -> list[dict[str, Any]]:
        """转成 OpenAI chat completions 的 tools 参数格式。"""
        return [t.schema() for t in self._tools.values()]

    async def dispatch(self, name: str, args: dict[str, Any]) -> ToolResult:
        """按名调用工具。未知工具或执行异常都降级为一段说明文本，绝不中断 agent 循环。"""
        tool = self._tools.get(name)
        if tool is None:
            return ToolResult(
                content=f"工具 {name} 不存在。可用工具：{', '.join(self._tools.keys())}",
                summary={"error": "unknown_tool", "name": name},
            )
        try:
            return await tool.run(**args)
        except Exception as exc:  # 工具失败不拖垮整轮，把错误回填给模型让它自行处理
            return ToolResult(
                content=f"工具 {name} 执行失败：{type(exc).__name__}: {exc}",
                summary={"error": type(exc).__name__, "name": name, "message": str(exc)},
            )
