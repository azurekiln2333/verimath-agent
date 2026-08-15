from __future__ import annotations

from dataclasses import dataclass, field, replace
from typing import Any

from app.agents.guard import ContentGuard
from app.artifacts.planner import plan_artifact
from app.skills.method_selector import extract_features, recommend_method, render_recommendation
from app.skills.exercise import generate_exercise, render_exercise
from app.skills.registry import route_for_query
from app.skills.solution_writer import SOLUTION_GUIDE, parse_matrix_literals, try_offline_solution
from app.skills.courseware import generate_courseware, render_courseware_md


@dataclass(frozen=True)
class AgentResponse:
    route: str
    text: str
    requires_clarification: bool = False
    sources: list[dict[str, Any]] = field(default_factory=list)
    flags: dict[str, Any] = field(default_factory=dict)
    # 可视化件。空列表表示这次回答不配图 —— 这是合法且常见的情况，
    # 前端必须能优雅处理（纯文字回答依然完整可用）。
    artifacts: list[dict[str, Any]] = field(default_factory=list)


class TutorRouter:
    def __init__(self, guard: ContentGuard | None = None) -> None:
        self.guard = guard or ContentGuard()

    def answer(self, query: str, retrieved: list[dict[str, Any]] | None = None) -> AgentResponse:
        retrieved = retrieved or []
        guard_result = self.guard.check(query)
        if not guard_result.allowed:
            return AgentResponse(
                route="guard",
                text=guard_result.safe_answer,
                flags={"guard_reason": guard_result.reason},
            )
        route = self.route(query)
        if route == "method_selection":
            response = self._method_selection(query, retrieved)
        elif route == "exercise":
            response = self._exercise(query, retrieved)
        elif route == "solution":
            response = self._solution(query, retrieved)
        elif route == "courseware":
            response = self._courseware(query, retrieved)
        else:
            response = self._concept(query, retrieved)
        return self._attach_artifact(query, response)

    def _attach_artifact(self, query: str, response: AgentResponse) -> AgentResponse:
        """给回答挂上确定性选出的可视化件。

        任何失败都必须静默降级为纯文字 —— 配图是增强，不是回答的前提。
        文字答案已经完整，绝不能因为画图出错而丢掉它。
        """
        try:
            plan = plan_artifact(query, response.route)
        except Exception:
            return response
        if not plan.hit or plan.spec is None:
            return response
        try:
            payload = plan.spec.as_dict()
        except Exception:
            return response
        flags = dict(response.flags)
        flags["artifact_rule"] = plan.matched_rule
        flags["artifact_kind"] = plan.spec.kind
        flags["artifact_tier"] = "deterministic"
        return replace(response, artifacts=[payload], flags=flags)

    def route(self, query: str) -> str:
        """manifest 驱动：skills 注册表关键词优先（产物意图技能在前），
        未命中走内置兜底（method_selection/exercise 的历史关键词，
        保留是为 manifest 漏词时的安全网）。"""
        q = query.lower()
        skill_route = route_for_query(query)
        if skill_route:
            return skill_route
        # 有矩阵字面量但没命中任何词（如「求 [[4,7],[2,6]] 的逆」）：
        # 矩阵在场的 query 几乎必然是线代求解，交给 solution 骨架
        # （其内部会再判断能否离线直答）。
        if parse_matrix_literals(query):
            return "solution"
        if any(k in q for k in ("t检验", "anova", "方差分析", "回归", "logistic", "卡方", "bootstrap",
                                  "假设检验", "统计方法", "用什么检验", "用什么方法", "选什么检验",
                                  "均值比较", "成绩比较", "组比较", "比例比较", "两组比较", "组间比较",
                                  "该用什么", "独立性检验", "相关分析")):
            return "method_selection"
        if any(k in q for k in ("出题", "练习", "每日一题", "讲评", "错题", "组卷")):
            return "exercise"
        return "concept"

    def _solution(self, query: str, sources: list[dict[str, Any]]) -> AgentResponse:
        """逐步解答：题面带矩阵字面量时离线内核直答；否则给引导骨架，
        模型开启后由 agent loop 解析题目并调 linalg_step_solve。"""
        offline = try_offline_solution(query)
        text = offline or SOLUTION_GUIDE
        return AgentResponse(
            route="solution",
            sources=sources,
            text=text,
            flags={"offline_kernel": offline is not None},
        )

    def _courseware(self, query: str, sources: list[dict[str, Any]]) -> AgentResponse:
        cw = generate_courseware(query)
        return AgentResponse(
            route="courseware",
            sources=sources,
            text=render_courseware_md(cw),
            flags={"courseware_source": "template"},
        )

    def _method_selection(self, query: str, sources: list[dict[str, Any]]) -> AgentResponse:
        rec = recommend_method(extract_features(query))
        text = render_recommendation(rec)
        return AgentResponse(
            route="method_selection",
            requires_clarification=not rec.confident,
            sources=sources,
            text=text,
            flags={"needs_design_info": not rec.confident,
                   "recommended_method": rec.primary if rec.confident else ""},
        )

    def _concept(self, query: str, sources: list[dict[str, Any]]) -> AgentResponse:
        if "中心极限定理" in query:
            return AgentResponse(
                route="concept",
                sources=sources,
                text=(
                    "结论先行：中心极限定理说的是，在常见条件下，许多随机变量相加或取平均后，标准化结果会越来越接近正态分布。"
                    "它是用正态近似做抽样推断、置信区间和很多检验的底层理由。\n\n"
                    "适用条件：最经典版本要求随机变量独立同分布，期望和方差存在且方差有限。实际应用里还要警惕强相关、重尾分布、样本量太小或极端离群值。\n\n"
                    "公式/直觉：若 X1,...,Xn 独立同分布，E(Xi)=mu，Var(Xi)=sigma^2，则 "
                    "(sum Xi - n mu)/(sigma sqrt(n)) 会近似服从 N(0,1)。直觉上，很多小随机扰动叠加后，单个扰动的形状被平均掉，整体波动呈钟形。\n\n"
                    "操作步骤：\n"
                    "1. 判断研究对象是不是“和”或“均值”，例如样本均值、总需求、总误差。\n"
                    "2. 检查独立性、同分布近似和方差是否有限。\n"
                    "3. 样本量足够时，用正态近似计算概率、置信区间或检验统计量。\n"
                    "4. 若分布偏态很强或重尾，优先画图、做模拟，必要时用 Bootstrap 或稳健方法。\n\n"
                    "常见误区：中心极限定理不是说“原始数据会变成正态”，而是说“和或均值的标准化分布趋近正态”；也不是样本量一到 30 就自动可靠。\n\n"
                    "下一步练习：试着判断“500 间客房是否会超过电力容量”这类总量概率题为什么能用中心极限定理。"
                ),
            )
        return AgentResponse(
            route="concept",
            sources=sources,
            text=(
                "结论先行：我会用“定义 -> 直觉 -> 公式 -> 例子 -> 易错点”的结构解释统计概念。\n\n"
                f"你问的是：{query.strip() or '一个统计学概念'}\n\n"
                "核心概念：先明确对象是随机变量、样本统计量、参数，还是模型假设。\n\n"
                "直觉说明：统计学通常是在不确定数据中估计规律，并量化这种不确定性。\n\n"
                "操作步骤：\n"
                "1. 写出变量和参数。\n"
                "2. 明确分布或抽样假设。\n"
                "3. 推导或查找对应统计量。\n"
                "4. 用置信区间、效应量和图形解释结果。\n\n"
                "常见陷阱：把样本现象直接当总体规律；把相关关系写成因果关系。"
            ),
        )

    def _exercise(self, query: str, sources: list[dict[str, Any]]) -> AgentResponse:
        ex = generate_exercise(query)
        return AgentResponse(
            route="exercise",
            sources=sources,
            text=render_exercise(ex),
            flags={"exercise_topic": ex.topic,
                   "latex_self_check": ex.self_check_ok},
        )
