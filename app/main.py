from __future__ import annotations

import asyncio
import re
import uuid
from dataclasses import replace
from typing import Any, AsyncIterator

from pathlib import Path

from fastapi import FastAPI, Request
from fastapi.responses import HTMLResponse, JSONResponse, StreamingResponse
from fastapi.staticfiles import StaticFiles
from pydantic import BaseModel, ValidationError

from app.agents import TutorRouter
from app.agents.router import AgentResponse
from app.logging_store import InteractionLogger
from app.learning_store import LearningStore
from app.model_client import ModelMessage, OpenAICompatibleClient
from app.panel_html import PANEL_HTML
from app.protocol import (
    CLEAR_CONTEXT_METHODS,
    JsonRpcRequest,
    extract_session_id,
    extract_task_id,
    extract_user_text,
    jsonrpc_error,
    jsonrpc_result,
    sse_event,
)
from app.rag.store import KeywordRetriever
from app.security import SignatureVerifier
from app.sessions import SessionStore
from app.settings import settings
from app.skills import list_skills
from app.test_records import TestRecordStore
from app.trace_store import TraceStore

app = FastAPI(title=settings.app_name, version=settings.app_version)

sessions = SessionStore(max_history_turns=settings.max_history_turns, db_path=settings.sqlite_path)
router = TutorRouter()
verifier = SignatureVerifier(settings)
logger = InteractionLogger(settings.sqlite_path)
retriever = KeywordRetriever(settings.sqlite_path)
model_client = OpenAICompatibleClient(settings)
test_records = TestRecordStore(settings.data_dir)
trace_store = TraceStore(settings.trace_sqlite_path)
learning_store = LearningStore(settings.sqlite_path)


def _record_learning(session_id: str, route: str, sources: list[dict[str, Any]]) -> None:
    """学习记录旁路：失败不中断主链（比照 trace 旁路精神）。"""
    try:
        learning_store.record_turn(session_id, route, sources)
    except Exception:
        pass

_STATIC_DIR = Path(__file__).resolve().parent / "static"
if _STATIC_DIR.is_dir():
    app.mount("/static", StaticFiles(directory=str(_STATIC_DIR)), name="static")


class PanelChatRequest(BaseModel):
    query: str
    # None = 沿用该 session 已存偏好；显式值 = 覆盖并回写为新默认
    use_model: bool | None = None
    answer_style: str | None = None
    session_id: str | None = None


def _resolve_prefs(session_id: str, payload: "PanelChatRequest") -> tuple[bool, str]:
    """解析本轮生效的偏好：请求显式值优先并回写默认；否则用 session 已存默认。"""
    state = sessions.get_or_create(session_id)
    if payload.use_model is not None or payload.answer_style is not None:
        state = sessions.set_preferences(
            session_id,
            answer_style=payload.answer_style,
            use_model=payload.use_model,
        )
    return state.use_model, state.answer_style


@app.get("/healthz")
async def healthz() -> dict[str, Any]:
    return {
        "status": "ok",
        "app": settings.app_name,
        "version": settings.app_version,
        "signature_required": settings.enforce_signature,
    }


@app.get("/", response_class=HTMLResponse)
async def index() -> HTMLResponse:
    return HTMLResponse(PANEL_HTML)


@app.get("/dashboard", response_class=HTMLResponse)
async def dashboard() -> HTMLResponse:
    return HTMLResponse(PANEL_HTML)


@app.get("/api/panel/status")
async def panel_status() -> dict[str, Any]:
    return {
        "status": "ok",
        "app": settings.app_name,
        "version": settings.app_version,
        "model": {
            "enabled": model_client.enabled,
            "base": settings.model_api_base,
            "name": settings.model_name,
            "key_present": bool(settings.model_api_key),
        },
        "corpus": retriever.stats(),
        "records": {
            "chat_count": logger.count(channel="panel"),
            "a2a_count": logger.count(channel="a2a"),
            "eval_count": len(test_records.recent_eval_runs(limit=100)),
            "learning_count": learning_store.count(),
        },
        "retrieval_limit": settings.retrieval_limit,
        "signature_required": settings.enforce_signature,
        "skills": list_skills(),
    }


@app.post("/api/panel/chat")
async def panel_chat(payload: PanelChatRequest) -> dict[str, Any]:
    query = payload.query.strip()
    if not query:
        return {
            "status": "empty",
            "route": "none",
            "content": "请输入一个统计学习问题。",
            "sources": [],
            "flags": {},
            "requires_clarification": True,
        }
    task_id = f"panel-{uuid.uuid4().hex}"
    session_id = payload.session_id or "panel"
    use_model, answer_style = _resolve_prefs(session_id, payload)
    trace = trace_store.recorder(
        channel="panel", session_id=session_id, task_id=task_id, query=query, use_model=use_model
    )
    trace.checkpoint("received")
    history = _history_as_messages(session_id)
    response = await answer_query(
        query,
        use_model=use_model,
        answer_style=answer_style,
        history=history,
    )
    await summarize_sources(query, response.sources)
    trace.checkpoint("answering", {"route": response.route})
    response = _attach_trace(response, trace.trace_id)
    sessions.append_turn(session_id, "user", query)
    sessions.append_turn(session_id, "assistant", response.text)
    trace.message("user", query)
    trace.message("assistant", response.text)
    trace.checkpoint("final")
    trace.finish(status="completed", route=response.route, flags=dict(response.flags))
    await trace.flush()
    logger.log(
        session_id=session_id,
        task_id=task_id,
        route=response.route,
        query=query,
        answer=response.text,
        sources=response.sources,
        flags=response.flags,
        channel="panel",
        trace_id=trace.trace_id,
    )
    _record_learning(session_id, response.route, response.sources)
    return {
        "task_id": task_id,
        "status": "input_required" if response.requires_clarification else "completed",
        "route": response.route,
        "content": response.text,
        "sources": response.sources,
        "flags": response.flags,
        "requires_clarification": response.requires_clarification,
    }


@app.get("/api/panel/history")
async def panel_history(limit: int = 20) -> dict[str, Any]:
    return {"items": logger.recent(limit=limit, channel="panel")}


@app.post("/api/panel/chat/stream")
async def panel_chat_stream(payload: PanelChatRequest) -> StreamingResponse:
    """面板真流式：先出检索+骨架（meta），再逐 token 推 LLM 增强（delta），最后 done。
    guard/追问/模型关闭时退回一次性 final。"""
    return StreamingResponse(
        _panel_stream(payload),
        media_type="text/event-stream; charset=utf-8",
        headers={"Cache-Control": "no-cache", "Connection": "keep-alive"},
    )


class ClearContextRequest(BaseModel):
    session_id: str | None = None


@app.post("/api/panel/clear-context")
async def panel_clear_context(payload: ClearContextRequest) -> dict[str, Any]:
    """清空面板会话的多轮上下文（不删历史落库，仅清内存会话）。"""
    session_id = payload.session_id or "panel"
    sessions.clear_context(session_id)
    return {"ok": True, "session_id": session_id}


class RenderFailRequest(BaseModel):
    message: str = ""
    trace_id: str | None = None


@app.post("/api/panel/render-fail")
async def panel_render_fail(payload: RenderFailRequest) -> dict[str, Any]:
    """前端 KaTeX 渲染失败上报，落一条 render_fail trace 事件。"""
    rec = trace_store.recorder(
        channel="panel", session_id="panel", task_id="render-fail", query="", use_model=False
    )
    rec.event("render_fail", {"message": payload.message[:500], "src_trace": payload.trace_id})
    rec.finish(status="completed")
    await rec.flush()
    return {"ok": True}


@app.get("/api/panel/test-runs")
async def panel_test_runs(limit: int = 20) -> dict[str, Any]:
    return {"items": test_records.recent_eval_runs(limit=limit)}


@app.get("/api/panel/session/{session_id}/overview")
async def panel_session_overview(session_id: str, limit: int = 10) -> dict[str, Any]:
    """统一读出：把某 session 的偏好/学习记录/聊天/测试聚合成一个画像。只读，不改既有端点。"""
    state = sessions.get_or_create(session_id)
    profile = learning_store.get_profile(session_id) or {
        "turn_count": 0, "route_counts": {}, "topics": [],
        "last_route": None, "last_active": None,
    }
    chat = [
        item for item in logger.recent(limit=100, channel="panel")
        if item.get("session_id") == session_id
    ][:limit]
    return {
        "session_id": session_id,
        "preferences": {"answer_style": state.answer_style, "use_model": state.use_model},
        "learning": {
            "turn_count": profile["turn_count"],
            "route_counts": profile["route_counts"],
            "topics": profile["topics"],
            "last_route": profile["last_route"],
            "last_active": profile["last_active"],
        },
        "chat": chat,
        "tests": test_records.recent_eval_runs(limit=limit),
    }


@app.post("/a2a", response_model=None)
async def a2a(request: Request) -> JSONResponse | StreamingResponse:
    verification = verifier.verify(request.headers)
    if not verification.ok:
        return JSONResponse(
            status_code=401,
            content=jsonrpc_error(None, 401, "Unauthorized", {"reason": verification.reason}),
        )
    try:
        payload = await request.json()
        rpc = JsonRpcRequest.model_validate(payload)
    except (ValidationError, ValueError) as exc:
        return JSONResponse(
            status_code=400,
            content=jsonrpc_error(None, -32700, "Invalid JSON-RPC request", str(exc)),
        )

    header_session_id = request.headers.get("agent-session-id")
    session = sessions.get_or_create(extract_session_id(rpc.params, header_session_id))

    if rpc.method == "initialize":
        return JSONResponse(
            headers={"agent-session-id": session.session_id},
            content=jsonrpc_result(
                rpc.id,
                {
                    "sessionId": session.session_id,
                    "protocol": "Streamable HTTP + JSON-RPC + SSE",
                    "capabilities": {
                        "streaming": True,
                        "contextCache": True,
                        "taskCancel": True,
                    },
                },
            ),
        )
    if rpc.method == "notifications/initialized":
        return JSONResponse(
            headers={"agent-session-id": session.session_id},
            content=jsonrpc_result(rpc.id, {"ok": True, "sessionId": session.session_id}),
        )
    if rpc.method == "message/stream":
        task_id = extract_task_id(rpc.params) or f"task-{uuid.uuid4().hex}"
        return StreamingResponse(
            _stream_message(rpc, session.session_id, task_id),
            media_type="text/event-stream; charset=utf-8",
            headers={
                "Cache-Control": "no-cache",
                "Connection": "keep-alive",
                "agent-session-id": session.session_id,
            },
        )
    if rpc.method == "tasks/cancel":
        task_id = extract_task_id(rpc.params)
        if task_id:
            sessions.cancel(session.session_id, task_id)
        return JSONResponse(
            headers={"agent-session-id": session.session_id},
            content=jsonrpc_result(rpc.id, {"ok": True, "taskId": task_id}),
        )
    if rpc.method in CLEAR_CONTEXT_METHODS:
        sessions.clear_context(session.session_id)
        return JSONResponse(
            headers={"agent-session-id": session.session_id},
            content=jsonrpc_result(rpc.id, {"ok": True, "sessionId": session.session_id}),
        )
    return JSONResponse(
        status_code=404,
        headers={"agent-session-id": session.session_id},
        content=jsonrpc_error(rpc.id, -32601, f"Method not found: {rpc.method}"),
    )


async def _stream_message(
    rpc: JsonRpcRequest,
    session_id: str,
    task_id: str,
) -> AsyncIterator[str]:
    query = extract_user_text(rpc.params)
    if not query:
        query = "请说明你想学习的统计学主题。"
    use_model = extract_use_model(rpc.params)
    trace = trace_store.recorder(
        channel="a2a", session_id=session_id, task_id=task_id, query=query, use_model=use_model
    )
    yield sse_event(
        "status",
        jsonrpc_result(rpc.id, {"taskId": task_id, "status": "received"}),
    )
    trace.checkpoint("received")
    await asyncio.sleep(0.01)
    if sessions.is_cancelled(session_id, task_id):
        trace.finish(status="cancelled")
        await trace.flush()
        yield sse_event("final", jsonrpc_result(rpc.id, {"taskId": task_id, "status": "cancelled"}))
        return

    yield sse_event(
        "status",
        jsonrpc_result(rpc.id, {"taskId": task_id, "status": "retrieving"}),
    )
    trace.checkpoint("retrieving")
    span = trace.start_tool_run("rag_retrieve", {"query": query, "limit": settings.retrieval_limit})
    retrieved = [chunk.as_dict() for chunk in retriever.search(query, limit=settings.retrieval_limit)]
    trace.finish_tool_run(span, status="ok", output={"hits": len(retrieved)})
    trace.event("retrieval", {"hits": len(retrieved)})
    await asyncio.sleep(0.01)
    if sessions.is_cancelled(session_id, task_id):
        trace.finish(status="cancelled")
        await trace.flush()
        yield sse_event("final", jsonrpc_result(rpc.id, {"taskId": task_id, "status": "cancelled"}))
        return

    history = _history_as_messages(session_id)
    response = await answer_query(
        query, retrieved=retrieved, use_model=use_model, history=history
    )
    await summarize_sources(query, response.sources)
    trace.checkpoint("answering", {"route": response.route})
    response = _attach_trace(response, trace.trace_id)
    sessions.append_turn(session_id, "user", query)
    sessions.append_turn(session_id, "assistant", response.text)
    trace.message("user", query)
    trace.message("assistant", response.text)
    logger.log(
        session_id=session_id,
        task_id=task_id,
        route=response.route,
        query=query,
        answer=response.text,
        sources=response.sources,
        flags=response.flags,
        trace_id=trace.trace_id,
    )
    _record_learning(session_id, response.route, response.sources)
    yield sse_event(
        "message",
        jsonrpc_result(
            rpc.id,
            {
                "taskId": task_id,
                "status": "input_required" if response.requires_clarification else "answering",
                "route": response.route,
                "content": response.text,
                "sources": response.sources,
                "flags": response.flags,
            },
        ),
    )
    yield sse_event(
        "final",
        jsonrpc_result(
            rpc.id,
            {
                "taskId": task_id,
                "status": "completed",
                "route": response.route,
                "content": response.text,
                "sources": response.sources,
                "flags": response.flags,
            },
        ),
    )
    trace.checkpoint("final")
    trace.finish(status="completed", route=response.route, flags=dict(response.flags))
    await trace.flush()


def _attach_trace(response: AgentResponse, trace_id: str) -> AgentResponse:
    flags = dict(response.flags)
    flags["trace_id"] = trace_id
    return replace(response, flags=flags)


async def _panel_stream(payload: PanelChatRequest) -> AsyncIterator[str]:
    query = payload.query.strip()
    if not query:
        yield sse_event("final", {"status": "empty", "route": "none",
                                  "content": "请输入一个统计学习问题。", "sources": [],
                                  "flags": {}, "requires_clarification": True})
        return
    task_id = f"panel-{uuid.uuid4().hex}"
    session_id = payload.session_id or "panel"
    use_model, answer_style = _resolve_prefs(session_id, payload)
    style = normalize_answer_style(answer_style)
    trace = trace_store.recorder(
        channel="panel", session_id=session_id, task_id=task_id, query=query, use_model=use_model
    )
    trace.checkpoint("received")
    span = trace.start_tool_run("rag_retrieve", {"query": query, "limit": settings.retrieval_limit})
    retrieved = [chunk.as_dict() for chunk in retriever.search(query, limit=settings.retrieval_limit)]
    trace.finish_tool_run(span, status="ok", output={"hits": len(retrieved)})
    trace.event("retrieval", {"hits": len(retrieved)})

    skeleton = apply_answer_style_flag(router.answer(query, retrieved), answer_style)
    skeleton = _attach_trace(skeleton, trace.trace_id)
    # meta 先行：先填确定性回退卡片，前端立刻拿到可读来源，不等 LLM 摘要
    fill_fallback_cards(skeleton.sources)
    yield sse_event("meta", {"taskId": task_id, "route": skeleton.route,
                             "sources": skeleton.sources, "flags": skeleton.flags,
                             "requires_clarification": skeleton.requires_clarification})

    can_stream = (
        use_model and model_client.enabled
        and skeleton.route != "guard" and not skeleton.requires_clarification
    )
    # LLM 摘要卡片与答案流并发：摘要在后台跑，不拖慢首 token
    card_task = None
    if skeleton.sources and model_client.enabled:
        card_task = asyncio.create_task(summarize_sources(query, skeleton.sources))
    history = _history_as_messages(session_id)
    final_text = skeleton.text
    if can_stream:
        final_text = ""
        trace.checkpoint("answering", {"route": skeleton.route})
        mspan = trace.start_tool_run("model_stream", {"messages": len(history) + 2})
        try:
            messages = build_model_messages(query, skeleton, style, history)
            async for delta in model_client.stream_complete(messages):
                final_text += delta
                yield sse_event("delta", {"text": delta})
            trace.finish_tool_run(mspan, status="ok", output={"chars": len(final_text)})
            skeleton = replace(skeleton, flags={**skeleton.flags, "model_used": True})
        except Exception as exc:
            trace.finish_tool_run(mspan, status="error", error_type=type(exc).__name__)
            final_text = skeleton.text  # 流式失败回退骨架
            yield sse_event("delta", {"text": final_text})
            skeleton = replace(skeleton, flags={**skeleton.flags, "model_used": False,
                                                "model_error": type(exc).__name__})
    else:
        yield sse_event("delta", {"text": final_text})

    # 等 LLM 摘要卡片完成（多半已在流式期间跑完），失败时回退卡片仍在
    if card_task is not None:
        try:
            await card_task
        except Exception:
            pass

    yield sse_event("final", {"taskId": task_id, "status": "completed",
                              "route": skeleton.route, "content": final_text,
                              "sources": skeleton.sources, "flags": skeleton.flags,
                              "requires_clarification": skeleton.requires_clarification})
    trace.message("user", query)
    trace.message("assistant", final_text)
    trace.checkpoint("final")
    trace.finish(status="completed", route=skeleton.route, flags=dict(skeleton.flags))
    await trace.flush()
    sessions.append_turn(session_id, "user", query)
    sessions.append_turn(session_id, "assistant", final_text)
    logger.log(session_id=session_id, task_id=task_id, route=skeleton.route, query=query,
               answer=final_text, sources=skeleton.sources, flags=skeleton.flags,
               channel="panel", trace_id=trace.trace_id)
    _record_learning(session_id, skeleton.route, skeleton.sources)


def _history_as_messages(session_id: str | None) -> list[ModelMessage]:
    """把会话已存的轮次转成 ModelMessage，喂给模型做多轮上下文。
    仅取 user/assistant 轮，SessionStore 已按 max_history_turns 截断。"""
    if not session_id:
        return []
    state = sessions.get_or_create(session_id)
    messages: list[ModelMessage] = []
    for turn in state.history:
        role = turn.get("role")
        content = turn.get("content", "")
        if role in {"user", "assistant"} and content:
            messages.append(ModelMessage(role=role, content=content))
    return messages


def extract_use_model(params: Any) -> bool:
    if not isinstance(params, dict):
        return True
    value = params.get("useModel", params.get("use_model", True))
    if isinstance(value, bool):
        return value
    if isinstance(value, str):
        return value.lower() not in {"0", "false", "no", "off"}
    return True


async def answer_query(
    query: str,
    retrieved: list[dict[str, Any]] | None = None,
    use_model: bool = True,
    answer_style: str = "rigorous",
    history: list[ModelMessage] | None = None,
) -> AgentResponse:
    if retrieved is None:
        retrieved = [chunk.as_dict() for chunk in retriever.search(query, limit=settings.retrieval_limit)]
    response = router.answer(query, retrieved)
    response = apply_answer_style_flag(response, answer_style)
    if use_model:
        response = await enhance_with_model(
            query, response, normalize_answer_style(answer_style), history=history
        )
    return response


async def enhance_with_model(
    query: str,
    response: AgentResponse,
    answer_style: str = "rigorous",
    history: list[ModelMessage] | None = None,
) -> AgentResponse:
    if not model_client.enabled or response.route == "guard" or response.requires_clarification:
        return response
    try:
        answer = await model_client.complete(build_model_messages(query, response, answer_style, history))
    except Exception as exc:
        flags = dict(response.flags)
        flags["model_used"] = False
        flags["model_error"] = type(exc).__name__
        return replace(response, flags=flags)
    flags = dict(response.flags)
    flags["model_used"] = True
    return replace(response, text=answer, flags=flags)


def fill_fallback_cards(sources: list[dict[str, Any]]) -> None:
    """同步填入确定性回退卡片（excerpt/截断文本），供 meta 立即展示，不阻塞。"""
    for src in sources:
        src.setdefault("card", src.get("excerpt") or str(src.get("text", ""))[:160])


async def summarize_sources(
    query: str, sources: list[dict[str, Any]]
) -> list[dict[str, Any]]:
    """给每条命中来源生成一句话中文引用卡片（card 字段）。
    模型关闭/失败/解析不全时，逐条回退到 excerpt（离线确定性），保证永远有可读卡片。"""
    if not sources:
        return sources
    # 先给所有来源填好确定性回退卡片
    for src in sources:
        src.setdefault("card", src.get("excerpt") or str(src.get("text", ""))[:160])
    if not model_client.enabled:
        return sources
    numbered = []
    for i, src in enumerate(sources, start=1):
        meta = src.get("metadata", {})
        body = (src.get("excerpt") or str(src.get("text", "")))[:400]
        numbered.append(f"[{i}] 主题={meta.get('topic', '未知')}；内容：{body}")
    prompt = (
        "下面是检索到的资料片段（可能含 PDF 抽取噪音、公式乱码）。"
        "针对用户问题，为每条用一句话中文说明它讲了什么、和问题的关系。"
        "严格按 `编号. 摘要` 逐行输出，不加多余解释，不编造资料没有的内容。\n\n"
        f"用户问题：{query}\n\n资料：\n" + "\n".join(numbered)
    )
    messages = [
        ModelMessage(role="system", content="你是严谨的资料摘要助手，只做客观概括。"),
        ModelMessage(role="user", content=prompt),
    ]
    try:
        raw = await model_client.complete(messages)
    except Exception:
        return sources  # 回退卡片已就位
    cards = _parse_numbered_cards(raw, len(sources))
    for i, src in enumerate(sources):
        if cards.get(i):
            src["card"] = cards[i]
    return sources


def _parse_numbered_cards(raw: str, n: int) -> dict[int, str]:
    """解析分行摘要，返回 {0-based index: 摘要}。支持四种编号形式：
    `1. xxx`、`[1]. xxx`、`[1] xxx`（方括号+空格无分隔符）、`[1]xxx`。
    裸数字（无方括号）仍必须带分隔符，避免误吞 `3 个苹果` 这类正文行。"""
    out: dict[int, str] = {}
    # 方括号形式分隔符可选（括号本身即分隔）；裸数字形式必须带分隔符。
    pattern = re.compile(r"^(?:\[(\d+)\][\.、:：)]?|(\d+)[\.、:：)])\s*(.+)$")
    for line in raw.splitlines():
        line = line.strip()
        m = pattern.match(line)
        if not m:
            continue
        num = m.group(1) or m.group(2)
        idx = int(num) - 1
        content = m.group(3).strip()
        if 0 <= idx < n and content:
            out[idx] = content
    return out


def build_model_messages(
    query: str,
    response: AgentResponse,
    answer_style: str = "rigorous",
    history: list[ModelMessage] | None = None,
) -> list[ModelMessage]:
    source_text = format_sources_for_prompt(response.sources)
    style_instruction = answer_style_instruction(answer_style)
    cite_rule = citation_instruction(response.sources)
    system = (
        "你是一个面向统计学本科生的学习导师。回答必须严谨、中文、可教学，"
        "不能代写作业，不能输出未授权教材原文，不能把相关说成因果。"
        "如果资料不足，要明确说明并给出下一步提问。"
        "不要使用表情符号，不要寒暄。不要把经验规则说成定理，尤其不要说样本量大于30就能保证正态近似。"
        "所有数学公式必须使用 LaTeX 分隔符：行内公式用 \\(...\\)，独立公式用 \\[...\\]。"
        "不要把公式放进反引号代码块，不要裸写 \\frac、\\sum、\\bar 等命令。"
    )
    user = (
        f"学生问题：{query}\n\n"
        f"路由能力：{response.route}\n\n"
        f"规则导师骨架答案：\n{response.text}\n\n"
        f"可引用资料片段：\n{source_text or '无本地资料命中'}\n\n"
        "请在不改变骨架结论的前提下，按以下模板输出：\n"
        "1. 结论先行\n"
        "2. 适用条件\n"
        "3. 公式/直觉\n"
        "4. 操作步骤\n"
        "5. 常见误区\n"
        "6. 下一步练习\n"
        f"回答偏好：{style_instruction}\n"
        f"{cite_rule}"
    )
    return [
        ModelMessage(role="system", content=system),
        *(history or []),
        ModelMessage(role="user", content=user),
    ]


def normalize_answer_style(answer_style: str) -> str:
    if answer_style in {"examples", "concise"}:
        return answer_style
    return "rigorous"


def apply_answer_style_flag(response: AgentResponse, answer_style: str) -> AgentResponse:
    flags = dict(response.flags)
    flags["answer_style"] = normalize_answer_style(answer_style)
    return replace(response, flags=flags)


def answer_style_instruction(answer_style: str) -> str:
    style = normalize_answer_style(answer_style)
    if style == "examples":
        return "在保持数学严谨的前提下，多用具体例子、反例和类比，公式后必须配一个可理解的实例。"
    if style == "concise":
        return "节省时间，先给结论，压缩解释，只保留必要公式、关键条件和一个最小例子。"
    return "严谨优先，面向理学专业学生，必须说明定义、条件、公式、推导直觉、适用边界和常见误区。"


def format_sources_for_prompt(sources: list[dict[str, Any]]) -> str:
    lines: list[str] = []
    for index, source in enumerate(sources[:3], start=1):
        metadata = source.get("metadata", {})
        text = str(source.get("text", ""))[:500]
        lines.append(
            "\n".join(
                [
                    f"[{index}] source_category={metadata.get('source_category', '本地资料')}; "
                    f"course={metadata.get('course', 'unknown')}; "
                    f"topic={metadata.get('topic', 'unknown')}; "
                    f"doc_type={metadata.get('doc_type', 'unknown')}; "
                    f"ingest={metadata.get('ingest_policy', 'unknown')}; "
                    f"license={metadata.get('license_status', 'unknown')}",
                    text,
                ]
            )
        )
    return "\n\n".join(lines)


def citation_instruction(sources: list[dict[str, Any]]) -> str:
    """根据是否有本地命中，给模型不同的引用纪律。这是防幻觉的核心约束。"""
    if not sources:
        return (
            "重要：本次检索在本地知识库没有命中任何资料。"
            "你必须在答案开头明确写出「本地资料未覆盖此问题，以下为通用知识」，"
            "不得编造引用编号，不得假装引用了本地资料。"
        )
    return (
        "引用纪律：上面每段资料带有 [1][2][3] 编号。"
        "当你使用某段资料的内容时，必须在该句末尾标注对应编号（如 [1]）。"
        "不要引用未提供的编号，不要长段复制原文，只做概括并标注来源。"
        "若某个结论没有本地资料支撑，明说这是通用知识而非来自本地库。"
    )
