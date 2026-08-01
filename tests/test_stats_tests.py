"""假设检验层的正确性断言。

基准同样来自可独立验证的关系，不用记忆值：
- t 检验：与手算公式对照；退化输入必须抛错而非返回垃圾
- ANOVA：k=2 时 F 必须等于 Student t 的平方（这是精确的代数恒等式）
- 卡方：2x2 表与手算对照；期望频数 < 5 必须进警告
- 相关：与回归斜率的关系、秩相关对单调变换的不变性

另有一组"契约"测试：**每个检验都必须返回置信区间和效应量**。
这不是风格检查 —— guard.py 的 statistical_integrity 规则要求答案里同时
报告效应量与置信区间，计算层若不给，上层就无法遵守自己的规则。
"""

from __future__ import annotations

import math

import pytest

from app.stats.tests import (
    _ranks,
    anova_oneway,
    chi2_independence,
    mean,
    one_sample_t,
    paired_t,
    pearson,
    spearman,
    stdev,
    student_t,
    variance,
    welch_t,
)

A = [5.1, 4.9, 6.2, 5.8, 5.5, 5.3, 6.0, 5.7]
B = [4.2, 4.5, 3.9, 4.8, 4.1, 4.4, 4.0, 4.6]


# --------------------------------------------------------------- 描述统计


def test_variance_is_unbiased_by_default() -> None:
    """ddof=1 是推断统计的默认。写成 0 会系统性低估总体方差。"""
    xs = [2.0, 4.0, 4.0, 4.0, 5.0, 5.0, 7.0, 9.0]
    assert variance(xs, ddof=1) == pytest.approx(32.0 / 7.0, rel=1e-15)
    assert variance(xs, ddof=0) == pytest.approx(4.0, rel=1e-15)
    assert stdev(xs) == pytest.approx(math.sqrt(32.0 / 7.0), rel=1e-15)


def test_empty_or_singleton_raises() -> None:
    with pytest.raises(ValueError):
        mean([])
    with pytest.raises(ValueError):
        variance([1.0])          # n-ddof = 0，无法估计


def test_ranks_average_ties() -> None:
    assert _ranks([10, 20, 30]) == [1.0, 2.0, 3.0]
    assert _ranks([10, 20, 20, 30]) == [1.0, 2.5, 2.5, 4.0]
    assert _ranks([5, 5, 5]) == [2.0, 2.0, 2.0]


# ----------------------------------------------------------------- t 检验


def test_one_sample_t_matches_hand_formula() -> None:
    xs = [5.0, 6.0, 7.0, 8.0, 9.0]
    r = one_sample_t(xs, mu0=6.0)
    expect_t = (7.0 - 6.0) / (stdev(xs) / math.sqrt(5))
    assert r.statistic == pytest.approx(expect_t, rel=1e-14)
    assert r.df == 4.0
    # estimate 是样本均值本身，与 CI 同标度
    assert r.estimate == pytest.approx(7.0, rel=1e-14)
    assert r.detail["mean_minus_mu0"] == pytest.approx(1.0, rel=1e-14)
    lo, hi = r.ci
    assert lo < r.estimate < hi
    assert (lo + hi) / 2 == pytest.approx(7.0, rel=1e-14)


def test_one_sample_ci_contains_mu0_iff_not_significant() -> None:
    """单样本检验的对偶关系是"CI 是否包含 mu0"，不是"是否包含 0"。
    这条断言防的是 estimate 与 ci 标度不一致的 bug。"""
    xs = [5.0, 6.0, 7.0, 8.0, 9.0]
    for mu0 in (2.0, 5.0, 6.0, 7.0, 12.0):
        r = one_sample_t(xs, mu0=mu0)
        contains = r.ci[0] <= mu0 <= r.ci[1]
        assert contains == (r.p_value >= 0.05), f"mu0={mu0} 时 CI 与 p 值矛盾"


def test_welch_t_statistic_and_df() -> None:
    r = welch_t(A, B)
    v1, v2, n1, n2 = variance(A), variance(B), len(A), len(B)
    se = math.sqrt(v1 / n1 + v2 / n2)
    assert r.statistic == pytest.approx((mean(A) - mean(B)) / se, rel=1e-14)
    expect_df = (v1 / n1 + v2 / n2) ** 2 / (
        (v1 / n1) ** 2 / (n1 - 1) + (v2 / n2) ** 2 / (n2 - 1)
    )
    assert r.df == pytest.approx(expect_df, rel=1e-14)
    # Welch 自由度必须落在 min(n1,n2)-1 与 n1+n2-2 之间
    assert min(n1, n2) - 1 <= r.df <= n1 + n2 - 2


def test_welch_does_not_use_pooled_sd_for_effect_size() -> None:
    """Welch 的效应量分母用两组标准差的均方根，不用合并标准差 ——
    后者假设方差齐性，与 Welch 自身前提矛盾。"""
    r = welch_t(A, B)
    rms = math.sqrt((variance(A) + variance(B)) / 2)
    assert r.effect_size == pytest.approx((mean(A) - mean(B)) / rms, rel=1e-14)


def test_student_t_uses_pooled_variance() -> None:
    r = student_t(A, B)
    n1, n2 = len(A), len(B)
    sp2 = ((n1 - 1) * variance(A) + (n2 - 1) * variance(B)) / (n1 + n2 - 2)
    se = math.sqrt(sp2 * (1 / n1 + 1 / n2))
    assert r.statistic == pytest.approx((mean(A) - mean(B)) / se, rel=1e-14)
    assert r.df == n1 + n2 - 2


def test_welch_and_student_agree_when_variances_equal() -> None:
    """方差与样本量都相等时两者应重合。这是交叉验证两条独立代码路径。"""
    x = [1.0, 2.0, 3.0, 4.0, 5.0]
    y = [3.0, 4.0, 5.0, 6.0, 7.0]
    w, s = welch_t(x, y), student_t(x, y)
    assert w.statistic == pytest.approx(s.statistic, rel=1e-13)
    assert w.df == pytest.approx(s.df, rel=1e-13)
    assert w.p_value == pytest.approx(s.p_value, rel=1e-13)


def test_paired_t_differs_from_independent_t() -> None:
    """把配对数据当独立样本会低估相关、放大标准误。
    这里构造强正相关的配对数据，配对 t 的 |t| 必须显著更大。"""
    before = [10.0, 12.0, 14.0, 16.0, 18.0, 20.0]
    after = [11.0, 13.2, 15.1, 17.3, 19.2, 21.1]
    p = paired_t(before, after)
    w = welch_t(before, after)
    assert abs(p.statistic) > abs(w.statistic) * 5
    assert p.df == len(before) - 1
    assert p.p_value < w.p_value


def test_paired_t_requires_equal_length() -> None:
    with pytest.raises(ValueError):
        paired_t([1.0, 2.0, 3.0], [1.0, 2.0])


@pytest.mark.parametrize("alt", ["greater", "less"])
def test_one_sided_p_values_are_complementary(alt: str) -> None:
    r = one_sample_t(A, mu0=5.0, alternative=alt)
    other = "less" if alt == "greater" else "greater"
    r2 = one_sample_t(A, mu0=5.0, alternative=other)
    assert r.p_value + r2.p_value == pytest.approx(1.0, rel=1e-13)


def test_two_sided_p_is_twice_the_smaller_one_sided() -> None:
    two = one_sample_t(A, mu0=5.0).p_value
    g = one_sample_t(A, mu0=5.0, alternative="greater").p_value
    lt = one_sample_t(A, mu0=5.0, alternative="less").p_value
    assert two == pytest.approx(2 * min(g, lt), rel=1e-13)


def test_zero_variance_raises_not_returns_inf() -> None:
    """常数样本必须抛错。返回 inf 会让上层误以为"极显著"。"""
    with pytest.raises(ValueError):
        one_sample_t([3.0, 3.0, 3.0], mu0=1.0)
    with pytest.raises(ValueError):
        student_t([2.0, 2.0, 2.0], [2.0, 2.0, 2.0])


def test_invalid_alternative_raises() -> None:
    with pytest.raises(ValueError):
        one_sample_t(A, alternative="both-ways")


# ------------------------------------------------------------------ ANOVA


def test_anova_two_groups_equals_student_t_squared() -> None:
    """k=2 时 F = t²，这是精确的代数恒等式，是最强的交叉验证。"""
    a = anova_oneway([A, B])
    s = student_t(A, B)
    assert a.statistic == pytest.approx(s.statistic**2, rel=1e-12)
    assert a.p_value == pytest.approx(s.p_value, rel=1e-11)
    assert a.df == 1.0
    assert a.detail["df_within"] == len(A) + len(B) - 2


def test_anova_ss_decomposition() -> None:
    """SS_total = SS_between + SS_within 必须严格成立。"""
    groups = [[1.0, 2.0, 3.0], [4.0, 5.0, 6.0], [7.0, 9.0, 11.0]]
    r = anova_oneway(groups)
    allx = [x for g in groups for x in g]
    grand = mean(allx)
    ss_total = sum((x - grand) ** 2 for x in allx)
    ss_b = r.detail["ms_between"] * r.detail["df_between"]
    ss_w = r.detail["ms_within"] * r.detail["df_within"]
    assert ss_b + ss_w == pytest.approx(ss_total, rel=1e-12)
    assert r.detail["eta_squared"] == pytest.approx(ss_b / ss_total, rel=1e-12)


def test_anova_omega_squared_below_eta_squared() -> None:
    """omega² 是偏差校正版，必须小于有偏的 eta²。报告时该用 omega²。"""
    r = anova_oneway([[1.0, 2.0, 3.0], [2.0, 3.0, 4.0], [3.0, 4.0, 5.0]])
    assert r.detail["omega_squared"] < r.detail["eta_squared"]
    assert r.effect_name.startswith("omega")


def test_anova_warns_post_hoc_needed() -> None:
    """ANOVA 显著只说明"至少有一组不同"，必须提示做事后比较。"""
    r = anova_oneway([A, B, [7.0, 7.5, 8.0, 7.2, 7.8, 7.1, 7.9, 7.4]])
    assert any("事后" in note for note in r.assumptions)


def test_anova_rejects_degenerate_input() -> None:
    with pytest.raises(ValueError):
        anova_oneway([A])                  # 只有一组
    with pytest.raises(ValueError):
        anova_oneway([A, [1.0]])           # 有组样本量 < 2
    with pytest.raises(ValueError):
        anova_oneway([[2.0, 2.0], [2.0, 2.0]])   # 组内方差为 0


# ---------------------------------------------------------------- 卡方检验


def test_chi2_2x2_matches_hand_calculation() -> None:
    table = [[20.0, 30.0], [30.0, 20.0]]
    r = chi2_independence(table)
    # 各格期望频数都是 25，统计量 = 4 * (5²/25) = 4
    assert r.statistic == pytest.approx(4.0, rel=1e-14)
    assert r.df == 1.0
    assert r.detail["min_expected"] == pytest.approx(25.0, rel=1e-14)
    # Cramér's V = sqrt(chi2 / (n * min(r-1,c-1))) = sqrt(4/100) = 0.2
    assert r.effect_size == pytest.approx(0.2, rel=1e-14)


def test_chi2_independent_table_gives_zero() -> None:
    """完全独立的表统计量必须恰好为 0。"""
    r = chi2_independence([[10.0, 20.0], [30.0, 60.0]])
    assert r.statistic == pytest.approx(0.0, abs=1e-12)
    assert r.p_value == pytest.approx(1.0, abs=1e-12)


def test_chi2_flags_low_expected_frequency() -> None:
    """期望频数 < 5 时必须警告并指向 Fisher 精确检验 ——
    这是卡方近似失效的主要场景，沉默是危险的。"""
    r = chi2_independence([[1.0, 2.0], [3.0, 1.0]])
    assert r.detail["min_expected"] < 5.0
    assert any("Fisher" in note for note in r.assumptions)


def test_chi2_always_warns_about_causation() -> None:
    r = chi2_independence([[20.0, 30.0], [30.0, 20.0]])
    assert any("因果" in note for note in r.assumptions)


def test_chi2_rejects_malformed_table() -> None:
    with pytest.raises(ValueError):
        chi2_independence([[1.0, 2.0]])                    # 只有一行
    with pytest.raises(ValueError):
        chi2_independence([[1.0, 2.0], [3.0]])             # 行长不齐
    with pytest.raises(ValueError):
        chi2_independence([[0.0, 0.0], [0.0, 0.0]])        # 总频数 0


# ---------------------------------------------------------------- 相关分析


def test_pearson_perfect_linear() -> None:
    x = [1.0, 2.0, 3.0, 4.0, 5.0]
    r = pearson(x, [2.0, 4.0, 6.0, 8.0, 10.0])
    assert r.estimate == pytest.approx(1.0, rel=1e-14)
    assert r.effect_size == pytest.approx(1.0, rel=1e-14)
    r_neg = pearson(x, [10.0, 8.0, 6.0, 4.0, 2.0])
    assert r_neg.estimate == pytest.approx(-1.0, rel=1e-14)


def test_pearson_ci_within_bounds_and_contains_r() -> None:
    r = pearson(A, B)
    lo, hi = r.ci
    assert -1.0 <= lo <= r.estimate <= hi <= 1.0


def test_pearson_misses_nonlinear_relation() -> None:
    """y = x² 在对称区间上 Pearson r ≈ 0，但关系是完全确定的。
    这就是"r 小不等于无关系"，assumptions 必须点明。"""
    x = [-3.0, -2.0, -1.0, 0.0, 1.0, 2.0, 3.0]
    r = pearson(x, [v * v for v in x])
    assert abs(r.estimate) < 1e-12
    assert any("非线性" in note for note in r.assumptions)


def test_spearman_invariant_under_monotone_transform() -> None:
    """秩相关只看序，对单调变换不变 —— 这是它相对 Pearson 的核心优势。"""
    x = [1.0, 2.0, 3.0, 4.0, 5.0, 6.0]
    y = [2.0, 1.0, 4.0, 3.0, 6.0, 5.0]
    base = spearman(x, y).estimate
    logged = spearman([math.exp(v) for v in x], y).estimate
    assert base == pytest.approx(logged, rel=1e-13)


def test_spearman_detects_monotone_nonlinear() -> None:
    """指数关系：Spearman 给 1.0，Pearson 明显小于 1。"""
    x = [1.0, 2.0, 3.0, 4.0, 5.0, 6.0]
    y = [math.exp(v) for v in x]
    assert spearman(x, y).estimate == pytest.approx(1.0, rel=1e-14)
    assert pearson(x, y).estimate < 0.95


def test_correlation_rejects_constant_column() -> None:
    with pytest.raises(ValueError):
        pearson([1.0, 1.0, 1.0, 1.0], [1.0, 2.0, 3.0, 4.0])
    with pytest.raises(ValueError):
        pearson([1.0, 2.0], [1.0, 2.0])       # n < 3


# ------------------------------------------------- 契约：不许只返回 p 值

_ALL_RESULTS = [
    ("welch_t", lambda: welch_t(A, B)),
    ("student_t", lambda: student_t(A, B)),
    ("paired_t", lambda: paired_t(A, B)),
    ("one_sample_t", lambda: one_sample_t(A, mu0=5.0)),
    ("anova_oneway", lambda: anova_oneway([A, B])),
    ("chi2_independence", lambda: chi2_independence([[20.0, 30.0], [30.0, 20.0]])),
    ("pearson", lambda: pearson(A, B)),
    ("spearman", lambda: spearman(A, B)),
]


@pytest.mark.parametrize("name,factory", _ALL_RESULTS, ids=[n for n, _ in _ALL_RESULTS])
def test_every_test_reports_effect_size(name: str, factory) -> None:
    """效应量是硬要求。guard.py 的 statistical_integrity 规则要求答案里
    报告效应量，计算层不给的话上层无从遵守。"""
    r = factory()
    assert r.effect_size is not None, f"{name} 没给效应量"
    assert r.effect_name, f"{name} 的效应量没有名字，口径不明"


@pytest.mark.parametrize("name,factory", _ALL_RESULTS, ids=[n for n, _ in _ALL_RESULTS])
def test_every_test_declares_assumptions(name: str, factory) -> None:
    """显式列出未被自动验证的前提，避免把"算出来了"误当成"用对了"。"""
    r = factory()
    assert r.assumptions, f"{name} 没声明任何前提假设"


@pytest.mark.parametrize("name,factory", _ALL_RESULTS, ids=[n for n, _ in _ALL_RESULTS])
def test_p_value_in_valid_range(name: str, factory) -> None:
    r = factory()
    assert 0.0 <= r.p_value <= 1.0, f"{name} 的 p 值越界: {r.p_value}"


@pytest.mark.parametrize("name,factory", _ALL_RESULTS, ids=[n for n, _ in _ALL_RESULTS])
def test_result_is_json_serializable(name: str, factory) -> None:
    """as_dict 要能直接进 artifact spec 与 LLM 工具返回值。"""
    import json

    payload = factory().as_dict()
    json.dumps(payload, ensure_ascii=False)
    assert payload["name"]
    assert "p_value" in payload


def test_mean_difference_tests_report_ci() -> None:
    """均值差类检验必须给区间。ANOVA 的 F 检验不给参数区间是正确的 ——
    它没有单一参数可估，要靠事后比较，所以不纳入这条断言。"""
    for factory in (
        lambda: welch_t(A, B),
        lambda: student_t(A, B),
        lambda: paired_t(A, B),
        lambda: one_sample_t(A, mu0=5.0),
        lambda: pearson(A, B),
    ):
        r = factory()
        assert r.ci is not None, f"{r.name} 没给置信区间"
        assert r.ci[0] < r.ci[1]
        assert r.ci_level == 0.95


def test_ci_level_is_honored() -> None:
    """99% 区间必须比 95% 宽。"""
    narrow = one_sample_t(A, mu0=5.0, ci_level=0.95).ci
    wide = one_sample_t(A, mu0=5.0, ci_level=0.99).ci
    assert wide[0] < narrow[0] and wide[1] > narrow[1]


def test_ci_excludes_zero_iff_significant() -> None:
    """95% CI 是否含 0 必须与 p<0.05 一致。这是两条独立计算路径的
    互验：CI 走 t_ppf，p 值走 t_cdf。"""
    for xs, ys in ((A, B), (A, A[::-1]), ([1.0, 2.0, 3.0], [1.1, 2.2, 2.9])):
        r = welch_t(xs, ys)
        contains_zero = r.ci[0] <= 0.0 <= r.ci[1]
        assert contains_zero == (r.p_value >= 0.05), f"CI 与 p 值不一致: {r.as_dict()}"
