# -*- coding: utf-8 -*-
"""GateCraft 长任务最小状态机（ProjectStore + 阶段门）。"""
from app.projects.store import MAX_ATTEMPTS, STAGES, ProjectStore

__all__ = ["ProjectStore", "STAGES", "MAX_ATTEMPTS"]
