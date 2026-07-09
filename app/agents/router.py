from __future__ import annotations

from dataclasses import dataclass, field
from typing import Any

from app.agents.guard import ContentGuard
from app.skills.method_selector import extract_features, recommend_method, render_recommendation
from app.skills.exercise import generate_exercise, render_exercise


@dataclass(frozen=True)
class AgentResponse:
    route: str
    text: str
    requires_clarification: bool = False
    sources: list[dict[str, Any]] = field(default_factory=list)
    flags: dict[str, Any] = field(default_factory=dict)


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
            return self._method_selection(query, retrieved)
        if route == "learning_path":
            return self._learning_path(query, retrieved)
        if route == "exercise":
            return self._exercise(query, retrieved)
        return self._concept(query, retrieved)

    def route(self, query: str) -> str:
        q = query.lower()
        if any(k in q for k in ("学习路线", "怎么学", "复习计划", "课程规划", "自学")):
            return "learning_path"
        if any(k in q for k in ("t检验", "anova", "方差分析", "回归", "logistic", "卡方", "bootstrap",
                                 "假设检验", "统计方法", "用什么检验", "用什么方法", "选什么检验",
                                 "均值比较", "成绩比较", "组比较", "比例比较", "两组比较", "组间比较",
                                 "该用什么", "独立性检验", "相关分析")):
            return "method_selection"
        if any(k in q for k in ("出题", "练习", "每日一题", "讲评", "错题", "组卷")):
            return "exercise"
        return "concept"

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

    def _learning_path(self, query: str, sources: list[dict[str, Any]]) -> AgentResponse:
        return AgentResponse(
            route="learning_path",
            sources=sources,
            text=(
                "结论先行：统计本科核心学习路线建议按“概率基础 -> 数理统计 -> 回归建模 -> 计算实现 -> 专题应用”推进。\n\n"
                "1. 概率论：随机变量、分布、期望方差、大数定律、中心极限定理。\n"
                "2. 数理统计：抽样分布、估计、置信区间、假设检验、似然思想。\n"
                "3. 回归与方差分析：线性模型、诊断、ANOVA、Logistic 回归。\n"
                "4. 统计计算：Python/R 数据清洗、可视化、Bootstrap、交叉验证。\n"
                "5. 专题扩展：时间序列、贝叶斯、生存分析、因果推断。\n\n"
                "学习方法：每章固定做三件事：概念卡片、典型题、真实数据小实验。\n\n"
                "下一步练习：告诉我你的年级、已学课程和薄弱点，我给你排 4 周计划。"
            ),
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
