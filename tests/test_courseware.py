# -*- coding: utf-8 -*-
"""courseware 结构化生成测试：FakeModel 驱动，覆盖成功/自检失败回退/验算三态。"""
import asyncio
import json

from app.skills.courseware import (
    generate_courseware,
    generate_courseware_with_model,
    render_courseware_md,
)

SECTIONS = [
    {"id": "motivation", "title": "动机问题", "content": "为什么需要 \\(n-1\\)？"},
    {"id": "definition", "title": "定义与记号", "content": "样本方差 \\(s^2\\)。"},
    {"id": "theorem", "title": "定理与条件", "content": "条件：独立同分布。"},
    {"id": "example", "title": "例子与计算", "content": "算得 \\(s^2=5\\)。"},
    {"id": "pitfalls", "title": "常见误区", "content": "误区一：除以 n。"},
    {"id": "exercises", "title": "练习", "content": "练习 1。"},
    {"id": "summary", "title": "小结", "content": "三句话以内。"},
]


def run(coro):
    return asyncio.run(coro)


class FakeModel:
    def __init__(self, outputs):
        self.outputs = list(outputs)
        self.calls = 0

    @property
    def enabled(self):
        return True

    async def complete(self, messages, response_format=None, **_):
        self.calls += 1
        return self.outputs.pop(0)


def _cw_json(answer_check=None):
    obj = {"topic": "样本方差", "sections": SECTIONS}
    if answer_check:
        obj["answer_check"] = answer_check
    return json.dumps(obj, ensure_ascii=False)


class Disabled:
    enabled = False

    async def complete(self, *a, **k):  # pragma: no cover
        raise AssertionError("disabled client must not be called")


def test_offline_fallback():
    cw, md = run(generate_courseware_with_model("任意主题", None, None))
    assert cw.source == "template"
    assert "七段式" in md


def test_disabled_client_falls_back():
    cw, _ = run(generate_courseware_with_model("任意", Disabled(), None))
    assert cw.source == "template"


def test_model_success_with_seven_sections():
    model = FakeModel([_cw_json()])
    cw, md = run(generate_courseware_with_model("样本方差", model, None))
    assert cw.source == "model"
    assert cw.self_check_ok
    assert len(cw.sections) == 7
    assert "## 动机问题" in md


def test_example_verified_when_check_ok():
    model = FakeModel([_cw_json({"operation": "det", "matrix": [[2, 1], [1, 3]],
                                 "expected": "5"})])
    cw, md = run(generate_courseware_with_model("行列式", model, None))
    assert cw.example_verified is True
    assert "已通过计算内核" in md


def test_example_mismatch_flagged():
    model = FakeModel([_cw_json({"operation": "det", "matrix": [[2, 1], [1, 3]],
                                 "expected": "999"})])
    cw, md = run(generate_courseware_with_model("行列式", model, None))
    assert cw.example_verified is False
    assert "复核" in md


def test_incomplete_sections_retry_then_fallback():
    bad = json.dumps({"topic": "x", "sections": SECTIONS[:3]}, ensure_ascii=False)
    model = FakeModel([bad, bad])  # 两次都不完整
    cw, _ = run(generate_courseware_with_model("主题", model, None))
    assert cw.source == "template"
    assert model.calls == 2
