"""教学常用分布的 pdf / cdf / ppf。

设计约束：
- 纯 Python、零第三方依赖（不引 scipy，避免 Windows 上的编译工具链问题）
- 与 app/static/statlib.js 走同一套算法，跨语言结果可 parity 断言
- 精度目标：norm_cdf 接近机器 epsilon；t/chi2/F 的 cdf |ε| < 1e-12

命名沿用统计学惯例：pdf 密度、cdf 分布函数、sf 生存函数（1-cdf）、ppf 分位数。
sf 单列是因为右尾概率直接算比 1-cdf 精度高（避免大 cdf 相减的灾难性抵消）。
"""

from __future__ import annotations

from math import erfc, exp, expm1, inf, lgamma, log, log1p, pi, sqrt

from app.stats.special import (
    betainc,
    gammainc,
    gammaincc,
    invert_cdf,
    invert_sf,
    log_beta,
)

_SQRT2 = sqrt(2.0)
_SQRT2PI = sqrt(2.0 * pi)


# ---------------------------------------------------------------- 正态分布


def norm_pdf(x: float, mu: float = 0.0, sigma: float = 1.0) -> float:
    if sigma <= 0.0:
        raise ValueError("sigma 必须大于 0")
    z = (x - mu) / sigma
    return exp(-0.5 * z * z) / (sigma * _SQRT2PI)


def norm_cdf(x: float, mu: float = 0.0, sigma: float = 1.0) -> float:
    if sigma <= 0.0:
        raise ValueError("sigma 必须大于 0")
    return 0.5 * erfc(-(x - mu) / (sigma * _SQRT2))


def norm_sf(x: float, mu: float = 0.0, sigma: float = 1.0) -> float:
    """右尾 P(X > x)。用 erfc 直接算，远尾不会退化成 0。"""
    if sigma <= 0.0:
        raise ValueError("sigma 必须大于 0")
    return 0.5 * erfc((x - mu) / (sigma * _SQRT2))


# Acklam 逆正态有理逼近系数。中心区与两尾各一组。
_A = (-3.969683028665376e+01, 2.209460984245205e+02, -2.759285104469687e+02,
      1.383577518672690e+02, -3.066479806614716e+01, 2.506628277459239e+00)
_B = (-5.447609879822406e+01, 1.615858368580409e+02, -1.556989798598866e+02,
      6.680131188771972e+01, -1.328068155288572e+01)
_C = (-7.784894002430293e-03, -3.223964580411365e-01, -2.400758277161838e+00,
      -2.549732539343734e+00, 4.374664141464968e+00, 2.938163982698783e+00)
_D = (7.784695709041462e-03, 3.224671290700398e-01, 2.445134137142996e+00,
      3.754408661907416e+00)
_P_LOW = 0.02425
_P_HIGH = 1.0 - _P_LOW


def norm_ppf(p: float, mu: float = 0.0, sigma: float = 1.0) -> float:
    """标准正态分位数。Acklam 逼近（|ε|<1.15e-9）+ 一步 Halley 精化到机器精度。

    Halley 比 Newton 多一阶，一次迭代就把 1e-9 拉到 1e-16，不需要循环。
    """
    if sigma <= 0.0:
        raise ValueError("sigma 必须大于 0")
    if p <= 0.0:
        return -inf
    if p >= 1.0:
        return inf

    if p < _P_LOW:
        q = sqrt(-2.0 * log(p))
        x = (((((_C[0] * q + _C[1]) * q + _C[2]) * q + _C[3]) * q + _C[4]) * q + _C[5]) / \
            ((((_D[0] * q + _D[1]) * q + _D[2]) * q + _D[3]) * q + 1.0)
    elif p <= _P_HIGH:
        q = p - 0.5
        r = q * q
        x = (((((_A[0] * r + _A[1]) * r + _A[2]) * r + _A[3]) * r + _A[4]) * r + _A[5]) * q / \
            (((((_B[0] * r + _B[1]) * r + _B[2]) * r + _B[3]) * r + _B[4]) * r + 1.0)
    else:
        q = sqrt(-2.0 * log1p(-p))
        x = -(((((_C[0] * q + _C[1]) * q + _C[2]) * q + _C[3]) * q + _C[4]) * q + _C[5]) / \
            ((((_D[0] * q + _D[1]) * q + _D[2]) * q + _D[3]) * q + 1.0)

    # Halley 精化：e 是当前误差，u 归一化后按二阶公式修正
    e = 0.5 * erfc(-x / _SQRT2) - p
    u = e * _SQRT2PI * exp(0.5 * x * x)
    x = x - u / (1.0 + 0.5 * x * u)
    return mu + sigma * x




# ------------------------------------------------------------- Student t 分布


def t_pdf(x: float, df: float) -> float:
    if df <= 0.0:
        raise ValueError("df 必须大于 0")
    half = 0.5 * (df + 1.0)
    log_c = lgamma(half) - lgamma(0.5 * df) - 0.5 * log(df * pi)
    return exp(log_c - half * log(1.0 + x * x / df))


def t_cdf(x: float, df: float) -> float:
    """P(T <= x)。

    有两个等价的不完全 beta 形式，**各有失效区**，按 |x| 分支：

    - 中心区（|x| < 1）：P(|T|<=x) = I_{x²/(df+x²)}(1/2, df/2)，
      cdf = 0.5 ± half。自变量随 x² 平滑趋 0，x=1e-10 也保精度。
    - 尾部（|x| >= 1）：小尾 = 0.5 * I_{df/(df+x²)}(df/2, 1/2)。
      直接算出小的那一侧，不做 0.5 减接近 0.5 的数。

    分支点必须取 |x|=1，**不能取 x²=df**。判据要看结果落在哪，不是看自变量：
    df=100, x=-8.03 时 x²=64.4 < df 会误入中心区，而那里
    I_{0.39}(0.5, 50) ≈ 1 - 2e-12，算 0.5-half 会把 2e-12 的有效位全丢掉
    （实测相对误差 2.2e-5）。而 |x|<1 时任何 df 下 cdf 都落在 (0.16, 0.84)，
    两式都远离抵消区；|x|>=1 时尾部式的自变量单调趋 0，同样安全。
    """
    if df <= 0.0:
        raise ValueError("df 必须大于 0")
    if x == 0.0:
        return 0.5
    if abs(x) < 1.0:
        half = 0.5 * betainc(0.5, 0.5 * df, x * x / (df + x * x))
        return 0.5 + half if x > 0.0 else 0.5 - half
    tail = 0.5 * betainc(0.5 * df, 0.5, df / (df + x * x))
    return 1.0 - tail if x > 0.0 else tail


def t_sf(x: float, df: float) -> float:
    return t_cdf(-x, df)


def t_ppf(p: float, df: float) -> float:
    """t 分位数。对称，所以只在 p<0.5 一侧求解再镜像 —— 避免大 p 时
    在 cdf 接近 1 的平坦区二分，那里相对精度会退化。"""
    if p <= 0.0:
        return -inf
    if p >= 1.0:
        return inf
    if p == 0.5:
        return 0.0
    if p > 0.5:
        return -t_ppf(1.0 - p, df)
    return invert_cdf(lambda v: t_cdf(v, df), p, -1.0, 0.0, grow=True)


# --------------------------------------------------------------- 卡方分布


def chi2_pdf(x: float, df: float) -> float:
    if df <= 0.0:
        raise ValueError("df 必须大于 0")
    if x < 0.0:
        return 0.0
    if x == 0.0:
        return 0.0 if df > 2.0 else inf if df < 2.0 else 0.5
    k = 0.5 * df
    return exp((k - 1.0) * log(x) - 0.5 * x - k * log(2.0) - lgamma(k))


def chi2_cdf(x: float, df: float) -> float:
    if df <= 0.0:
        raise ValueError("df 必须大于 0")
    if x <= 0.0:
        return 0.0
    return gammainc(0.5 * df, 0.5 * x)


def chi2_sf(x: float, df: float) -> float:
    if x <= 0.0:
        return 1.0
    return gammaincc(0.5 * df, 0.5 * x)


def chi2_ppf(p: float, df: float) -> float:
    """p>0.5 时改解 sf(x)=1-p，避开 cdf 在右侧的平坦区。"""
    if p <= 0.0:
        return 0.0
    if p >= 1.0:
        return inf
    if p > 0.5:
        return invert_sf(lambda v: chi2_sf(v, df), 1.0 - p, 0.0, max(1.0, df))
    return invert_cdf(lambda v: chi2_cdf(v, df), p, 0.0, max(1.0, df))


# ------------------------------------------------------------------ F 分布


def f_pdf(x: float, dfn: float, dfd: float) -> float:
    if dfn <= 0.0 or dfd <= 0.0:
        raise ValueError("dfn 与 dfd 必须大于 0")
    if x < 0.0:
        return 0.0
    if x == 0.0:
        return 0.0 if dfn > 2.0 else inf if dfn < 2.0 else 1.0
    a, b = 0.5 * dfn, 0.5 * dfd
    log_p = (
        a * log(dfn) + b * log(dfd)
        + (a - 1.0) * log(x)
        - (a + b) * log(dfd + dfn * x)
        - log_beta(a, b)
    )
    return exp(log_p)


def f_cdf(x: float, dfn: float, dfd: float) -> float:
    if dfn <= 0.0 or dfd <= 0.0:
        raise ValueError("dfn 与 dfd 必须大于 0")
    if x <= 0.0:
        return 0.0
    return betainc(0.5 * dfn, 0.5 * dfd, dfn * x / (dfn * x + dfd))


def f_sf(x: float, dfn: float, dfd: float) -> float:
    if x <= 0.0:
        return 1.0
    return betainc(0.5 * dfd, 0.5 * dfn, dfd / (dfn * x + dfd))


def f_ppf(p: float, dfn: float, dfd: float) -> float:
    """p>0.5 时解 sf(x)=1-p。也可用倒数性质（1/X ~ F(dfd,dfn)），
    但直接解小尾更少一次除法误差。"""
    if p <= 0.0:
        return 0.0
    if p >= 1.0:
        return inf
    if p > 0.5:
        return invert_sf(lambda v: f_sf(v, dfn, dfd), 1.0 - p, 0.0, 2.0)
    return invert_cdf(lambda v: f_cdf(v, dfn, dfd), p, 0.0, 2.0)


# ---------------------------------------------------------------- Beta 分布


def beta_pdf(x: float, a: float, b: float) -> float:
    if a <= 0.0 or b <= 0.0:
        raise ValueError("a 与 b 必须大于 0")
    if x < 0.0 or x > 1.0:
        return 0.0
    if x in (0.0, 1.0):
        edge = (x == 0.0 and a < 1.0) or (x == 1.0 and b < 1.0)
        return inf if edge else (1.0 if (a == 1.0 and b == 1.0) else 0.0)
    return exp((a - 1.0) * log(x) + (b - 1.0) * log(1.0 - x) - log_beta(a, b))


def beta_cdf(x: float, a: float, b: float) -> float:
    return betainc(a, b, x)


def beta_sf(x: float, a: float, b: float) -> float:
    """右尾。用对称式 1-I_x(a,b) = I_{1-x}(b,a)，不做减法。"""
    return betainc(b, a, 1.0 - x)


def beta_ppf(p: float, a: float, b: float) -> float:
    """p>0.5 时解 sf(x)=1-p，避开 cdf 右侧平坦区。"""
    if p <= 0.0:
        return 0.0
    if p >= 1.0:
        return 1.0
    if p > 0.5:
        return invert_sf(lambda v: beta_sf(v, a, b), 1.0 - p, 0.0, 1.0, grow=False)
    return invert_cdf(lambda v: beta_cdf(v, a, b), p, 0.0, 1.0, grow=False)


# ---------------------------------------------------------------- 指数分布


def expon_pdf(x: float, scale: float = 1.0) -> float:
    if scale <= 0.0:
        raise ValueError("scale 必须大于 0")
    if x < 0.0:
        return 0.0
    return exp(-x / scale) / scale


def expon_cdf(x: float, scale: float = 1.0) -> float:
    if scale <= 0.0:
        raise ValueError("scale 必须大于 0")
    if x <= 0.0:
        return 0.0
    # 用 expm1 而非 1-exp：x/scale 很小时后者会灾难性抵消
    return -expm1(-x / scale)


def expon_ppf(p: float, scale: float = 1.0) -> float:
    if p <= 0.0:
        return 0.0
    if p >= 1.0:
        return inf
    # log1p(-p) 而非 log(1-p)：p 极小时后者丢掉全部有效位
    return -scale * log1p(-p)


# ------------------------------------------------------- 二项分布（离散）


def binom_pmf(k: int, n: int, p: float) -> float:
    if n < 0 or not 0.0 <= p <= 1.0:
        raise ValueError("需要 n >= 0 且 0 <= p <= 1")
    if k < 0 or k > n:
        return 0.0
    if p == 0.0:
        return 1.0 if k == 0 else 0.0
    if p == 1.0:
        return 1.0 if k == n else 0.0
    log_c = lgamma(n + 1.0) - lgamma(k + 1.0) - lgamma(n - k + 1.0)
    return exp(log_c + k * log(p) + (n - k) * log(1.0 - p))


def binom_cdf(k: int, n: int, p: float) -> float:
    """P(X <= k) = I_{1-p}(n-k, k+1)。用不完全 beta 避免逐项求和的累积误差。"""
    if k < 0:
        return 0.0
    if k >= n:
        return 1.0
    return betainc(n - k, k + 1.0, 1.0 - p)


# ------------------------------------------------------- 泊松分布（离散）


def poisson_pmf(k: int, lam: float) -> float:
    if lam < 0.0:
        raise ValueError("lam 必须 >= 0")
    if k < 0:
        return 0.0
    return exp(k * log(lam) - lam - lgamma(k + 1.0)) if lam > 0.0 else float(k == 0)


def poisson_cdf(k: int, lam: float) -> float:
    """P(X <= k) = Q(k+1, lam)，上不完全 gamma。"""
    if k < 0:
        return 0.0
    if lam == 0.0:
        return 1.0
    return gammaincc(k + 1.0, lam)
