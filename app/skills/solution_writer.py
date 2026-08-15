# -*- coding: utf-8 -*-
"""solution_writer：线代逐步解答技能（主产品 A）。

分工（数值纪律）：
- 矩阵解析与讲解组织 = 模型（agent loop 中完成）
- 一切矩阵数值 = linalg 内核（Fraction 精确 + SymPy 复算凭证）

本模块提供：
- SOLUTION_GUIDE：离线骨架（模型关闭时引导学生给出矩阵）
- parse_matrix_literals()：从题面文本抢救 JSON 字面量矩阵（离线也能算）
- render_kernel_solution()：内核结果渲染成编号步骤 Markdown
"""
from __future__ import annotations

import json
import re
from typing import Any

from app.linalg.matrix import FracMatrix

SOLUTION_GUIDE = (
    "结论先行：我可以对线性代数问题做**逐步求解 + 独立验算**——"
    "每个行变换都写出来，最后用 SymPy 复算出具凭证，数值绝不会口算出错。\n\n"
    "我能算：行列式、逆矩阵、秩、RREF、线性方程组（含基础解系）、"
    "特征值与特征向量（含可对角化判定）、Jordan 标准形、二次型（标准形/"
    "惯性指数/正定性判定）、零空间、列空间。\n\n"
    "请把题目贴进来。最方便的格式是直接给出矩阵，例如：\n"
    "「求 [[2,1],[1,3]] 的逆矩阵」或「解方程组 [[1,2],[3,4]]x=[5,11]」。\n"
    "也可以用自然语言描述，我会先提取矩阵再逐步计算。"
)

# 抢救 JSON 字面量：[[2,1],[1,3]] 或 [[2, 1], [1, 3]]（含负数与分数字符串）
_MATRIX_RE = re.compile(r"\[\s*\[\s*-?[\d./\"']+[^\]]*\](\s*,\s*\[[^\]]*\])*\s*\]")


def parse_matrix_literals(text: str) -> list[list[list[Any]]]:
    """从题面提取全部 JSON 字面量矩阵。解析失败即跳过（模型兜底）。"""
    found: list[list[list[Any]]] = []
    for m in _MATRIX_RE.finditer(text or ""):
        try:
            obj = json.loads(m.group(0))
        except json.JSONDecodeError:
            continue
        if _is_matrix(obj):
            found.append(obj)
    return found


def _is_matrix(obj: Any) -> bool:
    return (
        isinstance(obj, list) and obj
        and all(isinstance(r, list) and r for r in obj)
        and all(isinstance(c, (int, float, str)) for r in obj for c in r)
        and len({len(r) for r in obj}) == 1
    )


def try_offline_solution(query: str) -> str | None:
    """离线直答：题面含矩阵字面量 + 明确算子关键词时，直接内核求解。

    返回渲染好的 Markdown；条件不满足返回 None（走模型 agent loop）。
    这是「模型不在也能交付核心价值」的降级路径。
    """
    matrices = parse_matrix_literals(query)
    if not matrices:
        return None
    a = matrices[0]
    try:
        FracMatrix.from_json(a)
    except (ValueError, ZeroDivisionError):
        return None
    q = query.lower()
    # 算子判定：关键词足够明确才离线直答，避免算错对象。
    # solve 不离线直答：b（右端列）未知时内核无法猜，交给模型解析。
    op = None
    if "逆" in q:
        op = "inverse"
    elif "二次型" in q or "正定" in q or "负定" in q or "半正定" in q or "半负定" in q             or "惯性" in q or "符号差" in q or "配方法" in q:
        op = "quadratic_form"
    elif "若尔当" in q or "若当" in q or "jordan" in q or "标准形" in q:
        op = "jordan"
    elif "特征" in q:
        op = "eigen"
    elif "行列式" in q:
        op = "det"
    elif "秩" in q:
        op = "rank"
    elif "行阶梯" in q or "rref" in q:
        op = "rref"
    if op is None:
        return None
    from app.linalg import det, eigen, inverse, jordan, quadratic_form, rank, rref
    from app.linalg.tool import _OPERATIONS, render_steps_md

    ops = {
        "inverse": inverse, "eigen": eigen, "det": det,
        "rank": rank, "rref": rref, "jordan": jordan,
        "quadratic_form": quadratic_form,
    }
    try:
        result = ops[op](FracMatrix.from_json(a))
    except (ValueError, ZeroDivisionError, ArithmeticError):
        return None
    return render_steps_md(_OPERATIONS[op], result)


def render_solution_guide() -> str:
    """离线骨架入口（与 registry entrypoint 对齐）。"""
    return SOLUTION_GUID
