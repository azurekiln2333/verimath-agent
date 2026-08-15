# -*- coding: utf-8 -*-
"""W1 演示脚本：三个内核算子的逐步输出（无需模型、无需密钥）。

演示内容：
  1) 3x3 逆矩阵（Gauss-Jordan 全步骤 + SymPy 复算凭证）
  2) 2x2 特征值（特征方程 + 特征空间 + 可对角化判定）
  3) 含自由变量的线性方程组（通解 + 基础解系）
  4) Jordan 标准形（块结构 + 过渡矩阵 + 相似不变量复算）
  5) 二次型（标准形 + 惯性指数 + 正定性判定）

运行：.venv\\Scripts\\python.exe scripts\\demo_linalg.py
"""
import asyncio
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parents[1]))
if sys.stdout.encoding and sys.stdout.encoding.lower() not in ("utf-8", "utf8"):
    sys.stdout.reconfigure(encoding="utf-8", errors="replace")

from app.linalg.tool import LinalgStepSolveTool


async def main() -> None:
    tool = LinalgStepSolveTool()
    demos = [
        ("inverse", [[2, 1, 0], [1, 3, 1], [0, 1, 2]], None),
        ("eigen", [[4, 1], [2, 3]], None),
        ("solve", [[1, 2, 3], [2, 4, 6]], [6, 12]),
        ("jordan", [[3, 1, 0], [0, 3, 0], [0, 0, 3]], None),
        ("quadratic_form", [[2, 1], [1, 2]], None),
    ]
    for op, matrix, b in demos:
        result = await tool.run(operation=op, matrix=matrix, b=b)
        print("=" * 60)
        print(f"operation = {op}")
        print("=" * 60)
        print(result.content)
        print()


if __name__ == "__main__":
    asyncio.run(main())
