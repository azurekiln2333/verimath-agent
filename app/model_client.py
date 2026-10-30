"""OpenAI 兼容的模型客户端。

两套接口共存：
- complete() / stream_complete()：纯文本问答，给 artifact_agent / exercise /
  summarize_sources / 滚动摘要等「不需要工具调用」的旁路用。签名不变，零回归。
- chat() / stream_chat()：带 tools 的工具调用接口，给 Agent 循环用。
  chat() 非流式（SDK 已拼好 tool_calls，最稳）；stream_chat() 流式，文本逐 token
  推送、tool_calls 在流结束时拼装好一次性给出 —— 兼得打字机体验与工具调用。

ModelMessage 扩展了 tool_calls / tool_call_id / name 三个可选字段以承载工具调用
消息历史（assistant 带 tool_calls；role=tool 带 tool_call_id+name）。to_dict()
只输出非 None 字段，避免给 API 发 "tool_calls": null 这类噪音。
"""
from __future__ import annotations

import json
from contextlib import asynccontextmanager
from collections.abc import AsyncIterator
from dataclasses import dataclass, field

import httpx

from app.settings import Settings


@dataclass(frozen=True)
class ModelMessage:
    """一条对话消息。支持三种角色形态：
    - 普通：role + content
    - assistant 工具调用：role="assistant" + content? + tool_calls
    - 工具结果：role="tool" + content + tool_call_id + name
    frozen 不影响构造：都有默认值，位置参数 ModelMessage("system","hi") 仍可用。
    """
    role: str
    content: str | list[dict] | None = None
    tool_calls: list[dict] | None = None       # 仅 assistant：[{id,type,function:{name,arguments}}]
    tool_call_id: str | None = None            # 仅 role="tool"
    name: str | None = None                    # 仅 role="tool"：工具名
    # DeepSeek 思考模式：模型进行工具调用的轮次，reasoning_content 必须在后续所有请求中
    # 完整回传给 API，否则返回 400。仅 assistant 工具调用消息需要带（普通多轮可省略，API 会忽略）。
    reasoning_content: str | None = None

    def to_dict(self) -> dict:
        """序列化给 API，只带非 None 字段。"""
        d: dict = {"role": self.role}
        if self.content is not None:
            d["content"] = self.content
        if self.tool_calls is not None:
            d["tool_calls"] = self.tool_calls
        if self.tool_call_id is not None:
            d["tool_call_id"] = self.tool_call_id
        if self.name is not None:
            d["name"] = self.name
        if self.reasoning_content is not None:
            d["reasoning_content"] = self.reasoning_content
        return d


@dataclass
class ToolCall:
    """一次工具调用。arguments 已解析为 dict；模型给的 JSON 不可解析时退化为 {}。"""
    id: str
    name: str
    arguments: dict = field(default_factory=dict)


@dataclass
class ChatResult:
    """非流式工具调用的返回。content 可能为 None（模型只调工具不说话）。
    reasoning_content 为 DeepSeek 思考模式的思维链内容（工具调用轮次需回传）。"""
    content: str | None
    tool_calls: list[ToolCall]
    finish_reason: str
    reasoning_content: str | None = None


@dataclass
class StreamEvent:
    """流式事件。type 取值：
    - "thinking"：思考链增量（DeepSeek reasoning_content，text 有值）—— 先于 delta 到达
    - "delta"：文本增量（text 有值）
    - "tool_calls"：本轮流结束且模型要调工具（tool_calls 有值）
    - "done"：本轮流结束且无工具调用，本轮即最终答案
    一轮流式只会以 tool_calls 或 done 之一收尾。思考链在收尾前流式推送。
    """
    type: str
    text: str = ""
    tool_calls: list[ToolCall] = field(default_factory=list)
    finish_reason: str = ""


class OpenAICompatibleClient:
    def __init__(self, settings: Settings) -> None:
        self.settings = settings
        self._http: httpx.AsyncClient | None = None

    async def start(self) -> None:
        if self._http is None:
            limits = httpx.Limits(max_connections=8, max_keepalive_connections=4)
            self._http = httpx.AsyncClient(
                transport=httpx.AsyncHTTPTransport(retries=1, limits=limits),
            )

    async def aclose(self) -> None:
        if self._http is not None:
            await self._http.aclose()
            self._http = None

    @asynccontextmanager
    async def _transport(self, timeout: float):
        if self._http is not None:
            yield self._http
        else:
            # Standalone scripts/tests have no application lifespan to own a pool.
            async with httpx.AsyncClient(timeout=timeout) as client:
                yield client

    @property
    def enabled(self) -> bool:
        return bool(
            self.settings.model_enabled
            and self.settings.model_api_base
            and self.settings.model_api_key
        )

    def _base_payload(
        self,
        thinking: bool | None = None,
        temperature: float | None = None,
    ) -> dict:
        """所有请求共用的基础 payload：model + 思考模式参数。
        DeepSeek 思考模式默认开启，reasoning_content 与 content 同级返回。
        思考模式不支持 temperature/top_p（静默忽略），故思考开启时不发 temperature。

        per-call 覆盖（None=沿用 settings 默认）：
        - thinking=False：禁用思考模式（用于 HTML 代码生成等不需要深度推理、
          且对延迟敏感的任务，避免思考链拖慢响应）。
        - temperature：仅在思考关闭时生效。"""
        payload: dict = {"model": self.settings.model_name}
        payload["max_tokens"] = self.settings.model_max_output_tokens
        use_thinking = self.settings.model_thinking if thinking is None else thinking
        if use_thinking:
            payload["thinking"] = {"type": "enabled"}
            payload["reasoning_effort"] = self.settings.model_reasoning_effort
        else:
            # 显式禁用思考模式：DeepSeek 思考默认 enabled，仅省略 thinking 参数不会关闭它。
            # 必须发 {"thinking":{"type":"disabled"}} 才能真正关闭（用于 HTML 代码生成等
            # 不需要深度推理、且对延迟敏感的任务，避免思考链拖慢响应）。
            payload["thinking"] = {"type": "disabled"}
            payload["temperature"] = 0.2 if temperature is None else temperature
        return payload

    # -------------------------------------------------- 纯文本接口（旁路用）

    async def complete(
        self,
        messages: list[ModelMessage],
        response_format: dict | None = None,
        thinking: bool | None = None,
        temperature: float | None = None,
        timeout: float = 180,
        model: str | None = None,
        max_tokens: int | None = None,
    ) -> str:
        if not self.enabled:
            raise RuntimeError("MODEL_ENABLED, MODEL_API_BASE, and MODEL_API_KEY are not configured")
        url = self.settings.model_api_base.rstrip("/") + "/chat/completions"
        payload = self._base_payload(thinking=thinking, temperature=temperature)
        payload.update({
            "messages": [message.to_dict() for message in messages],
            "stream": False,
        })
        if response_format is not None:
            payload["response_format"] = response_format
        if model:
            payload["model"] = model
        if max_tokens is not None:
            payload["max_tokens"] = max_tokens
        headers = {"Authorization": f"Bearer {self.settings.model_api_key}"}
        async with self._transport(timeout) as client:
            response = await client.post(url, headers=headers, json=payload, timeout=httpx.Timeout(timeout, connect=10, pool=10))
            response.raise_for_status()
            data = response.json()
        choice = data["choices"][0]
        if choice.get("finish_reason") in {"length", "content_filter"}:
            raise RuntimeError("model_output_incomplete")
        content = choice["message"].get("content")
        if not isinstance(content, str) or not content.strip():
            raise ValueError("model_output_empty")
        return content

    async def stream_complete(self, messages: list[ModelMessage]) -> AsyncIterator[str]:
        """流式返回 token 增量（OpenAI 兼容 SSE）。逐段 yield delta 文本。纯文本，不带工具。"""
        if not self.enabled:
            raise RuntimeError("MODEL_ENABLED, MODEL_API_BASE, and MODEL_API_KEY are not configured")
        url = self.settings.model_api_base.rstrip("/") + "/chat/completions"
        payload = self._base_payload()
        payload.update({
            "messages": [message.to_dict() for message in messages],
            "stream": True,
        })
        headers = {"Authorization": f"Bearer {self.settings.model_api_key}"}
        async with self._transport(60) as client:
            async with client.stream("POST", url, headers=headers, json=payload, timeout=httpx.Timeout(60, connect=10, pool=10)) as response:
                response.raise_for_status()
                async for line in response.aiter_lines():
                    delta = _parse_sse_delta(line)
                    if delta:
                        yield delta

    # -------------------------------------------------- 工具调用接口（Agent 用）

    async def chat(
        self,
        messages: list[ModelMessage],
        tools: list[dict] | None = None,
        tool_choice: str = "auto",
        thinking: bool | None = None,
        max_tokens: int | None = None,
    ) -> ChatResult:
        """非流式工具调用。SDK/API 已把 tool_calls.arguments 拼成完整 JSON 字符串，
        这里直接 json.loads。最稳的工具调用路径，stream_chat 不可靠时的回退。"""
        if not self.enabled:
            raise RuntimeError("MODEL_ENABLED, MODEL_API_BASE, and MODEL_API_KEY are not configured")
        url = self.settings.model_api_base.rstrip("/") + "/chat/completions"
        payload = self._base_payload(thinking=thinking)
        if max_tokens is not None:
            payload["max_tokens"] = max_tokens
        payload.update({
            "messages": [m.to_dict() for m in messages],
            "stream": False,
        })
        if tools:
            payload["tools"] = tools
            payload["tool_choice"] = tool_choice
        headers = {"Authorization": f"Bearer {self.settings.model_api_key}"}
        async with self._transport(90) as client:
            response = await client.post(url, headers=headers, json=payload, timeout=httpx.Timeout(90, connect=10, pool=10))
            response.raise_for_status()
            data = response.json()
        choice = data["choices"][0]
        msg = choice.get("message", {})
        finish = choice.get("finish_reason", "stop")
        calls: list[ToolCall] = []
        for tc in msg.get("tool_calls") or []:
            fn = tc.get("function", {})
            args_raw = fn.get("arguments", "")
            try:
                args = json.loads(args_raw) if args_raw else {}
            except (json.JSONDecodeError, TypeError):
                args = {}
            calls.append(ToolCall(id=tc.get("id", ""), name=fn.get("name", ""), arguments=args))
        return ChatResult(
            content=msg.get("content"),
            tool_calls=calls,
            finish_reason=finish,
            reasoning_content=msg.get("reasoning_content"),
        )

    async def stream_chat(
        self,
        messages: list[ModelMessage],
        tools: list[dict] | None = None,
        tool_choice: str = "auto",
        thinking: bool | None = None,
        max_tokens: int | None = None,
    ) -> AsyncIterator[StreamEvent]:
        """流式工具调用：思考链(reasoning_content)逐段 yield("thinking")；
        文本逐 token yield("delta")；流结束时若模型要调工具，
        把跨 chunk 的 tool_call 分片拼装成完整 ToolCall 列表 yield("tool_calls")，
        否则 yield("done")。

        DeepSeek 思考模式：reasoning_content 先于 content 到达。调用方需把每轮累加的
        reasoning_content 回传到下一轮的 assistant 消息（工具调用场景，否则 API 400）。

        tool_call 分片拼装：OpenAI 流式协议里 tool_calls 按 index 分片到达，
        首片带 id+name，后续片只带 function.arguments 字符串片段，需按 index 累加。
        """
        if not self.enabled:
            raise RuntimeError("MODEL_ENABLED, MODEL_API_BASE, and MODEL_API_KEY are not configured")
        url = self.settings.model_api_base.rstrip("/") + "/chat/completions"
        payload = self._base_payload(thinking=thinking)
        if max_tokens is not None:
            payload["max_tokens"] = max_tokens
        payload.update({
            "messages": [m.to_dict() for m in messages],
            "stream": True,
        })
        if tools:
            payload["tools"] = tools
            payload["tool_choice"] = tool_choice
        headers = {"Authorization": f"Bearer {self.settings.model_api_key}"}

        # index → {id, name, args}
        tc_buf: dict[int, dict] = {}
        finish_reason = None
        async with self._transport(120) as client:
            async with client.stream("POST", url, headers=headers, json=payload, timeout=httpx.Timeout(120, connect=10, pool=10)) as response:
                response.raise_for_status()
                async for line in response.aiter_lines():
                    delta, fr = _parse_sse_chunk(line)
                    if fr:
                        finish_reason = fr
                    if delta is None:
                        continue
                    # 思考链增量（先于 content 到达）
                    reasoning = delta.get("reasoning_content")
                    if reasoning:
                        yield StreamEvent("thinking", text=reasoning)
                    text = delta.get("content")
                    if text:
                        yield StreamEvent("delta", text=text)
                    # 工具调用分片：按 index 累加
                    for frag in delta.get("tool_calls") or []:
                        idx = frag.get("index", 0)
                        buf = tc_buf.setdefault(idx, {"id": "", "name": "", "args": ""})
                        if frag.get("id"):
                            buf["id"] = frag["id"]
                        fn = frag.get("function") or {}
                        if fn.get("name"):
                            buf["name"] = fn["name"]
                        if fn.get("arguments"):
                            buf["args"] += fn["arguments"]

        if finish_reason is None:
            raise RuntimeError("model_stream_incomplete")
        if finish_reason not in {"stop", "tool_calls"}:
            raise RuntimeError("model_output_incomplete")
        # 流结束：有 tool_calls → 拼装；否则 → done
        if tc_buf:
            calls: list[ToolCall] = []
            for idx in sorted(tc_buf):
                buf = tc_buf[idx]
                try:
                    args = json.loads(buf["args"]) if buf["args"] else {}
                except (json.JSONDecodeError, TypeError):
                    args = {}
                calls.append(ToolCall(
                    id=buf["id"] or f"call_{idx}",
                    name=buf["name"],
                    arguments=args,
                ))
            yield StreamEvent("tool_calls", tool_calls=calls, finish_reason=finish_reason or "tool_calls")
        else:
            yield StreamEvent("done", finish_reason=finish_reason or "stop")


# ----------------------------------------------------------- SSE 解析


def _parse_sse_delta(line: str) -> str:
    """从一行 SSE 中解析出 choices[0].delta.content；非数据行/结束标记返回空串。
    供纯文本 stream_complete 用。"""
    line = line.strip()
    if not line or not line.startswith("data:"):
        return ""
    data = line[len("data:"):].strip()
    if not data or data == "[DONE]":
        return ""
    try:
        obj = json.loads(data)
        return obj["choices"][0]["delta"].get("content") or ""
    except (json.JSONDecodeError, KeyError, IndexError):
        return ""


def _parse_sse_chunk(line: str) -> tuple[dict | None, str | None]:
    """解析一行 SSE，返回 (delta 对象, finish_reason)。
    非数据行/结束标记返回 (None, None)。供 stream_chat 用 —— 需要整个 delta 对象
    （含 content 与 tool_calls 分片），而不只是 content 字符串。"""
    line = line.strip()
    if not line or not line.startswith("data:"):
        return None, None
    data = line[len("data:"):].strip()
    if not data or data == "[DONE]":
        return None, None
    try:
        obj = json.loads(data)
        choice = obj["choices"][0]
        return choice.get("delta") or None, choice.get("finish_reason")
    except (json.JSONDecodeError, KeyError, IndexError):
        return None, None
