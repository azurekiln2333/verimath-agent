from __future__ import annotations

import asyncio
import json
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
from app.agents.artifact_agent import generate_spec as generate_tier2_spec
from app.agents.router import AgentResponse
from app.artifacts.planner import plan_artifact
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
from app.rag.loaders import RawDocument, chunk_document
from app.rag.store import KeywordRetriever
from app.security import SignatureVerifier
from app.sessions import SessionStore, estimate_tokens
from app.settings import settings
from app.skills import list_skills
from app.skills.exercise import generate_exercise_with_model, render_exercise
from app.test_records import TestRecordStore
from app.tools import build_tool_registry
from app.trace_store import TraceStore

app = FastAPI(title=settings.app_name, version=settings.app_version)

sessions = SessionStore(max_history_turns=settings.max_history_turns, db_path=settings.sqlite_path)
router = TutorRouter()
verifier = SignatureVerifier(settings)
logger = InteractionLogger(settings.sqlite_path)
retriever = KeywordRetriever(settings.sqlite_path)
model_client = OpenAICompatibleClient(settings)
# Agent 工具集：把绘图/出题/选方法/查库/生成HTML组件 封装为模型可调用工具。
# 依赖注入共享的 retriever 与 model_client；模型关闭时工具仍可调用（除依赖模型的那几个）。
tool_registry = build_tool_registry(retriever, model_client, retrieval_limit=settings.retrieval_limit)
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
            "artifacts": [],
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
    profile_text = format_profile_for_prompt(learning_store.get_profile(session_id))
    response = await answer_query(
        query,
        use_model=use_model,
        answer_style=answer_style,
        history=history,
        profile_text=profile_text,
    )
    await summarize_sources(query, response.sources)
    trace.checkpoint("answering", {"route": response.route})
    response = _attach_trace(response, trace.trace_id)
    sessions.append_turn(session_id, "user", query)
    sessions.append_turn(session_id, "assistant", response.text)
    _fire_and_forget_summary(session_id)
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
        "artifacts": response.artifacts,
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


class CancelRequest(BaseModel):
    task_id: str
    session_id: str | None = None


@app.post("/api/panel/cancel")
async def panel_cancel(payload: CancelRequest) -> dict[str, Any]:
    """提前结束对话：注册取消信号，正在运行的 agent 循环/流式会在下次检查点中断。"""
    session_id = payload.session_id or "panel"
    sessions.cancel(session_id, payload.task_id)
    return {"ok": True, "task_id": payload.task_id, "session_id": session_id}


class ArtifactRequest(BaseModel):
    query: str
    route: str = "concept"
    spec: dict[str, Any] | None = None   # 若前端已持有确定性 spec，直接回放


@app.post("/api/panel/artifact")
async def panel_artifact(payload: ArtifactRequest) -> dict[str, Any]:
    """按需生成可视化组件：用户点击「生成可视化」按钮后调用。
    优先级：前端传入 spec > Tier1 确定性规则 > Tier2/Canvas 模型生成。"""
    # 1) 前端已持有 spec（Tier1 命中时 offer 带 spec）→ 直接回放
    if payload.spec and payload.spec.get("kind"):
        return {"ok": True, "artifact": payload.spec}
    # 2) Tier1 确定性规则
    try:
        plan = plan_artifact(payload.query, payload.route)
        if plan.hit and plan.spec is not None:
            return {"ok": True, "artifact": plan.spec.as_dict(),
                    "tier": "deterministic", "rule": plan.matched_rule}
    except Exception:
        pass
    # 3) Tier2 / Canvas 模型生成
    if model_client.enabled:
        try:
            plan = await generate_tier2_spec(
                payload.query, payload.route, model_client,
                _history_as_messages(None),
            )
            if plan.hit and plan.spec is not None:
                return {"ok": True, "artifact": plan.spec.as_dict(),
                        "tier": "tier2", "rule": plan.matched_rule or "tier2:model"}
        except Exception:
            pass
    return {"ok": False, "detail": "未能生成可视化组件（规则未命中且模型不可用/失败）。"}


class NotesRequest(BaseModel):
    text: str
    course: str = "我的笔记"
    topic: str = ""
    doc_type: str = "self_note"   # self_note 在 score_row 里权重最高，检索优先命中


@app.post("/api/panel/notes")
async def panel_notes(payload: NotesRequest) -> dict[str, Any]:
    """更新知识库：把用户笔记分块后增量入库（不动现有数据）。

    复用 loaders.chunk_document 的段落/句子感知分块；入库后 doc_type=self_note
    会被 score_row 加最高权重，后续提问相关内容时优先命中并标注来源。
    长度上限保护 + 简单清洗，避免恶意或误操作灌入超大内容。
    """
    text = (payload.text or "").strip()
    if not text:
        return {"ok": False, "detail": "笔记内容为空"}
    if len(text) > 50_000:
        return {"ok": False, "detail": "笔记过长（>5万字），请分批提交"}
    doc = RawDocument(
        source=f"self_note:{payload.course}",
        text=text,
        metadata={
            "doc_id": f"self_note-{uuid.uuid4().hex[:8]}",
            "title": payload.topic or payload.course,
            "course": payload.course or "我的笔记",
            "topic": payload.topic or payload.course or "我的笔记",
            "doc_type": payload.doc_type or "self_note",
            "language": "zh",
            "provenance": "self",
            "source": "user_note",
            "ingest_policy": "main",
            "license_status": "self_owned_or_authorized",
        },
    )
    chunks = chunk_document(doc)
    inserted = retriever.add_chunks(chunks)
    return {"ok": True, "chunks": inserted, "course": payload.course, "topic": payload.topic}


@app.get("/api/panel/context")
async def panel_context(session_id: str = "panel") -> dict[str, Any]:
    """返回当前会话的多轮上下文：轮次数、历史消息列表、偏好设置。
    前端用来展示上下文状态，让学生知道模型已经看到了哪些对话。"""
    state = sessions.get_or_create(session_id)
    turns = []
    for turn in state.history:
        role = turn.get("role", "")
        content = turn.get("content", "")
        ts = turn.get("ts", 0)
        if role in {"user", "assistant"} and content:
            # 截断过长内容，前端只需要摘要展示
            preview = content[:200] + ("..." if len(content) > 200 else "")
            turns.append({"role": role, "preview": preview, "ts": ts,
                          "char_count": len(content)})
    return {
        "session_id": session_id,
        "turn_count": len(turns),
        "max_turns": sessions.max_history_turns * 2,
        "answer_style": state.answer_style,
        "use_model": state.use_model,
        "created_at": state.created_at,
        "updated_at": state.updated_at,
        "turns": turns,
    }


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


class FeedbackRequest(BaseModel):
    query: str = ""
    route: str = ""
    trace_id: str | None = None
    feedback: str = "none"   # up / down / none


@app.post("/api/panel/feedback")
async def panel_feedback(payload: FeedbackRequest) -> dict[str, Any]:
    """用户对回答的反馈（👍/👎）。落一条 feedback trace 事件，供后续分析回答质量。
    fire-and-forget 语义：前端不阻塞，后端失败也不影响主链。"""
    fb = (payload.feedback or "none").strip().lower()
    if fb not in {"up", "down", "none"}:
        fb = "none"
    rec = trace_store.recorder(
        channel="panel", session_id="panel", task_id="feedback", query="", use_model=False
    )
    rec.event("feedback", {
        "feedback": fb,
        "route": payload.route,
        "query": payload.query[:500],
        "src_trace": payload.trace_id,
    })
    rec.finish(status="completed")
    await rec.flush()
    return {"ok": True, "feedback": fb}


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
    profile_text = format_profile_for_prompt(learning_store.get_profile(session_id))
    response = await answer_query(
        query, retrieved=retrieved, use_model=use_model, history=history, profile_text=profile_text
    )
    await summarize_sources(query, response.sources)
    trace.checkpoint("answering", {"route": response.route})
    response = _attach_trace(response, trace.trace_id)
    sessions.append_turn(session_id, "user", query)
    sessions.append_turn(session_id, "assistant", response.text)
    _fire_and_forget_summary(session_id)
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
                "artifacts": response.artifacts,
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
                "artifacts": response.artifacts,
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


def build_agent_messages(
    query: str,
    response: AgentResponse,
    answer_style: str = "rigorous",
    history: list[ModelMessage] | None = None,
    profile_text: str | None = None,
) -> list[ModelMessage]:
    """构造 Agent 循环的种子消息：system（含工具使用指导 + 教学排版规范）+ 历史 + user。

    与 build_model_messages 共用来源/引用/风格逻辑，但 system 多了「工具能力」段，
    明确告诉模型可以且应当主动调用工具，并说明组件以按钮形式呈现（不要在文字里硬画）。
    """
    source_text = format_sources_for_prompt(response.sources)
    style_instruction = answer_style_instruction(answer_style)
    cite_rule = citation_instruction(response.sources)
    system = (
        "你是 VeriMath Agent，一个面向统计学本科生的学习导师。语气像一个耐心的师兄：可以适度寒暄、自然口语化，但数学必须严谨。"
        "中文回答，可教学，不能代写作业，不能输出未授权教材原文，不能把相关说成因果。资料不足时明确说明并给出下一步提问。"
        "不要把经验规则说成定理，尤其不要说样本量大于30就能保证正态近似。"
        "\n\n排版规范（决定可读性）：用 Markdown 二级标题 `##` 把回答拆成清晰的知识点小节；每节 2-4 句短段落。"
        "关键公式用独立 `$$...$$` 居中成块；行内公式用 \\(...\\)。直觉/口诀用 `> ` 引用块；易错点用 `**⚠️ 常见误区**`。"
        "\n\n工具能力（核心 —— 你是一个 agent，不是问答机）：你拥有以下工具：plot_distribution（生成可交互分布/检验图）、"
        "generate_exercise（出题）、recommend_method（推荐统计方法）、search_knowledge_base（查本地资料防幻觉）、"
        "build_canvas（生成自定义 HTML 可视化组件，突破固定图上限）、"
        "linalg_step_solve（线性代数逐步计算器：求逆/行列式/特征值/解方程组/基础解系/秩，逐步展示并用 SymPy 复算）。"
        "需要可视化、出题、查本地资料、或要演示/动画时，**主动调用对应工具**，不要凭空用文字描述本该由工具产出的东西。"
        "\n\n数值纪律（硬规则）：**任何数值断言（矩阵结果、行列式、特征值、方程解、统计量）必须先调用计算工具获得，"
        "禁止口算或凭记忆给出计算结果**。工具会返回带 SymPy 复算凭证的逐步结果，你在其上做解释和教学，不改动数值。"
        "简单加减乘除也不例外——你的算术会错，工具不会。"
        "工具结果会回填给你，你据此组织最终回答。可视化组件不会自动展示，会以「生成可视化」按钮呈现，用户点击后才渲染——"
        "所以文字里可以自然地提示「下方可点击查看可视化」。不要为了调用而调用：纯概念解释、澄清提问、闲聊不需要工具。"
        "\n\n对话能力：你能看到完整历史对话（已做滚动摘要），请承接上文深入，必要时主动追问澄清，支持多轮深度探讨。"
        "结尾用一两句口语化小结收束，探讨模式下再抛一个深入问题引导继续。"
    )
    if profile_text:
        system = system + "\n" + profile_text
    user = (
        f"学生问题：{query}\n\n"
        f"路由能力：{response.route}\n\n"
        f"规则导师骨架答案（仅供参考结论，不要照抄结构）：\n{response.text}\n\n"
        f"可引用资料片段：\n{source_text or '无本地资料命中'}\n\n"
        "请按排版规范给出清晰、有层次的回答；需要时主动调用工具增强。"
        f"\n回答偏好：{style_instruction}\n{cite_rule}"
    )
    return [
        ModelMessage(role="system", content=system),
        *(history or []),
        ModelMessage(role="user", content=user),
    ]


def _assistant_tool_msg(text: str, tool_calls: list, reasoning_content: str | None = None) -> ModelMessage:
    """构造 assistant 工具调用消息（带 tool_calls），用于回填进对话历史。
    reasoning_content：DeepSeek 思考模式下，工具调用轮次的思考链必须在后续请求中
    完整回传给 API，否则返回 400。由调用方按轮累加后传入。"""
    return ModelMessage(
        role="assistant",
        content=text or None,
        tool_calls=[
            {
                "id": tc.id,
                "type": "function",
                "function": {
                    "name": tc.name,
                    "arguments": json.dumps(tc.arguments, ensure_ascii=False),
                },
            }
            for tc in tool_calls
        ],
        reasoning_content=reasoning_content,
    )


async def run_agent_loop_stream(
    seed_messages: list[ModelMessage],
    registry,
    session_id: str,
    task_id: str,
    max_iterations: int = 6,
) -> AsyncIterator[tuple[str, dict]]:
    """Agent 循环：调模型→有工具调用就执行→结果回填→再调，直到无工具调用或达上限。

    yield (event_name, data) 供 _panel_stream 转 SSE：
      thinking / delta / tool_call / tool_result / artifact_offer / done / max_iter / cancelled / error
    - thinking：DeepSeek 思考模式的 reasoning_content 增量，先于 delta 到达。
      每轮一个思考块，前端暗色可折叠面板呈现。
    设计借鉴 MathModelAgent 的 CoderAgent.run：while 循环 + max_chat_turns 守卫 +
    assistant(tool_calls)→role=tool 回填；区别在于这里用流式 stream_chat（文本逐 token，
    工具调用在流尾拼装），让前端有打字机效果 + 工具调用过程可见。
    取消：每轮及每个 delta 前检查 sessions.is_cancelled，命中即 yield cancelled 并返回。

    思考模式 + 工具调用：每轮累加的 reasoning_content 必须回传到下一轮的 assistant
    消息（_assistant_tool_msg），否则 DeepSeek API 返回 400。
    """
    messages = list(seed_messages)
    tools_schema = registry.to_openai_schema()
    final_text = ""

    for iteration in range(max_iterations):
        if sessions.is_cancelled(session_id, task_id):
            yield ("cancelled", {})
            return
        turn_text = ""
        turn_reasoning = ""   # 本轮思考链累加，工具调用时需回传给 API
        terminal: tuple[str, Any] | None = None
        try:
            async for ev in model_client.stream_chat(messages, tools=tools_schema, tool_choice="auto"):
                if sessions.is_cancelled(session_id, task_id):
                    yield ("cancelled", {})
                    return
                if ev.type == "thinking":
                    turn_reasoning += ev.text
                    yield ("thinking", {"text": ev.text})
                elif ev.type == "delta":
                    turn_text += ev.text
                    final_text += ev.text
                    yield ("delta", {"text": ev.text})
                elif ev.type == "tool_calls":
                    terminal = ("tool_calls", ev.tool_calls)
                elif ev.type == "done":
                    terminal = ("done", None)
        except asyncio.CancelledError:
            yield ("cancelled", {})
            return
        except Exception as exc:
            yield ("error", {"message": f"{type(exc).__name__}: {exc}"})
            return

        if terminal is None:
            # 流异常中断且无终止事件：用已累积文本收尾
            break

        kind, payload = terminal
        if kind == "done":
            yield ("done", {"text": final_text})
            return

        # tool_calls：assistant 工具调用消息入历史 → 逐个执行 → role=tool 结果回填
        # 思考模式：reasoning_content 必须随 assistant 消息回传，否则 API 400
        tool_calls = payload
        messages.append(_assistant_tool_msg(
            turn_text, tool_calls,
            reasoning_content=turn_reasoning or None,
        ))
        for tc in tool_calls:
            yield ("tool_call", {"id": tc.id, "name": tc.name, "arguments": tc.arguments})
            result = await registry.dispatch(tc.name, tc.arguments)
            ok = "error" not in (result.summary or {})
            yield ("tool_result", {
                "id": tc.id, "name": tc.name,
                "summary": result.summary, "ok": ok,
            })
            if result.artifact_offer:
                yield ("artifact_offer", result.artifact_offer)
            messages.append(ModelMessage(
                role="tool", content=result.content, tool_call_id=tc.id, name=tc.name,
            ))
        # 工具轮的文字（turn_text）作为 agent 的过程旁白保留在 final_text 里，不回退

    # 达迭代上限：把已生成内容交回，由调用方决定是否补说明
    yield ("max_iter", {"text": final_text})


async def _panel_stream(payload: PanelChatRequest) -> AsyncIterator[str]:
    query = payload.query.strip()
    if not query:
        yield sse_event("final", {"status": "empty", "route": "none",
                                  "content": "请输入一个统计学习问题。", "sources": [],
                                  "flags": {}, "artifacts": [],
                                  "requires_clarification": True})
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
    history = _history_as_messages(session_id)
    profile_text = format_profile_for_prompt(learning_store.get_profile(session_id))
    # exercise route：模型结构化生成原创试题替换模板骨架（不流式，一次性下发）
    if (skeleton.route == "exercise" and use_model and model_client.enabled
            and not skeleton.requires_clarification):
        try:
            skeleton = await _enhance_exercise_with_model(query, skeleton, history)
        except Exception:
            pass
    # 组件改为「按需按钮」：meta 不再携带 artifacts（避免一上来就自动渲染图），
    # 所有可视化都通过 artifact_offer 事件下发，前端显示「生成可视化」按钮，用户点击才渲染。
    yield sse_event("meta", {"taskId": task_id, "route": skeleton.route,
                             "sources": skeleton.sources, "flags": skeleton.flags,
                             "artifacts": [],
                             "requires_clarification": skeleton.requires_clarification})

    can_stream = (
        use_model and model_client.enabled
        and skeleton.route != "guard" and not skeleton.requires_clarification
    )
    # exercise 模型题已结构化生成，不再走流式文字增强（避免把试题再被 LLM 改写）
    if skeleton.route == "exercise" and skeleton.flags.get("exercise_source") == "model":
        can_stream = False
    # LLM 摘要卡片与答案流并发：摘要在后台跑，不拖慢首 token
    card_task = None
    if skeleton.sources and model_client.enabled:
        card_task = asyncio.create_task(summarize_sources(query, skeleton.sources))

    final_text = skeleton.text
    offer_emitted = False
    loop_cancelled = False
    if can_stream:
        # Agent 循环：模型可调用工具（绘图/出题/查库/生成HTML组件），工具产出走 artifact_offer。
        final_text = ""
        trace.checkpoint("answering", {"route": skeleton.route, "mode": "agent"})
        mspan = trace.start_tool_run("agent_loop", {"tools": tool_registry.names()})
        try:
            seed = build_agent_messages(query, skeleton, style, history, profile_text)
            async for ev_name, ev_data in run_agent_loop_stream(
                seed, tool_registry, session_id, task_id, max_iterations=6
            ):
                if ev_name == "delta":
                    final_text += ev_data["text"]
                    yield sse_event("delta", {"text": ev_data["text"]})
                elif ev_name == "thinking":
                    # DeepSeek 思考链增量：前端暗色可折叠面板呈现，默认收起
                    yield sse_event("thinking", {"text": ev_data["text"]})
                elif ev_name == "tool_call":
                    yield sse_event("tool_call", ev_data)
                    trace.event("tool_call", ev_data)
                elif ev_name == "tool_result":
                    yield sse_event("tool_result", ev_data)
                    trace.event("tool_result", ev_data)
                elif ev_name == "artifact_offer":
                    offer_emitted = True
                    yield sse_event("artifact_offer", ev_data)
                elif ev_name == "done":
                    pass  # 文本已在 delta 里逐 token 累积
                elif ev_name == "max_iter":
                    if not final_text:
                        final_text = skeleton.text
                        yield sse_event("delta", {"text": final_text})
                    else:
                        note = "\n\n> ⚙️ 已达工具调用次数上限，以上为当前结果。"
                        final_text += note
                        yield sse_event("delta", {"text": note})
                elif ev_name == "cancelled":
                    loop_cancelled = True
                    break
                elif ev_name == "error":
                    raise RuntimeError(ev_data.get("message", "agent loop error"))
            trace.finish_tool_run(mspan, status="ok", output={"chars": len(final_text)})
            skeleton = replace(skeleton, flags={**skeleton.flags, "model_used": True,
                                                "agent_loop": True})
        except asyncio.CancelledError:
            trace.finish_tool_run(mspan, status="cancelled")
            loop_cancelled = True
            skeleton = replace(skeleton, flags={**skeleton.flags, "model_used": True,
                                                "agent_loop": True, "cancelled": True})
        except Exception as exc:
            # Agent 循环失败 → 回退到纯文本流式（不带工具），再失败回退骨架
            trace.finish_tool_run(mspan, status="error", error_type=type(exc).__name__)
            try:
                final_text = ""
                messages = build_model_messages(query, skeleton, style, history, profile_text)
                async for delta in model_client.stream_complete(messages):
                    if sessions.is_cancelled(session_id, task_id):
                        raise asyncio.CancelledError("用户停止生成")
                    final_text += delta
                    yield sse_event("delta", {"text": delta})
                skeleton = replace(skeleton, flags={**skeleton.flags, "model_used": True,
                                                    "agent_loop": False,
                                                    "model_error": type(exc).__name__})
            except asyncio.CancelledError:
                loop_cancelled = True
                skeleton = replace(skeleton, flags={**skeleton.flags, "model_used": True,
                                                    "cancelled": True})
            except Exception:
                if not final_text:
                    final_text = skeleton.text
                    yield sse_event("delta", {"text": final_text})
                skeleton = replace(skeleton, flags={**skeleton.flags, "model_used": False,
                                                    "model_error": type(exc).__name__})
        # Agent 没产出任何文本（罕见，如模型直接 done 空内容）→ 回退骨架
        if not loop_cancelled and not final_text:
            final_text = skeleton.text
            yield sse_event("delta", {"text": final_text})
    else:
        yield sse_event("delta", {"text": final_text})

    # 非 Agent 路径（exercise/guard/模型关闭/澄清），或 Agent 路径模型没调绘图工具时：
    # 把确定性 Tier1 组件以「生成可视化」按钮形式下发，保证该有的可视化不丢。
    if not offer_emitted and skeleton.artifacts and skeleton.route != "guard":
        for payload in skeleton.artifacts:
            offer = {
                "tier": "deterministic",
                "spec": payload,
                "query": query,
                "route": skeleton.route,
                "title": payload.get("title", "可视化组件"),
                "caption": payload.get("caption", ""),
            }
            yield sse_event("artifact_offer", offer)
            offer_emitted = True

    # 等 LLM 摘要卡片完成（多半已在流式期间跑完），失败时回退卡片仍在
    if card_task is not None:
        try:
            await card_task
        except Exception:
            pass

    yield sse_event("final", {"taskId": task_id,
                              "status": "cancelled" if loop_cancelled else "completed",
                              "route": skeleton.route, "content": final_text,
                              "sources": skeleton.sources, "flags": skeleton.flags,
                              "artifacts": [],
                              "requires_clarification": skeleton.requires_clarification})
    trace.message("user", query)
    trace.message("assistant", final_text)
    trace.checkpoint("final")
    trace.finish(status="completed", route=skeleton.route, flags=dict(skeleton.flags))
    await trace.flush()
    sessions.append_turn(session_id, "user", query)
    sessions.append_turn(session_id, "assistant", final_text)
    _fire_and_forget_summary(session_id)
    logger.log(session_id=session_id, task_id=task_id, route=skeleton.route, query=query,
               answer=final_text, sources=skeleton.sources, flags=skeleton.flags,
               channel="panel", trace_id=trace.trace_id)
    _record_learning(session_id, skeleton.route, skeleton.sources)


def _history_as_messages(session_id: str | None) -> list[ModelMessage]:
    """把会话已存的轮次转成 ModelMessage，喂给模型做多轮上下文。
    顺序：滚动摘要（若有）作首条 system 消息 → 最近轮次按 token 预算从近到远截断。
    summary 永远保留；旧轮次超 context_token_budget 时优先丢弃最旧的，避免模型上下文溢出。"""
    if not session_id:
        return []
    state = sessions.get_or_create(session_id)
    messages: list[ModelMessage] = []
    budget = settings.context_token_budget
    used = 0
    if state.summary:
        summary_msg = ModelMessage("system", f"先前对话摘要（供参考）：{state.summary}")
        used += estimate_tokens(summary_msg.content)
        messages.append(summary_msg)
    # 从最近向最旧累加，超预算即止——保留最近的、丢最旧的
    kept: list[ModelMessage] = []
    for turn in reversed(state.history):
        role = turn.get("role")
        content = turn.get("content", "")
        if role not in {"user", "assistant"} or not content:
            continue
        cost = estimate_tokens(content)
        if used + cost > budget:
            break
        used += cost
        kept.append(ModelMessage(role=role, content=content))
    kept.reverse()
    messages.extend(kept)
    return messages


async def _generate_summary(new_turns_text: str, prev_summary: str) -> str | None:
    """调模型把新增对话并入已有摘要，返回更新后的摘要文本。失败返回 None。"""
    system = (
        "你是统计学习导师的上下文摘要器。把多轮对话压缩成紧凑的中文摘要，"
        "保留：学生问过的主题、已掌握/未理解的点、显式偏好。不编造，不超过 200 字。"
    )
    user = (
        f"已有摘要：\n{prev_summary or '（无）'}\n\n"
        f"新增对话：\n{new_turns_text}\n\n"
        "输出更新后的完整摘要（仅摘要正文，不要标题和解释）。"
    )
    try:
        return await model_client.complete(
            [ModelMessage("system", system), ModelMessage("user", user)]
        )
    except Exception:
        return None


async def maybe_summarize_context(session_id: str) -> None:
    """滚动摘要：history 超过软上限(max_history_turns*2)时，把最旧的超出部分压缩成 summary，
    并从 history pop 出去。模型关闭/失败/未超阈值 → 静默返回，绝不阻塞主链。"""
    try:
        if not session_id or not model_client.enabled:
            return
        state = sessions.get_or_create(session_id)
        soft_cap = sessions.max_history_turns * 2
        turns = state.history
        if len(turns) <= soft_cap:
            return
        # 留最近 soft_cap 条，压缩更旧的
        to_summarize = turns[:-soft_cap] if soft_cap > 0 else list(turns)
        if not to_summarize:
            return
        dialog = "\n".join(
            f"{t.get('role', 'user')}: {str(t.get('content', ''))[:300]}"
            for t in to_summarize if t.get("role") in {"user", "assistant"}
        )
        if not dialog.strip():
            sessions.pop_oldest_turns(session_id, len(to_summarize))
            return
        new_summary = await _generate_summary(dialog, state.summary)
        if not new_summary:
            return  # 摘要失败，保留原文，下一轮再试
        sessions.set_summary(session_id, new_summary.strip())
        sessions.pop_oldest_turns(session_id, len(to_summarize))
    except Exception:
        # 旁路任务：任何异常都静默，绝不影响主链（下一轮还会再试）
        pass


def _fire_and_forget_summary(session_id: str) -> None:
    """旁路触发上下文摘要：失败/无事件循环都不影响主链。下一轮才会用上新摘要。"""
    try:
        loop = asyncio.get_running_loop()
    except RuntimeError:
        return  # 无运行中的事件循环（如同步测试），静默跳过，不创建无用协程
    loop.create_task(maybe_summarize_context(session_id))


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
    profile_text: str | None = None,
) -> AgentResponse:
    """统一回答入口（收敛后唯一编排）：
    骨架 → 可用模型时走 Agent 工具循环（exercise 例外，走结构化生成+验算）→ 失败回退骨架。
    旧的 enhance_with_model 纯润色路径与 _attach_tier2_artifact 兜底路径已删除：
    工具调用能力覆盖两者，且模型可主动查库/算数，不再需要被动喂资料。"""
    if retrieved is None:
        retrieved = [chunk.as_dict() for chunk in retriever.search(query, limit=settings.retrieval_limit)]
    response = router.answer(query, retrieved)
    response = apply_answer_style_flag(response, answer_style)
    if use_model and model_client.enabled and response.route != "guard" and not response.requires_clarification:
        if response.route == "exercise":
            # 试题：结构化模型生成（JSON + latex 自检 + 内核验算），失败回退模板骨架
            response = await _enhance_exercise_with_model(query, response, history)
        elif response.route == "courseware":
            # 课件：结构化七段式生成（JSON + latex 自检 + 例题验算），失败回退骨架
            response = await _enhance_courseware_with_model(query, response, history)
        else:
            response = await _agent_answer(query, response, answer_style, history, profile_text)
    return response


async def _enhance_courseware_with_model(
    query: str,
    response: AgentResponse,
    history: list[ModelMessage] | None,
) -> AgentResponse:
    from app.skills.courseware import generate_courseware_with_model, render_courseware_md
    try:
        cw, _md = await generate_courseware_with_model(query, model_client, history)
    except Exception:
        return response
    if cw.source != "model":
        return response  # 模型未启用或生成失败，保留骨架
    flags = dict(response.flags)
    flags["courseware_source"] = "model"
    flags["latex_self_check"] = cw.self_check_ok
    flags["example_verified"] = cw.example_verified
    return replace(response, text=render_courseware_md(cw), flags=flags)


async def _agent_answer(
    query: str,
    response: AgentResponse,
    answer_style: str,
    history: list[ModelMessage] | None,
    profile_text: str | None,
) -> AgentResponse:
    """非流式 Agent 工具循环（a2a / 非流式面板共用）。失败回退骨架，绝不抛出。"""
    try:
        seed = build_agent_messages(
            query, response, normalize_answer_style(answer_style), history, profile_text
        )
        text, artifacts, model_error = await run_agent_loop(seed, tool_registry)
    except Exception as exc:
        text, artifacts, model_error = "", [], type(exc).__name__
    flags = dict(response.flags)
    if text:
        flags["model_used"] = True
        flags["agent_loop"] = True
        if model_error:
            flags["model_error"] = model_error
        return replace(response, text=text, artifacts=artifacts or response.artifacts, flags=flags)
    flags["model_used"] = False
    if model_error:
        flags["model_error"] = model_error
    return replace(response, flags=flags)


async def run_agent_loop(
    seed_messages: list[ModelMessage],
    registry,
    max_iterations: int = 6,
) -> tuple[str, list[dict[str, Any]], str | None]:
    """非流式 Agent 循环：调模型（带工具）→ 有工具调用就执行回填 → 直到无调用或达上限。

    返回 (最终文本, artifact 列表, 错误名或 None)。与 run_agent_loop_stream 同构，
    供 a2a 与非流式面板使用；思考链 reasoning_content 按轮回传（DeepSeek 400 约束）。
    """
    messages = list(seed_messages)
    tools_schema = registry.to_openai_schema()
    final_text = ""
    artifacts: list[dict[str, Any]] = []

    for _ in range(max_iterations):
        result = await model_client.chat(messages, tools=tools_schema, tool_choice="auto")
        if not result.tool_calls:
            return (result.content or final_text or "").strip() or final_text, artifacts, None
        messages.append(_assistant_tool_msg(
            result.content or "", result.tool_calls,
            reasoning_content=result.reasoning_content,
        ))
        for tc in result.tool_calls:
            tool_result = await registry.dispatch(tc.name, tc.arguments)
            if tool_result.artifact_offer:
                artifacts.append(tool_result.artifact_offer.get("spec", {}))
            messages.append(ModelMessage(
                role="tool", content=tool_result.content, tool_call_id=tc.id, name=tc.name,
            ))
    # 达迭代上限：返回模型最后一段可读文本（若有）
    return final_text, artifacts, "max_iterations"


async def _enhance_exercise_with_model(
    query: str,
    response: AgentResponse,
    history: list[ModelMessage] | None,
) -> AgentResponse:
    """exercise route：用模型生成原创试题替换模板骨架。

    模型生成 + latex 自检，失败/未启用 → 保留 router 给的模板骨架（response 不变）。
    """
    try:
        ex = await generate_exercise_with_model(query, "basic", "", model_client, history)
    except Exception:
        return response
    if ex.source != "model":
        return response  # 模型未启用或自检失败，保留模板骨架
    flags = dict(response.flags)
    flags["exercise_source"] = "model"
    flags["exercise_topic"] = ex.topic
    flags["latex_self_check"] = ex.self_check_ok
    flags["answer_verified"] = ex.answer_verified
    return replace(response, text=render_exercise(ex), flags=flags)


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


def format_profile_for_prompt(profile: dict[str, Any] | None) -> str:
    """把学习画像格式化成简短中文文本，注入 system prompt 供个性化参考。
    profile 为 None/空画像时返回空串（不注入，避免噪音）。"""
    if not profile:
        return ""
    parts: list[str] = []
    turn_count = profile.get("turn_count", 0)
    if turn_count:
        parts.append(f"已累计交互 {turn_count} 轮")
    topics = profile.get("topics") or []
    if topics:
        shown = "、".join(topics[:6])
        more = f"等共 {len(topics)} 个" if len(topics) > 6 else ""
        parts.append(f"近期学过主题：{shown}{more}")
    route_counts = profile.get("route_counts") or {}
    if route_counts:
        top = sorted(route_counts.items(), key=lambda kv: kv[1], reverse=True)
        top_routes = [r for r, _ in top[:3] if r]
        if top_routes:
            parts.append(f"常问能力：{'、'.join(top_routes)}")
    if not parts:
        return ""
    return "学生学习画像（供个性化参考，勿生硬复述）：" + "；".join(parts) + "。"


def build_model_messages(
    query: str,
    response: AgentResponse,
    answer_style: str = "rigorous",
    history: list[ModelMessage] | None = None,
    profile_text: str | None = None,
) -> list[ModelMessage]:
    source_text = format_sources_for_prompt(response.sources)
    style_instruction = answer_style_instruction(answer_style)
    cite_rule = citation_instruction(response.sources)
    system = (
        "你是 VeriMath Agent，一个面向统计学本科生的学习导师。语气像一个耐心的师兄：可以适度寒暄、自然口语化，但数学必须严谨。"
        "中文回答，可教学，不能代写作业，不能输出未授权教材原文，不能把相关说成因果。资料不足时明确说明并给出下一步提问。"
        "不要把经验规则说成定理，尤其不要说样本量大于30就能保证正态近似。"
        "\n\n排版规范（很重要，决定可读性）："
        "用 Markdown 二级标题 `##` 把回答拆成清晰的知识点小节，每节聚焦一个要点；标题简短（如「## 直觉：为什么平方」「## 公式」「## 适用条件」）。"
        "每节用 2-4 句短段落，避免大段密集文字。关键公式用独立 `$$...$$` 居中成块；行内公式用 \\(...\\)。"
        "不要把公式放进反引号代码块，不要裸写 \\frac、\\sum、\\bar 等命令。"
        "直觉、口诀、要点用 `> ` 引用块突出；易错点用 `**⚠️ 常见误区**` 开头单独成段；可用有序/无序列表呈现步骤。"
        "\n\n对话能力：你能看到完整历史对话（已做滚动摘要），请承接上文深入，必要时主动追问澄清，支持多轮深度探讨。"
        "结尾用一两句口语化小结收束，探讨模式下再抛一个深入问题引导继续。"
    )
    if profile_text:
        system = system + "\n" + profile_text
    user = (
        f"学生问题：{query}\n\n"
        f"路由能力：{response.route}\n\n"
        f"规则导师骨架答案（仅供参考结论，不要照抄结构）：\n{response.text}\n\n"
        f"可引用资料片段：\n{source_text or '无本地资料命中'}\n\n"
        "请用上述排版规范给出一份清晰、有层次、可读性高的回答：用 `##` 小节组织知识点，公式独立成块，要点用引用块，易错点用 callout。"
        "不要机械套用固定模板，按问题类型自适应结构（概念题重直觉与对比，步骤题重分步，讨论题重多角度）。"
        f"\n回答偏好：{style_instruction}\n"
        f"{cite_rule}"
    )
    return [
        ModelMessage(role="system", content=system),
        *(history or []),
        ModelMessage(role="user", content=user),
    ]


def normalize_answer_style(answer_style: str) -> str:
    if answer_style in {"examples", "concise", "discuss", "caveman"}:
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
    if style == "caveman":
        return (
            "极简模式：结论先行，删掉寒暄与铺垫，每段不超过 3 句，用短句。"
            "但数学内容绝不压缩：公式必须完整 LaTeX、条件与适用边界必须保留、"
            "单位与数值精确。压缩的只是连接性文字，不是数学。"
        )
    if style == "discuss":
        return "探讨模式：像同行研讨一样多角度展开，主动给出不同视角与反例，结尾抛出一个深入追问引导继续探讨。"
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
