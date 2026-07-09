from __future__ import annotations

import json
from typing import Any

from pydantic import BaseModel, ConfigDict, Field


JSONRPC_VERSION = "2.0"
CLEAR_CONTEXT_METHODS = {
    "clearContext",
    "clearContextRPC",
    "context/clear",
    "clear_context",
}


class JsonRpcRequest(BaseModel):
    model_config = ConfigDict(extra="allow")

    jsonrpc: str = Field(default=JSONRPC_VERSION)
    id: str | int | None = None
    method: str
    params: dict[str, Any] = Field(default_factory=dict)


def jsonrpc_result(request_id: str | int | None, result: Any) -> dict[str, Any]:
    return {"jsonrpc": JSONRPC_VERSION, "id": request_id, "result": result}


def jsonrpc_error(
    request_id: str | int | None,
    code: int,
    message: str,
    data: Any | None = None,
) -> dict[str, Any]:
    payload: dict[str, Any] = {
        "jsonrpc": JSONRPC_VERSION,
        "id": request_id,
        "error": {"code": code, "message": message},
    }
    if data is not None:
        payload["error"]["data"] = data
    return payload


def sse_event(event: str, payload: Any) -> str:
    data = json.dumps(payload, ensure_ascii=False, separators=(",", ":"))
    return f"event: {event}\ndata: {data}\n\n"


def extract_session_id(params: dict[str, Any], header_session_id: str | None) -> str | None:
    candidates = [
        header_session_id,
        params.get("sessionId"),
        params.get("session_id"),
        params.get("agentSessionId"),
        params.get("agentLoginSessionId"),
    ]
    session = params.get("session")
    if isinstance(session, dict):
        candidates.extend([session.get("sessionId"), session.get("id")])
    for candidate in candidates:
        if candidate:
            return str(candidate)
    return None


def extract_task_id(params: dict[str, Any]) -> str | None:
    for key in ("taskId", "task_id", "id", "messageId"):
        if params.get(key):
            return str(params[key])
    return None


def extract_user_text(value: Any) -> str:
    """Best-effort text extraction from Xiaoyi/A2A-like payloads.

    Official payload variants are still evolving. The POC accepts multiple
    common shapes so local tests can focus on A2A behavior before platform
    integration hardens the exact schema.
    """
    chunks: list[str] = []

    def visit(node: Any, key_hint: str = "") -> None:
        if node is None:
            return
        if isinstance(node, str):
            if key_hint.lower() in {
                "text",
                "content",
                "query",
                "prompt",
                "userinput",
                "utterance",
            }:
                chunks.append(node)
            return
        if isinstance(node, list):
            for item in node:
                visit(item, key_hint)
            return
        if isinstance(node, dict):
            for key, child in node.items():
                visit(child, key)

    for key in ("text", "query", "prompt", "input", "message", "messages", "data"):
        if key in value:
            visit(value[key], key)
    if not chunks:
        visit(value)
    return "\n".join(dict.fromkeys(chunk.strip() for chunk in chunks if chunk.strip()))

