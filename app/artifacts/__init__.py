"""可视化件（artifact）的类型化契约。

分层理由：LLM 只输出**一份被校验过的参数 spec**，绝不输出可执行代码。
渲染由前端预置的 widget 负责。这样做的代价是能表达的图形有限，
换来的是：

1. 不会因为模型写错一行 JS 就白屏 —— spec 校验失败可以降级为纯文字。
2. 参数是结构化的，可以进 trace、可以复现、可以被测试断言。
3. 无需在生产路径上执行模型生成的代码（Tier 2 沙箱是独立的、可关的）。

对模型能力的现实假设：让模型填 12 个字段的 JSON，成功率远高于让它写
40 行无 bug 的 canvas 代码。所以默认路径走 Tier 1（预置 widget）。
"""

from app.artifacts.spec import (
    ArtifactSpec,
    ArtifactValidationError,
    WIDGET_REGISTRY,
    build_artifact,
    describe_widgets_for_prompt,
    validate_artifact_dict,
)

__all__ = [
    "ArtifactSpec",
    "ArtifactValidationError",
    "WIDGET_REGISTRY",
    "build_artifact",
    "describe_widgets_for_prompt",
    "validate_artifact_dict",
]
