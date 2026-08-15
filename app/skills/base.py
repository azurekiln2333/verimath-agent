# -*- coding: utf-8 -*-
from __future__ import annotations

from dataclasses import dataclass, field


@dataclass(frozen=True)
class Skill:
    """SkillPack 元数据（manifest）。

    route：该技能绑定的路由名。keywords 供路由匹配（manifest 驱动，
    加技能不改 router 代码），entrypoint 是模块内函数名（展示/文档用）。
    """

    name: str
    description: str
    route: str = ""
    keywords: tuple[str, ...] = field(default_factory=tuple)
    entrypoint: str = ""

    def matches(self, query: str) -> bool:
        q = query.lower()
        return any(k.lower() in q for k in self.keywords)
