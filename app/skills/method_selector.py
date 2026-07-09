from __future__ import annotations

from dataclasses import dataclass, field


@dataclass(frozen=True)
class DesignFeatures:
    """从学生描述里抽出的研究设计信号。None 表示未知，用于判断信息是否足够。"""

    outcome: str | None = None          # continuous / categorical / count / ordinal
    n_groups: int | None = None
    paired: bool | None = None
    goal: str | None = None             # compare / associate / predict / relate
    skewed: bool | None = None


@dataclass(frozen=True)
class Recommendation:
    confident: bool
    primary: str = ""
    reasoning: str = ""
    conditions: tuple[str, ...] = field(default_factory=tuple)
    alternatives: tuple[str, ...] = field(default_factory=tuple)
    cautions: tuple[str, ...] = field(default_factory=tuple)
    missing: tuple[str, ...] = field(default_factory=tuple)


_OUTCOME_KEYS = {
    "continuous": ("连续", "成绩", "身高", "体重", "均值", "平均", "分数", "测量值"),
    "categorical": ("分类", "类别", "比例", "是否", "有无", "阳性", "二分类", "占比"),
    "count": ("计数", "次数", "频数", "个数"),
    "ordinal": ("有序", "等级", "评分等级", "满意度", "李克特"),
}
_GOAL_KEYS = {
    "compare": ("比较", "差异", "对比", "高低", "优劣", "组间"),
    "associate": ("关联", "相关性", "独立性", "列联"),
    "predict": ("预测", "回归", "建模", "影响因素", "控制协变量"),
    "relate": ("相关", "线性关系", "相关系数"),
}


def _match(query: str, table: dict[str, tuple[str, ...]]) -> str | None:
    for label, keys in table.items():
        if any(k in query for k in keys):
            return label
    return None


def extract_features(query: str) -> DesignFeatures:
    q = query.lower()
    outcome = _match(query, _OUTCOME_KEYS)
    goal = _match(query, _GOAL_KEYS)

    paired: bool | None = None
    if any(k in query for k in ("配对", "前后测", "重复测量", "同一批", "同一组人")):
        paired = True
    elif any(k in query for k in ("独立", "两组不同", "不同的人", "互不相关")):
        paired = False

    n_groups: int | None = None
    if any(k in query for k in ("两组", "2组", "两个班", "两类", "两种")):
        n_groups = 2
    elif any(k in query for k in ("三组", "3组", "多组", "多个班", "几组", "三个及以上")):
        n_groups = 3

    skewed: bool | None = None
    if any(k in query for k in ("偏态", "偏斜", "重尾", "离群", "异常值", "非正态")):
        skewed = True
    elif any(k in query for k in ("正态", "近似正态", "钟形")):
        skewed = False

    return DesignFeatures(outcome=outcome, n_groups=n_groups, paired=paired, goal=goal, skewed=skewed)


_COMMON_CAUTIONS = (
    "先画图和描述统计，别一上来就套检验。",
    "同时报告效应量和置信区间，不要只看 p 值。",
    "把配对数据当独立样本会低估相关、放大差异。",
)


def recommend_method(features: DesignFeatures) -> Recommendation:
    """基于研究设计的决策树。信息不足时返回 confident=False 并列出待补项。"""
    missing = _missing_fields(features)
    if missing:
        return Recommendation(confident=False, missing=missing,
                              reasoning="研究设计信息不足，无法直接指定方法，需先补齐关键项。")

    goal, outcome = features.goal, features.outcome
    if goal == "associate" or (outcome == "categorical" and goal != "predict"):
        return _categorical_branch(features)
    if goal == "predict":
        return _predict_branch(features)
    if goal == "relate":
        return Recommendation(confident=True, primary="Pearson/Spearman 相关系数",
            reasoning="目标是量化两个变量的线性/单调关系强度，而非组间比较。",
            conditions=("线性且近似正态用 Pearson；偏态或有序用 Spearman。",),
            alternatives=("需要控制其他变量时改用偏相关或多元回归。",),
            cautions=("相关不等于因果；注意离群值对 Pearson 的强影响。",))
    # 默认：连续变量的组间均值比较
    return _compare_means_branch(features)


def _missing_fields(f: DesignFeatures) -> tuple[str, ...]:
    missing: list[str] = []
    if f.goal is None and f.outcome is None:
        missing.append("研究目标（比较/关联/预测/相关）")
    if f.outcome is None:
        missing.append("因变量类型（连续/分类/计数/有序）")
    if f.goal in (None, "compare") and f.outcome == "continuous":
        # 配对已隐含两次测量，不再要求分组数量
        if f.n_groups is None and not f.paired:
            missing.append("分组数量（两组/三组及以上）")
        # 两组或分组未知时必须知道独立/配对，否则无法在 Welch t 与配对 t 间抉择
        if f.paired is None and (f.n_groups is None or f.n_groups == 2):
            missing.append("样本结构（独立/配对/重复测量）")
    return tuple(missing)


def _compare_means_branch(f: DesignFeatures) -> Recommendation:
    if f.n_groups is not None and f.n_groups >= 3:
        if f.skewed:
            return Recommendation(confident=True, primary="Kruskal-Wallis 检验",
                reasoning="三组及以上、连续但分布偏态，用非参数的 Kruskal-Wallis 更稳健。",
                conditions=("各组独立；关注分布位置差异。",),
                alternatives=("分布近似正态时用单因素 ANOVA；方差不齐用 Welch ANOVA。",),
                cautions=_COMMON_CAUTIONS + ("显著后需做多重比较校正（如 Dunn 检验）。",))
        return Recommendation(confident=True, primary="单因素 ANOVA",
            reasoning="三组及以上均值比较，直接两两 t 检验会抬高整体一类错误率。",
            conditions=("各组独立、近似正态、方差齐性。",),
            alternatives=("方差不齐用 Welch ANOVA；偏态用 Kruskal-Wallis。",),
            cautions=_COMMON_CAUTIONS + ("显著后用 Tukey HSD 等做事后多重比较。",))
    if f.paired:
        if f.skewed:
            return Recommendation(confident=True, primary="Wilcoxon 符号秩检验",
                reasoning="配对/前后测且分布偏态，用非参数的符号秩检验。",
                conditions=("同一对象两次测量的差值。",),
                alternatives=("差值近似正态时用配对 t 检验。",),
                cautions=_COMMON_CAUTIONS)
        return Recommendation(confident=True, primary="配对样本 t 检验",
            reasoning="同一批对象前后两次测量，配对设计能消除个体间差异。",
            conditions=("差值近似正态；样本为配对。",),
            alternatives=("差值偏态用 Wilcoxon 符号秩；样本极小时用 Bootstrap。",),
            cautions=_COMMON_CAUTIONS)
    if f.skewed:
        return Recommendation(confident=True, primary="Mann-Whitney U 检验",
            reasoning="两独立组、连续但分布偏态，用非参数的 Mann-Whitney U。",
            conditions=("两组独立；关注分布位置差异。",),
            alternatives=("分布近似正态用 Welch t 检验；也可用 Bootstrap 置信区间。",),
            cautions=_COMMON_CAUTIONS)
    return Recommendation(confident=True, primary="Welch t 检验",
        reasoning="两独立组连续变量比较，Welch 不假设方差齐性，比 Student t 更稳健，应作默认。",
        conditions=("两组独立、近似正态；不要求方差相等。",),
        alternatives=("已确认方差齐性可用 Student t；偏态用 Mann-Whitney 或 Bootstrap。",),
        cautions=_COMMON_CAUTIONS)


def _categorical_branch(f: DesignFeatures) -> Recommendation:
    return Recommendation(confident=True, primary="卡方检验（独立性）",
        reasoning="分类变量之间的关联/独立性，用列联表卡方检验。",
        conditions=("各观测独立；期望频数普遍 ≥5。",),
        alternatives=("小样本或期望频数过低用 Fisher 精确检验；有序分类用 Cochran-Armitage 趋势检验。",),
        cautions=("卡方只说明有无关联，不给方向和强度，需配合 Cramér's V。",
                  "关联不等于因果。",))


def _predict_branch(f: DesignFeatures) -> Recommendation:
    if f.outcome == "categorical":
        return Recommendation(confident=True, primary="Logistic 回归",
            reasoning="因变量是分类（尤其二分类），用 Logistic 回归建模并可控制协变量。",
            conditions=("观测独立；自变量与 logit 近似线性；样本量足够。",),
            alternatives=("多分类用多项 Logistic；有序结局用有序 Logistic。",),
            cautions=("注意共线性和过拟合；报告 OR 与置信区间。",))
    return Recommendation(confident=True, primary="多元线性回归",
        reasoning="连续因变量、需要预测或控制协变量，用线性回归。",
        conditions=("线性、残差独立同方差近似正态、无严重共线性。",),
        alternatives=("非线性关系考虑广义可加模型；异方差用稳健标准误。",),
        cautions=("做残差诊断；回归系数是条件关系，非因果。",))


_DESIGN_QUESTIONS = (
    "1. 因变量是什么，连续/分类/计数/有序？",
    "2. 自变量或分组变量是什么，有几组？",
    "3. 样本是独立、配对，还是重复测量？",
    "4. 样本量分别是多少，是否有明显离群值或偏态？",
    "5. 目标是比较均值、比例、相关，还是预测/解释？",
    "6. 是否需要控制协变量或分层因素？",
)


def render_recommendation(rec: Recommendation) -> str:
    """把结构化推荐渲染成教学文本，供离线路由与 LLM 骨架共用。"""
    if not rec.confident:
        lines = ["结论先行：现在还不能直接指定检验方法，需要先补齐研究设计信息。", ""]
        if rec.missing:
            lines.append("请重点补充：")
            lines += [f"- {m}" for m in rec.missing]
            lines.append("")
        lines.append("完整的设计信息清单：")
        lines += list(_DESIGN_QUESTIONS)
        return "\n".join(lines)

    lines = [
        f"结论先行：建议优先使用 {rec.primary}。",
        "",
        f"为什么：{rec.reasoning}",
        "",
        "适用条件：",
        *[f"- {c}" for c in rec.conditions],
        "",
        "备选方案：",
        *[f"- {a}" for a in rec.alternatives],
        "",
        "常见误区：",
        *[f"- {c}" for c in rec.cautions],
        "",
        "下一步：把变量类型、分组和样本量发我，可以帮你画完整方法决策树。",
    ]
    return "\n".join(lines)
