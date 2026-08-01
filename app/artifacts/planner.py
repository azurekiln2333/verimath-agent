"""从问题文本确定性地挑选可视化件。

为什么不直接让模型决定：**确定性路径的成功率是 100%，模型选型不是。**
"中心极限定理"这类问题该配哪张图是固定的，没必要每次都花一次模型调用
去赌它选对。模型只在确定性规则不命中时才介入（见 app/agents/artifact_agent.py）。

这也让核心教学场景可回归测试 —— 规则命中是可断言的，模型输出不是。
"""

from __future__ import annotations

import re
from dataclasses import dataclass

from app.artifacts.spec import ArtifactSpec, build_artifact


@dataclass(frozen=True)
class PlanResult:
    """规则命中结果。matched_rule 写进 trace，便于排查「为什么配了这张图」。"""

    spec: ArtifactSpec | None
    matched_rule: str = ""

    @property
    def hit(self) -> bool:
        return self.spec is not None


# 关键词 → 规则。顺序有意义：越具体的规则排前面。
# 例如「置信区间的覆盖率」要走 CI widget，不能被「置信区间」泛化到别处。


def _clt(_: str) -> ArtifactSpec:
    return build_artifact(
        "sampling_distribution",
        "中心极限定理：样本均值的抽样分布",
        "左图是总体分布（强右偏），右图是样本均值的分布。拖动 n 会看到："
        "总体形状始终不变，而均值的分布越来越接近钟形。这正是中心极限定理的内容 ——"
        "它说的是均值的分布趋于正态，不是原始数据会变成正态。",
        population="expon",
        sample_size=5,
        n_samples=2000,
        statistic="mean",
        overlay_normal=True,
        interactive=["sample_size", "seed"],
    )


def _ci_coverage(_: str) -> ArtifactSpec:
    return build_artifact(
        "confidence_interval",
        "置信区间的含义：覆盖率演示",
        "每一条横线是一次重复实验得到的 95% 置信区间，红色的那些没盖住真值。"
        "长期来看约 95% 的区间会盖住真值 —— 随机的是区间，真值是固定的。"
        "所以「某个给定区间有 95% 概率包含真值」这个说法是错的。",
        true_mean=0.0,
        true_sd=1.0,
        sample_size=20,
        n_intervals=50,
        ci_level=0.95,
        interactive=["sample_size", "ci_level", "seed"],
    )


def _power(_: str) -> ArtifactSpec:
    return build_artifact(
        "power_curve",
        "检验效能与样本量",
        "曲线是功效随每组样本量的变化。虚线是目标功效 0.8，点线是 α。"
        "注意功效永远不会低于 α（效应量为 0 时功效恰好等于 α），"
        "以及效应量越小、所需样本量增长得越快。",
        x_axis="n",
        effect_size=0.5,
        n_per_group=30,
        alpha=0.05,
        target_power=0.8,
        compare=[0.2, 0.8],
        interactive=["alpha", "effect_size"],
    )


def _p_value(_: str) -> ArtifactSpec:
    return build_artifact(
        "hypothesis_test",
        "p 值是什么：零分布下的尾部面积",
        "曲线是 H₀ 为真时统计量的分布。绿色阴影是 p 值 —— "
        "假设 H₀ 成立，得到「至少这么极端」结果的概率。红色是拒绝域。"
        "p 值不是 H₀ 为真的概率，也不是效应大小。",
        test="t",
        df=18,
        statistic=2.31,
        alpha=0.05,
        alternative="two-sided",
        show_p_area=True,
        show_rejection=True,
    )


def _distribution(family: str, params: dict, title: str, caption: str) -> ArtifactSpec:
    return build_artifact(
        "distribution_explorer",
        title,
        caption,
        family=family,
        params=params,
        show="pdf",
    )


def _t_distribution(_: str) -> ArtifactSpec:
    return _distribution(
        "t",
        {"df": 5},
        "t 分布：自由度如何影响尾部",
        "拖动 df 观察尾部厚度。df 小时尾部明显比正态厚 —— "
        "这就是小样本要用 t 临界值而不是 1.96 的原因。df 增大后曲线趋近标准正态。",
    )


def _normal(_: str) -> ArtifactSpec:
    return _distribution(
        "normal",
        {"mu": 0, "sigma": 1},
        "正态分布",
        "拖动 μ 平移曲线，拖动 σ 改变宽度。曲线下的总面积恒为 1，"
        "所以变宽必然变矮。",
    )


def _chi2(_: str) -> ArtifactSpec:
    return _distribution(
        "chi2",
        {"df": 3},
        "卡方分布",
        "只取非负值，右偏。df 增大时偏度减小并趋近正态。"
        "拟合优度检验与独立性检验的统计量在 H₀ 下近似服从它。",
    )


def _f_dist(_: str) -> ArtifactSpec:
    return _distribution(
        "f",
        {"dfn": 3, "dfd": 20},
        "F 分布",
        "两个方差之比的分布，非负右偏。ANOVA 的 F 统计量在 H₀ 下服从它 —— "
        "分子是组间方差，分母是组内方差。",
    )


def _binomial(_: str) -> ArtifactSpec:
    return _distribution(
        "binom",
        {"n": 20, "p": 0.5},
        "二项分布",
        "n 次独立试验中成功次数的分布。拖动 p 看偏斜方向，"
        "n 增大时形状趋近正态 —— 这是正态近似二项的依据。",
    )


def _poisson(_: str) -> ArtifactSpec:
    return _distribution(
        "poisson",
        {"lam": 4},
        "泊松分布",
        "单位时间/空间内稀有事件发生次数的分布。均值与方差都等于 λ。"
        "λ 增大时趋近正态。",
    )


def _exponential(_: str) -> ArtifactSpec:
    return _distribution(
        "expon",
        {"scale": 1.0},
        "指数分布",
        "等待时间的分布，具备无记忆性。scale 就是均值。"
        "它是泊松过程相邻事件间隔的分布。",
    )


def _beta(_: str) -> ArtifactSpec:
    return _distribution(
        "beta",
        {"a": 2, "b": 3},
        "Beta 分布",
        "定义在 [0,1] 上，常用来描述比例或概率的不确定性。"
        "拖动 α、β 看形状：两者相等时对称，α=β=1 时退化为均匀分布。",
    )


def _t_test_viz(_: str) -> ArtifactSpec:
    return build_artifact(
        "hypothesis_test",
        "t 检验的零分布与拒绝域",
        "曲线是 H₀（两组均值相等）为真时 t 统计量的分布。"
        "红色是双侧拒绝域，绿色阴影是当前观测值对应的 p 值。"
        "拖动观测值看 p 值怎么随之变化。",
        test="t",
        df=18,
        statistic=2.31,
        alpha=0.05,
        alternative="two-sided",
    )


def _anova_viz(_: str) -> ArtifactSpec:
    return build_artifact(
        "hypothesis_test",
        "ANOVA 的 F 检验",
        "F 统计量在 H₀（各组均值全相等）下服从 F 分布，只看右尾。"
        "注意：F 显著只说明「至少有一组不同」，要知道是哪几组不同，"
        "必须做事后多重比较（如 Tukey HSD）。",
        test="f",
        df=2,
        df2=27,
        statistic=4.2,
        alpha=0.05,
        alternative="greater",
    )


def _chi2_test_viz(_: str) -> ArtifactSpec:
    return build_artifact(
        "hypothesis_test",
        "卡方检验的零分布",
        "卡方统计量非负，只看右尾。绿色阴影是 p 值。"
        "注意卡方只说明有无关联，不给方向和强度 —— 需要配合 Cramér's V。",
        test="chi2",
        df=3,
        statistic=7.8,
        alpha=0.05,
        alternative="greater",
    )


def _effect_size_viz(_: str) -> ArtifactSpec:
    return build_artifact(
        "effect_size",
        "为什么不能只看 p 值",
        "三项研究的效应量与 95% 置信区间。研究 C 虽然「显著」，"
        "但区间极宽，实际信息量很低；研究 B 不显著，却不能因此断定无效应 —— "
        "它的区间同时包含了可观的正效应。区间宽度反映的是估计精度。",
        items=[
            {"label": "研究 A（n=200）", "estimate": 0.42, "ci_low": 0.14, "ci_high": 0.70},
            {"label": "研究 B（n=30）", "estimate": 0.35, "ci_low": -0.18, "ci_high": 0.88},
            {"label": "研究 C（n=12）", "estimate": 1.10, "ci_low": 0.05, "ci_high": 2.15},
        ],
        null_value=0.0,
        x_label="效应量 Cohen's d",
    )


def _correlation_viz(_: str) -> ArtifactSpec:
    # 一组相关强但明显非因果的数据，用于讲「相关不等于因果」
    xs = [1.0, 2.0, 3.0, 4.0, 5.0, 6.0, 7.0, 8.0, 9.0, 10.0]
    ys = [2.3, 3.1, 4.6, 5.2, 6.8, 7.1, 8.9, 9.2, 10.8, 11.3]
    return build_artifact(
        "scatter_regression",
        "相关与回归",
        "散点加最小二乘拟合线，虚线是回归线的 95% 置信带 —— "
        "注意它在两端变宽，这说明外推不可靠。R² 只衡量线性解释力，"
        "既不保证模型正确，也不说明因果方向。",
        x=xs,
        y=ys,
        show_fit=True,
        show_residuals=True,
        show_ci_band=True,
        x_label="x",
        y_label="y",
    )


def _lln_viz(_: str) -> ArtifactSpec:
    return build_artifact(
        "sampling_distribution",
        "大数定律 vs 中心极限定理",
        "大数定律说的是样本均值收敛到总体均值（右图分布越来越集中），"
        "中心极限定理说的是均值的分布形状趋于正态（右图越来越像钟形）。"
        "两者说的是同一件事的不同侧面：一个讲位置，一个讲形状。拖动 n 同时观察这两点。",
        population="uniform",
        sample_size=5,
        n_samples=2000,
        statistic="mean",
        overlay_normal=True,
        interactive=["sample_size", "seed"],
    )


# 规则表：(规则名, 匹配的正则, 构造函数)
# 顺序即优先级 —— 具体规则必须排在泛化规则之前。
_RULES: tuple[tuple[str, re.Pattern[str], object], ...] = (
    # 具体误解优先
    ("ci_coverage", re.compile(
        r"置信区间.*(含义|理解|意味|覆盖|误解|解释|到底)"
        r"|(含义|理解|意味|覆盖|误解|怎么解释).*置信区间"
        r"|95%.*概率.*(区间|里面|包含)"
        r"|区间估计.*含义"
    ), _ci_coverage),
    # lln 必须排在 clt 之前：同时提到两者时，该给「对比」那张图而不是单讲 CLT
    ("lln", re.compile(r"大数定律|大数法则|\bLLN\b", re.I), _lln_viz),
    ("clt", re.compile(r"中心极限定理|\bCLT\b|抽样分布.*正态|为什么.*样本均值.*正态", re.I), _clt),
    ("p_value", re.compile(
        r"p\s*值.*(是什么|含义|意味|理解|误解|多少|怎么算|解释)"
        r"|(什么是|理解|解释).*p\s*值"
        r"|显著性水平.*含义"
        r"|p<0?\.05",
        re.I,
    ), _p_value),
    # 样本量的问法两个语序都要覆盖：「样本量怎么算」与「怎么算样本量」
    ("power", re.compile(
        r"功效|效能|检验力|\bpower\b"
        r"|样本量.*(多少|怎么|计算|估算|需要|确定)"
        r"|(多少|怎么|如何|计算|估算|确定|算).*样本量"
        r"|样本量估算|需要多少(人|个|样本)",
        re.I,
    ), _power),
    ("effect_size", re.compile(r"效应量|effect size|只看\s*p|不要只看\s*p|cohen", re.I), _effect_size_viz),
    # 具体检验
    ("anova", re.compile(r"anova|方差分析|单因素|F\s*检验", re.I), _anova_viz),
    ("chi2_test", re.compile(r"卡方检验|独立性检验|列联表|拟合优度", re.I), _chi2_test_viz),
    ("t_test", re.compile(r"t\s*检验|welch|两组.*(比较|差异)|均值比较", re.I), _t_test_viz),
    ("correlation", re.compile(r"相关(系数|分析|不等于因果)?|回归|pearson|spearman|散点", re.I), _correlation_viz),
    # 分布本身（排在检验之后：「t 检验」不应命中「t 分布」）
    ("t_dist", re.compile(r"t\s*分布|学生分布|自由度.*(尾部|影响)", re.I), _t_distribution),
    ("chi2_dist", re.compile(r"卡方分布|χ²|chi.?square", re.I), _chi2),
    ("f_dist", re.compile(r"F\s*分布", re.I), _f_dist),
    ("binomial", re.compile(r"二项分布|伯努利", re.I), _binomial),
    ("poisson", re.compile(r"泊松|poisson", re.I), _poisson),
    ("exponential", re.compile(r"指数分布|无记忆性", re.I), _exponential),
    ("beta_dist", re.compile(r"beta\s*分布|贝塔分布", re.I), _beta),
    ("normal", re.compile(r"正态分布|高斯分布|normal distribution|钟形", re.I), _normal),
)


def plan_artifact(query: str, route: str = "") -> PlanResult:
    """按规则表挑一个可视化件。没命中就返回空结果（上层可交给模型或不配图）。

    route 目前只用于排除 guard —— 被守门拦下的请求不该配图。
    """
    if route == "guard":
        return PlanResult(None)
    text = query or ""
    for name, pattern, factory in _RULES:
        if pattern.search(text):
            try:
                return PlanResult(factory(text), name)
            except Exception:
                # 构造失败绝不能影响文字回答，静默降级为不配图
                return PlanResult(None, f"{name}:failed")
    return PlanResult(None)


def rule_names() -> list[str]:
    """供测试与文档使用的规则清单。"""
    return [name for name, _, _ in _RULES]
