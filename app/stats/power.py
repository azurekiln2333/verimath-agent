"""功效与样本量。

这块是 hypothesis-test-visualizer 和 power-sample-size 两个可视化件的计算内核，
也是纠正"p<0.05 就是发现了效应"这个误解的关键 —— 学生需要看到
α、效应量、样本量、功效四者是一个联动的四角关系，动一个另外三个就变。

近似口径说明：两样本 t 检验的功效用中心化正态近似（把非中心 t 近似成
平移的 t），这是教科书标准做法，在 n >= 10 时与精确非中心 t 的差异
通常在 0.01 量级。精确非中心 t 需要额外的特殊函数，教学场景不必要 ——
但这个近似必须**显式声明**，不能让学生以为是精确值。
"""

from __future__ import annotations

from dataclasses import dataclass
from math import ceil, sqrt

from app.stats.distributions import norm_ppf, t_cdf, t_ppf, t_sf


@dataclass(frozen=True)
class PowerResult:
    power: float
    alpha: float
    effect_size: float
    n_per_group: float
    test: str
    alternative: str
    approximation: str
    beta: float

    def as_dict(self) -> dict:
        return {
            "power": self.power,
            "beta": self.beta,
            "alpha": self.alpha,
            "effect_size": self.effect_size,
            "n_per_group": self.n_per_group,
            "test": self.test,
            "alternative": self.alternative,
            "approximation": self.approximation,
        }


def power_two_sample_t(
    effect_size: float,
    n_per_group: float,
    alpha: float = 0.05,
    alternative: str = "two-sided",
) -> PowerResult:
    """两独立样本 t 检验的功效。effect_size 是 Cohen's d。

    非中心参数 ncp = d * sqrt(n/2)。把非中心 t 近似成**平移的 t**：
    power ≈ P(T > t_crit - ncp)，双侧再加另一侧。

    为什么用平移 t 而非平移正态：临界值取自 t 分布，若拿它去查正态，
    d=0 时功效算出来是 0.00965 而不是 α=0.01（t 尾巴比正态厚）。
    换成同一个 t 分布后，d=0 时功效**恰好等于 α** —— 这是功效实现最强的
    自洽检查，也让"功效不可能低于一类错误率"这个教学要点成立。
    """
    if n_per_group < 2:
        raise ValueError("每组样本量必须 >= 2")
    if not 0.0 < alpha < 1.0:
        raise ValueError("alpha 必须在 (0,1)")
    df = 2.0 * n_per_group - 2.0
    ncp = abs(effect_size) * sqrt(n_per_group / 2.0)
    if alternative == "two-sided":
        crit = t_ppf(1.0 - alpha / 2.0, df)
        # 两侧都算：效应为正时右侧主导，左侧那点贡献在小效应时不可忽略
        power = t_sf(crit - ncp, df) + t_cdf(-crit - ncp, df)
    elif alternative in ("greater", "less"):
        crit = t_ppf(1.0 - alpha, df)
        power = t_sf(crit - ncp, df)
    else:
        raise ValueError("alternative 只能是 two-sided / greater / less")
    power = min(1.0, max(0.0, power))
    return PowerResult(
        power=power,
        beta=1.0 - power,
        alpha=alpha,
        effect_size=effect_size,
        n_per_group=float(n_per_group),
        test="两独立样本 t 检验",
        alternative=alternative,
        approximation="非中心 t 用正态近似，n>=10 时误差通常 <0.01",
    )


def sample_size_two_sample_t(
    effect_size: float,
    power: float = 0.8,
    alpha: float = 0.05,
    alternative: str = "two-sided",
    max_n: int = 100000,
) -> PowerResult:
    """反解每组样本量。先用正态闭式给起点，再逐步递增到达标。

    闭式起点：n = 2*(z_{1-α/2} + z_{power})² / d²。
    它系统性偏小（忽略了 t 比正态尾巴厚），所以之后必须向上搜索校正。
    """
    if effect_size == 0.0:
        raise ValueError("效应量为 0 时任何样本量都达不到功效")
    if not 0.0 < power < 1.0:
        raise ValueError("power 必须在 (0,1)")
    z_a = norm_ppf(1.0 - alpha / (2.0 if alternative == "two-sided" else 1.0))
    z_b = norm_ppf(power)
    n = max(2, ceil(2.0 * (z_a + z_b) ** 2 / effect_size**2))
    while n <= max_n:
        got = power_two_sample_t(effect_size, n, alpha, alternative)
        if got.power >= power:
            return got
        n += 1
    raise ValueError(f"在 n <= {max_n} 内无法达到功效 {power}")


def power_one_sample_t(
    effect_size: float,
    n: float,
    alpha: float = 0.05,
    alternative: str = "two-sided",
) -> PowerResult:
    """单样本 / 配对 t 检验的功效。ncp = d * sqrt(n)。"""
    if n < 2:
        raise ValueError("样本量必须 >= 2")
    df = n - 1.0
    ncp = abs(effect_size) * sqrt(n)
    if alternative == "two-sided":
        crit = t_ppf(1.0 - alpha / 2.0, df)
        power = t_sf(crit - ncp, df) + t_cdf(-crit - ncp, df)
    else:
        crit = t_ppf(1.0 - alpha, df)
        power = t_sf(crit - ncp, df)
    power = min(1.0, max(0.0, power))
    return PowerResult(
        power=power,
        beta=1.0 - power,
        alpha=alpha,
        effect_size=effect_size,
        n_per_group=float(n),
        test="单样本/配对 t 检验",
        alternative=alternative,
        approximation="非中心 t 用正态近似",
    )


def critical_region_two_sample_t(
    n_per_group: float, alpha: float = 0.05, alternative: str = "two-sided"
) -> dict:
    """返回临界值与拒绝域边界，供 hypothesis-test-visualizer 画阴影区。"""
    df = 2.0 * n_per_group - 2.0
    if alternative == "two-sided":
        crit = t_ppf(1.0 - alpha / 2.0, df)
        return {"df": df, "alpha": alpha, "lower": -crit, "upper": crit,
                "alternative": alternative}
    crit = t_ppf(1.0 - alpha, df)
    if alternative == "greater":
        return {"df": df, "alpha": alpha, "lower": crit, "upper": None,
                "alternative": alternative}
    return {"df": df, "alpha": alpha, "lower": None, "upper": -crit,
            "alternative": alternative}
