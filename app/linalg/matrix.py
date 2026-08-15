# -*- coding: utf-8 -*-
"""线性代数计算内核：精确算术 + 逐步记录。

设计原则（与 app/stats 同源）：
- 一切数值用 Fraction 精确计算，禁止浮点漂移；
- 每个行变换记一个 Step（公式 + 前后矩阵 + 教学注解），供前端逐步展示；
- SymPy 只做特征多项式求根与复算对照（parity），不替代我们的消元循环。
"""
from __future__ import annotations

from fractions import Fraction
from dataclasses import dataclass, field
from typing import Any


@dataclass(frozen=True)
class Step:
    """一步矩阵操作。formula 如 `r_2 \\leftarrow r_2 - 2r_1`。"""

    op: str
    formula: str
    before_latex: str
    after_latex: str
    note: str = ""

    def as_dict(self) -> dict[str, Any]:
        return {
            "op": self.op,
            "formula": self.formula,
            "before": self.before_latex,
            "after": self.after_latex,
            "note": self.note,
        }


def frac(value: Any) -> Fraction:
    """把 JSON 里的数字/字符串（"2/3"、"-1.5"）转成 Fraction。"""
    if isinstance(value, Fraction):
        return value
    if isinstance(value, bool):
        raise ValueError("矩阵元素不能是布尔值")
    if isinstance(value, int):
        return Fraction(value)
    f = Fraction(str(value))
    return f


def frac_latex(f: Fraction) -> str:
    """Fraction 的 LaTeX 表示。整数直接写，分数用 \\frac，负号前置。"""
    if f.denominator == 1:
        return str(f.numerator)
    sign = "-" if f < 0 else ""
    return rf"{sign}\frac{{{abs(f.numerator)}}}{{{f.denominator}}}"


class FracMatrix:
    """Fraction 精确矩阵。行变换在此发生，Step 由调用方收集。"""

    def __init__(self, rows: list[list[Fraction]]) -> None:
        if not rows or not rows[0]:
            raise ValueError("矩阵不能为空")
        width = len(rows[0])
        if any(len(r) != width for r in rows):
            raise ValueError("矩阵每行长度必须一致")
        self.rows = [list(r) for r in rows]
        self.m = len(self.rows)
        self.n = width

    @classmethod
    def from_json(cls, data: list[list[Any]]) -> "FracMatrix":
        if not isinstance(data, list) or not data:
            raise ValueError("matrix 必须是非空二维数组")
        return cls([[frac(cell) for cell in row] for row in data])

    @classmethod
    def identity(cls, n: int) -> "FracMatrix":
        return cls([
            [Fraction(1) if i == j else Fraction(0) for j in range(n)]
            for i in range(n)
        ])

    def copy(self) -> "FracMatrix":
        return FracMatrix([list(r) for r in self.rows])

    def augmented(self, other: "FracMatrix") -> "FracMatrix":
        if self.m != other.m:
            raise ValueError("行数不一致，无法拼接增广矩阵")
        return FracMatrix([list(a) + list(b) for a, b in zip(self.rows, other.rows)])

    def column(self, j: int) -> list[Fraction]:
        return [self.rows[i][j] for i in range(self.m)]

    def latex(self) -> str:
        body = r" \\ ".join(
            " & ".join(frac_latex(c) for c in row) for row in self.rows
        )
        return rf"\begin{{bmatrix}} {body} \end{{bmatrix}}"

    def swap_rows(self, i: int, j: int, steps: list[Step], note: str = "") -> None:
        formula = rf"r_{{{i + 1}}} \leftrightarrow r_{{{j + 1}}}"
        before = self.latex()
        self.rows[i], self.rows[j] = self.rows[j], self.rows[i]
        steps.append(Step("swap_rows", formula, before, self.latex(), note or "交换两行"))

    def scale_row(self, i: int, k: Fraction, steps: list[Step], note: str = "") -> None:
        formula = rf"r_{{{i + 1}}} \leftarrow {frac_latex(k)} \, r_{{{i + 1}}}"
        before = self.latex()
        self.rows[i] = [k * c for c in self.rows[i]]
        steps.append(Step("scale_row", formula, before, self.latex(), note or "将该行化为首 1"))

    def add_row(self, i: int, j: int, k: Fraction, steps: list[Step], note: str = "") -> None:
        """r_i ← r_i + k·r_j。k 为负即消去。"""
        formula = (
            rf"r_{{{i + 1}}} \leftarrow r_{{{i + 1}}} - {frac_latex(-k)} \, r_{{{j + 1}}}"
            if k < 0
            else rf"r_{{{i + 1}}} \leftarrow r_{{{i + 1}}} + {frac_latex(k)} \, r_{{{j + 1}}}"
        )
        before = self.latex()
        self.rows[i] = [a + k * b for a, b in zip(self.rows[i], self.rows[j])]
        label = note or f"消去第 {i + 1} 行主元列的非零元"
        steps.append(Step("add_row", formula, before, self.latex(), label))

    def is_zero_row(self, i: int) -> bool:
        return all(c == 0 for c in self.rows[i])

    def first_nonzero_col(self, i: int) -> int | None:
        for j, c in enumerate(self.rows[i]):
            if c != 0:
                return j
        return None
