"""Persistence, ownership and independent Canvas lifecycle regression tests."""
from __future__ import annotations

import asyncio
import json
from types import SimpleNamespace
from unittest.mock import AsyncMock

import httpx
import pytest

import app.main as main
from app.artifact_jobs import ArtifactService
from app.artifacts.planner import plan_artifact
from app.logging_store import InteractionLogger
from app.model_client import StreamEvent
from app.model_client import ChatResult, ModelMessage, ToolCall
from app.rag.store import RetrievedChunk
from app.panel_store import PanelStore
from app.protocol import sse_event
from app.sessions import SessionStore
from app.tools.handlers import BuildCanvasTool
from app.tools.handlers import SearchKnowledgeBaseTool
from app.tools.registry import ToolRegistry


def seed(store, session="one", task="first", content="中心极限定理：样本均值的抽样分布"):
    mid = store.begin_turn(session, task, "问题", {"route": "concept"})
    store.finish_turn(mid, content, "completed", {"route": "concept"})
    return mid


@pytest.fixture
def isolated(tmp_path, monkeypatch):
    path = tmp_path / "panel.sqlite"
    store = PanelStore(path)
    fake = SimpleNamespace(enabled=False)
    service = ArtifactService(store, fake)
    monkeypatch.setattr(main, "panel_store", store)
    monkeypatch.setattr(main, "artifact_service", service)
    monkeypatch.setattr(main, "model_client", fake)
    monkeypatch.setattr(main, "sessions", SessionStore(db_path=path))
    monkeypatch.setattr(main, "logger", InteractionLogger(path))
    return store, service


def test_legacy_import_preserves_original_and_is_idempotent(tmp_path):
    path = tmp_path / "legacy.sqlite"
    log = InteractionLogger(path)
    log.log(session_id="legacy", task_id="old", route="concept", query="旧问题", answer="旧回答",
            sources=[], flags={}, channel="panel")
    store = PanelStore(path)
    store.import_legacy()
    store.import_legacy()
    assert [m["content"] for m in store.messages("legacy")] == ["旧问题", "旧回答"]
    assert len(log.recent(channel="panel")) == 1
    assert store.sessions()[0]["title"] == "旧问题"


def test_visualization_uses_question_topic_before_incidental_answer_terms(isolated):
    store, service = isolated
    mid = store.begin_turn("normal", "normal-turn", "什么是正态分布", {"route": "concept"})
    text = "正态分布对称轴在均值处。样本均值涉及中心极限定理，回归里也会用到正态假设。"
    store.finish_turn(mid, text, "completed", {"route": "concept"})
    offer = service.collect_offers("normal", mid, text, "concept")[0]
    spec = store.offer("normal", mid, offer["offer_id"])["spec"]
    assert spec["kind"] == "distribution_explorer" and spec["params"]["family"] == "normal"


def test_full_transcript_pagination_and_session_isolation(isolated):
    store, _ = isolated
    for i in range(6):
        seed(store, task=f"turn-{i}", content=f"回答 {i}")
    seed(store, session="other", task="other")
    recent = store.messages("one", limit=4)
    older = store.messages("one", before=recent[0]["seq"], limit=8)
    assert len(recent) == 4 and len(older) == 8
    assert len({m["message_id"] for m in older + recent}) == 12
    assert all(m["session_id"] == "one" for m in older + recent)


def test_final_is_persisted_before_it_is_emitted(isolated):
    store, _ = isolated

    async def run():
        final = None
        async for frame in main._panel_stream(main.PanelChatRequest(
            query="什么是中心极限定理", session_id="one", use_model=False,
        )):
            if "event: meta\n" in frame:
                meta = json.loads(frame.split("data: ")[1])
                assert meta["artifacts"] == []
                assert store.message("one", meta["message_id"])["status"] == "streaming"
            if "event: final\n" in frame:
                final = json.loads(frame.split("data: ")[1])
                saved = store.message("one", final["message_id"])
                assert saved["content"] == final["content"]
                assert saved["status"] == "completed"
                assert final["visualization_offers"]
                assert "spec" not in final["visualization_offers"][0]
                assert not store.jobs("one")  # Offering never creates a job.
        assert final is not None
        assert len(main.sessions.get_or_create("one").history) == 2

    asyncio.run(run())


@pytest.mark.parametrize("use_model", [None, False])
def test_chat_defaults_to_model_and_honors_explicit_offline(isolated, monkeypatch, use_model):
    calls = []

    async def stream_chat(messages, **kwargs):
        calls.append((messages, kwargs))
        yield StreamEvent(type="delta", text="模型回答：中心极限定理描述样本均值的极限分布。")
        yield StreamEvent(type="done", finish_reason="stop")

    monkeypatch.setattr(main, "model_client", SimpleNamespace(enabled=True, stream_chat=stream_chat))
    monkeypatch.setattr(main, "retriever", SimpleNamespace(search=lambda *args, **kwargs: []))

    async def run():
        payload = {"query": "什么是中心极限定理", "session_id": "default-model"}
        if use_model is not None:
            payload["use_model"] = use_model
        async with httpx.AsyncClient(transport=httpx.ASGITransport(app=main.app), base_url="http://test") as client:
            response = await client.post("/api/panel/chat/stream", json=payload)
        assert response.status_code == 200
        final = next(json.loads(frame.split("data: ", 1)[1])
                     for frame in response.text.split("\n\n") if frame.startswith("event: final\n"))
        if use_model is None:
            assert len(calls) == 1
            assert calls[0][1]["tools"]
            assert final["content"].startswith("模型回答：")
            assert final["flags"]["model_used"] is True
            assert final["flags"]["agent_loop"] is True
        else:
            assert not calls
            assert not final["flags"].get("model_used")
            assert "中心极限定理" in final["content"]

    asyncio.run(run())


def test_followup_makes_fresh_model_call_with_history_and_persists_its_own_question(isolated, monkeypatch):
    store, _ = isolated
    calls = []
    replies = ["先看两组数据是否配对。是同一批学生的前后测吗？",
               "同一批学生的前后测应分析每人的差值。你能提供每个人前后对应的分数吗？"]

    async def stream_chat(messages, **kwargs):
        calls.append(list(messages))
        yield StreamEvent("delta", text=replies[len(calls) - 1])
        yield StreamEvent("done", finish_reason="stop")

    monkeypatch.setattr(main, "model_client", SimpleNamespace(enabled=True, stream_chat=stream_chat))
    monkeypatch.setattr(main, "retriever", SimpleNamespace(search=lambda *args, **kwargs: []))

    async def run():
        finals = []
        for query in ("两组成绩比较应该用什么检验", "是同一批学生，前后各测了一次"):
            frames = [frame async for frame in main._panel_stream(main.PanelChatRequest(
                query=query, session_id="fresh-followup", use_model=True))]
            finals.append(next(json.loads(f.split("data: ", 1)[1]) for f in frames if "event: final\n" in f))
        assert len(calls) == 2  # Missing design information must also be handled by the model.
        assert any(m.role == "user" and m.content == "两组成绩比较应该用什么检验" for m in calls[1])
        assert any(m.role == "assistant" and m.content == replies[0] for m in calls[1])
        assert finals[0]["coach"]["question"] == "是同一批学生的前后测吗？"
        assert finals[1]["coach"]["question"] == "你能提供每个人前后对应的分数吗？"
        assert finals[1]["coach"]["source"] == "model"
        assert not finals[1]["coach"]["hints"]
        restored = store.message("fresh-followup", finals[1]["message_id"])
        assert restored["coach"] == finals[1]["coach"]
    asyncio.run(run())


def test_disconnect_preserves_partial_answer_once(isolated, monkeypatch):
    store, _ = isolated
    closed = []

    async def events(payload):
        try:
            yield sse_event("meta", {"taskId": "partial", "route": "concept"})
            yield sse_event("delta", {"text": "已经生成的文字"})
            await asyncio.Event().wait()
        finally:
            closed.append(True)

    monkeypatch.setattr(main, "_panel_stream_events", events)

    async def run():
        stream = main._panel_stream(main.PanelChatRequest(query="问题", session_id="one", use_model=False))
        await anext(stream)
        await anext(stream)
        await stream.aclose()
        await asyncio.sleep(0)
        assert store.message("one", "partial:assistant")["content"] == "已经生成的文字"
        assert store.message("one", "partial:assistant")["status"] == "cancelled"
        assert len(main.logger.recent(channel="panel")) == 1

    asyncio.run(run())
    assert closed


@pytest.mark.parametrize("streaming", [True, False])
def test_additional_retrieval_reaches_final_sources_and_saved_messages(isolated, monkeypatch, streaming):
    store, _ = isolated
    source = RetrievedChunk(42, "极坐标的面积元来自雅可比。", 5, {"title": "合成坐标笔记"})
    retriever = SimpleNamespace(search=lambda query, **kw: [source] if query == "极坐标" else [])
    registry = ToolRegistry([SearchKnowledgeBaseTool(retriever)])
    seen = []

    async def chat(messages, **kwargs):
        seen.append(list(messages))
        if not any(m.role == "tool" for m in messages):
            return ChatResult("", [ToolCall("find", "search_knowledge_base", {"query": "极坐标"})], "tool_calls")
        assert "[1]" in messages[-1].content and "雅可比" in messages[-1].content
        return ChatResult("面积元中的 r 来自雅可比。[1]", [], "stop")

    async def stream_chat(messages, **kwargs):
        result = await chat(messages, **kwargs)
        if result.content:
            yield StreamEvent("delta", text=result.content)
        yield StreamEvent("tool_calls" if result.tool_calls else "done", tool_calls=result.tool_calls)

    monkeypatch.setattr(main, "model_client", SimpleNamespace(enabled=True, chat=chat, stream_chat=stream_chat))
    monkeypatch.setattr(main, "retriever", retriever)
    monkeypatch.setattr(main, "tool_registry", registry)
    monkeypatch.setattr(main, "panel_tool_registry", registry)

    async def run():
        if streaming:
            frames = [f async for f in main._panel_stream(main.PanelChatRequest(
                query="为什么要乘r", session_id="rag-citation", use_model=True))]
            events = {f.splitlines()[0][7:]: json.loads(f.split("data: ", 1)[1]) for f in frames}
            assert events["meta"]["sources"] == []
            final = events["final"]
            assert final["sources"][0]["chunk_id"] == 42
            assert events["sources"]["sources"] == final["sources"]
            assert store.message("rag-citation", final["message_id"])["sources"] == final["sources"]
        else:
            response = await main.answer_query("为什么要乘r")
            assert response.sources[0]["chunk_id"] == 42
            assert "[1]" in response.text
        assert len(seen) == 2

    asyncio.run(run())


@pytest.mark.parametrize("streaming", [True, False])
def test_followup_uses_history_only_for_retrieval_keeps_original_user_turn(isolated, monkeypatch, streaming):
    queries = []
    monkeypatch.setattr(main, "retriever", SimpleNamespace(search=lambda q, **kw: queries.append(q) or []))
    main.sessions.append_turn("context-rag", "user", "二重积分怎样使用极坐标换元")
    main.sessions.append_turn("context-rag", "assistant", "面积元需要乘以雅可比。")
    async def run():
        if streaming:
            frames = [f async for f in main._panel_stream(main.PanelChatRequest(
                query="为什么要乘r", session_id="context-rag", use_model=False))]
            assert frames
            assert main.sessions.get_or_create("context-rag").history[-2]["content"] == "为什么要乘r"
        else:
            await main.answer_query("为什么要乘r", use_model=False,
                history=[ModelMessage("user", "二重积分怎样使用极坐标换元")])
        assert len(queries) == 1 and "极坐标" in queries[0]
    asyncio.run(run())


def test_model_failure_preserves_partial_text_without_second_generation(isolated, monkeypatch):
    store, _ = isolated
    retry = AsyncMock(side_effect=AssertionError("Must not regenerate emitted text"))

    async def stream_chat(*args, **kwargs):
        yield StreamEvent("delta", text="已经生成的答案")
        raise ConnectionError("fixture interruption")

    monkeypatch.setattr(main, "model_client", SimpleNamespace(enabled=True, stream_chat=stream_chat,
                                                             stream_complete=retry))

    async def run():
        frames = [frame async for frame in main._panel_stream(main.PanelChatRequest(
            query="解释置信区间", session_id="partial-model", use_model=True))]
        final = next(json.loads(frame.split("data: ", 1)[1]) for frame in frames if "event: final\n" in frame)
        assert final["content"].count("已经生成的答案") == 1
        assert "已中断" in final["content"] and final["status"] == "interrupted"
        assert store.message("partial-model", final["message_id"])["status"] == "interrupted"
        retry.assert_not_called()

    asyncio.run(run())


def test_deferred_canvas_tool_never_calls_builder(monkeypatch):
    builder = AsyncMock(side_effect=AssertionError("Must wait for a click"))
    monkeypatch.setattr("app.skills.canvas_builder.build", builder)
    result = asyncio.run(BuildCanvasTool(SimpleNamespace(enabled=True), defer=True).run("几何演示"))
    assert result.summary["deferred"]
    assert result.artifact_offer["tier"] == "canvas"
    builder.assert_not_called()


def test_model_unavailable_does_not_pass_generic_offline_text_off_as_a_solution(isolated, monkeypatch):
    store, _ = isolated
    async def stream_chat(*args, **kwargs):
        raise ConnectionError("fixture unavailable")
        yield
    monkeypatch.setattr(main, "model_client", SimpleNamespace(enabled=True, stream_chat=stream_chat))
    async def run():
        frames = [frame async for frame in main._panel_stream(main.PanelChatRequest(
            query="求圆的切线和二重积分", session_id="unavailable", use_model=True))]
        final = next(json.loads(frame.split("data: ", 1)[1]) for frame in frames if "event: final\n" in frame)
        assert final["status"] == "interrupted" and "模型暂时未能完成" in final["content"]
        assert "随机变量" not in final["content"]
        assert store.message("unavailable", final["message_id"])["content"] == final["content"]
    asyncio.run(run())


def test_greeting_keeps_model_response_and_skips_background_model_suggestions(isolated, monkeypatch):
    store, service = isolated
    calls = []

    async def stream_chat(messages, **kwargs):
        calls.append(kwargs)
        assert kwargs["thinking"] is False and kwargs["tools"] == []
        assert messages[-1].content == "你好"
        assert "工具能力" not in messages[0].content
        yield StreamEvent("delta", text="你好！有什么想学习的？")
        yield StreamEvent("done", finish_reason="stop")

    discover = AsyncMock()
    monkeypatch.setattr(service, "discover", discover)
    monkeypatch.setattr(main, "model_client", SimpleNamespace(enabled=True, stream_chat=stream_chat))

    async def run():
        frames = [f async for f in main._panel_stream(main.PanelChatRequest(
            query="你好", session_id="greeting", use_model=True))]
        final = next(json.loads(f.split("data: ", 1)[1]) for f in frames if f.startswith("event: final\n"))
        assert final["status"] == "completed" and final["content"] == "你好！有什么想学习的？"
        assert store.message("greeting", final["message_id"])["content"] == final["content"]
        assert len(calls) == 1
        discover.assert_not_called()

    asyncio.run(run())


@pytest.mark.parametrize("status,code,hint", [
    (401, "authentication_failed", "鉴权失败"), (403, "access_denied", "拒绝访问"),
    (404, "model_not_found", "模型或接口路径不存在"), (400, "invalid_request", "参数是否受支持"),
    (429, "rate_limited", "额度不足"), (503, "upstream_error", "上游模型服务异常"),
])
def test_upstream_status_reaches_saved_answer_without_leaking_secrets(isolated, monkeypatch, status, code, hint):
    store, _ = isolated

    async def stream_chat(*args, **kwargs):
        request = httpx.Request("POST", "https://private.invalid/v1?secret=private-key",
                                headers={"Authorization": "Bearer private-key"})
        raise httpx.HTTPStatusError("private-key upstream details", request=request,
                                   response=httpx.Response(status, text="private-key", request=request))
        yield

    monkeypatch.setattr(main, "model_client", SimpleNamespace(enabled=True, stream_chat=stream_chat))

    async def run():
        frames = [f async for f in main._panel_stream(main.PanelChatRequest(
            query="你好", session_id="upstream-failure", use_model=True))]
        final = next(json.loads(f.split("data: ", 1)[1]) for f in frames if f.startswith("event: final\n"))
        assert final["status"] == "interrupted" and hint in final["content"]
        assert final["flags"]["model_error"] == code
        assert final["flags"]["model_http_status"] == status
        assert final["flags"]["model_error_type"] == "HTTPStatusError"
        assert "private-key" not in "".join(frames) and "private.invalid" not in "".join(frames)
        assert store.message("upstream-failure", final["message_id"])["content"] == final["content"]

    asyncio.run(run())


def test_slow_canvas_does_not_block_next_chat_or_change_ownership(isolated, monkeypatch):
    store, service = isolated

    async def run():
        started, release = asyncio.Event(), asyncio.Event()
        mid = seed(store)
        offer = service.collect_offers("one", mid, store.message("one", mid)["content"], "concept")[0]
        spec = plan_artifact("中心极限定理").spec.as_dict()

        async def generate(job):
            started.set()
            await release.wait()
            return spec

        monkeypatch.setattr(service, "_generate", generate)
        async with httpx.AsyncClient(transport=httpx.ASGITransport(app=main.app), base_url="http://test") as client:
            body = {k: offer[k] for k in ("session_id", "message_id", "offer_id")}
            created = await client.post("/api/panel/artifact-jobs", json=body)
            assert created.status_code == 202
            job = created.json()
            await asyncio.wait_for(started.wait(), 1)
            duplicate = (await client.post("/api/panel/artifact-jobs", json=body)).json()
            assert duplicate["job_id"] == job["job_id"]
            reply = await asyncio.wait_for(client.post("/api/panel/chat/stream", json={
                "session_id": "one", "query": "什么是置信区间", "use_model": False,
            }), 5)
            assert "event: final" in reply.text
            assert store.job(job["job_id"])["status"] == "running"
            wrong = await client.post(f"/api/panel/artifact-jobs/{job['job_id']}/cancel", json={"session_id": "other"})
            assert wrong.status_code == 404
            release.set()
            for _ in range(100):
                if store.job(job["job_id"])["status"] == "succeeded":
                    break
                await asyncio.sleep(.01)
            result = store.job(job["job_id"])
            assert result["status"] == "succeeded" and result["message_id"] == mid
            restored = (await client.get("/api/panel/sessions/one/messages")).json()["items"]
            assert len(restored) == 4
            assert restored[1]["artifact_jobs"][0]["artifact"] == spec
            assert restored[3]["artifact_jobs"] == []
        await service.stop()

    asyncio.run(run())


def test_failure_retry_and_queue_cancel_are_independent(isolated, monkeypatch):
    store, service = isolated

    async def run():
        mid = seed(store)
        offer = service.collect_offers("one", mid, "中心极限定理", "concept")[0]
        service.start()
        fail = AsyncMock(side_effect=RuntimeError("fixture"))
        monkeypatch.setattr(service, "_generate", fail)
        job = service.submit("one", mid, offer["offer_id"])
        for _ in range(100):
            if store.job(job["job_id"])["status"] == "failed":
                break
            await asyncio.sleep(.01)
        assert store.job(job["job_id"])["status"] == "failed"
        gate = asyncio.Event()

        async def wait(job):
            await gate.wait()
            return plan_artifact("中心极限定理").spec.as_dict()

        monkeypatch.setattr(service, "_generate", wait)
        retry = service.submit("one", mid, offer["offer_id"], job["job_id"])
        assert retry["job_id"] != job["job_id"]
        assert service.submit("one", mid, offer["offer_id"], job["job_id"])["job_id"] == retry["job_id"]
        for _ in range(100):
            if store.job(retry["job_id"])["status"] == "running":
                break
            await asyncio.sleep(.01)
        second_mid = seed(store, task="queued")
        second_offer = service.collect_offers("one", second_mid, "中心极限定理", "concept")[0]
        queued = service.submit("one", second_mid, second_offer["offer_id"])
        assert queued["status"] == "queued"
        service.cancel("one", queued["job_id"])
        assert store.job(retry["job_id"])["status"] == "running"
        service.cancel("one", retry["job_id"])
        await asyncio.sleep(.02)
        assert store.job(retry["job_id"])["status"] == "cancelled"
        assert store.job(queued["job_id"])["status"] == "cancelled"
        await service.stop()

    asyncio.run(run())


def test_restart_marks_work_interrupted_and_allows_retry(isolated):
    store, service = isolated
    mid = seed(store)
    offer = service.collect_offers("one", mid, "中心极限定理", "concept")[0]
    job = store.create_job("one", mid, offer["offer_id"])
    store.claim_job()
    store.begin_turn("one", "incomplete", "未完成", {})
    reopened = PanelStore(store.path)
    reopened.recover()
    assert reopened.job(job["job_id"])["status"] == "interrupted"
    assert reopened.message("one", "incomplete:assistant")["status"] == "interrupted"
    assert reopened.create_job("one", mid, offer["offer_id"], job["job_id"])["job_id"] != job["job_id"]


def test_candidate_discovery_runs_after_answer_and_never_generates_html(isolated):
    store, _ = isolated

    async def run():
        gate = asyncio.Event()
        mid = seed(store, content="几何中垂直平分线的结构关系")

        async def judge(*args, **kwargs):
            await gate.wait()
            return '{"suitable":true,"title":"垂直平分线"}'

        fake = SimpleNamespace(enabled=True, complete=AsyncMock(side_effect=judge))
        service = ArtifactService(store, fake)
        service.discover("one", mid)
        assert store.artifact_state("one")["checking"] == [mid]
        assert not store.jobs("one")
        gate.set()
        await asyncio.gather(*service.discoveries.values())
        offer = store.offers("one")[0]
        assert offer["message_id"] == mid and offer["tier"] == "canvas"
        assert not store.artifact_state("one")["pending"]
        assert not store.jobs("one")
        await service.stop()

    asyncio.run(run())
