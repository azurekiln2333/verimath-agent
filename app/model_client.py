from __future__ import annotations

import json
from collections.abc import AsyncIterator
from dataclasses import dataclass

import httpx

from app.settings import Settings


@dataclass(frozen=True)
class ModelMessage:
    role: str
    content: str


class OpenAICompatibleClient:
    def __init__(self, settings: Settings) -> None:
        self.settings = settings

    @property
    def enabled(self) -> bool:
        return bool(
            self.settings.model_enabled
            and self.settings.model_api_base
            and self.settings.model_api_key
        )

    async def complete(self, messages: list[ModelMessage]) -> str:
        if not self.enabled:
            raise RuntimeError("MODEL_ENABLED, MODEL_API_BASE, and MODEL_API_KEY are not configured")
        url = self.settings.model_api_base.rstrip("/") + "/chat/completions"
        payload = {
            "model": self.settings.model_name,
            "messages": [message.__dict__ for message in messages],
            "temperature": 0.2,
            "stream": False,
        }
        headers = {"Authorization": f"Bearer {self.settings.model_api_key}"}
        async with httpx.AsyncClient(timeout=60) as client:
            response = await client.post(url, headers=headers, json=payload)
            response.raise_for_status()
            data = response.json()
        return data["choices"][0]["message"]["content"]

    async def stream_complete(self, messages: list[ModelMessage]) -> AsyncIterator[str]:
        """流式返回 token 增量（OpenAI 兼容 SSE）。逐段 yield delta 文本。"""
        if not self.enabled:
            raise RuntimeError("MODEL_ENABLED, MODEL_API_BASE, and MODEL_API_KEY are not configured")
        url = self.settings.model_api_base.rstrip("/") + "/chat/completions"
        payload = {
            "model": self.settings.model_name,
            "messages": [message.__dict__ for message in messages],
            "temperature": 0.2,
            "stream": True,
        }
        headers = {"Authorization": f"Bearer {self.settings.model_api_key}"}
        async with httpx.AsyncClient(timeout=60) as client:
            async with client.stream("POST", url, headers=headers, json=payload) as response:
                response.raise_for_status()
                async for line in response.aiter_lines():
                    delta = _parse_sse_delta(line)
                    if delta:
                        yield delta


def _parse_sse_delta(line: str) -> str:
    """从一行 SSE 中解析出 choices[0].delta.content；非数据行/结束标记返回空串。"""
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
