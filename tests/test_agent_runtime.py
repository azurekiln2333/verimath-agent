from __future__ import annotations

import asyncio
from types import SimpleNamespace

import pytest

from app.agent_runtime import iterate_agent
from app.model_client import ChatResult, ModelMessage, StreamEvent, ToolCall
from app.tools.base import ToolResult
from app.tools.registry import ToolRegistry
from app.tools.statistics import CalculateStatisticsTool


class DoubleTool:
    name = "double"

    def schema(self):
        return {"type": "function", "function": {"name": self.name, "parameters": {
            "type": "object", "properties": {"n": {"type": "integer", "minimum": 1, "maximum": 9}},
            "required": ["n"],
        }}}

    async def run(self, n):
        return ToolResult(str(n * 2), summary={"n": n * 2})


@pytest.mark.parametrize("streaming", [True, False])
def test_both_transports_preserve_tool_messages_reasoning_and_narration(streaming):
    seen = []

    async def chat(messages, **kwargs):
        seen.append(list(messages))
        if len(seen) == 1:
            return ChatResult("先计算。", [ToolCall("call-1", "double", {"n": 3})],
                              "tool_calls", reasoning_content="需要精确计算")
        assert messages[-2].reasoning_content == "需要精确计算"
        assert messages[-2].tool_calls[0]["id"] == "call-1"
        assert messages[-1].content == "6" and messages[-1].tool_call_id == "call-1"
        return ChatResult("结果为 6。", [], "stop")

    async def stream_chat(messages, **kwargs):
        result = await chat(messages, **kwargs)
        if result.reasoning_content:
            yield StreamEvent("thinking", text=result.reasoning_content)
        yield StreamEvent("delta", text=result.content)
        yield StreamEvent("tool_calls" if result.tool_calls else "done", tool_calls=result.tool_calls)

    async def run():
        client = SimpleNamespace(chat=chat, stream_chat=stream_chat)
        events = [event async for event in iterate_agent(client, ToolRegistry([DoubleTool()]),
                  [ModelMessage("user", "计算")], streaming=streaming)]
        assert events[-1] == ("done", {"text": "先计算。结果为 6。"})
        assert sum(name == "tool_call" for name, _ in events) == 1

    asyncio.run(run())


@pytest.mark.parametrize("stop", ["timeout", "cancel"])
def test_stalled_model_is_closed_on_timeout_or_user_stop(stop):
    closed = []

    async def run():
        cancelled = False

        async def stream_chat(*args, **kwargs):
            nonlocal cancelled
            try:
                yield StreamEvent("delta", text="部分结果")
                cancelled = stop == "cancel"
                await asyncio.Event().wait()
            finally:
                closed.append(True)

        events = [event async for event in iterate_agent(
            SimpleNamespace(stream_chat=stream_chat), ToolRegistry(), [], streaming=True,
            timeout=0.25 if stop == "timeout" else 1, cancelled=lambda: cancelled,
        )]
        assert events[0] == ("delta", {"text": "部分结果"})
        assert events[-1][0] == ("error" if stop == "timeout" else "cancelled")
        if stop == "timeout":
            assert events[-1][1]["code"] == "timeout"
        assert closed == [True]

    asyncio.run(run())


@pytest.mark.parametrize("args", [{}, {"n": True}, {"n": 30}, {"n": 3, "extra": 1}, [], {"n": float("nan")}])
def test_invalid_tool_arguments_never_execute(args):
    async def run():
        result = await ToolRegistry([DoubleTool()]).dispatch("double", args)
        assert result.summary["error"] == "invalid_arguments"
    asyncio.run(run())


def test_tool_timeout_returns_recoverable_result():
    class Stalled(DoubleTool):
        async def run(self, **kwargs):
            await asyncio.Event().wait()

    async def run():
        result = await ToolRegistry([Stalled()], timeout=.02).dispatch("double", {"n": 1})
        assert result.summary["error"] == "timeout"
    asyncio.run(run())


def test_statistical_tool_returns_effect_interval_and_unverified_assumptions():
    import json
    from app.stats.tests import welch_t

    async def run():
        a, b = [1, 2, 4, 5, 7], [3, 5, 7, 8, 10]
        registry = ToolRegistry([CalculateStatisticsTool()])
        result = await registry.dispatch("calculate_statistics", {"method": "welch_t", "a": a, "b": b})
        data = json.loads(result.content)
        assert data == welch_t(a, b).as_dict()
        assert data["ci"] and data["effect_size"] is not None and data["assumptions"]
        missing = await registry.dispatch("calculate_statistics", {"method": "one_sample_t", "a": a})
        assert "error" in missing.summary and "mu0" in missing.content
    asyncio.run(run())


@pytest.mark.parametrize("streaming", [True, False])
def test_tool_citations_continue_initial_numbers_and_stay_per_request(streaming):
    class SearchTool(DoubleTool):
        async def run(self, n):
            return ToolResult("unscoped content", sources=[{"chunk_id": n, "text": f"资料{n}"}])

    async def chat(messages, **kwargs):
        tool_messages = [m for m in messages if m.role == "tool"]
        if not tool_messages:
            return ChatResult("", [ToolCall("c1", "double", {"n": 2})], "tool_calls")
        if len(tool_messages) == 1:
            return ChatResult("", [ToolCall("c2", "double", {"n": 2}),
                                   ToolCall("c3", "double", {"n": 3})], "tool_calls")
        seeded = messages[0].content == "seeded"
        assert f"[{2 if seeded else 1}]" in tool_messages[0].content
        assert f"[{2 if seeded else 1}]" in tool_messages[1].content
        assert f"[{3 if seeded else 2}]" in tool_messages[2].content
        assert all("unscoped content" not in m.content for m in tool_messages)
        return ChatResult("完成", [], "stop")

    async def stream_chat(messages, **kwargs):
        result = await chat(messages, **kwargs)
        if result.content:
            yield StreamEvent("delta", text=result.content)
        yield StreamEvent("tool_calls" if result.tool_calls else "done", tool_calls=result.tool_calls)

    async def run():
        registry = ToolRegistry([SearchTool()])
        client = SimpleNamespace(chat=chat, stream_chat=stream_chat)

        async def one(seeded):
            initial = [{"chunk_id": 1, "text": "资料1"}] if seeded else []
            events = [e async for e in iterate_agent(client, registry,
                [ModelMessage("user", "seeded" if seeded else "empty")], streaming=streaming, sources=initial)]
            sources = [data["sources"] for name, data in events if name == "sources"]
            assert len(sources[0]) == (2 if seeded else 1)  # Earlier event is a snapshot.
            assert [s["chunk_id"] for s in sources[-1]] == ([1, 2, 3] if seeded else [2, 3])
            assert len(initial) == (1 if seeded else 0)

        await asyncio.gather(one(True), one(False))

    asyncio.run(run())
