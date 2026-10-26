"""artifact spec 契约测试。

这一层的价值全在"拒绝得干净"：模型输出会各种花式出错，
校验必须挡住每一种，并且只抛一种异常，让上层降级逻辑简单可靠。

**宁可不画图，也不能画错的图** —— 一张参数错误的分布图比没有图更有害，
因为学生会当成真的去理解。所以这里的测试全是"该拒的必须拒"。
"""

from __future__ import annotations

import json

import pytest

from app.artifacts import (
    WIDGET_REGISTRY,
    ArtifactSpec,
    ArtifactValidationError,
    build_artifact,
    describe_widgets_for_prompt,
    validate_artifact_dict,
)
from app.artifacts.spec import WIDGET_PURPOSE

_VALID = {
    "distribution_explorer": {"family": "normal", "params": {"mu": 0, "sigma": 1}},
    "hypothesis_test": {"test": "t", "df": 18, "statistic": 2.31},
    "sampling_distribution": {"population": "expon", "sample_size": 30},
    "confidence_interval": {"sample_size": 25},
    "power_curve": {"x_axis": "n", "effect_size": 0.5},
    "scatter_regression": {"x": [1, 2, 3, 4], "y": [2, 4, 5, 8]},
    "data_plot": {"series": [{"label": "A", "values": [1, 2, 3]}]},
    "effect_size": {
        "items": [{"label": "A", "estimate": 0.5, "ci_low": 0.1, "ci_high": 0.9}]
    },
    "function_plot": {"family": "quadratic", "a": 1, "b": -2, "c": -3},
}


def _wrap(kind: str, params: dict) -> dict:
    return {"kind": kind, "title": "标题", "caption": "说明文字", "params": params}


@pytest.mark.parametrize("kind", sorted(WIDGET_REGISTRY))
def test_every_widget_has_a_valid_example(kind: str) -> None:
    """注册表里每个 widget 都必须有可用样例 —— 新增 widget 时强制补上。"""
    assert kind in _VALID, f"{kind} 缺少测试样例"
    spec = validate_artifact_dict(_wrap(kind, _VALID[kind]))
    assert spec.kind == kind


@pytest.mark.parametrize("kind", sorted(WIDGET_REGISTRY))
def test_every_widget_has_purpose_text(kind: str) -> None:
    """每个 widget 必须有"什么时候用"的说明，否则模型无从选型。"""
    purpose = WIDGET_PURPOSE.get(kind, "")
    assert purpose, f"{kind} 没有用途说明"
    assert "时用" in purpose or "用" in purpose, f"{kind} 的说明没讲何时使用"


@pytest.mark.parametrize("kind", sorted(WIDGET_REGISTRY))
def test_as_dict_is_json_serializable(kind: str) -> None:
    payload = validate_artifact_dict(_wrap(kind, _VALID[kind])).as_dict()
    text = json.dumps(payload, ensure_ascii=False)
    assert json.loads(text)["kind"] == kind
    assert set(payload) == {"kind", "title", "caption", "params"}


def test_unknown_kind_rejected() -> None:
    with pytest.raises(ArtifactValidationError) as exc:
        validate_artifact_dict(_wrap("bar_chart_3d", {}))
    # 报错必须列出可用取值，模型才可能自我纠正
    assert "hypothesis_test" in str(exc.value)


def test_extra_fields_rejected() -> None:
    """多余字段必须拒。模型爱自己发明参数，静默忽略会让它以为生效了。"""
    with pytest.raises(ArtifactValidationError):
        validate_artifact_dict(_wrap("hypothesis_test", {
            "test": "t", "statistic": 1.0, "color": "red"
        }))
    with pytest.raises(ArtifactValidationError):
        validate_artifact_dict({
            "kind": "hypothesis_test", "title": "t", "caption": "c",
            "params": {"test": "t", "statistic": 1.0}, "extra_top": 1,
        })


def test_caption_is_mandatory() -> None:
    """图必须自带解释 —— 没有说明的统计图容易被误读。"""
    with pytest.raises(ArtifactValidationError):
        validate_artifact_dict({
            "kind": "hypothesis_test", "title": "标题", "caption": "",
            "params": {"test": "t", "statistic": 1.0},
        })
    with pytest.raises(ArtifactValidationError):
        validate_artifact_dict({
            "kind": "hypothesis_test", "title": "标题",
            "params": {"test": "t", "statistic": 1.0},
        })


def test_title_and_caption_length_bounded() -> None:
    """防止模型把整段解释塞进 caption 挤爆面板。"""
    with pytest.raises(ArtifactValidationError):
        validate_artifact_dict(_wrap_custom(title="标" * 200))
    with pytest.raises(ArtifactValidationError):
        validate_artifact_dict(_wrap_custom(caption="说" * 700))


def _wrap_custom(title: str = "标题", caption: str = "说明") -> dict:
    return {
        "kind": "hypothesis_test", "title": title, "caption": caption,
        "params": {"test": "t", "statistic": 1.0},
    }


def test_non_dict_input_rejected() -> None:
    for bad in ("字符串", 42, None, [1, 2], True):
        with pytest.raises(ArtifactValidationError):
            validate_artifact_dict(bad)


# --------------------------------------------------- 逐 widget 的参数约束


def test_hypothesis_test_param_constraints() -> None:
    for bad in (
        {"test": "t", "statistic": 1.0, "alpha": 0.0},
        {"test": "t", "statistic": 1.0, "alpha": 1.0},
        {"test": "t", "statistic": 1.0, "alpha": -0.1},
        {"test": "t", "statistic": 1.0, "df": 0},
        {"test": "t", "statistic": 1.0, "df": -5},
        {"test": "wilcoxon", "statistic": 1.0},
        {"test": "t", "statistic": 1.0, "alternative": "both"},
        {"test": "t"},                                    # 缺 statistic
    ):
        with pytest.raises(ArtifactValidationError):
            validate_artifact_dict(_wrap("hypothesis_test", bad))


def test_scatter_regression_length_and_size() -> None:
    with pytest.raises(ArtifactValidationError):
        validate_artifact_dict(_wrap("scatter_regression",
                                     {"x": [1, 2, 3], "y": [1, 2]}))
    with pytest.raises(ArtifactValidationError):
        validate_artifact_dict(_wrap("scatter_regression",
                                     {"x": [1, 2], "y": [1, 2]}))
    with pytest.raises(ArtifactValidationError):
        validate_artifact_dict(_wrap("scatter_regression",
                                     {"x": [1, 2, 3], "y": [1, 2, float("nan")]}))


def test_sampling_distribution_bounds() -> None:
    """上限存在的理由：n_samples=1e9 会把浏览器卡死。"""
    with pytest.raises(ArtifactValidationError):
        validate_artifact_dict(_wrap("sampling_distribution",
                                     {"population": "normal", "sample_size": 0}))
    with pytest.raises(ArtifactValidationError):
        validate_artifact_dict(_wrap("sampling_distribution",
                                     {"population": "normal", "sample_size": 5,
                                      "n_samples": 10_000_000}))
    with pytest.raises(ArtifactValidationError):
        validate_artifact_dict(_wrap("sampling_distribution",
                                     {"population": "cauchy", "sample_size": 5}))


def test_sampling_distribution_seed_defaults_present() -> None:
    """seed 必须有默认值并出现在载荷里 —— 复现性不能靠模型记得填。"""
    payload = validate_artifact_dict(_wrap(
        "sampling_distribution", {"population": "normal", "sample_size": 30}
    )).as_dict()
    assert isinstance(payload["params"]["seed"], int)


def test_confidence_interval_bounds() -> None:
    for bad in (
        {"sample_size": 1},
        {"sample_size": 25, "ci_level": 1.0},
        {"sample_size": 25, "ci_level": 0.0},
        {"sample_size": 25, "true_sd": 0},
        {"sample_size": 25, "n_intervals": 1000},
    ):
        with pytest.raises(ArtifactValidationError):
            validate_artifact_dict(_wrap("confidence_interval", bad))


def test_power_curve_bounds() -> None:
    for bad in (
        {"x_axis": "n", "alpha": 0},
        {"x_axis": "n", "target_power": 1.0},
        {"x_axis": "sample", "effect_size": 0.5},
        {"x_axis": "n", "n_per_group": 1},
    ):
        with pytest.raises(ArtifactValidationError):
            validate_artifact_dict(_wrap("power_curve", bad))


def test_data_plot_series_validation() -> None:
    for bad in (
        {"series": []},
        {"series": [{"label": "A", "values": []}]},
        {"series": [{"label": "A"}]},
        {"series": [{"label": "A", "values": [1, float("nan")]}]},
        {"series": [{"label": "A", "values": "1,2,3"}]},
        {"series": [{"label": str(i), "values": [1]} for i in range(9)]},
        {"series": [{"label": "A", "values": [1, 2]}], "kind": "pie"},
        {"series": [{"label": "A", "values": [1, 2]}], "bins": 0},
    ):
        with pytest.raises(ArtifactValidationError):
            validate_artifact_dict(_wrap("data_plot", bad))


def test_effect_size_requires_estimate_inside_ci() -> None:
    """点估计落在区间外说明上游算错了，必须拦住而不是画一张自相矛盾的图。"""
    with pytest.raises(ArtifactValidationError):
        validate_artifact_dict(_wrap("effect_size", {
            "items": [{"label": "A", "estimate": 5, "ci_low": 0, "ci_high": 1}]
        }))
    with pytest.raises(ArtifactValidationError):
        validate_artifact_dict(_wrap("effect_size", {
            "items": [{"label": "A", "estimate": 0.5, "ci_low": 0.9, "ci_high": 0.1}]
        }))
    with pytest.raises(ArtifactValidationError):
        validate_artifact_dict(_wrap("effect_size", {"items": [{"label": "A"}]}))


def test_distribution_explorer_family_and_params() -> None:
    with pytest.raises(ArtifactValidationError):
        validate_artifact_dict(_wrap("distribution_explorer",
                                     {"family": "weibull"}))
    with pytest.raises(ArtifactValidationError):
        validate_artifact_dict(_wrap("distribution_explorer",
                                     {"family": "t", "params": {"df": float("nan")}}))
    with pytest.raises(ArtifactValidationError):
        validate_artifact_dict(_wrap("distribution_explorer",
                                     {"family": "t", "show": "quantile"}))


# ------------------------------------------------------------ 提示词描述


def test_prompt_description_lists_all_widgets() -> None:
    """描述必须覆盖全部 widget，否则模型不知道某些 kind 的存在。"""
    text = describe_widgets_for_prompt()
    for kind in WIDGET_REGISTRY:
        assert kind in text, f"提示词描述缺少 {kind}"


def test_prompt_description_marks_required_fields() -> None:
    text = describe_widgets_for_prompt()
    assert "statistic*" in text, "必填字段应带 * 标记"
    assert "两侧" in text or "必填" in text


def test_prompt_description_stays_compact() -> None:
    """会拼进每次请求的系统提示词，太长会挤占上下文预算。"""
    text = describe_widgets_for_prompt()
    assert len(text) < 3000, f"widget 描述过长: {len(text)} 字符"


def test_prompt_description_can_be_subset() -> None:
    text = describe_widgets_for_prompt(["hypothesis_test"])
    assert "hypothesis_test" in text
    assert "power_curve" not in text


def test_build_artifact_helper() -> None:
    spec = build_artifact("power_curve", "功效曲线", "看样本量如何影响功效",
                          x_axis="n", effect_size=0.5)
    assert isinstance(spec, ArtifactSpec)
    assert spec.as_dict()["params"]["effect_size"] == 0.5
    with pytest.raises(ArtifactValidationError):
        build_artifact("power_curve", "t", "c", x_axis="bogus")
