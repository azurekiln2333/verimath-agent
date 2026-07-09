from __future__ import annotations

import re
from dataclasses import dataclass

# 常见数学命令：出现在数学环境外或代码块内都无法正确渲染
_MATH_COMMANDS = (
    r"\frac", r"\sum", r"\int", r"\prod", r"\sqrt", r"\bar", r"\hat",
    r"\alpha", r"\beta", r"\sigma", r"\mu", r"\pi", r"\cdot", r"\times",
    r"\leq", r"\geq", r"\infty", r"\partial", r"\nabla", r"\mathbb", r"\mathcal",
)

_FENCE_RE = re.compile(r"```.*?```", re.DOTALL)
_INLINE_CODE_RE = re.compile(r"`[^`\n]+`")


@dataclass(frozen=True)
class LatexIssue:
    kind: str          # unbalanced_inline | unbalanced_display | command_in_code | bare_command
    detail: str


def _strip_math_spans(text: str) -> str:
    """移除成对的 \\(...\\) 与 \\[...\\]，剩下的裸命令才算 bare。"""
    text = re.sub(r"\\\(.*?\\\)", " ", text, flags=re.DOTALL)
    text = re.sub(r"\\\[.*?\\\]", " ", text, flags=re.DOTALL)
    text = re.sub(r"\$\$.*?\$\$", " ", text, flags=re.DOTALL)
    text = re.sub(r"(?<!\\)\$[^$\n]+?(?<!\\)\$", " ", text)
    return text


def lint_latex(text: str) -> list[LatexIssue]:
    """静态检查答案文本的 LaTeX 可渲染性。不真渲染，仅供离线断言。"""
    issues: list[LatexIssue] = []
    text = text or ""

    # 1. 分隔符配对
    if text.count(r"\(") != text.count(r"\)"):
        issues.append(LatexIssue("unbalanced_inline", r"\( 与 \) 数量不匹配"))
    if text.count(r"\[") != text.count(r"\]"):
        issues.append(LatexIssue("unbalanced_display", r"\[ 与 \] 数量不匹配"))

    # 2. 数学命令误入代码块（围栏或行内 code）
    code_spans = _FENCE_RE.findall(text) + _INLINE_CODE_RE.findall(text)
    for span in code_spans:
        for cmd in _MATH_COMMANDS:
            if cmd in span:
                issues.append(LatexIssue("command_in_code", f"数学命令 {cmd} 出现在代码块中"))
                break

    # 3. 裸命令：数学命令出现在任何数学环境和代码块之外
    without_code = _INLINE_CODE_RE.sub(" ", _FENCE_RE.sub(" ", text))
    stripped = _strip_math_spans(without_code)
    for cmd in _MATH_COMMANDS:
        if cmd in stripped:
            issues.append(LatexIssue("bare_command", rf"数学命令 {cmd} 未包裹在 \(...\) 或 \[...\] 中"))

    return issues
