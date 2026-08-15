# -*- coding: utf-8 -*-
"""verify_answer 全算子验算测试（W2 遗留收口：solve 回代 / eigen 特征方程）。"""
from app.linalg.tool import verify_answer


class TestScalarOps:
    def test_det_ok(self):
        ok, actual = verify_answer("det", [[2, 1], [1, 3]], "5")
        assert ok and actual == "5"

    def test_det_bad(self):
        ok, _ = verify_answer("det", [[2, 1], [1, 3]], "6")
        assert not ok

    def test_rank_fraction_answer(self):
        ok, _ = verify_answer("rank", [[1, 2], [2, 4]], "1")
        assert ok


class TestMatrixOps:
    def test_inverse_match_fraction_style(self):
        ok, _ = verify_answer("inverse", [[2, 1], [1, 3]], "[[3/5, -1/5], [-1/5, 2/5]]")
        assert ok

    def test_inverse_mismatch(self):
        ok, _ = verify_answer("inverse", [[2, 1], [1, 3]], "[[1, 0], [0, 1]]")
        assert not ok

    def test_inverse_decimal_style(self):
        # 0.6 = 3/5，小数形式也应认可
        ok, _ = verify_answer("inverse", [[2, 1], [1, 3]], "[[0.6, -0.2], [-0.2, 0.4]]")
        assert ok

    def test_rref_match(self):
        ok, _ = verify_answer("rref", [[1, 2], [2, 4]], "[[1, 2], [0, 0]]")
        assert ok


class TestSolveVerification:
    def test_unique_solution_accepted(self):
        ok, _ = verify_answer("solve", [[1, 2], [3, 4]], "[1, 2]", b=[5, 11])
        assert ok

    def test_unique_solution_rejected(self):
        ok, _ = verify_answer("solve", [[1, 2], [3, 4]], "[2, 1]", b=[5, 11])
        assert not ok

    def test_fraction_solution(self):
        ok, _ = verify_answer("solve", [[2, 0], [0, 4]], "[3/2, 1/4]", b=[3, 1])
        assert ok

    def test_missing_b_rejected(self):
        ok, msg = verify_answer("solve", [[1, 2], [3, 4]], "[1, 2]", b=None)
        assert not ok


class TestEigenVerification:
    def test_integer_eigenvalues(self):
        ok, _ = verify_answer("eigen", [[4, 1], [2, 3]], "5, 2")
        assert ok

    def test_wrong_eigenvalue_rejected(self):
        ok, _ = verify_answer("eigen", [[4, 1], [2, 3]], "5, 3")
        assert not ok

    def test_radical_eigenvalue(self):
        # [[1,1],[1,1]] 特征值 0 和 2；用 sqrt 形式给 1±1 也行：1+1=2 合法
        ok, _ = verify_answer("eigen", [[1, 1], [1, 1]], "0, 1+1")
        assert ok

    def test_garbage_rejected(self):
        ok, _ = verify_answer("eigen", [[4, 1], [2, 3]], "abc")
        assert not ok
