"""具体工具实现：把现有能力封装成模型可调用的工具。

每个工具持有共享实例（retriever / model_client）的引用，由 build_tool_registry 注入。
工具失败一律降级为一段说明文本（见 ToolRegistry.dispatch），不中断 agent 循环。
"""
from __future__ import annotations

import asyncio
from typing import Any

from app.artifacts.planner import plan_artifact
from app.model_client import ModelMessage, OpenAICompatibleClient
from app.rag.store import KeywordRetriever
from app.skills.exercise import generate_exercise_with_model, render_exercise
from app.skills.method_selector import extract_features, recommend_method, render_recommendation
from app.tools.base import Tool, ToolResult


class PlotDistributionTool:
    """确定性选图：按规则匹配一个可交互 widget spec（Tier1）。
    命中则把 spec 作为 artifact_offer 返回，前端按需渲染。"""

    name = "plot_distribution"

    def schema(self) -> dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": self.name,
                "description": (
                    "为统计概念生成一个可交互的可视化组件（如分布曲线、假设检验、抽样分布等）。"
                    "调用后返回组件说明与可选的可视化 spec。当学生问及具体分布、检验、"
                    "或说『画一个/可视化/演示』时调用。"
                ),
                "parameters": {
                    "type": "object",
                    "properties": {
                        "query": {"type": "string", "description": "学生的原始问题或可视化需求"},
                        "route": {"type": "string", "description": "路由能力，如 concept/exercise/method_selection", "default": "concept"},
                    },
                    "required": ["query"],
                },
            },
        }

    async def run(self, query: str, route: str = "concept", **_: Any) -> ToolResult:
        try:
            plan = plan_artifact(query, route)
        except Exception as exc:
            return ToolResult(
                content=f"选图失败：{exc}。可继续用文字回答。",
                summary={"error": type(exc).__name__},
            )
        if not plan.hit or plan.spec is None:
            return ToolResult(
                content="没有匹配到确定性的可视化规则。可考虑调用 build_canvas 让模型生成自定义 HTML 组件，或继续文字回答。",
                summary={"hit": False, "route": route},
            )
        payload = plan.spec.as_dict()
        return ToolResult(
            content=f"已准备可视化组件「{payload.get('title', '')}」：{payload.get('caption', '')}。组件将以按钮形式呈现，用户点击后渲染。",
            summary={"hit": True, "kind": payload.get("kind"), "rule": plan.matched_rule},
            artifact_offer={
                "tier": "deterministic",
                "spec": payload,
                "query": query,
                "route": route,
                "title": payload.get("title", "可视化组件"),
                "caption": payload.get("caption", ""),
            },
        )


class GenerateExerciseTool:
    """出题工具：让模型按知识点+难度生成原创试题。"""

    name = "generate_exercise"

    def __init__(self, model_client: OpenAICompatibleClient) -> None:
        self.model_client = model_client

    def schema(self) -> dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": self.name,
                "description": (
                    "生成一道统计学练习题（含题干、提示、解题大纲）。当学生要『出题/练习/例题』时调用。"
                    "返回渲染好的题干文本，直接用于回答。"
                ),
                "parameters": {
                    "type": "object",
                    "properties": {
                        "topic": {"type": "string", "description": "题目主题/知识点，如『Welch t 检验』"},
                        "difficulty": {"type": "string", "enum": ["basic", "intermediate", "advanced"], "description": "难度", "default": "basic"},
                    },
                    "required": ["topic"],
                },
            },
        }

    async def run(self, topic: str, difficulty: str = "basic", **_: Any) -> ToolResult:
        ex = await generate_exercise_with_model(topic, difficulty, "", self.model_client, None)
        text = render_exercise(ex)
        return ToolResult(
            content=text,
            summary={"topic": ex.topic, "difficulty": difficulty,
                     "self_check_ok": ex.self_check_ok,
                     "answer_verified": ex.answer_verified},
        )


class RecommendMethodTool:
    """统计方法选择器：按研究设计走决策树推荐检验方法。"""

    name = "recommend_method"

    def schema(self) -> dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": self.name,
                "description": (
                    "按研究设计（变量类型/分组/配对/目标）推荐合适的统计检验或建模方法。"
                    "当学生问『用什么检验/方法/两组比较/相关性』时调用。返回推荐理由与备选。"
                ),
                "parameters": {
                    "type": "object",
                    "properties": {
                        "query": {"type": "string", "description": "学生的方法选择问题"},
                    },
                    "required": ["query"],
                },
            },
        }

    async def run(self, query: str, **_: Any) -> ToolResult:
        features = extract_features(query)
        rec = recommend_method(features)
        text = render_recommendation(rec)
        return ToolResult(
            content=text,
            summary={"primary": rec.primary, "confident": rec.confident},
        )


class SearchKnowledgeBaseTool:
    """检索本地知识库，返回命中片段。防幻觉：让模型基于本地资料回答。"""

    name = "search_knowledge_base"

    def __init__(self, retriever: KeywordRetriever, limit: int = 5) -> None:
        self.retriever = retriever
        self.limit = limit

    def schema(self) -> dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": self.name,
                "description": (
                    "检索本地数学与统计知识库，返回最相关的资料片段（含课程/主题/来源元数据）。"
                    "回答具体概念或需要引用本地资料时调用，确保答案有据可依、可标注来源。"
                    "追问时把指代还原为当前讨论的概念再检索；未命中可以换用更具体的关键词。"
                ),
                "parameters": {
                    "type": "object",
                    "properties": {
                        "query": {"type": "string", "description": "检索关键词或问题"},
                        "limit": {"type": "integer", "minimum": 1, "maximum": 10, "description": "返回片段数", "default": 5},
                    },
                    "required": ["query"],
                },
            },
        }

    async def run(self, query: str, limit: int | None = None, **_: Any) -> ToolResult:
        n = max(1, min(limit if limit is not None else self.limit, 10))
        chunks = await asyncio.to_thread(self.retriever.search, query, limit=n)
        if not chunks:
            return ToolResult(
                content="本次检索未命中相关本地资料，不代表库内没有。可换用相关概念再次检索；已有来源仍然有效，不能编造引用。",
                summary={"hits": 0},
            )
        return ToolResult(
            content="本地知识库检索完成，来源编号由本轮回答统一分配。",
            summary={"hits": len(chunks)},
            sources=[chunk.as_dict() for chunk in chunks],
        )


class BuildCanvasTool:
    """让模型生成自包含 HTML 组件（Canvas 模式），突破固定 widget 上限。"""

    name = "build_canvas"

    def __init__(self, model_client: OpenAICompatibleClient, defer: bool = False) -> None:
        self.model_client = model_client
        self.defer = defer

    def schema(self) -> dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": self.name,
                "description": (
                    "生成一个自定义的可交互 HTML 可视化组件（自包含，含内联 CSS/JS，可用 SVG/canvas）。"
                    "当固定 widget 不足以表达、或学生要『演示/动画/自定义可视化』时调用。"
                    "组件在沙箱 iframe 中渲染，安全隔离。"
                ),
                "parameters": {
                    "type": "object",
                    "properties": {
                        "query": {"type": "string", "description": "可视化需求描述，如『中心极限定理演示，n从1到30』"},
                        "context_hint": {"type": "string", "description": "可选的上下文提示，帮助模型理解当前对话", "default": ""},
                    },
                    "required": ["query"],
                },
            },
        }

    async def run(self, query: str, context_hint: str = "", **_: Any) -> ToolResult:
        if self.defer:
            return ToolResult(
                content="已记录可视化建议。文字回答完成后提供生成按钮，用户点击后后台制作；目前尚未生成图形。",
                summary={"hit": True, "deferred": True},
                artifact_offer={"tier": "canvas", "title": query[:60], "query": query,
                                "context_hint": context_hint, "route": "concept"},
            )
        # 延迟导入避免循环依赖（canvas_builder 可能反向引用 tools）
        from app.skills.canvas_builder import build as build_canvas
        spec = await build_canvas(query, context_hint, self.model_client)
        if spec is None:
            return ToolResult(
                content="自定义 HTML 组件生成失败，请改用文字描述或调用 plot_distribution。",
                summary={"hit": False},
            )
        # fallback_template：模型生成失败/关闭时走了预制模板兜底（canvas_templates）
        tpl = spec.get("fallback_template")
        content = f"已生成自定义可视化组件「{spec.get('title', query)}」。组件将以按钮形式呈现，用户点击后渲染。"
        if tpl:
            content = f"已用预制模板生成可视化组件「{spec.get('title', query)}」（模板兜底：{tpl}）。组件将以按钮形式呈现，用户点击后渲染。"
        return ToolResult(
            content=content,
            summary={"hit": True, "kind": "html_canvas", "fallback_template": tpl},
            artifact_offer={
                "tier": "canvas",
                "spec": spec,
                "query": query,
                "route": "concept",
                "title": spec.get("title", "自定义可视化"),
                "caption": spec.get("caption", "模型生成的可交互 HTML 组件"),
            },
        )


def build_tool_registry(
    retriever: KeywordRetriever,
    model_client: OpenAICompatibleClient,
    retrieval_limit: int = 5,
    defer_canvas: bool = False,
) -> "ToolRegistry":
    """组装默认工具集。依赖注入共享实例，返回就绪的 ToolRegistry。"""
    from app.tools.registry import ToolRegistry
    from app.linalg.tool import LinalgStepSolveTool
    from app.tools.statistics import CalculateStatisticsTool
    from app.tools.calculus import CalculateCalculusTool
    return ToolRegistry([
        PlotDistributionTool(),
        GenerateExerciseTool(model_client),
        RecommendMethodTool(),
        SearchKnowledgeBaseTool(retriever, limit=retrieval_limit),
        BuildCanvasTool(model_client, defer=defer_canvas),
        LinalgStepSolveTool(),
        CalculateStatisticsTool(),
        CalculateCalculusTool(),
    ])
