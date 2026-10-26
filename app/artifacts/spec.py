"""artifact spec 的定义与校验。

每个 widget 声明自己的参数模型（pydantic），注册表把 kind 映射到模型。
校验失败抛 ArtifactValidationError，上层据此降级为纯文字回答 ——
**宁可不画图，也不能画错的图**：一张参数错误的分布图比没有图更有害。
"""

from __future__ import annotations

from typing import Any, Literal

from pydantic import BaseModel, ConfigDict, Field, ValidationError, field_validator


class ArtifactValidationError(ValueError):
    """spec 不合法。携带人类可读的原因，便于写进 trace 与降级说明。"""


class _Base(BaseModel):
    model_config = ConfigDict(extra="forbid")


# --------------------------------------------------------------------- 参数模型


class DistributionExplorerParams(_Base):
    """分布探索器：画 pdf/cdf，可标临界值与阴影区。

    教学用途：把"分布形状随参数怎么变"变成可拖动的直觉。
    """

    family: Literal["normal", "t", "chi2", "f", "beta", "expon", "binom", "poisson"]
    # 各分布的参数用统一的 params 字典，由 widget 按 family 取用。
    # 不为每个分布单独建模型，是因为前端 widget 本来就要 switch(family)，
    # 分开建模只会让注册表膨胀而不增加安全性。
    params: dict[str, float] = Field(default_factory=dict)
    show: Literal["pdf", "cdf", "both"] = "pdf"
    shade_from: float | None = None
    shade_to: float | None = None
    mark_x: list[float] = Field(default_factory=list)
    x_min: float | None = None
    x_max: float | None = None
    interactive: list[str] = Field(default_factory=list)

    @field_validator("params")
    @classmethod
    def _finite_params(cls, v: dict[str, float]) -> dict[str, float]:
        for key, val in v.items():
            if not isinstance(val, (int, float)) or val != val:
                raise ValueError(f"params.{key} 必须是有限数值")
        return v


class HypothesisTestParams(_Base):
    """假设检验可视化：零分布 + 拒绝域 + 观测统计量 + p 值面积。

    这是"p 值到底是什么"最有效的一张图 —— 面积可见，学生不会再把
    p 值当成"H0 为真的概率"。
    """

    test: Literal["z", "t", "chi2", "f"]
    df: float | None = None
    df2: float | None = None
    statistic: float
    alpha: float = 0.05
    alternative: Literal["two-sided", "greater", "less"] = "two-sided"
    show_p_area: bool = True
    show_rejection: bool = True

    @field_validator("alpha")
    @classmethod
    def _alpha_range(cls, v: float) -> float:
        if not 0.0 < v < 1.0:
            raise ValueError("alpha 必须在 (0, 1) 之间")
        return v

    @field_validator("df", "df2")
    @classmethod
    def _df_positive(cls, v: float | None) -> float | None:
        if v is not None and v <= 0:
            raise ValueError("自由度必须大于 0")
        return v


class SamplingDistributionParams(_Base):
    """抽样分布模拟：中心极限定理的可视化。

    seed 是必需的：教学上"再来一次得到一样的结果"与"换个种子看是否巧合"
    都要能做到。
    """

    population: Literal["normal", "uniform", "expon", "bimodal", "skewed"]
    sample_size: int = Field(ge=1, le=1000)
    n_samples: int = Field(default=1000, ge=10, le=20000)
    statistic: Literal["mean", "median", "variance", "max"] = "mean"
    # 上界与前端「随机种子」滑块的范围一致。超范围的种子会被 <input type=range>
    # 静默夹到边界，导致滑块显示值与实际渲染值不一致、且无法恢复初始图。
    seed: int = Field(default=607, ge=1, le=999)
    overlay_normal: bool = True
    interactive: list[str] = Field(default_factory=list)


class ConfidenceIntervalParams(_Base):
    """置信区间的覆盖率演示：画很多条区间，标出没盖住真值的那些。

    专治"95% CI 意味着参数有 95% 概率落在里面"这个误解 ——
    看见 100 条里有约 5 条打红，就理解了频率派的含义。
    """

    true_mean: float = 0.0
    true_sd: float = Field(default=1.0, gt=0)
    sample_size: int = Field(ge=2, le=500)
    n_intervals: int = Field(default=50, ge=5, le=300)
    ci_level: float = Field(default=0.95, gt=0, lt=1)
    seed: int = Field(default=607, ge=1, le=999)
    interactive: list[str] = Field(default_factory=list)


class PowerCurveParams(_Base):
    """功效曲线：α、效应量、样本量、功效的四角关系。"""

    x_axis: Literal["n", "effect_size", "alpha"] = "n"
    effect_size: float = 0.5
    n_per_group: int = Field(default=30, ge=2, le=5000)
    alpha: float = Field(default=0.05, gt=0, lt=1)
    alternative: Literal["two-sided", "greater", "less"] = "two-sided"
    target_power: float = Field(default=0.8, gt=0, lt=1)
    compare: list[float] = Field(default_factory=list)
    interactive: list[str] = Field(default_factory=list)


class ScatterRegressionParams(_Base):
    """散点 + 回归线：相关与回归的关系，以及"相关不等于因果"。"""

    x: list[float]
    y: list[float]
    show_fit: bool = True
    show_residuals: bool = False
    show_ci_band: bool = False
    x_label: str = "x"
    y_label: str = "y"

    @field_validator("y")
    @classmethod
    def _no_nan(cls, v: list[float]) -> list[float]:
        if any(val != val for val in v):
            raise ValueError("y 中不能含 NaN")
        return v

    def model_post_init(self, __context: Any) -> None:
        if len(self.x) != len(self.y):
            raise ValueError("x 与 y 长度必须相同")
        if len(self.x) < 3:
            raise ValueError("散点回归至少需要 3 个点")


class DataPlotParams(_Base):
    """原始数据的分布图：直方图 / 箱线图 / 点图。

    做假设检验前先看数据 —— 这个习惯本身就是教学内容。
    """

    series: list[dict[str, Any]]
    kind: Literal["histogram", "box", "dot", "violin"] = "histogram"
    bins: int | None = Field(default=None, ge=1, le=200)
    overlay_normal: bool = False
    x_label: str = ""

    @field_validator("series")
    @classmethod
    def _valid_series(cls, v: list[dict[str, Any]]) -> list[dict[str, Any]]:
        if not v:
            raise ValueError("series 不能为空")
        if len(v) > 8:
            raise ValueError("最多 8 组数据")
        for i, s in enumerate(v):
            values = s.get("values")
            if not isinstance(values, list) or len(values) < 1:
                raise ValueError(f"series[{i}].values 必须是非空数组")
            for val in values:
                if not isinstance(val, (int, float)) or val != val:
                    raise ValueError(f"series[{i}].values 含非有限数值")
        return v


class EffectSizeParams(_Base):
    """效应量与置信区间的并排比较 —— 逼着人看区间而不是只看 p 值。"""

    items: list[dict[str, Any]]
    null_value: float = 0.0
    x_label: str = "效应量"

    @field_validator("items")
    @classmethod
    def _valid_items(cls, v: list[dict[str, Any]]) -> list[dict[str, Any]]:
        if not v:
            raise ValueError("items 不能为空")
        if len(v) > 20:
            raise ValueError("最多 20 项")
        for i, item in enumerate(v):
            for key in ("label", "estimate", "ci_low", "ci_high"):
                if key not in item:
                    raise ValueError(f"items[{i}] 缺少 {key}")
            if not item["ci_low"] <= item["estimate"] <= item["ci_high"]:
                raise ValueError(f"items[{i}] 的点估计必须落在区间内")
        return v


# ----------------------------------------------------------------------- 注册表

class FunctionPlotParams(_Base):
    """函数图像：一次 / 二次 / 幂 / 指数等，可叠加另一条曲线做对比。

    初中到大学一年级的"函数与方程"通用图。二次函数额外标顶点、对称轴与
    判别式 —— 这三样是学生最容易只背结论、不看图的点。
    """

    family: Literal["linear", "quadratic", "cubic", "power", "exponential", "log"]
    a: float = 1.0
    b: float = 0.0
    c: float = 0.0
    domain: list[float] | None = None
    compare: list[dict[str, Any]] = Field(default_factory=list)
    show_roots: bool = True
    show_vertex: bool = True
    show_axis: bool = True
    x_min: float | None = None
    x_max: float | None = None
    interactive: list[str] = Field(default_factory=list)

    @field_validator("domain")
    @classmethod
    def _domain_pair(cls, v: list[float] | None) -> list[float] | None:
        if v is None:
            return v
        if len(v) != 2 or not v[0] < v[1]:
            raise ValueError("domain 必须是 [下限, 上限] 且下限 < 上限")
        return v

    @field_validator("compare")
    @classmethod
    def _compare_shape(cls, v: list[dict[str, Any]]) -> list[dict[str, Any]]:
        if len(v) > 3:
            raise ValueError("最多叠加 3 条对比曲线")
        for i, item in enumerate(v):
            for key in ("a", "b", "c"):
                if key in item and not isinstance(item[key], (int, float)):
                    raise ValueError(f"compare[{i}].{key} 必须是数值")
            if item.get("family") and item["family"] not in {
                "linear", "quadratic", "cubic", "power", "exponential", "log"
            }:
                raise ValueError(f"compare[{i}].family 不支持")
        return v


WIDGET_REGISTRY: dict[str, type[_Base]] = {
    "distribution_explorer": DistributionExplorerParams,
    "hypothesis_test": HypothesisTestParams,
    "sampling_distribution": SamplingDistributionParams,
    "confidence_interval": ConfidenceIntervalParams,
    "power_curve": PowerCurveParams,
    "scatter_regression": ScatterRegressionParams,
    "data_plot": DataPlotParams,
    "effect_size": EffectSizeParams,
    "function_plot": FunctionPlotParams,
}

# 每个 widget 的一句话用途 + 何时该选它。会拼进系统提示词，
# 所以措辞直接影响模型选型质量 —— 写清"什么时候用"比写"是什么"更有效。
WIDGET_PURPOSE: dict[str, str] = {
    "distribution_explorer": "画某个分布的 pdf/cdf。学生问“这个分布长什么样”“参数变了会怎样”时用。",
    "hypothesis_test": "画零分布 + 拒绝域 + 观测统计量 + p 值面积。讲 p 值含义、讲某次具体检验结论时用。",
    "sampling_distribution": "模拟抽样分布。讲中心极限定理、讲“为什么样本均值近似正态”时用。",
    "confidence_interval": "画多条 CI 并标出未覆盖真值的那些。纠正“95% 概率落在区间内”这个误解时用。",
    "power_curve": "画功效随样本量/效应量/α 的变化。讲检验效能、算样本量时用。",
    "scatter_regression": "散点 + 拟合线。讲相关、回归、相关不等于因果时用（需要用户给出数据）。",
    "data_plot": "画原始数据的直方图/箱线图。用户给了数据、需要先看分布形状时用。",
    "effect_size": "并排比较多个效应量及其 CI。强调“别只看 p 值”时用。",
    "function_plot": "画一次/二次函数图像，标出零点、顶点、对称轴与判别式。"
                     "学生问函数图像、方程解的个数、最值、抛物线与 x 轴交点时用。",
}


class ArtifactSpec(BaseModel):
    """一个可渲染的可视化件。

    caption 是必需的：图必须自带解释。一张没有说明的统计图容易被误读，
    而误读统计图正是这个产品要解决的问题。
    """

    model_config = ConfigDict(extra="forbid")

    kind: str
    title: str = Field(min_length=1, max_length=120)
    caption: str = Field(min_length=1, max_length=600)
    params: dict[str, Any]

    @field_validator("kind")
    @classmethod
    def _known_kind(cls, v: str) -> str:
        if v not in WIDGET_REGISTRY:
            raise ValueError(
                f"未知的 widget kind: {v!r}。可用: {sorted(WIDGET_REGISTRY)}"
            )
        return v

    def validated_params(self) -> _Base:
        """按 kind 校验 params，返回类型化对象。"""
        model = WIDGET_REGISTRY[self.kind]
        return model.model_validate(self.params)

    def as_dict(self) -> dict[str, Any]:
        """给前端的载荷。params 走校验后的 dump，剔除多余字段。"""
        return {
            "kind": self.kind,
            "title": self.title,
            "caption": self.caption,
            "params": self.validated_params().model_dump(mode="json"),
        }


def validate_artifact_dict(raw: Any) -> ArtifactSpec:
    """把模型输出的原始 dict 变成校验过的 ArtifactSpec。

    失败一律抛 ArtifactValidationError（而不是让 pydantic 的
    ValidationError 冒到上层），这样调用方只需要 catch 一种异常，
    降级逻辑不会因为异常类型漏判而崩掉整个回答。
    """
    if not isinstance(raw, dict):
        raise ArtifactValidationError(f"artifact 必须是对象，得到 {type(raw).__name__}")
    try:
        spec = ArtifactSpec.model_validate(raw)
        spec.validated_params()
    except ValidationError as exc:
        raise ArtifactValidationError(_format_errors(exc)) from exc
    except ValueError as exc:
        raise ArtifactValidationError(str(exc)) from exc
    return spec


def _format_errors(exc: ValidationError) -> str:
    parts = []
    for err in exc.errors()[:6]:
        loc = ".".join(str(p) for p in err.get("loc", ())) or "(根)"
        parts.append(f"{loc}: {err.get('msg', '无效')}")
    return "; ".join(parts)


def build_artifact(kind: str, title: str, caption: str, **params: Any) -> ArtifactSpec:
    """代码侧构造 artifact 的便捷入口（skill 用，不经过模型）。"""
    return validate_artifact_dict(
        {"kind": kind, "title": title, "caption": caption, "params": params}
    )


def describe_widgets_for_prompt(kinds: list[str] | None = None) -> str:
    """生成给模型看的 widget 清单（含参数 schema 摘要）。

    只列必填字段与枚举取值 —— 完整 JSON Schema 太长会挤占上下文，
    而模型真正需要知道的是"有哪些 kind""每个 kind 必须给什么"。
    """
    names = kinds if kinds is not None else sorted(WIDGET_REGISTRY)
    lines: list[str] = []
    for name in names:
        model = WIDGET_REGISTRY.get(name)
        if model is None:
            continue
        lines.append(f"- {name}: {WIDGET_PURPOSE.get(name, '')}")
        schema = model.model_json_schema()
        required = set(schema.get("required", ()))
        fields = []
        for field, meta in schema.get("properties", {}).items():
            enum = meta.get("enum")
            if enum is None:
                for variant in meta.get("anyOf", ()):
                    if "enum" in variant:
                        enum = variant["enum"]
                        break
            hint = "|".join(str(e) for e in enum) if enum else _type_hint(meta)
            mark = "*" if field in required else ""
            fields.append(f"{field}{mark}: {hint}")
        lines.append(f"    参数: {', '.join(fields)}")
    lines.append("  (带 * 的是必填；未列出的字段不要写，会被拒绝)")
    return "\n".join(lines)


def _type_hint(meta: dict[str, Any]) -> str:
    t = meta.get("type")
    if t == "array":
        return "数组"
    if t in ("number", "integer"):
        return "数值"
    if t == "boolean":
        return "true|false"
    if t == "string":
        return "字符串"
    if t == "object":
        return "对象"
    if "anyOf" in meta:
        return "数值或 null"
    return "值"
