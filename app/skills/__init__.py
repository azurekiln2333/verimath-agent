"""SkillPack：可组合的教学能力单元。

每个 skill 是一个自包含模块，暴露：
- 元数据（name/description/keywords）供路由与前端展示
- 一个纯函数入口（无副作用，便于离线测试）

skills 不直接碰 A2A/SSE 契约，只产出结构化结果或教学文本，由 router/main 组装。
"""

from app.skills.base import Skill
from app.skills.method_selector import recommend_method, render_recommendation
from app.skills.exercise import generate_exercise
from app.skills.registry import SKILL_REGISTRY, list_skills

__all__ = [
    "Skill",
    "recommend_method",
    "render_recommendation",
    "generate_exercise",
    "SKILL_REGISTRY",
    "list_skills",
]
