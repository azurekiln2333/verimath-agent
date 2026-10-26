"""工具注册与调度中心。"""
from __future__ import annotations

import asyncio
import json
import math
from typing import Any

from app.tools.base import Tool, ToolResult


class ToolRegistry:
    """管理一组工具：注册、转 OpenAI schema、按名分发。"""

    def __init__(self, tools: list[Tool] | None = None, *, timeout: float = 90) -> None:
        self._tools: dict[str, Tool] = {}
        self._schemas: dict[str, dict] = {}
        self.timeout = timeout
        for t in tools or []:
            self.register(t)

    def register(self, tool: Tool) -> None:
        self._tools[tool.name] = tool
        self._schemas[tool.name] = tool.schema()

    def get(self, name: str) -> Tool | None:
        return self._tools.get(name)

    def names(self) -> list[str]:
        return list(self._tools.keys())

    def to_openai_schema(self) -> list[dict[str, Any]]:
        """转成 OpenAI chat completions 的 tools 参数格式。"""
        return list(self._schemas.values())

    async def dispatch(self, name: str, args: dict[str, Any]) -> ToolResult:
        """按名调用工具。未知工具或执行异常都降级为一段说明文本，绝不中断 agent 循环。"""
        tool = self._tools.get(name)
        if tool is None:
            return ToolResult(
                content=f"工具 {name} 不存在。可用工具：{', '.join(self._tools.keys())}",
                summary={"error": "unknown_tool", "name": name},
            )
        try:
            if not isinstance(args, dict) or len(json.dumps(args, allow_nan=False)) > 64000:
                raise ValueError("工具参数必须是对象且不超过 64000 字节")
            _validate(args, self._schemas[name]["function"]["parameters"])
        except (ValueError, TypeError, RecursionError) as exc:
            return ToolResult(content=f"工具参数不合法：{exc}，请修正后再调用。",
                              summary={"error": "invalid_arguments", "name": name})
        try:
            async with asyncio.timeout(self.timeout):
                result = await tool.run(**args)
            if len(result.content) > 32000:
                return ToolResult(content=result.content[:32000] + "\n（工具结果过长，已截断；请缩小问题范围。）",
                                  summary={**result.summary, "truncated": True},
                                  artifact_offer=result.artifact_offer)
            return result
        except TimeoutError:
            return ToolResult(content=f"工具 {name} 计算超时，请缩小输入后重试。",
                              summary={"error": "timeout", "name": name})
        except Exception as exc:  # 工具失败不拖垮整轮，把错误回填给模型让它自行处理
            return ToolResult(
                content=f"工具 {name} 执行失败：{type(exc).__name__}: {exc}",
                summary={"error": type(exc).__name__, "name": name, "message": str(exc)},
            )


def _validate(value: Any, schema: dict, path: str = "arguments") -> None:
    """Validate the schema subset used by our tools, without another dependency."""
    kind = schema.get("type")
    matches = {
        "object": isinstance(value, dict), "array": isinstance(value, list),
        "string": isinstance(value, str), "boolean": isinstance(value, bool),
        "integer": isinstance(value, int) and not isinstance(value, bool),
        "number": isinstance(value, (int, float)) and not isinstance(value, bool),
    }
    if kind in matches and not matches[kind]:
        raise ValueError(f"{path} 类型应为 {kind}")
    if "enum" in schema and value not in schema["enum"]:
        raise ValueError(f"{path} 不在允许的选项中")
    if isinstance(value, dict):
        props = schema.get("properties", {})
        missing = set(schema.get("required", [])) - value.keys()
        if missing:
            raise ValueError(f"{path} 缺少 {', '.join(sorted(missing))}")
        if props and value.keys() - props.keys():
            raise ValueError(f"{path} 含未定义参数")
        for key, item in value.items():
            _validate(item, props.get(key, {}), f"{path}.{key}")
    elif isinstance(value, list):
        if not schema.get("minItems", 0) <= len(value) <= schema.get("maxItems", 2000):
            raise ValueError(f"{path} 元素数量超限")
        for item in value:
            _validate(item, schema.get("items", {}), path + "[]")
    elif isinstance(value, str):
        if not schema.get("minLength", 0) <= len(value) <= schema.get("maxLength", 16000):
            raise ValueError(f"{path} 文本长度超限")
    elif isinstance(value, (int, float)):
        if not math.isfinite(value):
            raise ValueError(f"{path} 必须为有限数")
        if value < schema.get("minimum", -math.inf) or value > schema.get("maximum", math.inf):
            raise ValueError(f"{path} 数值超限")
