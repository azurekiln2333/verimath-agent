# -*- coding: utf-8 -*-
"""linalg_step_solve 工具：单一入口多算子，供 Agent 循环调用。

数值纪律：本工具是线代数值的唯一权威来源。返回 content 为渲染好的
Markdown 步骤（含 SymPy 复算凭证），模型只解释、不重算。
"""
from __future__ import annotations

from fractions import Fraction
from typing import Any

from app.linalg import det, eigen, inverse, jordan, null_space, quadratic_form, rank, rref, solve, column_space
from app.linalg.matrix import FracMatrix, Step, frac
from app.tools.base import Tool, ToolResult

_OPERATIONS = {
    "rref": "最简行阶梯形",
    "rank": "秩",
    "det": "行列式",
    "inverse": "逆矩阵",
    "solve": "线性方程组 Ax=b",
    "eigen": "特征值与特征向量",
    "jordan": "Jordan 标准形",
    "quadratic_form": "二次型标准形/惯性指数/正定性",
    "null_space": "零空间/基础解系",
    "column_space": "列空间",
}


def render_steps_md(name: str, result) -> str:
    """把 LinalgResult 渲染成 Markdown 步骤文本（面板 KaTeX 直接渲染）。"""
    lines = [f"**{name}**", "", f"$$ {result.answer_latex} $$", ""]
    if result.verified:
        lines.append("> ✅ 已用 SymPy 独立复算，与逐步计算结果一致（验算凭证）。")
    else:
        lines.append("> ⚠️ SymPy 复算未确认一致，结果请谨慎引用。")
    lines.append("")
    lines.append("**逐步过程：**")
    lines.append("")
    for k, s in enumerate(result.steps, start=1):
        if s.op in {"swap_rows", "scale_row", "add_row"}:
            lines.append(f"第 {k} 步：${s.formula}$")
            lines.append("")
            lines.append(f"$$ {s.after_latex} $$")
        else:
            lines.append(f"第 {k} 步：${s.formula}$")
        if s.note:
            lines.append(f"\n{s.note}")
        lines.append("")
    return "\n".join(lines)


class LinalgStepSolveTool:
    name = "linalg_step_solve"

    def schema(self) -> dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": self.name,
                "description": (
                    "线性代数逐步计算器：精确分数算术，逐步展示每个行变换，"
                    "并用 SymPy 独立复算出具验算凭证。支持 rref/rank/det/inverse/"
                    "solve/eigen/jordan/quadratic_form/null_space/column_space。"
                    "任何矩阵数值问题（求逆、行列式、特征值、解方程组、基础解系、"
                    "Jordan 标准形、二次型标准形/惯性指数/正定性、线性相关性、秩）"
                    "都必须调用本工具获得答案，禁止口算。"
                ),
                "parameters": {
                    "type": "object",
                    "properties": {
                        "operation": {
                            "type": "string",
                            "enum": list(_OPERATIONS),
                            "description": "要执行的计算",
                        },
                        "matrix": {
                            "type": "array",
                            "items": {"type": "array", "items": {}},
                            "description": "矩阵，行优先二维数组，元素可为数字或 \"a/b\" 分数字符串。"
                                           "quadratic_form 时给二次型的对称矩阵",
                        },
                        "expression": {
                            "type": "string",
                            "description": "仅在 operation=quadratic_form 时可选：二次型表达式（Python 语法，"
                                           "如 \"x**2 + 2*x*y + y**2\"），与 matrix 二选一",
                        },
                        "b": {
                            "type": "array",
                            "items": {},
                            "description": "仅在 operation=solve 时需要：右端常数列",
                        },
                    },
                    "required": ["operation"],
                },
            },
        }

    async def run(self, operation: str, matrix: list[list[Any]] | None = None,
                  expression: str | None = None, b: list[Any] | None = None,
                  **_: Any) -> ToolResult:
        if operation not in _OPERATIONS:
            return ToolResult(
                content=f"未知算子 {operation}。可用：{', '.join(_OPERATIONS)}",
                summary={"error": "unknown_operation"},
            )
        if operation == "quadratic_form" and matrix is None and expression is not None:
            try:
                result = quadratic_form(expression=expression)
            except ValueError as exc:
                return ToolResult(content=f"二次型解析失败：{exc}", summary={"error": "invalid_input"})
            except Exception as exc:
                return ToolResult(
                    content=f"计算失败：{type(exc).__name__}: {exc}",
                    summary={"error": type(exc).__name__},
                )
            md = render_steps_md(_OPERATIONS[operation], result)
            return ToolResult(
                content=md,
                summary={
                    "operation": operation,
                    "verified": result.verified,
                    "n_steps": len(result.steps),
                    "answer": result.answer_value,
                },
            )
        if matrix is None:
            return ToolResult(
                content=f"{operation} 需要 matrix 参数。请给出矩阵。",
                summary={"error": "missing_matrix"},
            )
        try:
            a = FracMatrix.from_json(matrix)
        except Exception as exc:
            return ToolResult(
                content=f"矩阵解析失败：{exc}。matrix 必须是行长相齐的二维数组。",
                summary={"error": "bad_matrix"},
            )
        try:
            if operation == "rref":
                result = rref(a)
            elif operation == "rank":
                result = rank(a)
            elif operation == "det":
                result = det(a)
            elif operation == "inverse":
                result = inverse(a)
            elif operation == "solve":
                if b is None:
                    return ToolResult(
                        content="solve 需要 b（右端常数列）。请补 b 参数。",
                        summary={"error": "missing_b"},
                    )
                result = solve(a, b)
            elif operation == "eigen":
                result = eigen(a)
            elif operation == "jordan":
                result = jordan(a)
            elif operation == "quadratic_form":
                result = quadratic_form(matrix=matrix)
            elif operation == "null_space":
                result = null_space(a)
            else:
                result = column_space(a)
        except ValueError as exc:
            return ToolResult(content=f"计算失败：{exc}", summary={"error": "invalid_input"})
        except Exception as exc:
            return ToolResult(
                content=f"计算失败：{type(exc).__name__}: {exc}",
                summary={"error": type(exc).__name__},
            )
        md = render_steps_md(_OPERATIONS[operation], result)
        return ToolResult(
            content=md,
            summary={
                "operation": operation,
                "verified": result.verified,
                "n_steps": len(result.steps),
                "answer": result.answer_value,
            },
        )


def verify_answer(operation: str, matrix: list[list[Any]], expected: str,
                  b: list[Any] | None = None) -> tuple[bool, str]:
    """出题验算：拿模型声称的答案与内核重算比对。

    返回 (是否一致, 内核算出的答案串)。expected 支持整数/分数/小数。
    - det/rank/inverse/rref：与内核 answer_value 直接比对（inverse/rref
      的 expected 为矩阵串 "[[a,b],[c,d]]"，逐项 Fraction 比对）。
    - solve：模型给解向量 "[x1, x2]"，内核回代 A·x=b 逐行验证（数学验证，
      不依赖格式）。
    - eigen：模型给特征值列表 "λ1, λ2"，逐个判 det(A-λI)=0（特征方程验证，
      支持 sqrt 等根式，sympy 解析）。
    - jordan：模型给 Jordan 形 J 的矩阵串 "[[a,b],[c,d]]"，用相似不变量
      （特征多项式数值抽查 + 核维数序列）与内核结果比对。
    - quadratic_form：模型给 "p,q"（正负惯性指数）或正定性关键词（正定/负定/
      半正定/半负定/不定），与内核判定比对。
    """
    a = FracMatrix.from_json(matrix)
    if operation == "det":
        actual = det(a).answer_value
    elif operation == "rank":
        actual = rank(a).answer_value
    elif operation == "rref":
        actual = rref(a).answer_value
    elif operation == "inverse":
        actual = inverse(a).answer_value
    elif operation == "solve":
        return _verify_solve(a, expected, b)
    elif operation == "eigen":
        return _verify_eigen(a, expected)
    elif operation == "jordan":
        return _verify_jordan(a, expected)
    elif operation == "quadratic_form":
        return _verify_qf(a, expected)
    else:
        return False, f"暂不支持 {operation} 的自动验算"
    if operation in {"det", "rank"}:
        try:
            exp = Fraction(str(expected).strip())
            act = Fraction(actual.strip())
            return exp == act, actual
        except (ValueError, ZeroDivisionError):
            return False, actual
    # inverse / rref：expected 与 actual 都是 "[[Fraction(..), ..], ..]" 形式的矩阵串，
    # 逐项解析比对
    ok = _matrix_str_equal(expected, actual)
    return ok, actual


def _verify_solve(a: FracMatrix, expected: str, b: list[Any] | None) -> tuple[bool, str]:
    if b is None:
        return False, "solve 验算需要 b"
    res = solve(a, b)
    st = res.detail.get("solution_type")
    text = str(expected).strip()
    # 无解 / 无穷解：按解型比对（无穷解回代特解验证）
    if text == "no_solution":
        return st == "no_solution", res.answer_value
    if text.startswith("infinite:"):
        if st != "infinite":
            return False, res.answer_value
        _, _, payload = text.partition(":")
        particular_str, _, _basis_str = payload.partition(";")
        try:
            pv = _parse_vector(particular_str)
        except (ValueError, ZeroDivisionError):
            return False, res.answer_value
        if len(pv) != a.n:
            return False, res.answer_value
        for i in range(a.m):
            lhs = sum(a.rows[i][j] * x for j, x in enumerate(pv))
            if lhs != frac(b[i]):
                return False, res.answer_value
        return True, res.answer_value
    # 唯一解：逐元素回代
    try:
        xs = _parse_vector(text)
    except (ValueError, ZeroDivisionError):
        return False, res.answer_value
    if len(xs) != a.n:
        return False, res.answer_value
    for i in range(a.m):
        lhs = sum(a.rows[i][j] * x for j, x in enumerate(xs))
        if lhs != frac(b[i]):
            return False, res.answer_value
    return True, res.answer_value


def _verify_eigen(a: FracMatrix, expected: str) -> tuple[bool, str]:
    import sympy
    res = eigen(a)
    lam = sympy.symbols("lambda")
    sp = sympy.Matrix([[sympy.Rational(c.numerator, c.denominator) for c in row] for row in a.rows])
    for part in str(expected).replace(";", ",").split(","):
        part = part.strip()
        if not part:
            continue
        try:
            val = sympy.sympify(part)
        except (sympy.SympifyError, ValueError):
            return False, res.answer_value
        if sympy.simplify((sp - sympy.eye(a.n) * val).det()) != 0:
            return False, res.answer_value
    return True, res.answer_value


def _verify_jordan(a: FracMatrix, expected: str) -> tuple[bool, str]:
    """验算 Jordan 形 J：解析模型给的矩阵串，用相似不变量比对。

    相似不变量 = 特征多项式（数值抽查）+ 每个特征值的核维数序列。
    两个矩阵相似 ⇔ 两者完全相同，因此不依赖 J 的块顺序。
    """
    import sympy
    from app.linalg.ops import _kernel_dims, _to_sympy
    res = jordan(a)
    try:
        J_expected = sympy.Matrix(sympy.sympify(str(expected).strip()))
    except (sympy.SympifyError, ValueError, TypeError):
        return False, res.answer_value
    if J_expected.shape != (a.n, a.n):
        return False, res.answer_value
    sp = _to_sympy(a)
    lam = sympy.symbols("lambda")
    roots_mult = sympy.roots(sp.charpoly(lam).as_expr())
    # 特征多项式数值抽查
    try:
        char_a = sp.charpoly(lam).as_expr()
        prod = sympy.Integer(1)
        for u, m in roots_mult.items():
            prod = prod * (lam - u) ** m
        for t in (sympy.Integer(0), sympy.Integer(1), sympy.Integer(-1), sympy.Integer(2)):
            va = sympy.N(char_a.subs(lam, t), 20)
            vj = sympy.N(prod.subs(lam, t), 20)
            if abs(complex(va - vj)) > 1e-9:
                return False, res.answer_value
    except Exception:
        pass
    # 核维数序列（对 A 与对模型给的 J 分别算）
    try:
        for u, m in roots_mult.items():
            da = _kernel_dims(sp, u, m, a.n)
            dj = _kernel_dims(J_expected, u, m, a.n)
            if da != dj:
                return False, res.answer_value
    except Exception:
        return False, res.answer_value
    return True, res.answer_value


def _verify_qf(a: FracMatrix, expected: str) -> tuple[bool, str]:
    """验算二次型结论：expected 为 "p,q"（正负惯性指数）或正定性关键词。"""
    try:
        res = quadratic_form(matrix=a.rows)
    except Exception as exc:
        return False, f"内核无法验算：{exc}"
    text = str(expected).strip()
    d = res.detail
    # 关键词形式：正定/负定/半正定/半负定/不定
    if text in {"正定", "负定", "半正定", "半负定", "不定"}:
        return text == d["definiteness"], res.answer_value
    # "p,q" 或 "p,q,s,def" 形式（允许带空格/全角逗号）
    cleaned = text.replace("，", ",").replace(" ", "").replace("；", ",")
    parts = [p for p in cleaned.split(",") if p]
    if len(parts) in {2, 4}:
        try:
            return (int(parts[0]), int(parts[1])) == (d["p"], d["q"]), res.answer_value
        except (ValueError, TypeError):
            return False, res.answer_value
    return False, res.answer_value


def _parse_vector(text: str) -> list[Fraction]:
    """"[1, 2]" 或 "1,2" 或 "(1, 2)" → [Fraction]。"""
    cleaned = str(text).strip().strip("[]()")
    parts = [p.strip() for p in cleaned.split(",") if p.strip()]
    if not parts:
        raise ValueError("empty vector")
    return [frac(p) for p in parts]


def _matrix_str_equal(expected: str, actual: str) -> bool:
    """比对矩阵串。actual 是内核 repr（"[[Fraction(1, 2), ..]]"），
    expected 是模型风格（"[[1/2, ..]]"，元素支持整数/分数/小数）。"""
    import re as _re

    frac_re = _re.compile(r"Fraction\((-?\d+),\s*(\d+)\)")
    # 小数分支必须放整数分支前，否则 "0.6" 被截成 "0"
    token_re = _re.compile(r"-?\d+\.\d+|-?\d+(?:\s*/\s*\d+)?")

    def parse_actual(s: str) -> list[Fraction] | None:
        pairs = frac_re.findall(s)
        if not pairs:
            return None
        return [Fraction(int(a), int(b)) for a, b in pairs]

    def parse_expected(s: str) -> list[Fraction] | None:
        s = frac_re.sub(lambda m: f"{m.group(1)}/{m.group(2)}", str(s))
        tokens = token_re.findall(s)
        if not tokens:
            return None
        try:
            return [frac(t) for t in tokens]
        except (ValueError, ZeroDivisionError):
            return None

    exp = parse_expected(expected)
    act = parse_actual(actual)
    if exp is None or act is None or len(exp) != len(act):
        return False
    return all(e == a for e, a in zip(exp, act))
