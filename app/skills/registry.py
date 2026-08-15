# -*- coding: utf-8 -*-
"""技能注册表（manifest 权威源）。

路由消费方式：TutorRouter.route() 先调 route_for_query()（manifest 关键词
匹配，具体技能排在泛化技能前），未命中再走内置兜底。加技能 = 在此注册
manifest + 写 handler 模块，不再改 router 代码。
"""
from __future__ import annotations

from app.skills.base import Skill


SKILL_REGISTRY: tuple[Skill, ...] = (
    # 顺序即优先级。产物意图技能（出题/课件）排在内容技能（求解）前：
    # 「出一道求逆矩阵的练习题」是出题，「特征值的课件」是课件，
    # 只有不含产物意图词时，矩阵内容词才路由到求解。
    Skill(
        name="exercise",
        description="可验证例题生成：产出原创题干+分步提示+解题大纲，LaTeX 自检 + 内核验算。",
        route="exercise",
        keywords=("出题", "练习", "每日一题", "讲评", "错题", "组卷", "例题"),
        entrypoint="app.skills.exercise:generate_exercise",
    ),
    Skill(
        name="courseware",
        description="课件/讲义生成：七段式结构（动机-定义-定理-例题-误区-练习-小结），LaTeX 自检。",
        route="courseware",
        keywords=("课件", "讲义", "备课", "教学材料", "复习提纲", "知识框架图"),
        entrypoint="app.skills.courseware:generate_courseware",
    ),
    Skill(
        name="solution_writer",
        description="线代逐步解答：贴题即得编号步骤 + 内核精确计算 + SymPy 复算凭证。",
        route="solution",
        keywords=("求逆", "求逆矩阵", "逆矩阵", "行列式", "特征值", "特征向量", "解线性方程组",
                  "线性方程组", "求秩", "基础解系", "列空间", "零空间", "行阶梯", "这道题", "求解矩阵",
                  "矩阵计算", "可对角化", "对角化", "jordan", "若尔当", "若当", "标准形", "二次型",
                  "惯性指数", "符号差", "正定", "负定", "半正定", "配方法", "施密特",
                  "线性相关", "基变换", "过渡矩阵"),
        entrypoint="app.skills.solution_writer:render_solution_guide",
    ),
    Skill(
        name="method_selector",
        description="统计方法选择器：按研究设计走决策树，推荐检验方法并给备选与误区。",
        route="method_selection",
        keywords=("统计方法", "用什么检验", "t检验", "anova", "方差分析", "卡方",
                  "回归", "logistic", "bootstrap", "假设检验", "怎么选"),
        entrypoint="app.skills.method_selector:recommend_method",
    ),
)


def route_for_query(query: str) -> str | None:
    """按 manifest 顺序返回第一个命中的技能路由。全不命中返回 None。"""
    for skill in SKILL_REGISTRY:
        if skill.route and skill.matches(query):
            return skill.route
    return None


def list_skills() -> list[dict[str, object]]:
    """供 /api/panel/status 或文档展示的 skill 清单。"""
    return [
        {"name": s.name, "description": s.description, "route": s.route,
         "keywords": list(s.keywords)}
        for s in SKILL_REGISTRY
    ]
