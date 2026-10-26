"""帮助阶梯：提供可解释的教学参考与离线备用提示。

规则按当前问题、尝试和求助信号记录建议等级，供界面展示与模型参考。
在线回答及追问由模型结合会话历史重新生成；用户可以随时要求直接解释、
换例子或完整步骤，等级不限制回答深度。固定提示仅用于离线备用路径。
"""

from __future__ import annotations

import re
from dataclasses import dataclass, field

from app.coach.misconceptions import Misconception

LEVELS = (
    (0, "复述与确认"),
    (1, "认知追问"),
    (2, "结构性提示"),
    (3, "局部示范"),
    (4, "完整解答"),
)

MAX_LEVEL = 4

_STUCK = (
    "不知道", "不会", "不懂", "不明白", "没思路", "卡住", "还是不行", "再讲",
    "看不懂", "直接说答案", "直接给答案", "告诉我答案", "算了",
)
_REQUEST_FULL = ("完整解答", "详细解答", "完整过程", "给我答案", "答案是什么", "怎么做这道",
                 "告诉我答案", "直接说答案", "直接告诉我")
_TRYING = ("我试了", "我算是", "我算到", "我写成", "我得到", "我认为", "是不是", "我猜")
_LEARNING_TASK = (
    "证明", "求解", "求", "解方程", "解方程组", "算出", "计算", "推导", "化简", "判断",
    "几有几个", "有几个根", "练习", "出题", "题目",
)
_EXPLAIN = (
    "什么是", "是什么", "为什么", "怎么理解", "如何理解", "长什么样", "图像", "画",
    "解释", "区别", "含义", "怎么用", "举例", "演示", "可视化", "代码", "帮我"
)


def _is_explain(text: str) -> bool:
    """概念/知识型提问：学生在这类消息里要的是讲解与图示，不是被卡住等提示。

    先剔除"帮我/请/能不能"等礼貌前缀，否则「帮我算行列式」会因为一个"帮"字
    被误判成讲解请求 —— 而它其实是要一个计算结果。
    """
    _EXPLAIN_DEFAULT = (
        "什么是", "是什么", "为什么", "怎么理解", "如何理解", "长什么样", "区别",
        "含义", "怎么用", "举例", "演示", "可视化", "图像",
    )
    _LEARNING = ("证明", "求解", "求出", "解方程", "解方程组",
                 "算出", "计算一下", "计算这个", "推导", "化简", "有几个根")
    q = (text or "").lower()
    q = re.sub(r"^(帮我|帮忙|请|麻烦|能否|可以)\s*(帮我|帮忙)?\s*", "", q)
    # 带等号的是"要证/要求的一个具体式子"（证明 x²-1=(x-1)(x+1)），不是讲解请求：
    # 否则模型会收到"讲解概念"的约束，把证明题讲成知识点，等于变相给了答案。
    if "=" in q:
        return False

    # 计算/证明类请求：即便带了"解释/图表"之类词，学生要的也是能直接核对的结论
    if any(k in q for k in _LEARNING) or re.search(r"帮我?算|算一下|求一下|算这个", q):
        return False
    # 「再讲讲 / 还是不懂」是求助信号，不是知识型提问：不能据此把等级重置为 L2
    if any(k in q for k in _STUCK):
        return False
    # 数值题：有矩阵字面量或纯数值算式 → 直接给结果，别让学生先复述
    if re.search(r"\[\s*\[|=\s*\d+\s*[+\-*/]", q):
        return False
    if any(k in q for k in _EXPLAIN_DEFAULT):
        return True
    # 泛化的"讲一讲/介绍一下/说说/教我"：默认按讲解型处理，而不是按题目辅导
    return any(k in q for k in ("讲一讲", "讲讲", "介绍一下", "说说", "教我", "帮我理解"))


_ATOMIC_MARKERS = ("是不是", "是否", "吗", "代表什么", "是什么意思", "对不对", "正确吗")
_ATOMIC_MAX_LEN = 60

# 选题、选方法、要规划、要材料、问"老师会怎么判分"这类请求：
# 学生要的是一个可执行的结论，不是一道待解的题。
_INTENT_MARKERS = (
    "用什么", "用哪种", "选什么", "怎么选", "如何选", "该用", "应该用", "哪种方法",
    "方法推荐", "学习路线", "怎么学", "复习计划", "学习计划", "学习规划",
    "出题", "出个题", "出一道", "组卷", "课件", "讲评", "错题",
    "查一下", "检索", "资料", "笔记",
)


def _is_learning_intent(text: str) -> bool:
    q = (text or "").lower()
    return any(k in q for k in _INTENT_MARKERS)


def _atomic_question(text: str) -> bool:
    """「p 值是不是 H₀ 为真的概率」—— 问的是一个是非命题，不是一道要去解的题。

    只把短的、带是非标记的句子算作这种问题；长句多半是题面，不该判成此类。
    """
    q = (text or "").strip()
    return len(q) <= _ATOMIC_MAX_LEN and any(k in q for k in _ATOMIC_MARKERS)


@dataclass
class LadderState:
    """一个学习会话里的帮助阶梯状态（持久化在学习档案里）。"""

    level: int = 0
    turns_at_level: int = 0

    def describe(self) -> str:
        name = dict(LEVELS).get(self.level, "")
        return f"L{self.level} · {name}"

    def advance(self) -> int:
        """升一级（带上限）。返回新等级。"""
        self.level = min(MAX_LEVEL, self.level + 1)
        self.turns_at_level = 0
        return self.level

    def reset(self) -> None:
        self.level = 0
        self.turns_at_level = 0


@dataclass(frozen=True)
class CoachDecision:
    """这一轮该给到什么帮助，以及为什么（原因要能给人看，评审才信）。

    reason 用于解释规则建议；在线界面优先展示模型本轮生成的学习提示。
    """

    level: int
    level_name: str
    reason: str
    advanced: bool = False
    # 给学生的一句话（可直接作为回答的开头段落）
    opener: str = ""
    # 本轮要问的那一个问题（L1 用）；空串表示不限制为单问
    question: str = ""
    hints: list[str] = field(default_factory=list)


def detect_signals(text: str) -> dict[str, bool]:
    q = (text or "").lower()
    return {
        "stuck": any(k in q for k in _STUCK),
        "request_full": any(k in q for k in _REQUEST_FULL),
        "trying": any(k in q for k in _TRYING),
        "explain": _is_explain(text),
        "learning_intent": _is_learning_intent(text),
        "misconception_question": _atomic_question(text),
        "question": "?" in q or "？" in q or any(k in q for k in ("为什么", "怎么", "如何", "吗")),
    }


def decide(
    state: LadderState,
    text: str,
    misconceptions: list[Misconception] | None = None,
) -> CoachDecision:
    """决定本轮帮助等级。规则全部可读、可测，不调用模型。

    升级：学生明确卡住且已在该级至少停留一轮 → 升一级；明确索要完整解答
    且当前 ≥ L2 → 直接到 L4（尊重意愿，但保留"重做一遍"的要求）。
    不升级：学生扔出一个想法（trying）→ 停在当前级并针对该想法追问，
    这比继续加提示更有效（自我解释效应）。
    """
    sig = detect_signals(text)
    misconceptions = misconceptions or []
    start = state.level
    advanced = False
    # 卡住 + 索要答案：按"索要答案"处理（L0 时也给一级示范，其余升到 L4）
    wants_full = sig["request_full"] and sig["stuck"]

    # 三类"直接给":学生不是在求一道题的解法，而是在求证一个具体说法、问一个概念、
    # 或明确要一个数值/方法结论。对这些情形摆出"先复述题意"的题目辅导姿势
    # 只会浪费彼此时间，所以直接给到能给出结论的等级。
    if sig["misconception_question"]:
        state.level = MAX_LEVEL
        advanced = state.level != start
        reason = "学生在求证一个具体命题：直接给出澄清与反例，再追问理解。"
    elif sig["explain"] or sig["learning_intent"]:
        # 概念提问建议 L2：直接讲解，是否追问由模型结合上下文决定。
        # 学习/选题/规划类请求（「两组成绩比较用什么检验」）同样给到结论 ——
        # 对这类问题要求"先复述题意"既不合上下文，也帮不上忙。
        # 只有下面"明确求解一道题"的情形才从 L0 起步。
        state.level = 2
        state.turns_at_level = 0
        advanced = state.level > start
        reason = ("概念/知识型提问：直接讲解，必要时用贴题例子或可视化帮助理解。"
                  if sig["explain"] else
                  "学习/选题/规划类提问：先给结论与理由，需要条件时再具体追问。")
    elif wants_full:
        # 明确索要完整解答。已有一轮以上铺垫 → 直接到 L4（尊重意愿，并要求重做一遍）；
        # 第一轮就开口 → 先给 L3 局部示范，留一次自己接下去的机会。
        state.level = MAX_LEVEL if state.level >= 1 else 3
        state.turns_at_level = 0
        advanced = state.level != start
        reason = ("学生明确要求完整解答：给出完整过程，并要求合上答案重做一遍。"
                  if state.level == MAX_LEVEL else
                  "学生第一轮就索要答案：先做一步示范，剩下的留给他。")
    elif sig["stuck"] and state.turns_at_level >= 1:
        advanced = state.advance() != start
        reason = f"学生在该级停留一轮后仍表示卡住，按阶梯上升一级（{start}→{state.level}）。"
    elif sig["stuck"] and state.turns_at_level == 0:
        reason = "学生表示卡住，但这是本级的第一次尝试：先降低问题难度再问一次，不直接加提示。"
    elif sig["trying"]:
        reason = "学生给出了自己的尝试：保留当前帮助等级，针对他的想法追问，让他把理由说出来。"
    else:
        reason = "常规轮次：维持当前帮助等级。"

    state.turns_at_level += 1

    opener, question, hints = _compose(state.level, text, misconceptions, sig)
    return CoachDecision(
        level=state.level,
        level_name=dict(LEVELS)[state.level],
        reason=reason,
        advanced=advanced,
        opener=opener,
        question=question,
        hints=hints,
    )


def _compose(
    level: int,
    text: str,
    misconceptions: list[Misconception],
    sig: dict[str, bool],
) -> tuple[str, str, list[str]]:
    """按等级生成开场语 / 单问 / 可选提示。文案刻意短，避免抢走思考。"""
    probe = misconceptions[0].probe if misconceptions else ""
    if level == 0:
        opener = "先用你自己的话，把这道题「已知什么、要求什么」各说一句。"
        return opener, "你能用一句话说清楚这道题最后要你求的是什么吗？", []
    if level == 1:
        q = probe or "你卡在具体哪一步？是不知道从哪里下手，还是某一步的规则想不起来？"
        return "先不急着算。我们只弄明白一件事。", q, []
    if level == 2:
        hints = ["把已知条件逐条写下来，标出哪些是「数据」、哪些是「假设」。",
                 "问自己：这里的未知量有几个？它满足哪些关系式？"]
        return ("下面先讲清楚概念和图示；讲完请你用自己的话复述一遍要点。",
                "看完之后，你能用自己的话解释：为什么关键的那个量会这样变化吗？", hints)
    if level == 3:
        hints = ["我演示第一步；第二步与它同类，你照着做，做完发给我。"]
        if probe:
            return "先看一个示范。", probe, hints
        return "先看一个示范。", "", hints
    opener = ("下面是完整解答。看完请合上答案，凭记忆自己重写一遍——"
              "这一步不能省，否则今天会、明天忘。")
    return opener, "", []


def ladder_markdown(decision: CoachDecision) -> str:
    """渲染成一段 Markdown 旁注，供回答末尾展示。"""
    lines = [
        f"> 🪜 **帮助阶梯 {decision.level}/{MAX_LEVEL} · {decision.level_name}**"
        f"——{decision.reason}",
    ]
    if decision.opener:
        lines.append(">")
        lines.append(f"> {decision.opener}")
    if decision.question:
        lines.append(">")
        lines.append(f"> ❓ {decision.question}")
    for h in decision.hints:
        lines.append(f"> - {h}")
    return "\n".join(lines)


def level_instruction(decision: CoachDecision) -> str:
    """Give the model context about support needs without locking it to canned questions."""
    base = (
        f"【教学参考】建议帮助等级 = L{decision.level}（{decision.level_name}）。"
        "这只是辅助信号。每轮结合完整上下文重新理解学生的卡点，重新生成解释或追问。"
        "学生要求直接解释、完整解答或换个例子时应当响应，不要让他反复复述题目。"
        "追问应针对刚才的具体概念、步骤或回答，不能套用固定句式；没有必要时不追问。"
    )
    rules = {
        0: "条件明确时直接给一个有用的起点；只有缺少关键条件才简短澄清。",
        1: "先解释最可能卡住的那一点，必要时再问一个具体的小问题。",
        2: "用直觉和一个贴题的例子讲清关键点，公式只保留理解所必需的。",
        3: "沿着学生上一轮的尝试示范关键一步，解释为什么这样做。",
        4: "直接回答当前问题，必要时给连贯步骤和可核对的依据，不强制添加自检清单。",
    }
    return base + rules.get(decision.level, "")


__all__ = [
    "CoachDecision",
    "LadderState",
    "MAX_LEVEL",
    "LEVELS",
    "decide",
    "detect_signals",
    "ladder_markdown",
    "level_instruction",
]
