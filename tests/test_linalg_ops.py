# -*- coding: utf-8 -*-
"""线代内核 parity 测试：Fraction 逐步计算 vs SymPy 独立复算，每算子多例。"""
from fractions import Fraction

import pytest

from app.linalg import (
    FracMatrix,
    column_space,
    det,
    eigen,
    inverse,
    null_space,
    rank,
    rref,
    solve,
)


def M(rows):
    return FracMatrix.from_json(rows)


class TestRrefRank:
    def test_rref_basic(self):
        r = rref(M([[1, 2], [2, 4]]))
        assert r.detail["rank"] == 1
        assert r.verified

    def test_rref_identity_stays(self):
        r = rref(M([[1, 0], [0, 1]]))
        assert r.detail["rank"] == 2
        assert len([s for s in r.steps if s.op in {"swap_rows", "scale_row", "add_row"}]) == 0

    def test_rref_fraction(self):
        r = rref(M([[2, 1], [1, 3]]))
        assert r.verified
        assert r.detail["pivot_cols"] == [0, 1]

    def test_rank_tall(self):
        r = rank(M([[1, 2, 3], [4, 5, 6], [7, 8, 9]]))
        assert r.answer_value == "2"
        assert r.verified

    def test_rank_zero_col(self):
        assert rank(M([[1, 0], [2, 0]])).answer_value == "1"


class TestDet:
    def test_det_2x2(self):
        assert det(M([[2, 1], [1, 3]])).answer_value == "5"

    def test_det_3x3_cofactor(self):
        r = det(M([[1, 2, 3], [4, 5, 6], [7, 8, 10]]))
        assert r.answer_value == "-3"
        assert r.verified
        assert any(s.op == "definition" for s in r.steps)

    def test_det_4x4_elimination(self):
        import sympy
        rows = [[2, 0, 1, 0], [0, 3, 0, 1], [1, 0, 4, 0], [0, 1, 0, 5]]
        r = det(M(rows))
        assert r.verified
        expected = sympy.Matrix(rows).det()
        assert Fraction(r.answer_value) == Fraction(int(expected.p), int(expected.q))

    def test_det_singular(self):
        assert det(M([[1, 2], [2, 4]])).answer_value == "0"

    def test_det_non_square_raises(self):
        with pytest.raises(ValueError):
            det(M([[1, 2]]))


class TestInverse:
    def test_inverse_2x2(self):
        r = inverse(M([[2, 1], [1, 3]]))
        assert r.detail["invertible"]
        assert r.verified

    def test_inverse_fraction_entries(self):
        r = inverse(M([[0, 2], [4, 0]]))
        assert r.verified

    def test_inverse_singular(self):
        r = inverse(M([[1, 2], [2, 4]]))
        assert not r.detail["invertible"]
        assert r.answer_value == "not_invertible"


class TestSolve:
    def test_unique(self):
        r = solve(M([[1, 2], [3, 4]]), [5, 11])
        assert r.detail["solution_type"] == "unique"
        assert r.answer_value == str([Fraction(1), Fraction(2)])
        assert r.verified

    def test_infinite_with_basis(self):
        r = solve(M([[1, 2, 3], [2, 4, 6]]), [1, 2])
        assert r.detail["solution_type"] == "infinite"
        assert r.verified

    def test_no_solution(self):
        r = solve(M([[1, 2], [2, 4]]), [1, 1])
        assert r.detail["solution_type"] == "no_solution"
        assert r.verified

    def test_three_unknowns_free(self):
        r = solve(M([[1, 1, 1], [2, 2, 2]]), [3, 6])
        assert r.detail["solution_type"] == "infinite"
        assert r.detail["free_vars"] == 2


class TestEigen:
    def test_eigen_diagonalizable(self):
        r = eigen(M([[4, 1], [2, 3]]))
        assert r.verified
        assert r.detail["diagonalizable"]

    def test_eigen_trace_det_identity(self):
        # 代数恒等式：trace=Σλ, det=Πλ 由 verified 隐式断言
        r = eigen(M([[6, 2], [2, 9]]))
        assert r.verified
        assert r.detail["diagonalizable"]

    def test_eigen_repeated_not_diagonalizable(self):
        r = eigen(M([[3, 1], [0, 3]]))
        assert not r.detail["diagonalizable"]

    def test_eigen_non_square_raises(self):
        with pytest.raises(ValueError):
            eigen(M([[1, 2]]))


class TestSpaces:
    def test_null_space_dim(self):
        r = null_space(M([[1, 2, 3], [2, 4, 6]]))
        assert r.verified
        assert r.detail["solution_type"] == "infinite"

    def test_column_space_pivots(self):
        r = column_space(M([[1, 2, 5], [2, 4, 11]]))
        assert r.detail["pivot_cols"] == [0, 2]
        assert r.detail["dim"] == 2


class TestSteps:
    def test_step_records_formula(self):
        r = rref(M([[2, 4], [1, 3]]))
        row_ops = [s for s in r.steps if s.op in {"swap_rows", "scale_row", "add_row"}]
        assert row_ops, "rref 必须记录行变换步骤"
        assert all(s.before_latex.startswith(r"\begin{bmatrix}") for s in row_ops)

    def test_latex_fraction_render(self):
        assert "frac" in FracMatrix([[Fraction(1, 2)]]).latex()
