# -*- coding: utf-8 -*-
"""courseware：课件/讲义生成技能（七段式，副产品 B）。

结构（GateCraft 写作范式的教学化改造——每段有判定标准，不是套模板）：
  1. 动机问题   —— 一个真实问题引入，不写"本节我们学习"
  2. 定义与记号 —— 形式定义 + 每个符号的直觉
  3. 定理与条件 —— 定理陈述 + 条件逐条解释 + 违反时会怎样
  4. 例子与计算 —— 例题含数值，数值可验算时必须过内核
  5. 常见误区   —— 至少 2 条，每条给反例
  6. 练习       —— 2-3 道分层练习（不给答案，给提示）
  7. 小结       —— 三句话以内 + 下一步学什么

生成管线：模型结构化 JSON → LaTeX 自检（失败回喂 1 次）→ 例题数值验算
（answer_check 可解析时过内核）→ 渲染 Markdown。
"""
from __future__ import annotations

import json
import re
from dataclasses import dataclass, field
from typing import Any

from app.model_client import ModelMessage, OpenAICompatibleClient
from app.render.latex_lint import lint_latex

SECTION_IDS = (
    ("motivation", "动机问题"),
    ("definition", "定义与记号"),
    ("theorem", "定理与条件"),
    ("example", "例子与计算"),
    ("pitfalls", "常见误区"),
    ("exercises", "练习"),
    ("summary", "小结"),
)


@dataclass(frozen=True)
class Courseware:
    topic: str
    sections: tuple[dict[str, str], ...] = field(default_factory=tuple)
    self_check_ok: bool = True
    self_check_issues: tuple[str, ...] = field(default_factory=tuple)
    example_verified: bool | None = None   # None = 无可验算数值
    verification_note: str = ""
    source: str = "template"


_TEMPLATE_FALLBACK = (
    "结论先行：课件生成需要模型支持（当前离线）。\n\n"
    "离线时我能做的是：给出七段式课件骨架，你填内容——\n"
    "1. 动机问题：这个概念解决什么真实问题？\n"
    "2. 定义与记号：形式定义 + 每个符号的直觉\n"
    "3. 定理与条件：定理陈述 + 条件逐条解释 + 违反时会怎样\n"
    "4. 例子与计算：一道带数值的例题\n"
    "5. 常见误区：至少 2 条，每条配反例\n"
    "6. 练习：2-3 道分层练习\n"
    "7. 小结：三句话 + 下一步\n\n"
    "开启模型后重新发送主题，我按此结构生成完整课件。"
)


def generate_courseware(topic: str = "") -> Courseware:
    """离线兜底：骨架指引（模型关闭/失败时保证输出可用）。"""
    return Courseware(topic=topic or "未指定主题", source="template",
                      sections=tuple({"id": sid, "title": title, "content": ""}
                                     for sid, title in SECTION_IDS))


async def generate_courseware_with_model(
    topic: str,
    model_client: OpenAICompatibleClient | None = None,
    history: list[ModelMessage] | None = None,
) -> tuple[Courseware, str]:
    """模型生成课件，返回 (Courseware, 渲染好的 Markdown)。

    LaTeX 自检失败回喂 1 次；例题 answer_check 可解析时过内核验算。
    全部失败回退骨架模板。
    """
    if model_client is None or not model_client.enabled or not topic.strip():
        cw = generate_courseware(topic)
        return cw, _TEMPLATE_FALLBACK
    from app.skills._json_utils import extract_json_object as _extract_json_object
    from app.linalg.tool import verify_answer

    feedback = ""
    for _attempt in range(2):
        try:
            raw = await _ask_model(topic, model_client, history, feedback)
        except Exception:
            break
        obj = _extract_json_object(raw)
        if obj is None:
            feedback = "上次输出不是合法 JSON。只输出一个 JSON 对象，不要代码块包裹。"
            continue
        cw = _courseware_from_json(topic, obj)
        if cw is None:
            feedback = "缺少 problem 或 sections 字段，或 sections 不完整。按七段式补全。"
            continue
        if not cw.self_check_ok:
            feedback = "LaTeX 自检未通过：公式必须用 \\(...\\) 行内、$$...$$ 独立块。"
            continue
        check = obj.get("answer_check") if isinstance(obj.get("answer_check"), dict) else None
        if check:
            ok, actual = verify_answer(
                check.get("operation", ""), check.get("matrix", []),
                check.get("expected", ""), b=check.get("b"),
            )
            note = ("例题数值已过内核复算。" if ok
                    else f"例题声称答案 {check.get('expected')} 与内核复算 {actual} 不一致。")
            from dataclasses import replace
            cw = replace(cw, example_verified=ok, verification_note=note)
        return cw, render_courseware_md(cw)
    return generate_courseware(topic), _TEMPLATE_FALLBACK


async def _ask_model(topic: str, model_client: OpenAICompatibleClient,
                     history: list[ModelMessage] | None, feedback: str) -> str:
    sections_desc = "\n".join(f'    {{"id": "{sid}", "title": "{title}", "content": "..."}},'
                              for sid, title in SECTION_IDS)
    system = (
        "你是大学数学课件作者。按七段式生成课件，输出 JSON："
        '{"topic": "...", "sections": [...]，每段 {"id", "title", "content"}，'
        'id 顺序必须是：' + ", ".join(sid for sid, _ in SECTION_IDS) + "。\n"
        "各段判定标准：\n"
        "1. motivation：以一个具体真实问题开头，禁止“本节我们学习”。\n"
        "2. definition：形式定义 + 每个符号一句话直觉。\n"
        "3. theorem：定理陈述 + 条件逐条解释 + 每条条件违反时的一个反例。\n"
        "4. example：一道完整例题，数值精确；有确定数值答案时输出顶层 answer_check 对象："
        '{"operation": "det|rank|inverse|rref|solve|eigen|jordan|quadratic_form", "matrix": [[...]], "expected": "答案", "b": [..]}。\n'
        "5. pitfalls：至少 2 条误区，每条带反例。\n"
        "6. exercises：2-3 道分层练习，只给提示不给答案。\n"
        "7. summary：不超过三句话 + 下一步。\n"
        "公式一律 \\(...\\) 行内、$$...$$ 独立块。只输出 JSON。\n"
        "sections 示例结构：\n" + sections_desc
    )
    messages = [
        ModelMessage(role="system", content=system),
        *(history or []),
        ModelMessage(role="user", content=f"课件主题：{topic}"),
    ]
    if feedback:
        messages.append(ModelMessage(role="user", content=f"纠错要求：{feedback}"))
    return await model_client.complete(messages, response_format={"type": "json_object"})


def _courseware_from_json(topic: str, obj: dict[str, Any]) -> Courseware | None:
    sections_raw = obj.get("sections")
    if not isinstance(sections_raw, list):
        return None
    by_id = {s.get("id"): s for s in sections_raw if isinstance(s, dict)}
    sections: list[dict[str, str]] = []
    all_text: list[str] = []
    for sid, title in SECTION_IDS:
        s = by_id.get(sid)
        if not s or not str(s.get("content", "")).strip():
            return None
        content = str(s["content"]).strip()
        sections.append({"id": sid, "title": str(s.get("title") or title), "content": content})
        all_text.append(content)
    issues_list = lint_latex("\n".join(all_text))
    return Courseware(
        topic=str(obj.get("topic", topic) or topic),
        sections=tuple(sections),
        self_check_ok=not issues_list,
        self_check_issues=tuple(f"{i.kind}: {i.detail}" for i in issues_list),
        source="model",
    )


def render_courseware_md(cw: Courseware) -> str:
    if cw.source == "template":
        return _TEMPLATE_FALLBACK
    lines = [f"# {cw.topic} · 学习讲义", ""]
    for s in cw.sections:
        lines.append(f"## {s['title']}")
        lines.append("")
        lines.append(s["content"])
        lines.append("")
    if cw.example_verified is True:
        lines.append("> ✅ 例题数值已通过计算内核独立复算。")
    elif cw.example_verified is False:
        lines.append(f"> ⚠️ {cw.verification_note} 请人工复核例题。")
    return "\n".join(lines)
