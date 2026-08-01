"""可复现随机数的断言。

核心契约：**同种子必出同序列**。教学场景要求学生能"再来一次一模一样"，
也能"换个种子看是不是巧合"。任何破坏这一点的改动都必须被这里挡住。

另有分布正确性的统计检验（用大样本核对均值/方差/分位数），
容差按理论标准误定，不是随手写的魔法数。
"""

from __future__ import annotations

import math

import pytest

from app.stats.rng import PCG32

_KNOWN_SEED = 20240607


def test_same_seed_same_sequence() -> None:
    a = PCG32(_KNOWN_SEED)
    b = PCG32(_KNOWN_SEED)
    assert [a.random() for _ in range(200)] == [b.random() for _ in range(200)]


def test_different_seed_different_sequence() -> None:
    a = [PCG32(1).random() for _ in range(20)]
    b = [PCG32(2).random() for _ in range(20)]
    assert a != b


def test_different_stream_different_sequence() -> None:
    """同 seed 不同 stream 必须独立 —— 支撑"同一次模拟里多条独立随机流"。"""
    a = [PCG32(7, stream=1).random() for _ in range(20)]
    b = [PCG32(7, stream=2).random() for _ in range(20)]
    assert a != b


def test_sequence_is_stable_across_runs() -> None:
    """回归护栏：锁死前 8 个输出。

    这些值不是从外部标准抄来的，而是本实现的输出快照。它的作用不是验证
    PCG32 算法正确（那由统计性质测试负责），而是**锁定序列不被无意改动** ——
    若有人改了 _next_uint32 或 random 的取位方式，这条会立刻红。
    statlib.js 必须复现同一串数，parity 测试用的就是它。
    """
    r = PCG32(42, stream=54)
    got = [r.random() for _ in range(8)]
    expect = [
        0.6303102186438938,
        0.7270080560068604,
        0.7486033647998483,
        0.7491247468042271,
        0.8989134056383017,
        0.1986622148470144,
        0.9276185126548473,
        0.17042659305610708,
    ]
    assert got == pytest.approx(expect, rel=1e-15)


def test_uint32_snapshot() -> None:
    """底层输出也锁死，便于定位 parity 失配是在 uint32 层还是 float 层。"""
    r = PCG32(42, stream=54)
    assert [r._next_uint32() for _ in range(4)] == [
        2707161783,
        2068313097,
        3122475824,
        2211639955,
    ]


def test_random_range_and_moments() -> None:
    """均匀分布的一二阶矩。容差按理论标准误的 4 倍定，不是魔法数。"""
    n = 200_000
    r = PCG32(1)
    xs = [r.random() for _ in range(n)]
    assert all(0.0 <= x < 1.0 for x in xs)
    se_mean = math.sqrt((1 / 12) / n)
    assert abs(sum(xs) / n - 0.5) < 4 * se_mean
    var = sum((x - 0.5) ** 2 for x in xs) / n
    assert abs(var - 1 / 12) < 0.001


def test_normal_moments() -> None:
    n = 100_000
    r = PCG32(99)
    xs = [r.normal(3.0, 2.0) for _ in range(n)]
    m = sum(xs) / n
    sd = math.sqrt(sum((x - m) ** 2 for x in xs) / (n - 1))
    assert abs(m - 3.0) < 4 * 2.0 / math.sqrt(n)
    assert abs(sd - 2.0) < 0.05


def test_normal_uses_both_box_muller_outputs() -> None:
    """Box-Muller 一次算两个值，缓存的那个下次必须被用掉。
    若缓存逻辑坏了，序列会变但矩仍然对 —— 所以靠快照锁。"""
    r = PCG32(5)
    first_four = [r.normal() for _ in range(4)]
    r2 = PCG32(5)
    assert [r2.normal() for _ in range(4)] == pytest.approx(first_four, rel=1e-15)
    # 偶数位与奇数位来自同一对，不应相等
    assert first_four[0] != first_four[1]


def test_exponential_and_bernoulli() -> None:
    n = 100_000
    r = PCG32(11)
    xs = [r.exponential(2.5) for _ in range(n)]
    assert all(x >= 0.0 for x in xs)
    assert abs(sum(xs) / n - 2.5) < 4 * 2.5 / math.sqrt(n)
    r2 = PCG32(12)
    ones = sum(r2.bernoulli(0.3) for _ in range(n))
    se = math.sqrt(0.3 * 0.7 / n)
    assert abs(ones / n - 0.3) < 4 * se


def test_binomial_and_poisson_moments() -> None:
    n = 40_000
    r = PCG32(13)
    xs = [r.binomial(20, 0.4) for _ in range(n)]
    assert abs(sum(xs) / n - 8.0) < 4 * math.sqrt(20 * 0.4 * 0.6) / math.sqrt(n)
    r2 = PCG32(14)
    ys = [r2.poisson(4.0) for _ in range(n)]
    assert all(y >= 0 for y in ys)
    assert abs(sum(ys) / n - 4.0) < 4 * 2.0 / math.sqrt(n)


def test_poisson_large_lambda_uses_normal_approx() -> None:
    """lam>30 走正态近似。这是显式的实现选择，均值仍须无偏。"""
    n = 20_000
    r = PCG32(15)
    ys = [r.poisson(50.0) for _ in range(n)]
    assert all(y >= 0 for y in ys)
    assert abs(sum(ys) / n - 50.0) < 4 * math.sqrt(50) / math.sqrt(n)


def test_randint_covers_range_uniformly() -> None:
    r = PCG32(16)
    counts = {k: 0 for k in range(1, 7)}
    n = 60_000
    for _ in range(n):
        counts[r.randint(1, 6)] += 1
    assert set(counts) == set(range(1, 7))
    se = math.sqrt(n * (1 / 6) * (5 / 6))
    for k, c in counts.items():
        assert abs(c - n / 6) < 5 * se, f"面 {k} 出现 {c} 次，偏离过大"


def test_randint_rejects_bad_range() -> None:
    with pytest.raises(ValueError):
        PCG32(1).randint(5, 4)


def test_shuffled_is_permutation_and_reproducible() -> None:
    items = list(range(20))
    a = PCG32(17).shuffled(items)
    b = PCG32(17).shuffled(items)
    assert a == b
    assert sorted(a) == items
    assert a != items                       # 极小概率恰好不变，固定种子下确定
    assert PCG32(18).shuffled(items) != a


def test_sample_from_is_with_replacement() -> None:
    """Bootstrap 要求有放回。抽 n 次出现重复才说明没搞成无放回。"""
    pop = [1, 2, 3, 4, 5]
    got = PCG32(19).sample_from(pop, 50)
    assert len(got) == 50
    assert all(g in pop for g in got)
    assert len(set(got)) < 50


def test_choice_rejects_empty() -> None:
    with pytest.raises(ValueError):
        PCG32(1).choice([])


def test_independent_instances_do_not_share_state() -> None:
    """两个实例必须互不干扰，否则并行模拟会串味。"""
    a, b = PCG32(21), PCG32(21)
    a.random()
    a.random()
    assert b.random() == pytest.approx(PCG32(21).random(), rel=1e-15)
