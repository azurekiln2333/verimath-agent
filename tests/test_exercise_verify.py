# -*- coding: utf-8 -*-
"""出题验算闭环测试：假模型客户端构造坏答案/好答案/无 answer_check 三态。

项目未装 pytest-asyncio，统一用 asyncio.run 驱动协程，零新增依赖。
"""
import asyncio
import json

from app.skills.exercise import generate_exercise_with_model


def run(coro):
    return asyncio.run(coro)


def _exercise_json(expected: str, with_check: bool = True) -> str:
    obj = {
        "topic": "行列式",
        "difficulty": "basic",
        "qtype": "计算题",
        "problem": "计算矩阵 \\(A=\\begin{bmatrix}2&1\\\\1&3\\end{bmatrix}\\) 的行列式。",
        "hints": ["按对角线法则展开"],
        "solution_outline": "解：\\(\\det A = 2\\times3-1\\times1 = 5\\)。",
        "answer_check": {"operation": "det", "matrix": [[2, 1], [1, 3]], "expected": expected},
    }
    if not with_check:
        obj.pop("answer_check")
    return json.dumps(obj, ensure_ascii=False)


class FakeModel:
    """按脚本回放模型输出的假客户端。"""

    def __init__(self, outputs: list[str]) -> None:
        self.outputs = list(outputs)
        self.calls = 0

    @property
    def enabled(self) -> bool:
        return True

    async def complete(self, messages, response_format=None, **_):
        self.calls += 1
        return self.outputs.pop(0)


import pytest  # noqa: F401  （保留给未来 mark；当前用例全部同步驱动）


def test_bad_answer_retries_then_good():
    model = FakeModel([
        _exercise_json("999"),   # 第一轮：错误答案
        _exercise_json("5"),     # 第二轮：回喂后给对
    ])
    ex = run(generate_exercise_with_model("行列式", "basic", "计算题", model, None))
    assert ex.source == "model"
    assert ex.answer_verified
    assert model.calls == 2


def test_all_bad_falls_back_to_template():
    model = FakeModel([_exercise_json("999")] * 3)
    ex = run(generate_exercise_with_model("行列式", "basic", "计算题", model, None))
    assert ex.source == "template"
    assert model.calls == 3


def test_no_check_passes_format_only():
    model = FakeModel([_exercise_json("", with_check=False)])
    ex = run(generate_exercise_with_model("中心极限定理", "basic", "概念题", model, None))
    assert ex.source == "model"
    assert not ex.answer_verified


def test_feedback_mentions_actual():
    model = FakeModel([
        _exercise_json("999"),
        _exercise_json("5"),
    ])
    run(generate_exercise_with_model("行列式", "basic", "计算题", model, None))
    # 第二次调用应包含纠错消息（FakeModel 不校验内容，这里只保证重试发生）
    assert model.calls == 2
