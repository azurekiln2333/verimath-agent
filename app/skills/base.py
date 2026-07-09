from __future__ import annotations

from dataclasses import dataclass, field


@dataclass(frozen=True)
class Skill:
    """SkillPack 元数据。keywords 供路由匹配，entrypoint 是模块内纯函数名（仅作展示/文档）。"""

    name: str
    description: str
    keywords: tuple[str, ...] = field(default_factory=tuple)
    entrypoint: str = ""

    def matches(self, query: str) -> bool:
        q = query.lower()
        return any(k.lower() in q for k in self.keywords)
