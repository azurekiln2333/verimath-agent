"""步骤级校验内核：把"严谨"从一句口号变成可执行、可复算的判定。

核心思想：**每一步都问同一个问题 —— 从这一步能推出下一步吗？**

对代数推导，这一步的判定是"两个表达式是否恒等"；对统计结论，是"函数值
是否逐一吻合"。两种都归约为"逐点采样 + 符号等价"的确定性检查，
因此在模型不可用时依然能跑，且结果可复现。

符号等价优先用 SymPy（精确）；SymPy 不在或解析失败时退化为纯标准库的
AST 求值器（受控的极小语言：+ - * / **、括号、命名变量、少量函数）。
两条路径对同一输入应给出相同判定，差异由 tests/test_step_verifier.py 约束。

设计取舍：宁可报"无法判定"，也不误报"正确"。
一个把错误推导判成正确的校验器，比没有校验器更糟。
"""

from __future__ import annotations

import ast
import math
import operator
import re
from dataclasses import dataclass, field
from fractions import Fraction
from typing import Any


class StepVerifierError(ValueError):
    """输入无法解析。上层据此降级为"无法判定"，而不是判错。"""


@dataclass(frozen=True)
class StepCheck:
    """单步判定结果。

    status: ok / sampled / mismatch / undecidable
    detail: 给学生的中文说明（不含答案泄露，例如不会说"正确答案是 x=2"）
    counterexample: 反例赋值（仅 mismatch 且找到明确反例时填），
        让学生能自己代入验证 —— 反例比结论更有说服力。
    """

    index: int
    status: str
    detail: str = ""
    counterexample: dict[str, float] = field(default_factory=dict)


@dataclass(frozen=True)
class ExpressionCheck:
    """自由表达式级判定（用于「我算出来是 c = 2，对吗」这类提问）。"""

    status: str
    detail: str
    counterexample: dict[str, float] = field(default_factory=dict)


# ----------------------------------------------------------------- 表达式解析

_ALLOWED_CHARS = re.compile(r"^[0-9A-Za-z_+\-*/().,^ \t]+$")


def normalize(text: str) -> str:
    """统一学生的书写习惯：LaTeX 片段、全角符号、常用别名。"""
    s = (text or "").strip()
    if len(s) > 2000:
        raise StepVerifierError("单个表达式请控制在 2000 字以内")
    if not s:
        raise StepVerifierError("空表达式")
    # Accept mathematical typography from the editor/pasted text, including multi-digit and negative powers.
    superscripts = str.maketrans('⁰¹²³⁴⁵⁶⁷⁸⁹⁺⁻', '0123456789+-')
    s = re.sub(r'[⁰¹²³⁴⁵⁶⁷⁸⁹⁺⁻]+', lambda match: '^(' + match[0].translate(superscripts) + ')', s)
    s = s.replace("−", "-").replace("×", "*").replace("·", "*").replace("÷", "/")
    s = s.replace("（", "(").replace("）", ")").replace("，", ",")
    # LaTeX 常见写法
    s = s.replace("\\left", "").replace("\\right", "").replace("\\,", " ").replace("\\cdot", "*")
    s = s.replace("\\times", "*").replace("\\div", "/").replace("\\pi", "pi")
    s = re.sub(r"\\frac\s*\{([^{}]*)\}\s*\{([^{}]*)\}", r"((\1)/(\2))", s)
    s = re.sub(r"\\sqrt\s*\{([^{}]*)\}", r"sqrt(\1)", s)
    s = re.sub(r"\\(ln|log|sin|cos|tan|exp)\b", r"\1", s)
    s = s.replace("^", "**")
    # 隐式乘法：(x+1)(x-1) → (x+1)*(x-1)；2x → 2*x；3(x) → 3*(x)；x(…) → x*(…)
    s = re.sub(r"\)\s*\(", ")*(", s)
    s = re.sub(r"(\d)\s*\(", r"\1*(", s)
    s = re.sub(r"(\d)\s*([A-Za-z_])", r"\1*\2", s)
    s = re.sub(r"\)\s*([A-Za-z_0-9])", r")*\1", s)
    s = re.sub(r"(?<![A-Za-z_0-9.])([A-Za-z_])\s*\(", r"\1*(", s)
    # 还原函数调用：sqrt*( 这类被误加乘号的写法
    for fn in ("sqrt", "ln", "log", "sin", "cos", "tan", "exp", "abs"):
        s = s.replace(fn + "*(", fn + "(")
    # 函数调用一律写成 sqrt(x) 这类形式，不把 a(b) 改写成乘法
    if not _ALLOWED_CHARS.match(s):
        raise StepVerifierError(f"表达式含不支持的字符：{text!r}")
    return s


_FUNCS: dict[str, Any] = {
    "sqrt": math.sqrt,
    "ln": lambda v: math.log(v) if v > 0 else float("nan"),
    "log": lambda v: math.log(v) if v > 0 else float("nan"),
    "sin": math.sin,
    "cos": math.cos,
    "tan": math.tan,
    "exp": math.exp,
    "abs": abs,
}

_BINOPS = {
    ast.Add: operator.add,
    ast.Sub: operator.sub,
    ast.Mult: operator.mul,
    ast.Div: operator.truediv,
    ast.Pow: operator.pow,
}
_UNOPS = {ast.UAdd: operator.pos, ast.USub: operator.neg}


def _eval_ast(node: ast.AST, env: dict[str, float]) -> float:
    """受控求值：只允许算术、命名变量与白名单函数。不触碰任何 builtin。"""
    if isinstance(node, ast.Expression):
        return _eval_ast(node.body, env)
    if isinstance(node, ast.Constant):
        if isinstance(node.value, bool) or not isinstance(node.value, (int, float)):
            raise StepVerifierError("不支持的常量")
        return float(node.value)
    if isinstance(node, ast.Name):
        if node.id not in env:
            raise StepVerifierError(f"未知变量：{node.id}")
        return env[node.id]
    if isinstance(node, ast.BinOp):
        op = _BINOPS.get(type(node.op))
        if op is None:
            raise StepVerifierError("不支持的运算符")
        return op(_eval_ast(node.left, env), _eval_ast(node.right, env))
    if isinstance(node, ast.UnaryOp):
        op = _UNOPS.get(type(node.op))
        if op is None:
            raise StepVerifierError("不支持的一元运算符")
        return op(_eval_ast(node.operand, env))
    if isinstance(node, ast.Call):
        if not isinstance(node.func, ast.Name) or node.func.id not in _FUNCS:
            raise StepVerifierError("只支持 sqrt/ln/log/sin/cos/tan/exp/abs")
        if node.keywords:
            raise StepVerifierError("函数不支持关键字参数")
        args = [_eval_ast(a, env) for a in node.args]
        if len(args) != 1:
            raise StepVerifierError("函数只接受一个参数")
        return _FUNCS[node.func.id](args[0])
    raise StepVerifierError("不支持的表达式结构")


def variables_of(expr: str) -> list[str]:
    """提取自由变量（按出现顺序去重，排除函数名与常量 pi/e）。"""
    s = normalize(expr)
    tree = ast.parse(s, mode="eval")
    names: list[str] = []
    for node in ast.walk(tree):
        if isinstance(node, ast.Name):
            if node.id in _FUNCS or node.id in {"pi", "e"}:
                continue
            if node.id not in names:
                names.append(node.id)
    return names


def _env_for(names: list[str], point: list[float]) -> dict[str, float]:
    env = {n: v for n, v in zip(names, point)}
    env["pi"] = math.pi
    env["e"] = math.e
    return env


def evaluate(expr: str, env: dict[str, float]) -> float:
    s = normalize(expr)
    return _eval_ast(ast.parse(s, mode="eval"), env)


def _close(a: float, b: float, scale: float = 1.0) -> bool:
    if math.isnan(a) or math.isnan(b):
        return math.isnan(a) and math.isnan(b)
    if math.isinf(a) or math.isinf(b):
        return a == b
    return abs(a - b) <= 1e-9 * max(1.0, abs(a), abs(b), scale)


# 固定的采样网格：确定性的，不依赖随机数，因此结果可复现、可写进测试。
_SAMPLE_GRID = [
    (-2.7,), (-1.3,), (-0.4,), (0.0,), (0.35,), (0.8,), (1.7,), (2.4,), (3.1,),
]
_TWO_D_GRID = [
    (0.37, -1.13), (1.21, 0.44), (-0.83, 2.05), (2.12, 1.46),
    (-1.57, -0.61), (0.92, -2.38), (-0.21, 0.17), (1.63, 2.71),
]


def _sample_points(n: int) -> list[tuple[float, ...]]:
    if n == 1:
        return _SAMPLE_GRID
    if n == 2:
        return _TWO_D_GRID
    # 3 个及以上：用确定性的准随机（黄金比序列），仍完全可复现
    phi = 0.6180339887498949
    pts = []
    for k in range(1, 13):
        row = []
        for j in range(n):
            frac = ((k * (j + 1) * phi) % 1.0) * 6.0 - 3.0
            row.append(round(frac, 6))
        pts.append(tuple(row))
    return pts


def expressions_equivalent(a: str, b: str) -> ExpressionCheck:
    """判定两个表达式是否在采样点上恒等。

    策略：先采样排错，再用符号计算确认；仅采样一致 → sampled，不代表数学证明。
    若某点明显不为零 → 判 mismatch 并返回该点作反例；
    若求值失败（定义域外、未知变量）→ 换点，全部失败则 undecidable。
    """
    try:
        na, nb = normalize(a), normalize(b)
    except StepVerifierError as exc:
        return ExpressionCheck("undecidable", f"无法解析表达式：{exc}")

    names = variables_of(na)
    for unknown in variables_of(nb):
        if unknown not in names:
            names.append(unknown)
    if not names:
        names = []

    points = _sample_points(len(names))
    checked = 0
    for point in points:
        env = _env_for(names, list(point))
        values = []
        for expression in (na, nb):
            try:
                value = evaluate(expression, env)
                values.append(value if math.isfinite(value) else None)
            except (StepVerifierError, ZeroDivisionError, ValueError, OverflowError):
                values.append(None)
        va, vb = values
        if (va is None) != (vb is None):
            return ExpressionCheck("mismatch", "两边的实数定义域不同", counterexample=dict(zip(names, point)))
        if va is None:
            continue
        checked += 1
        if not _close(va, vb):
            return ExpressionCheck(
                "mismatch",
                "在这一点上两边不相等",
                counterexample=dict(zip(names, point)),
            )
    if checked < 3:
        return ExpressionCheck("undecidable", "有效采样点太少（可能超出定义域），无法判定")

    # Numerical agreement is evidence, never a proof of an identity.
    exact = _sympy_equivalent(na, nb)
    if exact is True:
        return ExpressionCheck("ok", "已用符号计算确认在共同实数定义域内恒等")
    return ExpressionCheck("sampled", f"仅在 {checked} 个采样点上取值一致，尚未证明恒等")


def _sympy_equivalent(a: str, b: str) -> bool | None:
    """SymPy 符号简化为 0 时返回 True；不可用/解析失败返回 None。"""
    try:
        import sympy  # 可选依赖
    except Exception:
        return None
    try:
        # SymPy 用 ** 表幂，命名与 normalize 一致
        ea = sympy.sympify(a)
        eb = sympy.sympify(b)
        diff = sympy.simplify(ea - eb)
        return bool(diff == 0)
    except Exception:
        return None


# ----------------------------------------------------------------- 步骤链判定


def check_steps(steps: list[str]) -> list[StepCheck]:
    """检查一串推导步骤：相邻两步必须恒等。

    这是"严谨学习体验"最直接的实现：学生写「x²-1 = (x-1)(x+1)」
    「x²-1 = x²+1」这样的两行，第二步会被当场标红，并给出反例点。
    """
    cleaned = [s for s in (steps or []) if (s or "").strip()]
    if len(cleaned) > 30:
        raise StepVerifierError("一次最多核对 30 步，请分段提交")
    if len(cleaned) < 2:
        raise StepVerifierError("至少需要两步才能检查")
    out: list[StepCheck] = []
    for i in range(len(cleaned) - 1):
        result = expressions_equivalent(cleaned[i], cleaned[i + 1])
        out.append(StepCheck(index=i, status=result.status,
                             detail=result.detail,
                             counterexample=result.counterexample))
    return out


def first_error(checks: list[StepCheck]) -> StepCheck | None:
    for c in checks:
        if c.status == "mismatch":
            return c
    return None


# -------------------------------------------------------------- 简单算式核验


def fraction_of(text: str) -> Fraction:
    """把 3、0.25、3/4 这类字面量转成分数（供方程组根核验）。"""
    s = (text or "").strip().replace(" ", "")
    try:
        return Fraction(s)
    except (ValueError, ZeroDivisionError) as exc:
        raise StepVerifierError(f"不是合法数值：{text!r}") from exc


def substitution_is_zero(expr: str, assignment: dict[str, str]) -> bool:
    """把 assignment（变量→数值字面量）代入 expr，判断是否为 0。

    用于「解方程组」：把候选解代回原方程，结果必须是 0。
    分数精确：3.3333... 这类十进制输入走 Fraction，不会因浮点误差误判。
    """
    env = {k: float(fraction_of(v)) for k, v in assignment.items()}
    try:
        return _close(evaluate(expr, env), 0.0)
    except (StepVerifierError, ZeroDivisionError, ValueError, OverflowError):
        return False


__all__ = [
    "ExpressionCheck",
    "StepCheck",
    "StepVerifierError",
    "check_steps",
    "expressions_equivalent",
    "first_error",
    "fraction_of",
    "normalize",
    "substitution_is_zero",
    "variables_of",
]
