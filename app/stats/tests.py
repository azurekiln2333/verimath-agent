"""假设检验：统计量 + p 值 + 置信区间 + 效应量。

一条硬性设计约束：**每个检验必须同时返回置信区间和效应量**，不允许只返回
p 值。这不是风格偏好 —— router.py 的 _COMMON_CAUTIONS 和 guard.py 的
statistical_integrity 规则都要求"同时报告效应量和置信区间，不要只看 p 值"。
如果计算层只给 p 值，上层就没法遵守自己的规则。

TestResult 是统一返回形状，供 LLM 工具调用、artifact 初始数据、SVG 降级共用。
"""

from __future__ import annotations

from dataclasses import dataclass, field
from math import inf, isfinite, sqrt
from typing import Any

from app.stats.distributions import (
    chi2_sf,
    f_sf,
    norm_ppf,
    t_cdf,
    t_ppf,
)


@dataclass(frozen=True)
class TestResult:
    """检验结果的统一形状。

    ci 是主要参数（均值差 / 相关系数等）的区间，不是统计量本身的区间。
    effect_size 带名字，因为不同检验的效应量口径不同（d / eta² / V / r）。
    assumptions 列出这个检验依赖但**没有被自动验证**的前提 —— 显式列出比
    沉默更安全，避免把"算出来了"误当成"用对了"。
    """

    name: str
    statistic: float
    p_value: float
    df: float | None = None
    ci: tuple[float, float] | None = None
    ci_level: float = 0.95
    effect_size: float | None = None
    effect_name: str = ""
    estimate: float | None = None
    alternative: str = "two-sided"
    assumptions: tuple[str, ...] = field(default_factory=tuple)
    detail: dict[str, Any] = field(default_factory=dict)

    def as_dict(self) -> dict[str, Any]:
        """给 artifact spec / LLM 工具返回值用的可序列化形状。"""
        return {
            "name": self.name,
            "statistic": self.statistic,
            "p_value": self.p_value,
            "df": self.df,
            "ci": list(self.ci) if self.ci else None,
            "ci_level": self.ci_level,
            "effect_size": self.effect_size,
            "effect_name": self.effect_name,
            "estimate": self.estimate,
            "alternative": self.alternative,
            "assumptions": list(self.assumptions),
            "detail": self.detail,
        }


# ------------------------------------------------------------ 描述统计工具


def mean(xs: list[float]) -> float:
    if not xs:
        raise ValueError("样本不能为空")
    return sum(xs) / len(xs)


def variance(xs: list[float], ddof: int = 1) -> float:
    """样本方差。ddof=1 是无偏估计，这是统计推断的默认，不要写成 0。"""
    n = len(xs)
    if n - ddof <= 0:
        raise ValueError(f"样本量 {n} 不足以在 ddof={ddof} 下估计方差")
    m = mean(xs)
    return sum((x - m) ** 2 for x in xs) / (n - ddof)


def stdev(xs: list[float], ddof: int = 1) -> float:
    return sqrt(variance(xs, ddof))


def _two_sided_p_t(t: float, df: float) -> float:
    """双侧 p 值。用较小的那一侧再乘 2，避免大 cdf 相减丢精度。"""
    return 2.0 * min(t_cdf(t, df), 1.0 - t_cdf(t, df))


def _p_from_t(t: float, df: float, alternative: str) -> float:
    if alternative == "two-sided":
        return _two_sided_p_t(t, df)
    if alternative == "greater":
        return 1.0 - t_cdf(t, df)
    if alternative == "less":
        return t_cdf(t, df)
    raise ValueError("alternative 只能是 two-sided / greater / less")


# ---------------------------------------------------------------- t 检验族


def welch_t(
    a: list[float],
    b: list[float],
    alternative: str = "two-sided",
    ci_level: float = 0.95,
) -> TestResult:
    """两独立样本 Welch t 检验。**这是两组均值比较的默认选择**。

    不假设方差齐性。Student t 只在已确认方差相等时才更优，而"确认方差相等"
    本身需要一个检验（Levene），做完再选检验会抬高一类错误率 —— 所以直接
    默认 Welch 是更稳的做法，与 method_selector.py 的推荐一致。

    效应量用 Cohen's d，标准化分母取两组标准差的均方根。不用合并标准差：
    合并标准差假设方差相等，与 Welch 自身的前提矛盾。
    """
    n1, n2 = len(a), len(b)
    if n1 < 2 or n2 < 2:
        raise ValueError("两组样本量都必须 >= 2")
    m1, m2 = mean(a), mean(b)
    v1, v2 = variance(a), variance(b)
    se = sqrt(v1 / n1 + v2 / n2)
    diff = m1 - m2
    if se == 0.0:
        raise ValueError("两组方差都为 0，无法做 t 检验")
    t = diff / se
    # Welch–Satterthwaite 自由度
    num = (v1 / n1 + v2 / n2) ** 2
    den = (v1 / n1) ** 2 / (n1 - 1) + (v2 / n2) ** 2 / (n2 - 1)
    df = num / den
    p = _p_from_t(t, df, alternative)
    crit = t_ppf(1.0 - (1.0 - ci_level) / 2.0, df)
    ci = (diff - crit * se, diff + crit * se)
    d = diff / sqrt((v1 + v2) / 2.0)
    return TestResult(
        name="Welch t 检验",
        statistic=t,
        p_value=p,
        df=df,
        ci=ci,
        ci_level=ci_level,
        effect_size=d,
        effect_name="Cohen's d",
        estimate=diff,
        alternative=alternative,
        assumptions=(
            "两组相互独立（不是配对/重复测量）",
            "各组近似正态，或样本量足以让均值抽样分布接近正态",
            "不要求方差齐性（这正是 Welch 相对 Student t 的优势）",
        ),
        detail={"n1": n1, "n2": n2, "mean1": m1, "mean2": m2,
                "var1": v1, "var2": v2, "se": se},
    )


def student_t(
    a: list[float],
    b: list[float],
    alternative: str = "two-sided",
    ci_level: float = 0.95,
) -> TestResult:
    """两独立样本 Student t 检验（假设方差齐性）。

    只在已有外部依据确认方差相等时使用。默认请用 welch_t。
    """
    n1, n2 = len(a), len(b)
    if n1 < 2 or n2 < 2:
        raise ValueError("两组样本量都必须 >= 2")
    m1, m2 = mean(a), mean(b)
    v1, v2 = variance(a), variance(b)
    df = n1 + n2 - 2.0
    sp2 = ((n1 - 1) * v1 + (n2 - 1) * v2) / df       # 合并方差
    se = sqrt(sp2 * (1.0 / n1 + 1.0 / n2))
    if se == 0.0:
        raise ValueError("合并方差为 0，无法做 t 检验")
    diff = m1 - m2
    t = diff / se
    p = _p_from_t(t, df, alternative)
    crit = t_ppf(1.0 - (1.0 - ci_level) / 2.0, df)
    return TestResult(
        name="Student t 检验",
        statistic=t,
        p_value=p,
        df=df,
        ci=(diff - crit * se, diff + crit * se),
        ci_level=ci_level,
        effect_size=diff / sqrt(sp2),
        effect_name="Cohen's d（合并标准差）",
        estimate=diff,
        alternative=alternative,
        assumptions=(
            "两组相互独立",
            "各组近似正态",
            "**方差齐性** —— 这是相对 Welch 的额外假设，违背时一类错误率会失控",
        ),
        detail={"n1": n1, "n2": n2, "mean1": m1, "mean2": m2,
                "pooled_var": sp2, "se": se},
    )


def paired_t(
    before: list[float],
    after: list[float],
    alternative: str = "two-sided",
    ci_level: float = 0.95,
) -> TestResult:
    """配对样本 t 检验。本质是对差值做单样本 t 检验。

    把配对数据当独立样本处理会低估相关、放大标准误 —— 这是
    router.py 里 _COMMON_CAUTIONS 点名的常见错误。
    """
    if len(before) != len(after):
        raise ValueError("配对数据两列长度必须相同")
    diffs = [x - y for x, y in zip(before, after)]
    res = one_sample_t(diffs, mu0=0.0, alternative=alternative, ci_level=ci_level)
    return TestResult(
        name="配对样本 t 检验",
        statistic=res.statistic,
        p_value=res.p_value,
        df=res.df,
        ci=res.ci,
        ci_level=ci_level,
        effect_size=res.effect_size,
        effect_name="Cohen's d（差值标准差）",
        estimate=res.estimate,
        alternative=alternative,
        assumptions=(
            "同一对象的两次测量构成配对",
            "**差值**近似正态（不要求原始数据正态）",
        ),
        detail={"n_pairs": len(diffs), "mean_diff": res.estimate,
                "sd_diff": stdev(diffs)},
    )


def one_sample_t(
    xs: list[float],
    mu0: float = 0.0,
    alternative: str = "two-sided",
    ci_level: float = 0.95,
) -> TestResult:
    """单样本 t 检验：样本均值与已知常数 mu0 比较。"""
    n = len(xs)
    if n < 2:
        raise ValueError("样本量必须 >= 2")
    m = mean(xs)
    s = stdev(xs)
    if s == 0.0:
        raise ValueError("样本方差为 0，无法做 t 检验")
    se = s / sqrt(n)
    df = n - 1.0
    t = (m - mu0) / se
    crit = t_ppf(1.0 - (1.0 - ci_level) / 2.0, df)
    # estimate 与 ci 必须同一标度：都指样本均值本身，不是它与 mu0 的差。
    # 检验与区间的对偶关系是"CI 是否包含 mu0"，而非"是否包含 0" ——
    # 差值标度只有在 mu0=0（配对检验的情形）时才与均值标度重合。
    return TestResult(
        name="单样本 t 检验",
        statistic=t,
        p_value=_p_from_t(t, df, alternative),
        df=df,
        ci=(m - crit * se, m + crit * se),
        ci_level=ci_level,
        effect_size=(m - mu0) / s,
        effect_name="Cohen's d",
        estimate=m,
        alternative=alternative,
        assumptions=("观测相互独立", "近似正态或样本量足够"),
        detail={"n": n, "mean": m, "sd": s, "se": se, "mu0": mu0,
                "mean_minus_mu0": m - mu0},
    )


# ------------------------------------------------------------------- ANOVA


def anova_oneway(groups: list[list[float]], ci_level: float = 0.95) -> TestResult:
    """单因素方差分析。

    效应量给 eta² 和 omega²。eta² 是有偏的（样本量小时系统性偏大），
    omega² 做了偏差校正 —— 报告时优先用 omega²。
    """
    k = len(groups)
    if k < 2:
        raise ValueError("至少需要 2 组")
    if any(len(g) < 2 for g in groups):
        raise ValueError("每组样本量都必须 >= 2")
    n_total = sum(len(g) for g in groups)
    grand = sum(sum(g) for g in groups) / n_total
    ss_between = sum(len(g) * (mean(g) - grand) ** 2 for g in groups)
    ss_within = sum((x - mean(g)) ** 2 for g in groups for x in g)
    df_b = k - 1.0
    df_w = n_total - k
    if df_w <= 0:
        raise ValueError("组内自由度不足")
    ms_b, ms_w = ss_between / df_b, ss_within / df_w
    if ms_w == 0.0:
        raise ValueError("组内方差为 0，无法做 F 检验")
    f = ms_b / ms_w
    ss_total = ss_between + ss_within
    eta2 = ss_between / ss_total if ss_total > 0 else 0.0
    omega2_num = ss_between - df_b * ms_w
    omega2 = omega2_num / (ss_total + ms_w) if (ss_total + ms_w) > 0 else 0.0
    return TestResult(
        name="单因素 ANOVA",
        statistic=f,
        p_value=f_sf(f, df_b, df_w),
        df=df_b,
        ci=None,   # F 检验本身不给参数区间，事后比较才给
        ci_level=ci_level,
        effect_size=omega2,
        effect_name="omega²（偏差校正）",
        estimate=None,
        alternative="greater",
        assumptions=(
            "各组相互独立",
            "各组近似正态",
            "方差齐性 —— 违背时改用 Welch ANOVA",
            "显著只说明至少有一组不同，必须做事后多重比较（如 Tukey HSD）才知道是哪几组",
        ),
        detail={"k": k, "n_total": n_total, "df_between": df_b, "df_within": df_w,
                "ms_between": ms_b, "ms_within": ms_w, "eta_squared": eta2,
                "omega_squared": omega2, "group_means": [mean(g) for g in groups]},
    )


# --------------------------------------------------------------- 卡方检验


def chi2_independence(table: list[list[float]]) -> TestResult:
    """列联表独立性卡方检验。效应量用 Cramér's V。

    自动检查期望频数：有 cell 期望频数 < 5 时写进 assumptions 提示，
    因为这是卡方近似失效的主要场景，应改用 Fisher 精确检验。
    """
    r = len(table)
    if r < 2 or any(len(row) < 2 for row in table):
        raise ValueError("列联表至少需要 2x2")
    c = len(table[0])
    if any(len(row) != c for row in table):
        raise ValueError("列联表每行长度必须一致")
    total = sum(sum(row) for row in table)
    if total <= 0:
        raise ValueError("列联表总频数必须大于 0")
    row_sums = [sum(row) for row in table]
    col_sums = [sum(table[i][j] for i in range(r)) for j in range(c)]
    stat = 0.0
    min_expected = inf
    for i in range(r):
        for j in range(c):
            expected = row_sums[i] * col_sums[j] / total
            min_expected = min(min_expected, expected)
            if expected > 0:
                stat += (table[i][j] - expected) ** 2 / expected
    df = (r - 1.0) * (c - 1.0)
    v = sqrt(stat / (total * min(r - 1, c - 1)))
    notes = [
        "各观测相互独立（每个个体只进一个格子）",
        "期望频数普遍 >= 5",
        "卡方只说明有无关联，不给方向和强度 —— 必须配 Cramér's V",
        "关联不等于因果",
    ]
    if min_expected < 5.0:
        notes.append(
            f"警告：最小期望频数 {min_expected:.2f} < 5，卡方近似不可靠，"
            "改用 Fisher 精确检验"
        )
    return TestResult(
        name="卡方独立性检验",
        statistic=stat,
        p_value=chi2_sf(stat, df),
        df=df,
        effect_size=v,
        effect_name="Cramér's V",
        alternative="greater",
        assumptions=tuple(notes),
        detail={"rows": r, "cols": c, "total": total,
                "min_expected": min_expected,
                "row_sums": row_sums, "col_sums": col_sums},
    )


# ----------------------------------------------------------------- 相关分析


def _ranks(xs: list[float]) -> list[float]:
    """秩，并列取平均秩。Spearman 与非参数检验的基础。"""
    n = len(xs)
    order = sorted(range(n), key=lambda i: xs[i])
    out = [0.0] * n
    i = 0
    while i < n:
        j = i
        while j + 1 < n and xs[order[j + 1]] == xs[order[i]]:
            j += 1
        avg = (i + j) / 2.0 + 1.0
        for k in range(i, j + 1):
            out[order[k]] = avg
        i = j + 1
    return out


def pearson(
    x: list[float],
    y: list[float],
    alternative: str = "two-sided",
    ci_level: float = 0.95,
) -> TestResult:
    """Pearson 相关系数。置信区间走 Fisher z 变换。

    r 的抽样分布在 |r| 大时严重偏斜，直接用正态近似做区间会错。
    Fisher z = arctanh(r) 的分布近似正态，标准误 1/sqrt(n-3)，
    在 z 空间做区间再变换回来 —— 这是标准做法。
    """
    n = len(x)
    if n != len(y):
        raise ValueError("两列长度必须相同")
    if n < 3:
        raise ValueError("样本量必须 >= 3")
    mx, my = mean(x), mean(y)
    sxy = sum((a - mx) * (b - my) for a, b in zip(x, y))
    sxx = sum((a - mx) ** 2 for a in x)
    syy = sum((b - my) ** 2 for b in y)
    if sxx == 0.0 or syy == 0.0:
        raise ValueError("有一列是常数，相关系数无定义")
    r = sxy / sqrt(sxx * syy)
    r = max(-1.0, min(1.0, r))          # 夹住浮点溢出
    df = n - 2.0
    if abs(r) >= 1.0:
        t, p, ci = inf if r > 0 else -inf, 0.0, (r, r)
    else:
        t = r * sqrt(df / (1.0 - r * r))
        p = _p_from_t(t, df, alternative)
        from math import atanh, tanh
        z = atanh(r)
        se_z = 1.0 / sqrt(n - 3.0) if n > 3 else inf
        crit = norm_ppf(1.0 - (1.0 - ci_level) / 2.0)
        ci = ((tanh(z - crit * se_z), tanh(z + crit * se_z))
              if isfinite(se_z) else (-1.0, 1.0))
    return TestResult(
        name="Pearson 相关",
        statistic=t,
        p_value=p,
        df=df,
        ci=ci,
        ci_level=ci_level,
        effect_size=r * r,
        effect_name="R²（决定系数）",
        estimate=r,
        alternative=alternative,
        assumptions=(
            "两变量近似线性关系 —— 非线性关系 r 可能接近 0 却强相关",
            "近似二元正态；对离群值极敏感，一个点就能翻转结论",
            "相关不等于因果",
        ),
        detail={"n": n, "r": r, "mean_x": mx, "mean_y": my},
    )


def spearman(
    x: list[float],
    y: list[float],
    alternative: str = "two-sided",
    ci_level: float = 0.95,
) -> TestResult:
    """Spearman 秩相关：对秩做 Pearson。度量单调关系，不要求线性。"""
    if len(x) != len(y):
        raise ValueError("两列长度必须相同")
    res = pearson(_ranks(x), _ranks(y), alternative=alternative, ci_level=ci_level)
    return TestResult(
        name="Spearman 秩相关",
        statistic=res.statistic,
        p_value=res.p_value,
        df=res.df,
        ci=res.ci,
        ci_level=ci_level,
        effect_size=res.effect_size,
        effect_name="R²（基于秩）",
        estimate=res.estimate,
        alternative=alternative,
        assumptions=(
            "度量单调关系，不要求线性，对离群值比 Pearson 稳健",
            "并列值多时精度下降",
            "相关不等于因果",
        ),
        detail={"n": len(x), "rho": res.estimate},
    )
