from __future__ import annotations

from dataclasses import dataclass, field, replace

from app.model_client import ModelMessage, OpenAICompatibleClient
from app.render.latex_lint import lint_latex
from app.skills._json_utils import extract_json_object as _extract_json_object


@dataclass(frozen=True)
class Exercise:
    topic: str
    difficulty: str
    problem: str
    hints: tuple[str, ...] = field(default_factory=tuple)
    solution_outline: str = ""
    self_check_ok: bool = True
    self_check_issues: tuple[str, ...] = field(default_factory=tuple)
    qtype: str = ""           # 题型：计算/证明/应用/选择/填空
    source: str = "template"  # template / model（进 trace 便于评测归因）
    answer_verified: bool = False      # 数值答案是否通过内核复算
    verification_note: str = ""        # 验算说明（不一致时给差异）


# 原创题库骨架：按主题给出题干模板 + 分步提示 + 解题大纲（含 LaTeX 公式）。
# 不复刻受版权题库，均为可参数化的原创结构。
_TEMPLATES: dict[str, dict[str, object]] = {
    "clt": {
        "keys": ("中心极限定理", "clt", "抽样分布", "样本均值"),
        "problem": (
            "某酒店有 500 间客房，每间在高峰时段独立地以概率 0.75 用电，"
            "单间用电视为均值 \\(\\mu=1.2\\)、方差 \\(\\sigma^2=0.36\\) 的随机变量。"
            "用中心极限定理估计总用电量超过 \\(620\\) 的近似概率。"
        ),
        "hints": (
            "提示 1：总量是 500 个独立同分布变量之和，判断能否用中心极限定理。",
            "提示 2：写出和的期望 \\(n\\mu\\) 与标准差 \\(\\sigma\\sqrt{n}\\)。",
            "提示 3：标准化后查标准正态分布表。",
        ),
        "solution": (
            "解题大纲：设总量 \\(S=\\sum_{i=1}^{500} X_i\\)，则 \\(E(S)=500\\times1.2=600\\)，"
            "\\(\\mathrm{Var}(S)=500\\times0.36=180\\)，\\(\\mathrm{sd}(S)=\\sqrt{180}\\approx13.4\\)。"
            "标准化：\\[Z=\\frac{S-600}{\\sqrt{180}}.\\] "
            "所求为 \\(P(S>620)=P\\left(Z>\\frac{620-600}{13.4}\\right)\\approx P(Z>1.49)\\approx0.068.\\)"
        ),
    },
    "t_test": {
        "keys": ("t检验", "均值比较", "两组", "welch"),
        "problem": (
            "两个班分别用 A/B 教学法，期末成绩样本量为 \\(n_1=35, n_2=32\\)。"
            "请说明比较两班平均成绩时应检查哪些条件，写出 Welch t 统计量，并说明结论该怎么报告。"
        ),
        "hints": (
            "提示 1：先判断两样本是否独立。",
            "提示 2：检查正态近似、方差是否齐性、有无离群值。",
            "提示 3：Welch 不要求方差相等，写出其统计量与自由度思路。",
        ),
        "solution": (
            "解题大纲：两班为独立样本。Welch t 统计量："
            "\\[t=\\frac{\\bar{X}_1-\\bar{X}_2}{\\sqrt{s_1^2/n_1+s_2^2/n_2}}.\\] "
            "自由度用 Welch–Satterthwaite 近似。报告时给出均值差、95% 置信区间和效应量（如 Cohen's d），不要只给 p 值。"
        ),
    },
}

_DEFAULT_KEY = "clt"


def _select_template(topic: str) -> tuple[str, dict[str, object]]:
    q = topic.lower()
    for key, tpl in _TEMPLATES.items():
        if any(str(k).lower() in q for k in tpl["keys"]):
            return key, tpl
    return _DEFAULT_KEY, _TEMPLATES[_DEFAULT_KEY]


def generate_exercise(topic: str = "", difficulty: str = "basic") -> Exercise:
    """生成原创例题 + 分步提示 + 解题大纲，并用 latex_lint 自检公式可渲染。"""
    key, tpl = _select_template(topic)
    problem = str(tpl["problem"])
    hints = tuple(tpl["hints"])  # type: ignore[arg-type]
    solution = str(tpl["solution"])

    # 自检：解题大纲里的 LaTeX 必须能通过静态检查（分隔符配对、无裸命令、无代码块误入）
    issues_list = lint_latex(problem + "\n" + solution)
    issues = tuple(f"{i.kind}: {i.detail}" for i in issues_list)

    return Exercise(
        topic=key,
        difficulty=difficulty,
        problem=problem,
        hints=hints,
        solution_outline=solution,
        self_check_ok=not issues_list,
        self_check_issues=issues,
    )


def render_exercise(ex: Exercise, include_solution: bool = True) -> str:
    lines = [
        "结论先行：这是一道原创练习题，先自己尝试，再看提示与大纲，不直接给最终答案的代抄版本。",
        "",
        f"题目（{ex.topic}）：{ex.problem}",
        "",
        *ex.hints,
    ]
    if include_solution:
        lines += ["", ex.solution_outline]
    lines += ["", "下一步：告诉我章节、难度和题型，我再生成一组新的原创题。"]
    return "\n".join(lines)


async def generate_exercise_with_model(
    query: str,
    difficulty: str = "basic",
    qtype: str = "",
    model_client: OpenAICompatibleClient | None = None,
    history: list[ModelMessage] | None = None,
) -> Exercise:
    """带数值验算的出题：模型生成 → 内核复算 → 不一致回喂重生成（≤3 轮）。

    GateCraft 数值纪律的落点：题目声称的答案必须被确定性代码重算确认，
    任何一轮失败都回退模板题，保证输出永远可用且数值永远正确。
    answer_check 缺失（非计算题）时跳过验算，仅做 latex 自检。
    """
    if model_client is None or not model_client.enabled:
        return generate_exercise(query, difficulty)
    from app.linalg.tool import verify_answer
    messages: list[ModelMessage] = []
    last_note = ""
    for attempt in range(3):
        try:
            ex, check = await _ask_model_for_exercise_checked(
                query, difficulty, qtype, model_client, history, feedback=last_note
            )
        except Exception:
            return generate_exercise(query, difficulty)
        if ex is None or not ex.self_check_ok:
            last_note = "上次输出 LaTeX 自检未通过，必须严格使用 \\(...\\) 与 \\[...\\] 分隔符。"
            continue
        if check is None:
            return ex  # 非计算题，无 answer_check，格式自检已过
        ok, actual = verify_answer(
            check.get("operation", ""), check.get("matrix", []), check.get("expected", ""),
            b=check.get("b"),
        )
        if ok:
            return replace(ex, answer_verified=True, verification_note="内核复算一致")
        last_note = (
            f"你声称的答案 {check.get('expected')} 与精确复算结果 {actual} 不一致。"
            "重新出题：先在内心用行变换算出真实答案，再填 answer_check。"
        )
    return generate_exercise(query, difficulty)


async def _ask_model_for_exercise_checked(
    query: str,
    difficulty: str,
    qtype: str,
    model_client: OpenAICompatibleClient,
    history: list[ModelMessage] | None,
    feedback: str = "",
) -> tuple[Exercise | None, dict | None]:
    """模型出题（含 answer_check 字段）。feedback 非空时作为纠错消息注入。"""
    system = (
        "你是统计学与线性代数命题专家。按知识点、难度、题型生成一道原创试题。"
        "必须输出 JSON 对象，字段：topic, difficulty, qtype, problem, hints(数组), solution_outline。"
        "要求：\n"
        "1. problem 是题干，含具体情境与数值；solution_outline 是解题大纲，含关键公式与结论。\n"
        "2. 所有数学公式必须用 LaTeX 分隔符：行内 \\(...\\)，独立 \\[...\\]。\n"
        "3. hints 给 2-3 条分步提示，不直接给答案。\n"
        "4. 不要复刻任何受版权题库的原文，必须是原创。\n"
        "5. 计算题（有确定数值答案的）必须额外输出 answer_check 对象："
        '{"operation": "det|rank|inverse|rref|solve|eigen|jordan|quadratic_form", "matrix": [[...]], "expected": "答案", '
        '"b": [..]（仅 solve 需要）}。'
        "expected 格式：det/rank 给数值；inverse/rref 给矩阵串 \"[[a/b, c], ..]\"；"
        "solve 给解向量 \"[x1, x2]\"；eigen 给特征值列表 \"λ1, λ2\"（可用 sqrt 形式）；"
        "jordan 给 J 矩阵串 \"[[a, b], [c, d]]\"；quadratic_form 给惯性指数 \"p,q\" 或正定性关键词。"
        "expected 必须是你精确计算的结果（分数用 a/b 形式）。概念题/证明题省略 answer_check。\n"
        "6. 只输出 JSON，不要解释、不要 Markdown 代码块包裹。"
    )
    user = (
        f"知识点/诉求：{query or '概率论与数理统计'}\n"
        f"难度：{difficulty or 'basic'}（basic/medium/hard）\n"
        f"题型：{qtype or '计算题'}（计算/证明/应用/选择/填空）"
    )
    messages = [
        ModelMessage(role="system", content=system),
        *(history or []),
        ModelMessage(role="user", content=user),
    ]
    if feedback:
        messages.append(ModelMessage(role="user", content=f"出题纠错要求：{feedback}"))
    raw = await model_client.complete(messages, response_format={"type": "json_object"})
    return _parse_exercise_checked(raw, difficulty, qtype)


def _parse_exercise_checked(raw: str, difficulty: str, qtype: str) -> tuple[Exercise | None, dict | None]:
    obj = _extract_json_object(raw)
    if obj is None:
        return None, None
    check = obj.get("answer_check") if isinstance(obj.get("answer_check"), dict) else None
    ex = _exercise_from_json(obj, difficulty, qtype)
    return ex, check


def _exercise_from_json(obj: dict, difficulty: str, qtype: str) -> Exercise | None:
    """从模型 JSON 构造 Exercise，含 LaTeX 自检。problem/solution 缺一即弃。"""
    problem = str(obj.get("problem", "")).strip()
    solution = str(obj.get("solution_outline", "")).strip()
    if not problem or not solution:
        return None
    hints_raw = obj.get("hints", [])
    hints = tuple(str(h).strip() for h in hints_raw if str(h).strip()) if isinstance(hints_raw, list) else ()
    issues_list = lint_latex(problem + "\n" + solution)
    issues = tuple(f"{i.kind}: {i.detail}" for i in issues_list)
    topic = str(obj.get("topic", "")).strip() or "custom"
    return Exercise(
        topic=topic,
        difficulty=str(obj.get("difficulty", difficulty) or difficulty),
        problem=problem,
        hints=hints,
        solution_outline=solution,
        self_check_ok=not issues_list,
        self_check_issues=issues,
        qtype=str(obj.get("qtype", qtype) or qtype),
        source="model",
    )


