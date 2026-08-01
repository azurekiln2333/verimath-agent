"""Tier 2 可视化件选型：规则未命中时，让模型按 widget 清单生成 spec。

与 planner.py 的 Tier 1（确定性规则）互补：
- Tier 1 命中率 100% 但覆盖面有限（18 条规则只能覆盖核心教学场景）。
- Tier 2 用模型兜底任意知识点诉求（如"贝叶斯先验后验""核密度估计"），
  但成功率不稳定，所以只在 Tier 1 未命中时介入。

设计原则与 planner 一致：**任何失败都静默降级为 PlanResult(None)**。
上层（main.answer_query）无需感知 Tier 1/Tier 2 的区别，只看 PlanResult.hit。
配图是增强，不是回答的前提 —— 画错的图比不配图更有害，所以宁可不出图。

为什么是异步：模型调用是 I/O，而 router.answer 是同步的（被测试直接调用，
签名不能改）。所以 Tier 2 必须在 main.py 的异步路径触发，不能进 router。
"""

from __future__ import annotations

import json
import re
from typing import Any

from app.artifacts.planner import PlanResult
from app.artifacts.spec import (
    ArtifactValidationError,
    describe_widgets_for_prompt,
    validate_artifact_dict,
)
from app.model_client import ModelMessage, OpenAICompatibleClient


async def generate_spec(
    query: str,
    route: str,
    model_client: OpenAICompatibleClient,
    history: list[ModelMessage] | None = None,
) -> PlanResult:
    """规则未命中时，让模型按 widget 清单生成一个 artifact spec。

    返回 PlanResult：命中则带 spec，未命中/失败则 spec=None。
    与 plan_artifact 的未命中行为完全一致，调用方无需区分 Tier。
    """
    if not model_client.enabled or route == "guard":
        return PlanResult(None, "tier2:disabled")
    if not query or not query.strip():
        return PlanResult(None, "tier2:empty")

    widget_catalog = describe_widgets_for_prompt()
    system = (
        "你是统计可视化选型助手。根据学生问题选一个最合适的可交互 widget，"
        "帮助学生建立直觉。输出一个 JSON 对象，字段：kind、title、caption、params。\n"
        "- kind 必须是下列之一；params 必须符合该 widget 的参数 schema。\n"
        "- title 是图标题（≤40 字）；caption 是图的自解释文字（说明学生该看什么、能拖什么）。\n"
        "- 尽量在 params.interactive 里列出可调参数，让学生能拖动看变化。\n"
        "- 如果问题不适合配图（如纯概念定义、作业代写、学习路线），输出 {\"kind\": null}。\n"
        "- 只输出 JSON，不要代码、不要解释、不要 Markdown 代码块包裹。\n\n"
        f"可用 widget 清单：\n{widget_catalog}"
    )
    user = f"学生问题：{query}\n路由能力：{route}"
    messages = [
        ModelMessage(role="system", content=system),
        *(history or []),
        ModelMessage(role="user", content=user),
    ]

    try:
        raw = await model_client.complete(messages)
    except Exception:
        # 模型调用失败绝不影响文字回答 —— 文字答案已由 router 给出
        return PlanResult(None, "tier2:model_error")

    parsed = _extract_json(raw)
    if parsed is None:
        return PlanResult(None, "tier2:unparseable")
    if parsed.get("kind") is None:
        # 模型主动判断不宜配图 —— 这是正确行为，不是失败
        return PlanResult(None, "tier2:declined")

    try:
        spec = validate_artifact_dict(parsed)
    except ArtifactValidationError as exc:
        return PlanResult(None, f"tier2:invalid:{str(exc)[:120]}")
    except Exception:
        return PlanResult(None, "tier2:invalid")

    return PlanResult(spec, "tier2:model")


_JSON_OBJECT_RE = re.compile(r"\{.*\}", re.DOTALL)


def _extract_json(raw: str) -> dict[str, Any] | None:
    """从模型输出里提取 JSON 对象。容忍 ```json``` 包裹与前后多余文字。

    模型经常无视"不要代码块包裹"的指令，所以必须容错。
    """
    if not raw:
        return None
    text = raw.strip()
    # 优先：```json ... ``` 或 ``` ... ``` 包裹
    fenced = re.search(r"```(?:json)?\s*(\{.*?\})\s*```", text, re.DOTALL)
    candidate = fenced.group(1) if fenced else text
    try:
        obj = json.loads(candidate)
        if isinstance(obj, dict):
            return obj
    except json.JSONDecodeError:
        pass
    # 回退：抓整段里第一个 {...} 片段（贪婪到最后一个 }，容忍中间嵌套）
    m = _JSON_OBJECT_RE.search(text)
    if m:
        try:
            obj = json.loads(m.group(0))
            if isinstance(obj, dict):
                return obj
        except json.JSONDecodeError:
            return None
    return None
