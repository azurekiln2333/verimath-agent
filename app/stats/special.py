"""特殊函数：不完全 beta / gamma 及其反函数。

Python 侧直接用 stdlib 的 math.erf / math.erfc / math.lgamma（libm 实现，精度
接近机器 epsilon），不重复造。需要自己写的只有 stdlib 没有的不完全 beta 与
不完全 gamma —— 它们是 t / chi2 / F / beta 分布 CDF 的底座。

算法：修正 Lentz 连分数（Numerical Recipes 的 betacf / gcf）。反函数用带包围
的二分，单调收敛，且与 statlib.js 走同一套算法，便于跨语言 parity 断言。
"""

from __future__ import annotations

from math import exp, lgamma, log, log1p

_EPS = 3.0e-16
_FPMIN = 1.0e-300
_MAXIT = 300


def log_beta(a: float, b: float) -> float:
    """log B(a, b)。取对数避免 gamma 溢出。"""
    return lgamma(a) + lgamma(b) - lgamma(a + b)


def _betacf(a: float, b: float, x: float) -> float:
    """I_x(a,b) 的连分数部分。修正 Lentz：把 0 值夹到 FPMIN 防除零。"""
    qab, qap, qam = a + b, a + 1.0, a - 1.0
    c = 1.0
    d = 1.0 - qab * x / qap
    if abs(d) < _FPMIN:
        d = _FPMIN
    d = 1.0 / d
    h = d
    for m in range(1, _MAXIT + 1):
        m2 = 2 * m
        aa = m * (b - m) * x / ((qam + m2) * (a + m2))
        d = 1.0 + aa * d
        if abs(d) < _FPMIN:
            d = _FPMIN
        c = 1.0 + aa / c
        if abs(c) < _FPMIN:
            c = _FPMIN
        d = 1.0 / d
        h *= d * c
        aa = -(a + m) * (qab + m) * x / ((a + m2) * (qap + m2))
        d = 1.0 + aa * d
        if abs(d) < _FPMIN:
            d = _FPMIN
        c = 1.0 + aa / c
        if abs(c) < _FPMIN:
            c = _FPMIN
        d = 1.0 / d
        delta = d * c
        h *= delta
        if abs(delta - 1.0) < _EPS:
            break
    return h


def betainc(a: float, b: float, x: float) -> float:
    """正则化不完全 beta 函数 I_x(a, b)，取值 [0, 1]。

    x > (a+1)/(a+b+2) 时用对称式 I_x(a,b) = 1 - I_{1-x}(b,a)，
    让连分数始终在收敛快的一侧求值。
    """
    if x <= 0.0:
        return 0.0
    if x >= 1.0:
        return 1.0
    if a <= 0.0 or b <= 0.0:
        raise ValueError("betainc 需要 a > 0 且 b > 0")
    # log 形式的前因子，防大参数下 x**a 下溢
    front = exp(a * log(x) + b * log1p(-x) - log_beta(a, b))
    if x < (a + 1.0) / (a + b + 2.0):
        return front * _betacf(a, b, x) / a
    return 1.0 - exp(
        b * log1p(-x) + a * log(x) - log_beta(b, a)
    ) * _betacf(b, a, 1.0 - x) / b


def _gser(a: float, x: float) -> float:
    """P(a,x) 的幂级数展开，x < a+1 时收敛快。"""
    ap = a
    total = 1.0 / a
    delta = total
    for _ in range(_MAXIT):
        ap += 1.0
        delta *= x / ap
        total += delta
        if abs(delta) < abs(total) * _EPS:
            break
    return total * exp(-x + a * log(x) - lgamma(a))


def _gcf(a: float, x: float) -> float:
    """Q(a,x) 的连分数，x >= a+1 时收敛快。同样用修正 Lentz。"""
    b = x + 1.0 - a
    c = 1.0 / _FPMIN
    d = 1.0 / b
    h = d
    for i in range(1, _MAXIT + 1):
        an = -i * (i - a)
        b += 2.0
        d = an * d + b
        if abs(d) < _FPMIN:
            d = _FPMIN
        c = b + an / c
        if abs(c) < _FPMIN:
            c = _FPMIN
        d = 1.0 / d
        delta = d * c
        h *= delta
        if abs(delta - 1.0) < _EPS:
            break
    return exp(-x + a * log(x) - lgamma(a)) * h


def gammainc(a: float, x: float) -> float:
    """正则化下不完全 gamma P(a, x) = γ(a,x)/Γ(a)，取值 [0, 1]。"""
    if x < 0.0 or a <= 0.0:
        raise ValueError("gammainc 需要 a > 0 且 x >= 0")
    if x == 0.0:
        return 0.0
    if x < a + 1.0:
        return _gser(a, x)
    return 1.0 - _gcf(a, x)


def gammaincc(a: float, x: float) -> float:
    """正则化上不完全 gamma Q(a, x) = 1 - P(a, x)。"""
    return 1.0 - gammainc(a, x)


def invert_cdf(
    cdf,
    p: float,
    low: float,
    high: float,
    grow: bool = True,
) -> float:
    """用二分求 CDF 的反函数。通用分位数底座。

    二分而非 Newton：CDF 单调，二分无条件收敛，不会像 Newton 那样在尾部
    因导数趋零而发散。grow=True 时先把包围区间往外扩，用于 chi2 / F
    这类右侧无界的分布。

    收敛判据只用"区间宽度相对 mid"这一项，**不能加绝对容差**。极端分位数
    （p=1e-12）的真值本身就是 1e-8 量级的小数，任何绝对阈值都会在到达真值
    前就判定收敛，造成 4 个数量级的相对误差。这里靠浮点相邻性
    (mid == low or mid == high) 自然终止，保证跑到双精度极限。
    """
    if p <= 0.0:
        return low
    if p >= 1.0:
        return high
    if grow:
        for _ in range(200):
            if cdf(high) >= p:
                break
            high = high * 2.0 if high > 0 else 1.0
        for _ in range(200):
            if cdf(low) <= p:
                break
            low = low * 2.0 if low < 0 else -1.0
    for _ in range(200):
        mid = 0.5 * (low + high)
        if mid <= low or mid >= high:
            break                      # 浮点已无中间值，到极限
        if cdf(mid) < p:
            low = mid
        else:
            high = mid
    return 0.5 * (low + high)


def invert_sf(sf, q: float, low: float, high: float, grow: bool = True) -> float:
    """解 sf(x) = q，sf 单调递减。

    为什么需要它：p 接近 1 时 cdf 已经压到 1.0 附近的平坦区，在那里二分
    只能分辨到 1-cdf 的绝对精度，相对精度全丢（实测 f/beta 在 p=1-1e-8
    处相对误差 5e-10）。改成在小尾一侧解 sf(x)=1-p，自变量的相对精度
    就保住了。上层 ppf 对 p>0.5 一律走这条路。
    """
    if q <= 0.0:
        return high
    if q >= 1.0:
        return low
    if grow:
        for _ in range(200):
            if sf(high) <= q:
                break
            high = high * 2.0 if high > 0 else 1.0
        for _ in range(200):
            if sf(low) >= q:
                break
            low = low * 2.0 if low < 0 else -1.0
    for _ in range(200):
        mid = 0.5 * (low + high)
        if mid <= low or mid >= high:
            break
        if sf(mid) > q:
            low = mid
        else:
            high = mid
    return 0.5 * (low + high)
