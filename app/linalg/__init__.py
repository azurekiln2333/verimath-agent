# -*- coding: utf-8 -*-
"""线性代数计算内核公开 API。"""
from app.linalg.matrix import FracMatrix, Step, frac, frac_latex
from app.linalg.ops import (
    LinalgResult,
    column_space,
    det,
    eigen,
    inverse,
    jordan,
    quadratic_form,
    null_space,
    rank,
    rref,
    solve,
)

__all__ = [
    "FracMatrix",
    "Step",
    "frac",
    "frac_latex",
    "LinalgResult",
    "column_space",
    "det",
    "eigen",
    "inverse",
    "jordan",
    "quadratic_form",
    "null_space",
    "rank",
    "rref",
    "solve",
]