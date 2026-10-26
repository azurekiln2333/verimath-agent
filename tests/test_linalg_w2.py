# -*- coding: utf-8 -*-
"""W2 高代扩展测试：Jordan 标准形 + 二次型 + verify_answer 新算子。

原则与 W1 parity 一致：答案由本内核 Fraction/SymPy 精确计算，
verified 标志 = SymPy 独立复算一致，测试断言 verified 且结构正确。
"""
import pytest

from app.linalg import FracMatrix, jordan, quadratic_form
from app.linalg.tool import LinalgStepSolveTool, verify_answer


def M(rows):
    return FracMatrix.from_json(rows)


class TestJordan:
    def test_jordan_2x2_nondiagonalizable(self):
        """[[1,1],[0,1]]：单个 2 阶 Jordan 块，J 与 A 相同。"""
        r = jordan(M([[1, 1], [0, 1]]))
        assert r.verified
        blocks = r.detail["blocks"]
        assert blocks == [("1", 2)]
        assert r.detail["eigenvalues"][0]["geometric_mult"] == 1

    def test_jordan_diagonalizable(self):
        r = jordan(M([[2, 0], [0, 3]]))
        assert r.verified
        sizes = sorted(size for _, size in r.detail["blocks"])
        assert sizes == [1, 1]

    def test_jordan_nilpotent_3x3(self):
        """幂零矩阵：单个 3 阶块。"""
        r = jordan(M([[0, 1, 0], [0, 0, 1], [0, 0, 0]]))
        assert r.verified
        assert r.detail["blocks"] == [("0", 3)]

    def test_jordan_mixed_blocks(self):
        """[[3,1,0],[0,3,0],[0,0,3]]：一个 2 阶块 + 一个 1 阶块。"""
        r = jordan(M([[3, 1, 0], [0, 3, 0], [0, 0, 3]]))
        assert r.verified
        assert sorted(size for _, size in r.detail["blocks"]) == [1, 2]

    def test_jordan_complex_eigenvalues(self):
        """[[0,-1],[1,0]]：特征值 ±i，两个 1 阶块。"""
        r = jordan(M([[0, -1], [1, 0]]))
        assert r.verified
        assert [size for _, size in r.detail["blocks"]] == [1, 1]

    def test_jordan_textbook_3x3(self):
        """经典教材例：[[1,2,3],[0,1,0],[0,0,1]] → J(1,2)⊕J(1,1)。"""
        r = jordan(M([[1, 2, 3], [0, 1, 0], [0, 0, 1]]))
        assert r.verified
        assert sorted(size for _, size in r.detail["blocks"]) == [1, 2]

    def test_jordan_irreducible_charpoly(self):
        """特征多项式不可约（λ³-2 的友矩阵）：三个 1 阶块，根含根式与复数。"""
        r = jordan(M([[0, 0, 2], [1, 0, 0], [0, 1, 0]]))
        assert r.verified
        assert sorted(size for _, size in r.detail["blocks"]) == [1, 1, 1]

    def test_jordan_steps_include_kernel_dims(self):
        r = jordan(M([[1, 1], [0, 1]]))
        ops = [s.op for s in r.steps]
        assert "kernel_dims" in ops and "verify" in ops

    def test_jordan_non_square_raises(self):
        with pytest.raises(ValueError):
            jordan(M([[1, 2]]))


class TestQuadraticForm:
    def test_qf_identity_positive_definite(self):
        r = quadratic_form(matrix=[[1, 0], [0, 1]])
        assert r.verified
        assert r.detail["definiteness"] == "正定"
        assert (r.detail["p"], r.detail["q"]) == (2, 0)

    def test_qf_indefinite(self):
        r = quadratic_form(matrix=[[1, 0], [0, -1]])
        assert r.verified
        assert r.detail["definiteness"] == "不定"
        assert r.detail["signature"] == 0

    def test_qf_positive_definite_2x2(self):
        r = quadratic_form(matrix=[[2, 1], [1, 2]])
        assert r.verified
        assert r.detail["definiteness"] == "正定"

    def test_qf_semidefinite(self):
        """[[1,1],[1,1]]：特征值 0 与 2，半正定。"""
        r = quadratic_form(matrix=[[1, 1], [1, 1]])
        assert r.verified
        assert r.detail["definiteness"] == "半正定"
        assert r.detail["rank"] == 1

    def test_qf_negative_definite(self):
        r = quadratic_form(matrix=[[-1, 0], [0, -2]])
        assert r.verified
        assert r.detail["definiteness"] == "负定"
        assert (r.detail["p"], r.detail["q"]) == (0, 2)

    def test_qf_from_expression(self):
        """表达式路径：x²+2xy+y² 的矩阵是 [[1,1],[1,1]]。"""
        r = quadratic_form(expression="x**2 + 2*x*y + y**2")
        assert r.verified
        assert r.detail["definiteness"] == "半正定"

    def test_qf_expression_indefinite(self):
        r = quadratic_form(expression="x**2 + 4*x*y + y**2")
        assert r.verified
        assert r.detail["definiteness"] == "不定"
        assert r.detail["signature"] == 0

    def test_qf_zero_matrix(self):
        r = quadratic_form(matrix=[[0, 0], [0, 0]])
        assert r.detail["rank"] == 0
        assert r.detail["definiteness"] == "半正定"

    def test_qf_3x3(self):
        r = quadratic_form(matrix=[[2, 1, 0], [1, 2, 0], [0, 0, 1]])
        assert r.verified
        assert r.detail["definiteness"] == "正定"
        assert r.detail["p"] == 3

    def test_qf_nonsymmetric_raises(self):
        with pytest.raises(ValueError):
            quadratic_form(matrix=[[1, 2], [0, 1]])

    def test_qf_needs_input(self):
        with pytest.raises(ValueError):
            quadratic_form()

    def test_qf_non_homogeneous_raises(self):
        with pytest.raises(ValueError):
            quadratic_form(expression="x**2 + x")


class TestW2Tool:
    def test_quadratic_expression_does_not_evaluate_python_calls(self):
        with pytest.raises(ValueError, match="不支持函数或代码"):
            quadratic_form(expression="Symbol('x')**2")

    def test_tool_jordan_and_qf(self):
        import asyncio
        async def _run():
            tool = LinalgStepSolveTool()
            r = await tool.run(operation="jordan", matrix=[[1, 1], [0, 1]])
            assert r.summary["verified"] is True
            r2 = await tool.run(operation="quadratic_form", matrix=[[2, 1], [1, 2]])
            assert r2.summary["answer"].startswith("2,0")
            r3 = await tool.run(operation="quadratic_form", expression="x**2 + y**2")
            assert r3.summary["verified"] is True
        asyncio.run(_run())

    def test_tool_missing_matrix(self):
        import asyncio
        async def _run():
            tool = LinalgStepSolveTool()
            r = await tool.run(operation="jordan")
            assert "需要 matrix" in r.content
        asyncio.run(_run())


class TestW2VerifyAnswer:
    def test_verify_jordan_correct(self):
        ok, _ = verify_answer("jordan", [[1, 1], [0, 1]], "[[1, 1], [0, 1]]")
        assert ok

    def test_verify_jordan_wrong(self):
        ok, _ = verify_answer("jordan", [[1, 1], [0, 1]], "[[1, 0], [0, 1]]")
        assert not ok

    def test_verify_jordan_diagonalizable_equivalent(self):
        """相似矩阵（块顺序不同）也判定为正确：核维数序列相同。"""
        ok, _ = verify_answer("jordan", [[2, 0], [0, 3]], "[[3, 0], [0, 2]]")
        assert ok

    def test_verify_qf_signature(self):
        ok, _ = verify_answer("quadratic_form", [[2, 1], [1, 2]], "2,0")
        assert ok

    def test_verify_qf_keyword(self):
        ok, _ = verify_answer("quadratic_form", [[2, 1], [1, 2]], "正定")
        assert ok

    def test_verify_qf_wrong(self):
        ok, _ = verify_answer("quadratic_form", [[2, 1], [1, 2]], "1,1")
        assert not ok

    def test_verify_qf_nonsymmetric_returns_false(self):
        ok, note = verify_answer("quadratic_form", [[1, 2], [0, 1]], "正定")
        assert not ok
        assert "内核无法验算" in note
