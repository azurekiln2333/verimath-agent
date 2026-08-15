# -*- coding: utf-8 -*-
"""生成线性代数评测种子集：确定性随机矩阵 + 内核标准答案，写入 eval/seeds_linalg.jsonl。

为什么不用 LLM 出题：种子的职责是当「标准答案基准」——答案必须绝对可信，
内核算出的 Fraction 答案天然满足；LLM 出的题留给 run_eval 时模型作答，
再用本种子集比对（题可换，答案生成器不换）。

运行：.venv\\Scripts\\python.exe scripts\\gen_linalg_seeds.py
"""
import asyncio
import json
import random
import sys
from fractions import Fraction
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parents[1]))

from app.linalg import FracMatrix, det, inverse, jordan, quadratic_form, rank, rref, solve

EVAL_DIR = Path(__file__).resolve().parents[1] / "eval"
TARGET = 50


def rand_matrix(rng: random.Random, m: int, n: int) -> list[list[int]]:
    return [[rng.randint(-5, 5) for _ in range(n)] for _ in range(m)]


def frac_str(value: Fraction) -> str:
    return str(value)


def main() -> None:
    rng = random.Random(42)
    seeds: list[dict] = []

    def add(operation: str, matrix: list[list], expected: str,
            prompt: str, b: list | None = None) -> None:
        seeds.append({
            "id": f"linalg-{operation}-{len(seeds) + 1:03d}",
            "operation": operation,
            "matrix": matrix,
            **({"b": b} if b is not None else {}),
            "expected": expected,
            "prompt": prompt,
        })

    # det ×12（2x2 与 3x3）
    while sum(1 for s in seeds if s["operation"] == "det") < 12:
        n = rng.choice([2, 3])
        m = rand_matrix(rng, n, n)
        if all(all(c == 0 for c in row) for row in m):
            continue
        val = det(FracMatrix.from_json(m)).answer_value
        add("det", m, val, f"计算矩阵 {m} 的行列式。")

    # rank ×8
    while sum(1 for s in seeds if s["operation"] == "rank") < 8:
        m = rand_matrix(rng, rng.choice([2, 3]), 3)
        if all(all(c == 0 for c in row) for row in m):
            continue
        add("rank", m, rank(FracMatrix.from_json(m)).answer_value,
            f"求矩阵 {m} 的秩。")

    # inverse ×10（跳过不可逆）
    while sum(1 for s in seeds if s["operation"] == "inverse") < 10:
        n = rng.choice([2, 3])
        m = rand_matrix(rng, n, n)
        res = inverse(FracMatrix.from_json(m))
        if not res.detail.get("invertible"):
            continue
        add("inverse", m, res.answer_value, f"求矩阵 {m} 的逆矩阵。")

    # rref ×10
    while sum(1 for s in seeds if s["operation"] == "rref") < 10:
        m = rand_matrix(rng, rng.choice([2, 3]), rng.choice([2, 3]))
        if all(all(c == 0 for c in row) for row in m):
            continue
        add("rref", m, rref(FracMatrix.from_json(m)).answer_value,
            f"把矩阵 {m} 化为最简行阶梯形。")

    # solve ×10（8 个一致系统 + 2 个可能无解，如实记录）
    # expected 用验算器可解析的模型风格：唯一解 "x1, x2"；无解 "no_solution"；
    # 无穷解 "infinite:特解串;基础解系串"（验算器按解型比对）。
    def solve_expected(res) -> str:
        st = res.detail["solution_type"]
        if st == "no_solution":
            return "no_solution"
        if st == "infinite":
            p = res.detail.get("particular") or []
            basis = res.detail.get("basis") or []
            return "infinite:" + ", ".join(str(x) for x in p) + ";" + ";".join(
                ", ".join(str(x) for x in v) for v in basis)
        xs = res.detail.get("solution") or res.answer_value
        return ", ".join(str(x) for x in xs) if isinstance(xs, list) else str(xs)

    made = 0
    while made < 10:
        m = rand_matrix(rng, 3, 3)
        if made < 8:
            x = [rng.randint(-4, 4) for _ in range(3)]
            b = [sum(a * xi for a, xi in zip(row, x)) for row in m]
        else:
            b = [rng.randint(-9, 9) for _ in range(3)]
        res = solve(FracMatrix.from_json(m), b)
        if res.detail["solution_type"] == "unique" and made < 8:
            add("solve", m, solve_expected(res), f"解线性方程组 A={m}, b={b}。", b=b)
            made += 1
        elif made >= 8:
            add("solve", m, solve_expected(res), f"解线性方程组 A={m}, b={b}。", b=b)
            made += 1

    # W2 高代扩展：Jordan 标准形 + 二次型（手工精选教学用例，答案由内核算出）
    # jordan ×7：覆盖不可对角化/可对角化/幂零/混合块/复数根/不可约特征多项式
    w2_jordan = [
        [[1, 1], [0, 1]],
        [[2, 0], [0, 3]],
        [[0, 1, 0], [0, 0, 1], [0, 0, 0]],
        [[2, 1, 0], [0, 2, 1], [0, 0, 2]],
        [[3, 1, 0], [0, 3, 0], [0, 0, 3]],
        [[0, -1], [1, 0]],
        [[0, 0, 2], [1, 0, 0], [0, 1, 0]],
    ]
    for m in w2_jordan:
        res_j = jordan(FracMatrix.from_json(m))
        add("jordan", m, res_j.detail.get("jordan_plain", res_j.answer_value),
            f"求矩阵 {m} 的 Jordan 标准形。")

    # quadratic_form ×7：正定/负定/不定/半正定/表达式/零矩阵/3x3
    w2_qf = [
        ([[1, 0], [0, 1]], None),
        ([[1, 0], [0, -1]], None),
        ([[2, 1], [1, 2]], None),
        ([[1, 1], [1, 1]], None),
        ([[-1, 0], [0, -2]], None),
        ([[2, 1, 0], [1, 2, 0], [0, 0, 1]], None),
        ([[0, 0], [0, 0]], None),
    ]
    for m, _e in w2_qf:
        res_q = quadratic_form(matrix=m)
        add("quadratic_form", m, f"{res_q.detail['p']},{res_q.detail['q']}",
            f"判断二次型 xᵀA x（A={m}）的标准形、惯性指数与正定性。")
    res_qe = quadratic_form(expression="x**2 + 2*x*y + y**2")
    add("quadratic_form", [[1, 1], [1, 1]], f"{res_qe.detail['p']},{res_qe.detail['q']}",
        "判断二次型 x²+2xy+y² 是否正定。",)

    assert len(seeds) >= TARGET, f"应生成 ≥{TARGET} 条，实际 {len(seeds)}"
    EVAL_DIR.mkdir(exist_ok=True)
    out = EVAL_DIR / "seeds_linalg.jsonl"
    with open(out, "w", encoding="utf-8") as f:
        for s in seeds:
            f.write(json.dumps(s, ensure_ascii=False) + "\n")
    print(f"written {len(seeds)} seeds -> {out}")


if __name__ == "__main__":
    main()
