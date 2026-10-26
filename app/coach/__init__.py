"""VeriMath 教学脚手架：误概念诊断、帮助阶梯、过程证据。

三个子模块共同回答一个问题 ——
**"我们怎么证明学生真的在变懂，而不是在变依赖？"**

- misconceptions：识别问题里的典型误读，把它变成一句追问；
- ladder：显式化"给多少帮助"，让 AI 不当拐杖；
- store：把每一轮帮助等级与误区触发落盘，形成可审计的学情证据。
"""
from app.coach.ladder import (
    CoachDecision,
    LadderState,
    MAX_LEVEL,
    decide,
    detect_signals,
    ladder_markdown,
    level_instruction,
)
from app.coach.misconceptions import Misconception, diagnose, render_misconceptions
from app.coach.store import LearningEvent, ProcessStore

__all__ = [
    "CoachDecision",
    "LadderState",
    "LearningEvent",
    "MAX_LEVEL",
    "Misconception",
    "ProcessStore",
    "decide",
    "detect_signals",
    "diagnose",
    "ladder_markdown",
    "level_instruction",
    "render_misconceptions",
]
