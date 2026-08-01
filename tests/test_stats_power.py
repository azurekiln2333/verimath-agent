"""功效与样本量的断言。

功效计算用了正态近似（非中心 t 的近似），所以这里断言的是**结构性质**
而非高精度数值：单调性、边界行为、与样本量反解的自洽。这是诚实的做法 ——
对一个声明为近似的实现断言 1e-12 精度是自欺。

近似质量本身用一条独立断言约束：与教科书常用锚点（d=0.5, power=0.8,
alpha=0.05 → 每组约 64）对照，容忍 ±2 的差异。
"""

from __future__ import annotations

import pytest

from app.stats.power import (
    critical_region_two_sample_t,
    power_one_sample_t,
    power_two_sample_t,
    sample_size_two_sample_t,
)


def test_power_increases_with_sample_size() -> None:
    prev = 0.0
    for n in (5, 10, 20, 50, 100, 400):
        p = power_two_sample_t(0.5, n).power
        assert p > prev, f"n={n} 时功效未上升"
        prev = p
    assert prev > 0.99


def test_power_increases_with_effect_size() -> None:
    prev = 0.0
    for d in (0.05, 0.2, 0.5, 0.8, 1.5, 3.0):
        p = power_two_sample_t(d, 30).power
        assert p > prev
        prev = p


def test_power_increases_with_alpha() -> None:
    """放宽 α 换来更高功效 —— 这正是四角关系里最该让学生看见的权衡。"""
    prev = 0.0
    for alpha in (0.001, 0.01, 0.05, 0.1, 0.2):
        p = power_two_sample_t(0.5, 30, alpha=alpha).power
        assert p > prev
        prev = p


def test_one_sided_has_more_power_than_two_sided() -> None:
    """同 α 下单侧检验功效更高（把全部 α 押在一侧）。"""
    two = power_two_sample_t(0.5, 30, alternative="two-sided").power
    one = power_two_sample_t(0.5, 30, alternative="greater").power
    assert one > two


def test_power_in_unit_interval_and_beta_complements() -> None:
    for d in (0.0, 0.1, 0.5, 2.0, 10.0):
        for n in (2, 5, 50, 1000):
            r = power_two_sample_t(d, n)
            assert 0.0 <= r.power <= 1.0
            assert r.beta == pytest.approx(1.0 - r.power, rel=1e-15)


def test_zero_effect_power_equals_alpha() -> None:
    """效应量为 0 时功效必须退化成 α —— 这就是一类错误率本身。
    这条是整个功效实现最强的自洽检查。"""
    for alpha in (0.01, 0.05, 0.1):
        r = power_two_sample_t(0.0, 200, alpha=alpha)
        assert r.power == pytest.approx(alpha, rel=0.02)


def test_power_symmetric_in_effect_sign() -> None:
    """双侧检验对效应方向不敏感。"""
    assert power_two_sample_t(0.6, 40).power == pytest.approx(
        power_two_sample_t(-0.6, 40).power, rel=1e-15
    )


def test_sample_size_matches_textbook_anchor() -> None:
    """d=0.5, power=0.8, alpha=0.05 双侧 → 每组约 64。

    这是统计功效最广为引用的锚点（Cohen 的中等效应量约定）。容忍 ±3：
    实现用的是正态近似而非精确非中心 t，不该假装能精确复现。
    """
    r = sample_size_two_sample_t(0.5, power=0.8, alpha=0.05)
    assert 61 <= r.n_per_group <= 67, f"得到 {r.n_per_group}，偏离教科书锚点"
    assert r.power >= 0.8


def test_sample_size_roundtrips_with_power() -> None:
    """反解出的 n 代回功效函数必须达标，且 n-1 时不达标（即恰好是最小 n）。"""
    for d, target in ((0.2, 0.8), (0.5, 0.9), (0.8, 0.95), (1.2, 0.8)):
        r = sample_size_two_sample_t(d, power=target)
        n = int(r.n_per_group)
        assert power_two_sample_t(d, n).power >= target
        if n > 2:
            assert power_two_sample_t(d, n - 1).power < target


def test_sample_size_decreases_with_effect_size() -> None:
    prev = float("inf")
    for d in (0.1, 0.2, 0.5, 0.8, 1.5):
        n = sample_size_two_sample_t(d).n_per_group
        assert n < prev
        prev = n


def test_sample_size_increases_with_target_power() -> None:
    prev = 0.0
    for target in (0.5, 0.7, 0.8, 0.9, 0.99):
        n = sample_size_two_sample_t(0.4, power=target).n_per_group
        assert n > prev
        prev = n


def test_sample_size_rejects_zero_effect() -> None:
    """效应量为 0 时任何样本量都达不到功效，必须抛错而不是死循环。"""
    with pytest.raises(ValueError):
        sample_size_two_sample_t(0.0)
    with pytest.raises(ValueError):
        sample_size_two_sample_t(0.5, power=1.0)
    with pytest.raises(ValueError):
        sample_size_two_sample_t(0.5, power=0.0)


def test_sample_size_respects_max_n() -> None:
    """极小效应量在有限上限内无解时必须报错，不能无声返回上限。"""
    with pytest.raises(ValueError):
        sample_size_two_sample_t(0.001, power=0.99, max_n=500)


def test_one_sample_power_exceeds_two_sample_at_same_n() -> None:
    """同 n 下单样本的 ncp = d*sqrt(n)，两样本是 d*sqrt(n/2)，
    所以单样本功效更高。配对设计的优势就来自这里。"""
    assert power_one_sample_t(0.5, 30).power > power_two_sample_t(0.5, 30).power


def test_power_rejects_invalid_input() -> None:
    with pytest.raises(ValueError):
        power_two_sample_t(0.5, 1)
    with pytest.raises(ValueError):
        power_two_sample_t(0.5, 30, alpha=0.0)
    with pytest.raises(ValueError):
        power_two_sample_t(0.5, 30, alpha=1.0)
    with pytest.raises(ValueError):
        power_two_sample_t(0.5, 30, alternative="sideways")
    with pytest.raises(ValueError):
        power_one_sample_t(0.5, 1)


def test_power_result_is_serializable_and_declares_approximation() -> None:
    """approximation 字段必须非空：把近似说成精确是教学上不可接受的。"""
    import json

    for r in (power_two_sample_t(0.5, 30), power_one_sample_t(0.5, 30)):
        payload = r.as_dict()
        json.dumps(payload, ensure_ascii=False)
        assert payload["approximation"], "没有声明近似口径"
        assert payload["test"]


def test_critical_region_two_sided_is_symmetric() -> None:
    cr = critical_region_two_sample_t(20, alpha=0.05)
    assert cr["lower"] == pytest.approx(-cr["upper"], rel=1e-15)
    assert cr["df"] == 38.0


def test_critical_region_one_sided_has_single_bound() -> None:
    g = critical_region_two_sample_t(20, alpha=0.05, alternative="greater")
    assert g["upper"] is None and g["lower"] > 0
    lt = critical_region_two_sample_t(20, alpha=0.05, alternative="less")
    assert lt["lower"] is None and lt["upper"] < 0
    # 单侧临界值必须小于双侧（α 不用对半分）
    two = critical_region_two_sample_t(20, alpha=0.05)
    assert g["lower"] < two["upper"]


def test_critical_region_tightens_as_alpha_shrinks() -> None:
    prev = 0.0
    for alpha in (0.2, 0.1, 0.05, 0.01, 0.001):
        upper = critical_region_two_sample_t(30, alpha=alpha)["upper"]
        assert upper > prev
        prev = upper
