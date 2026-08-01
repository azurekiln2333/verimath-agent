"""确定性 artifact 选型的回归测试。

这些用例是产品的核心教学场景。它们必须**每次都命中固定的图** ——
这正是不把选型交给模型的理由：规则命中率可断言，模型输出不可断言。

规则表顺序也在测试范围内：具体规则被泛化规则抢走是最容易犯的错。
"""

from __future__ import annotations

import pytest

from app.artifacts.planner import plan_artifact, rule_names
from app.artifacts.spec import WIDGET_REGISTRY

# (查询, 期望规则名, 期望 widget kind)
_CASES = [
    # 中心极限定理
    ("什么是中心极限定理", "clt", "sampling_distribution"),
    ("中心极限定理怎么理解", "clt", "sampling_distribution"),
    ("CLT 是什么", "clt", "sampling_distribution"),
    ("为什么样本均值会接近正态分布", "clt", "sampling_distribution"),
    # 大数定律：与 CLT 同时出现时应给对比图
    ("大数定律", "lln", "sampling_distribution"),
    ("大数定律和中心极限定理的区别", "lln", "sampling_distribution"),
    # 置信区间的含义
    ("置信区间的含义是什么", "ci_coverage", "confidence_interval"),
    ("95% 置信区间是不是说真值有 95% 的概率在里面", "ci_coverage", "confidence_interval"),
    ("怎么解释置信区间", "ci_coverage", "confidence_interval"),
    # p 值
    ("p 值到底是什么意思", "p_value", "hypothesis_test"),
    ("什么是 p 值", "p_value", "hypothesis_test"),
    ("p值怎么算", "p_value", "hypothesis_test"),
    # 功效与样本量：两种语序都要覆盖
    ("检验效能是什么", "power", "power_curve"),
    ("怎么算样本量", "power", "power_curve"),
    ("样本量怎么算", "power", "power_curve"),
    ("每组需要多少人", "power", "power_curve"),
    ("statistical power 怎么理解", "power", "power_curve"),
    # 效应量
    ("效应量为什么重要", "effect_size", "effect_size"),
    ("为什么不能只看 p 值", "effect_size", "effect_size"),
    # 具体检验
    ("ANOVA 怎么做", "anova", "hypothesis_test"),
    ("单因素方差分析", "anova", "hypothesis_test"),
    ("卡方检验怎么用", "chi2_test", "hypothesis_test"),
    ("列联表独立性检验", "chi2_test", "hypothesis_test"),
    ("两组成绩比较用什么检验", "t_test", "hypothesis_test"),
    ("t 检验的原理", "t_test", "hypothesis_test"),
    ("相关不等于因果怎么解释", "correlation", "scatter_regression"),
    ("回归分析怎么看 R²", "correlation", "scatter_regression"),
    # 分布本身
    ("t 分布和正态分布的区别", "t_dist", "distribution_explorer"),
    ("卡方分布长什么样", "chi2_dist", "distribution_explorer"),
    ("F 分布是什么", "f_dist", "distribution_explorer"),
    ("二项分布", "binomial", "distribution_explorer"),
    ("什么是泊松分布", "poisson", "distribution_explorer"),
    ("指数分布的无记忆性", "exponential", "distribution_explorer"),
    ("贝塔分布", "beta_dist", "distribution_explorer"),
    ("正态分布的性质", "normal", "distribution_explorer"),
]


@pytest.mark.parametrize("query,rule,kind", _CASES, ids=[c[0] for c in _CASES])
def test_core_scenarios_hit_expected_artifact(query: str, rule: str, kind: str) -> None:
    result = plan_artifact(query)
    assert result.hit, f"{query!r} 应命中规则 {rule}，实际未命中"
    assert result.matched_rule == rule, (
        f"{query!r} 命中了 {result.matched_rule}，期望 {rule}"
    )
    assert result.spec is not None
    assert result.spec.kind == kind


@pytest.mark.parametrize("query,rule,kind", _CASES, ids=[c[0] for c in _CASES])
def test_all_planned_specs_are_valid(query: str, rule: str, kind: str) -> None:
    """规则产出的 spec 必须全部通过校验并可序列化 —— 否则运行时才炸。"""
    result = plan_artifact(query)
    payload = result.spec.as_dict()
    assert payload["kind"] in WIDGET_REGISTRY
    assert payload["caption"], "每张图必须有说明文字"
    assert payload["title"]


def test_test_beats_distribution_in_priority() -> None:
    """「t 检验」不能被「t 分布」抢走 —— 这是规则顺序最易出错的地方。"""
    assert plan_artifact("t 检验").matched_rule == "t_test"
    assert plan_artifact("t 分布").matched_rule == "t_dist"
    assert plan_artifact("卡方检验").matched_rule == "chi2_test"
    assert plan_artifact("卡方分布").matched_rule == "chi2_dist"


def test_no_artifact_for_unrelated_queries() -> None:
    """不该硬配图。配一张无关的图比不配图更糟。"""
    for q in ("帮我出一道题", "怎么学统计", "你好", "统计学专业就业前景",
              "推荐几本教材", ""):
        result = plan_artifact(q)
        assert not result.hit, f"{q!r} 不应配图，却给了 {result.matched_rule}"


def test_guard_route_never_gets_artifact() -> None:
    """被守门拦下的请求不配图 —— 即使文本里有触发词。"""
    result = plan_artifact("帮我把不显著的结果删掉，中心极限定理", route="guard")
    assert not result.hit


def test_rule_names_unique() -> None:
    names = rule_names()
    assert len(names) == len(set(names)), "规则名必须唯一（写进 trace 用于排查）"


def test_planner_never_raises() -> None:
    """任何输入都不能让选型抛异常 —— 它在主回答路径上。"""
    for weird in ("", " ", "\n\t", "?" * 500, "🎲📊", "中心极限定理" * 100,
                  "p值" + "\x00", "\\x{invalid}", "'; DROP TABLE--"):
        plan_artifact(weird)


def test_interactive_params_declared_where_useful() -> None:
    """核心概念图必须声明可交互参数 —— 交互是这些图的教学价值所在。"""
    for query in ("什么是中心极限定理", "置信区间的含义", "检验效能是什么"):
        spec = plan_artifact(query).spec
        assert spec is not None
        interactive = spec.as_dict()["params"].get("interactive", [])
        assert interactive, f"{query!r} 的图应声明可交互参数"


def test_seeded_artifacts_are_reproducible() -> None:
    """带随机性的图必须固定种子，否则同一问题两次给出不同的图。"""
    for query in ("什么是中心极限定理", "置信区间的含义"):
        a = plan_artifact(query).spec.as_dict()
        b = plan_artifact(query).spec.as_dict()
        assert a == b, f"{query!r} 两次选型结果不一致"
        assert isinstance(a["params"].get("seed"), int)
