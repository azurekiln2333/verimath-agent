"""One bounded model/tool loop shared by streaming and non-streaming transports."""
from __future__ import annotations

import asyncio
import json
import logging
import re
from contextlib import aclosing
from collections.abc import AsyncIterator, Callable

from app.model_client import ModelMessage, StreamEvent
from app.model_errors import describe_model_error
from app.rag.sources import SourceLedger


def is_smalltalk(query: str) -> bool:
    """Match standalone greetings only; a greeting followed by a task stays an agent request."""
    text = re.sub(r"[\s!！。.,，?？~～、]+", "", query).casefold()
    return text in {"你好", "您好", "你好呀", "你好啊", "嗨", "哈喽", "在吗", "早上好", "晚上好",
                    "早安", "晚安", "谢谢", "多谢", "再见", "hi", "hello", "hey", "thanks", "thankyou", "bye"}


async def iterate_agent(client, registry, seed: list[ModelMessage], *, streaming: bool,
                        max_iterations: int = 6, timeout: float = 180,
                        simple: bool = False,
                        sources: list[dict] | None = None,
                        cancelled: Callable[[], bool] = lambda: False) -> AsyncIterator[tuple[str, dict]]:
    messages = list(seed)
    ledger = SourceLedger(sources)
    schema = [] if simple else registry.to_openai_schema()
    options = {"thinking": False, "max_tokens": 256} if simple else {}
    text = ""
    try:
        async with asyncio.timeout(min(timeout, 30) if simple else timeout):
            for _ in range(1 if simple else max_iterations):
                if cancelled():
                    yield "cancelled", {}
                    return
                turn_text, reasoning = "", ""
                calls = None
                finished = False
                async with aclosing(_turn(client, messages, schema, streaming, options)) as events:
                    while True:
                        try:
                            event = await _await_active(anext(events), cancelled)
                        except StopAsyncIteration:
                            break
                        if event.type == "thinking":
                            reasoning += event.text
                            yield "thinking", {"text": event.text}
                        elif event.type == "delta":
                            text += event.text
                            turn_text += event.text
                            yield "delta", {"text": event.text}
                        elif event.type == "tool_calls":
                            calls = event.tool_calls
                        elif event.type == "done":
                            finished = True
                if calls is None:
                    if not finished:
                        raise RuntimeError("model_stream_incomplete")
                    yield "done", {"text": text}
                    return
                messages.append(ModelMessage("assistant", turn_text or None,
                    tool_calls=[{"id": call.id, "type": "function", "function": {
                        "name": call.name, "arguments": json.dumps(call.arguments, ensure_ascii=False),
                    }} for call in calls], reasoning_content=reasoning or None))
                for call in calls:
                    if cancelled():
                        yield "cancelled", {}
                        return
                    yield "tool_call", {"id": call.id, "name": call.name, "arguments": call.arguments}
                    result = await _await_active(registry.dispatch(call.name, call.arguments), cancelled)
                    yield "tool_result", {"id": call.id, "name": call.name, "summary": result.summary,
                                          "ok": "error" not in (result.summary or {})}
                    if result.artifact_offer:
                        yield "artifact_offer", result.artifact_offer
                    content = result.content
                    if result.sources:
                        content = ledger.add(result.sources)
                        yield "sources", {"sources": list(ledger.sources)}
                    messages.append(ModelMessage("tool", content, tool_call_id=call.id, name=call.name))
            yield "max_iter", {"text": text}
    except _UserCancelled:
        yield "cancelled", {}
    except Exception as exc:
        details = describe_model_error(exc)
        logging.getLogger(__name__).warning("Model call failed: code=%s type=%s http_status=%s",
                                           details["code"], details["error_type"], details["http_status"])
        yield "error", details


async def _turn(client, messages, schema, streaming, options):
    if streaming:
        async with aclosing(client.stream_chat(messages, tools=schema, tool_choice="auto", **options)) as events:
            async for event in events:
                yield event
    else:
        result = await client.chat(messages, tools=schema, tool_choice="auto", **options)
        if result.reasoning_content:
            yield StreamEvent("thinking", text=result.reasoning_content)
        if result.content:
            yield StreamEvent("delta", text=result.content)
        if result.tool_calls:
            yield StreamEvent("tool_calls", tool_calls=result.tool_calls)
        else:
            yield StreamEvent("done")


class _UserCancelled(Exception):
    pass


async def _await_active(awaitable, cancelled):
    """Cancel stalled network/tool work too, without starting a second execution."""
    pending = asyncio.ensure_future(awaitable)
    try:
        while not pending.done():
            if cancelled():
                raise _UserCancelled
            await asyncio.wait({pending}, timeout=0.1)
        return pending.result()
    finally:
        if not pending.done():
            pending.cancel()
        await asyncio.gather(pending, return_exceptions=True)
