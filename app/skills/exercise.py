from __future__ import annotations

from dataclasses import dataclass, field

from app.render.latex_lint import lint_latex


@dataclass(frozen=True)
class Exercise:
    topic: str
    difficulty: str
    problem: str
    hints: tuple[str, ...] = field(default_factory=tuple)
    solution_outline: str = ""
    self_check_ok: bool = True
    self_check_issues: tuple[str, ...] = field(default_factory=tuple)


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
