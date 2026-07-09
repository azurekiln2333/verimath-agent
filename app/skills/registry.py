from __future__ import annotations

from app.skills.base import Skill


SKILL_REGISTRY: tuple[Skill, ...] = (
    Skill(
        name="method_selector",
        description="统计方法选择器：按研究设计（变量类型/分组/配对/目标）走决策树，推荐检验方法并给备选与误区。",
        keywords=("统计方法", "用什么检验", "t检验", "anova", "方差分析", "卡方",
                  "回归", "logistic", "bootstrap", "假设检验", "怎么选"),
        entrypoint="app.skills.method_selector:recommend_method",
    ),
    Skill(
        name="exercise",
        description="可验证例题生成：产出原创题干+分步提示+解题大纲，并用 latex_lint 自检公式可渲染。",
        keywords=("出题", "练习", "每日一题", "讲评", "错题", "组卷", "例题"),
        entrypoint="app.skills.exercise:generate_exercise",
    ),
)


def list_skills() -> list[dict[str, object]]:
    """供 /api/panel/status 或文档展示的 skill 清单。"""
    return [
        {"name": s.name, "description": s.description, "keywords": list(s.keywords)}
        for s in SKILL_REGISTRY
    ]
