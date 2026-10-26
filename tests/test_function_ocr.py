"""函数图像可视化与拍照问疑的回归测试。"""

from __future__ import annotations

import pytest

from app.artifacts import build_artifact, validate_artifact_dict
from app.artifacts.planner import _poly_coefficients, plan_artifact
from app.ocr import OcrError, cluster_texts, redact, similarity
from app.ocr.service import _decode_image


# ------------------------------------------------------------ 系数解析


@pytest.mark.parametrize("expr,expected", [
    ("2x^2-4x+1", (2.0, -4.0, 1.0)),
    ("x²-2x-3", (1.0, -2.0, -3.0)),
    ("-x^2+4x-4", (-1.0, 4.0, -4.0)),
    ("x", (0.0, 1.0, 0.0)),
    ("2*x^2+3", (2.0, 0.0, 3.0)),
])
def test_poly_coefficients(expr, expected):
    assert _poly_coefficients(expr) == expected


@pytest.mark.parametrize("query,expected", [
    ("二次函数 y=2x^2-4x+1 的图像", (2.0, -4.0, 1.0)),
    ("画出 y = x^2 - 2x - 3 的图像", (1.0, -2.0, -3.0)),
    ("y=-x^2+4x-4 有几个根", (-1.0, 4.0, -4.0)),
])
def test_planner_uses_the_equation_in_the_question(query, expected):
    """画图必须画学生问的那个函数，不能退回默认的 y=x²。"""
    plan = plan_artifact(query)
    assert plan.matched_rule == "function_plot"
    params = plan.spec.params
    assert (params["a"], params["b"], params["c"]) == expected


def test_planner_linear_uses_k_as_slope():
    plan = plan_artifact("y = -3x + 5 图像")
    params = plan.spec.params
    assert params["family"] == "linear"
    assert params["a"] == -3.0 and params["c"] == 5.0


def test_planner_does_not_hijack_statistics_questions():
    assert plan_artifact("什么是正态分布").matched_rule == "normal"
    assert plan_artifact("中心极限定理").matched_rule == "clt"


def test_function_plot_spec_validates():
    spec = build_artifact(
        "function_plot", "抛物线", "说明", family="quadratic", a=1, b=-2, c=-3,
        interactive=["a", "b", "c"],
    )
    payload = spec.as_dict()
    assert validate_artifact_dict(payload).kind == "function_plot"


def test_function_plot_rejects_bad_domain():
    with pytest.raises(Exception):
        build_artifact("function_plot", "t", "c", family="linear", domain=[3, 1])


# ------------------------------------------------------------ 拍照问疑


def test_redact_removes_ids_and_names():
    text = "学生姓名：张三 学号：202312345678 问：什么是中心极限定理"
    out = redact(text)
    assert "张三" not in out
    assert "202312345678" not in out
    assert "中心极限定理" in out


def test_cluster_groups_similar_questions():
    texts = [
        "中心极限定理为什么样本均值服从正态分布",
        "中心极限定理的样本均值为什么近似正态",
        "p值到底是什么意思",
    ]
    clusters = cluster_texts(texts, threshold=0.15)
    assert len(clusters) == 2
    assert clusters[0].size == 2


def test_similarity_is_symmetric_and_bounded():
    a, b = "置信区间的含义", "置信区间的覆盖率"
    assert 0.0 <= similarity(a, b) <= 1.0
    assert similarity(a, b) == similarity(b, a)


def test_decode_rejects_unsupported_mime():
    with pytest.raises(OcrError):
        _decode_image("data:image/tiff;base64,AAAA")


def test_decode_rejects_bad_base64():
    with pytest.raises(OcrError):
        _decode_image("data:image/png;base64,!!!notbase64!!!")
