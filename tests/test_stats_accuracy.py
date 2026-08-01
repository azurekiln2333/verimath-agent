"""统计计算层的精度断言。

**基准来源原则**：全部用可独立验证的闭式解或自洽恒等式，不硬编码"记忆里的
scipy 输出"。开发这一层时凭记忆写的参考值有一半是错的（t_cdf、chi2_cdf、
f_cdf 都被误判为有 bug，实际实现是对的），闭式解才是可靠的真值。

四类基准：
1. 闭式特例    —— Cauchy 的 atan、df=2 的 t、df=1/2 的 chi2、I_x(1,1)=x 等
2. 自洽恒等式  —— cdf+sf=1、I_x(a,b)+I_{1-x}(b,a)=1、F(1,df)=t²
3. 往返一致    —— cdf(ppf(p))=p，在小尾一侧断言相对精度
4. 单调与边界  —— cdf 单调不减、pdf 非负、极限行为
"""

from __future__ import annotations

import math

import pytest

from app.stats.distributions import (
    beta_cdf,
    beta_ppf,
    beta_sf,
    binom_cdf,
    binom_pmf,
    chi2_cdf,
    chi2_ppf,
    chi2_sf,
    expon_cdf,
    expon_ppf,
    f_cdf,
    f_ppf,
    f_sf,
    norm_cdf,
    norm_pdf,
    norm_ppf,
    norm_sf,
    poisson_cdf,
    poisson_pmf,
    t_cdf,
    t_ppf,
    t_sf,
)
from app.stats.special import betainc, gammainc, gammaincc

_TAIL_PS = (1e-12, 1e-10, 1e-8, 1e-5, 0.001, 0.01, 0.1, 0.25)
_ALL_PS = _TAIL_PS + (0.5, 0.75, 0.9, 0.99, 0.999, 1 - 1e-5, 1 - 1e-8)


# ---------------------------------------------------- 1. 闭式特例：不完全 beta


@pytest.mark.parametrize("x", [0.001, 0.1, 0.3, 0.5, 0.7142857142857143, 0.9, 0.999])
def test_betainc_closed_forms(x: float) -> None:
    """I_x(a,b) 在 a/b 取小整数或 1/2 时有闭式解。"""
    assert betainc(1, 1, x) == pytest.approx(x, rel=1e-14)
    assert betainc(1, 5, x) == pytest.approx(1 - (1 - x) ** 5, rel=1e-14)
    assert betainc(3, 1, x) == pytest.approx(x**3, rel=1e-14)
    # I_x(1/2,1/2) = (2/pi) * arcsin(sqrt(x))，反正弦分布
    assert betainc(0.5, 0.5, x) == pytest.approx(
        2 / math.pi * math.asin(math.sqrt(x)), rel=1e-14
    )


@pytest.mark.parametrize("x", [0.01, 0.25, 0.5, 0.75, 0.99])
@pytest.mark.parametrize("a,b", [(2, 3), (0.5, 0.5), (50, 0.5), (500, 0.5), (5, 20)])
def test_betainc_symmetry_identity(x: float, a: float, b: float) -> None:
    """I_x(a,b) + I_{1-x}(b,a) == 1。连分数两个分支的一致性检查。"""
    assert betainc(a, b, x) + betainc(b, a, 1 - x) == pytest.approx(1.0, abs=1e-14)


@pytest.mark.parametrize("a", [0.5, 1.0, 2.5, 10.0, 100.0])
@pytest.mark.parametrize("x", [0.1, 1.0, 5.0, 50.0])
def test_gammainc_complement(a: float, x: float) -> None:
    assert gammainc(a, x) + gammaincc(a, x) == pytest.approx(1.0, abs=1e-15)


def test_gammainc_integer_closed_form() -> None:
    """整数 a 时 Q(a,x) = exp(-x) * sum_{k<a} x^k/k!。"""
    for a in (1, 2, 3, 5):
        for x in (0.5, 2.0, 7.0):
            expect = math.exp(-x) * sum(x**k / math.factorial(k) for k in range(a))
            assert gammaincc(a, x) == pytest.approx(expect, rel=1e-13)


# ------------------------------------------------------ 2. 闭式特例：各分布


@pytest.mark.parametrize("x", [-5.0, -1.0, 0.0, 0.5, 1.96, 4.0])
def test_norm_cdf_matches_erfc(x: float) -> None:
    assert norm_cdf(x) == pytest.approx(0.5 * math.erfc(-x / math.sqrt(2)), rel=1e-15)


def test_norm_cdf_known_symmetry() -> None:
    assert norm_cdf(0.0) == 0.5
    for x in (0.5, 1.0, 1.96, 3.0, 6.0):
        assert norm_cdf(-x) + norm_cdf(x) == pytest.approx(1.0, abs=1e-15)
        # sf 必须与镜像 cdf 完全一致，且远尾不塌成 0
        assert norm_sf(x) == pytest.approx(norm_cdf(-x), rel=1e-14)
    assert norm_sf(10.0) > 0.0


def test_norm_pdf_closed_form() -> None:
    assert norm_pdf(0.0) == pytest.approx(1 / math.sqrt(2 * math.pi), rel=1e-15)
    # 缩放性质：pdf(x; mu, s) = pdf((x-mu)/s) / s
    assert norm_pdf(3.0, 1.0, 2.0) == pytest.approx(norm_pdf(1.0) / 2.0, rel=1e-15)


@pytest.mark.parametrize("x", [-1e-10, -1e-6, -0.5, -3.0, -100.0, -1e6])
def test_t_cdf_df1_is_cauchy(x: float) -> None:
    """df=1 就是 Cauchy：cdf = 1/2 + arctan(x)/pi。

    注意只在 |x| 不大时用这个闭式做真值 —— |x| 很大时闭式自身
    (0.5 + 接近 -0.5 的数) 有灾难性抵消，反而不如实现精确。
    """
    expect = 0.5 + math.atan(x) / math.pi
    rel = 1e-13 if abs(x) <= 100 else 1e-5
    assert t_cdf(x, 1) == pytest.approx(expect, rel=rel)


@pytest.mark.parametrize("x", [-1e-8, -0.5, -3.0, -50.0])
def test_t_cdf_df2_closed_form(x: float) -> None:
    """df=2 有闭式：cdf = 1/2 + x / (2*sqrt(2+x^2))。"""
    expect = 0.5 + x / (2 * math.sqrt(2 + x * x))
    assert t_cdf(x, 2) == pytest.approx(expect, rel=1e-9)


@pytest.mark.parametrize("df", [1, 2, 3, 5, 10, 30, 100, 1000])
def test_t_cdf_symmetry_and_sf(df: float) -> None:
    for x in (0.1, 0.5, 1.0, 2.0, 8.03, 40.0):
        assert t_cdf(-x, df) + t_cdf(x, df) == pytest.approx(1.0, abs=1e-15)
        assert t_sf(x, df) == pytest.approx(t_cdf(-x, df), rel=1e-15)


@pytest.mark.parametrize("df", [1, 3, 100, 1000])
def test_t_cdf_continuous_at_branch_point(df: float) -> None:
    """|x|=1 是两种不完全 beta 形式的分支点，必须连续。"""
    eps = 1e-13
    lo, hi = t_cdf(-1 - eps, df), t_cdf(-1 + eps, df)
    assert abs(hi - lo) < 1e-12


@pytest.mark.parametrize("x", [0.1, 0.5, 3.84, 7.0, 20.0])
def test_chi2_closed_forms(x: float) -> None:
    """df=2 是指数分布；df=1 是 erf。"""
    assert chi2_cdf(x, 2) == pytest.approx(1 - math.exp(-x / 2), rel=1e-13)
    assert chi2_cdf(x, 1) == pytest.approx(math.erf(math.sqrt(x / 2)), rel=1e-13)


@pytest.mark.parametrize("df", [1, 2, 5, 30, 100])
def test_chi2_cdf_sf_complement(df: float) -> None:
    for x in (0.5, 5.0, 50.0, 200.0):
        assert chi2_cdf(x, df) + chi2_sf(x, df) == pytest.approx(1.0, abs=1e-15)


@pytest.mark.parametrize("x", [0.5, 2.0, 5.0])
def test_f_cdf_dfn2_closed_form(x: float) -> None:
    """dfn=2 时 I_y(1, dfd/2) 有闭式，y = 2x/(2x+dfd)。"""
    dfd = 8
    y = 2 * x / (2 * x + dfd)
    assert f_cdf(x, 2, dfd) == pytest.approx(1 - (1 - y) ** (dfd / 2), rel=1e-13)


@pytest.mark.parametrize("t,df", [(2.0, 10), (1.5, 20), (3.0, 5), (0.5, 3)])
def test_f_equals_t_squared(t: float, df: float) -> None:
    """F(1, df) 分布就是 t(df) 的平方：F_cdf(t², 1, df) = 2*t_cdf(t,df) - 1。"""
    assert f_cdf(t * t, 1, df) == pytest.approx(2 * t_cdf(t, df) - 1, rel=1e-13)


@pytest.mark.parametrize("dfn,dfd", [(3, 10), (1, 1), (5, 5), (20, 2), (1, 1000)])
def test_f_cdf_sf_complement(dfn: float, dfd: float) -> None:
    """容差 1e-13 而非 1e-14：dfn=1,dfd=1000,x=0.1 那一组要算
    betainc(0.5, 500, 1e-4)，b/a 达到 1000 量级，连分数的条件数变差，
    两个分支独立求值会差到 5e-14。已用 F(1,df)=t² 恒等式交叉验证 f_sf 侧
    准到 2.6e-14，所以这是连分数的固有精度上限，不是实现错误。
    13 位有效数字对教学与 p 值场景远超需要。"""
    for x in (0.1, 1.0, 4.0, 100.0):
        assert f_cdf(x, dfn, dfd) + f_sf(x, dfn, dfd) == pytest.approx(1.0, abs=1e-13)


@pytest.mark.parametrize("a,b", [(2, 3), (0.5, 0.5), (5, 1), (50, 50)])
def test_beta_cdf_sf_complement(a: float, b: float) -> None:
    for x in (0.01, 0.5, 0.99):
        assert beta_cdf(x, a, b) + beta_sf(x, a, b) == pytest.approx(1.0, abs=1e-13)


def test_expon_closed_form() -> None:
    for x in (1e-12, 0.5, 3.0):
        assert expon_cdf(x, 2.5) == pytest.approx(1 - math.exp(-x / 2.5), rel=1e-12)
    # 极小 p 必须靠 log1p 保精度，log(1-p) 会丢掉全部有效位
    assert expon_cdf(expon_ppf(1e-12, 2.5), 2.5) == pytest.approx(1e-12, rel=1e-14)


def test_binom_pmf_sums_to_one() -> None:
    for n, p in ((10, 0.5), (25, 0.3), (5, 0.9)):
        assert sum(binom_pmf(k, n, p) for k in range(n + 1)) == pytest.approx(1.0, abs=1e-14)


def test_binom_cdf_matches_pmf_sum() -> None:
    """cdf 走不完全 beta，pmf 逐项求和是独立路径，两者必须一致。"""
    for n, p in ((10, 0.5), (25, 0.3), (40, 0.72)):
        for k in range(0, n + 1, max(1, n // 7)):
            expect = sum(binom_pmf(i, n, p) for i in range(k + 1))
            assert binom_cdf(k, n, p) == pytest.approx(expect, rel=1e-12)


def test_poisson_cdf_matches_pmf_sum() -> None:
    for lam in (0.5, 2.5, 10.0):
        for k in (0, 1, 3, 8, 20):
            expect = sum(poisson_pmf(i, lam) for i in range(k + 1))
            assert poisson_cdf(k, lam) == pytest.approx(expect, rel=1e-12)


# ------------------------------------------------- 3. 往返精度（回归护栏）
#
# 这组测试在开发时抓出了 4 个真实 bug，每条都留了注释说明它防的是什么：
#   - invert_cdf 用绝对容差 → 1e-12 分位数相对误差 1.7e4
#   - t_cdf 单一 beta 形式 → x≈0 时塌成恰好 0.5
#   - t_cdf 分支判据错用 x²<df → df=100 远尾相对误差 2.2e-5
#   - expon_ppf/norm_ppf 用 log(1-p) → 极端 p 丢有效位


@pytest.mark.parametrize("p", _ALL_PS)
def test_norm_ppf_roundtrip(p: float) -> None:
    assert norm_cdf(norm_ppf(p)) == pytest.approx(p, rel=1e-13)


def test_norm_ppf_known_anchors() -> None:
    """双侧 95%/99% 临界值。这两个数是统计学最常用的锚点，
    用 erfc 反推自洽，不靠记忆。"""
    for level in (0.90, 0.95, 0.99):
        z = norm_ppf(1 - (1 - level) / 2)
        assert norm_cdf(z) - norm_cdf(-z) == pytest.approx(level, rel=1e-13)
    assert norm_ppf(0.5) == pytest.approx(0.0, abs=1e-15)


@pytest.mark.parametrize("df", [1, 2, 3, 5, 10, 30, 100, 1000])
@pytest.mark.parametrize("p", _TAIL_PS)
def test_t_ppf_roundtrip_small_tail(df: float, p: float) -> None:
    """在小尾一侧断言相对精度 —— 这是 p 值场景真正需要准的区域。"""
    assert t_cdf(t_ppf(p, df), df) == pytest.approx(p, rel=1e-11)


@pytest.mark.parametrize("df", [1, 2, 5, 30, 100])
@pytest.mark.parametrize("p", _TAIL_PS)
def test_chi2_ppf_roundtrip(df: float, p: float) -> None:
    assert chi2_cdf(chi2_ppf(p, df), df) == pytest.approx(p, rel=1e-11)


@pytest.mark.parametrize("dfn,dfd", [(3, 10), (1, 1), (5, 5), (20, 2)])
@pytest.mark.parametrize("p", _TAIL_PS)
def test_f_ppf_roundtrip(dfn: float, dfd: float, p: float) -> None:
    assert f_cdf(f_ppf(p, dfn, dfd), dfn, dfd) == pytest.approx(p, rel=1e-10)


@pytest.mark.parametrize("a,b", [(2, 3), (5, 1), (50, 50)])
@pytest.mark.parametrize("p", _TAIL_PS)
def test_beta_ppf_roundtrip(a: float, b: float, p: float) -> None:
    assert beta_cdf(beta_ppf(p, a, b), a, b) == pytest.approx(p, rel=1e-10)


@pytest.mark.parametrize("p", [0.9, 0.99, 0.999, 1 - 1e-5, 1 - 1e-8])
def test_upper_tail_ppf_solves_small_side(p: float) -> None:
    """p>0.5 时 ppf 必须改解 sf(x)=1-p。

    若仍在 cdf 侧二分，cdf 已压到 1.0 附近的平坦区，只能分辨到绝对精度，
    1-p 的相对精度全丢。这条断言就是那个修复的护栏。
    """
    q = 1.0 - p
    for dfn, dfd in ((3, 10), (5, 5)):
        assert f_sf(f_ppf(p, dfn, dfd), dfn, dfd) == pytest.approx(q, rel=1e-9)
    for df in (1, 5, 100):
        assert chi2_sf(chi2_ppf(p, df), df) == pytest.approx(q, rel=1e-9)
        assert t_sf(t_ppf(p, df), df) == pytest.approx(q, rel=1e-9)
    for a, b in ((2, 3), (50, 50)):
        assert beta_sf(beta_ppf(p, a, b), a, b) == pytest.approx(q, rel=1e-7)


# ---------------------------------------------------- 4. 单调性与边界行为


@pytest.mark.parametrize(
    "cdf,args",
    [
        (norm_cdf, ()),
        (t_cdf, (5,)),
        (t_cdf, (1000,)),
        (chi2_cdf, (3,)),
        (f_cdf, (3, 10)),
        (beta_cdf, (2, 3)),
        (expon_cdf, (2.0,)),
    ],
)
def test_cdf_monotone_nondecreasing(cdf, args: tuple) -> None:
    xs = [-8, -2, -0.5, 0, 0.25, 0.5, 0.9, 1.0, 1.5, 3.0, 12.0, 200.0]
    vals = [cdf(x, *args) for x in xs]
    assert all(b >= a - 1e-15 for a, b in zip(vals, vals[1:]))
    assert all(0.0 <= v <= 1.0 for v in vals)


def test_t_approaches_normal_as_df_grows() -> None:
    """df→∞ 时 t 收敛到正态。这是教学上要讲的性质，也是实现的交叉验证。"""
    for x in (0.5, 1.96, 3.0):
        assert t_cdf(x, 10_000) == pytest.approx(norm_cdf(x), abs=1e-4)
        assert abs(t_cdf(x, 100) - norm_cdf(x)) > abs(
            t_cdf(x, 10_000) - norm_cdf(x)
        )


def test_degenerate_params_raise() -> None:
    with pytest.raises(ValueError):
        norm_cdf(0.0, 0.0, 0.0)
    with pytest.raises(ValueError):
        t_cdf(1.0, 0.0)
    with pytest.raises(ValueError):
        chi2_cdf(1.0, -1.0)
    with pytest.raises(ValueError):
        f_cdf(1.0, 0.0, 5.0)
    with pytest.raises(ValueError):
        betainc(0.0, 1.0, 0.5)


def test_ppf_boundary_values() -> None:
    assert norm_ppf(0.0) == -math.inf
    assert norm_ppf(1.0) == math.inf
    assert chi2_ppf(0.0, 3) == 0.0
    assert chi2_ppf(1.0, 3) == math.inf
    assert beta_ppf(0.0, 2, 3) == 0.0
    assert beta_ppf(1.0, 2, 3) == 1.0
    assert t_ppf(0.5, 7) == 0.0
