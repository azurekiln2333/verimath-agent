"""canvas_builder skill：让模型生成自包含 HTML 可视化组件（Canvas 模式）。

突破 8 个固定 widget 的表达力上限：模型输出一个完整的 HTML 文档（内联 CSS/JS、
可用 SVG/<canvas>），前端在 sandbox iframe 中渲染，安全隔离。

三层保障（Part D 升级）：
1. 脚手架：若查询命中预制模板（canvas_templates.match_template），把模板 HTML 作为
   「参考实现示例」注入 system prompt，引导模型生成同风格/同交互模式的组件。
2. 模型生成：模型仍自行生成（参考但不照抄模板）。
3. 兜底：模型生成失败（解析为空 / 清洗后为空 / 异常 / 模型关闭）且命中模板时，
   直接用模板 HTML 构造 spec 返回，保证「该有的可视化不丢」。

失败降级：模型关闭且未命中模板 → 返回 None，上层静默跳过。
"""
from __future__ import annotations

import re
import logging
from html.parser import HTMLParser
from typing import Any

from app.model_client import ModelMessage, OpenAICompatibleClient
from app.skills.canvas_templates import (
    get_template_html,
    match_template,
    template_meta,
)

# 单个 HTML 组件的长度上限（字符），防止模型滥用导致前端卡顿
_MAX_HTML_LEN = 200_000

_SYSTEM_PROMPT = (
    "你是数学与统计可视化组件工程师。根据需求生成一个自包含的 HTML 可视化组件，"
    "用于帮助统计学本科生建立直觉。\n\n"
    "硬性要求：\n"
    "1. 输出一个完整的 HTML 文档（<html>...<style>...<body>...<script>...），所有 CSS/JS 必须内联，"
    "不得引用任何外部资源（无 <link>、无 <script src>、无外链图片/字体）。\n"
    "2. 可用 SVG、<canvas>、原生 JS；不得使用任何第三方库（无 d3/chart.js/three 等）。\n"
    "3. 适配 320-1100px 可变宽容器，高度由内容决定，不用 100vh 或固定大高度。背景透明，中文无衬线字体，文字用 var(--vm-ink,#242a27)，主色 var(--vm-accent,#365b46)，背景 var(--vm-bg,#fdfdfb)。统一浅灰边框、12px圆角，避免渐变背景与大装饰标题。\n"
    "绘图区高度优先280–360px，手机220–280px，不按整屏宽度铺成巨大的正方形。坐标等比例通过留白实现；把主要参数放在图上方或紧邻图，使打开卡片就能操作。\n"
    "4. 必须可交互：用滑块/按钮让用户改变参数并实时看到变化。可变参数使用带标签的原生 input/select；"
    "若有拖动点，提供坐标输入控件并与拖动双向同步，让键盘和触屏也能操作，宿主才能恢复参数。\n"
    "5. 数学公式用易读Unicode或 SVG 绘制，不要显示LaTeX源码、反引号或代码字体，不要依赖 KaTeX/MathJax（iframe 内没有这些库）。\n"
    "6. 代码要稳健：边界值不报错，参数变化即时重绘。用 ResizeObserver 监听内容容器宽度重绘 canvas，同时调整像素分辨率。数据不足时标注示例数据。不要自行发送高度消息，由宿主注入的桥接脚本统一测量。\n\n"
    "ResizeObserver 回调只处理宽度变化，宽度未变立即返回，用 requestAnimationFrame 合并重绘，避免在观察回调内循环修改尺寸。"
    "7. 优先解决本轮学生的具体困惑，不把所有知识点堆到一张图。几何坐标须等比例，标清点、向量及位移的角色。"
    "竖直切线用隐式直线表示；零向量的夹角未定义。用法向量与位移点积解释切线时，测试点Q必须能在平面自由移动，"
    "不能限制在原曲线上，否则无法展示切线上的其他点与点积的正负。曲线上的点与切线测试点角色不同，若同时出现要用不同符号。"
    "坐标控件输入的值应忠实保留，不能未经说明投影或吸附回曲线。换元中面积缩放用雅可比绝对值，"
    "扇形或小平行四边形对面积元的解释需标明是局部近似，不能把有限块近似说成精确等式。\n\n"
    "输出格式（严格）：先一行 `TITLE: 标题`，再一行 `CAPTION: 说明`，"
    "然后一个 ```html 代码块，其余什么都不要输出。"
)

# 脚手架后缀：命中模板时追加到 system prompt，作为风格/交互参考（不要照抄）
_SCAFFOLD_SUFFIX = (
    "\n\n参考实现示例（仅作风格与交互模式参考，请基于需求自行生成，不要直接照抄）：\n"
    "参考标题：{ref_title}\n"
    "```html\n{ref_html}\n```\n"
    "请在参考上述风格的基础上，针对本次需求生成更贴合的组件。"
)


def _sanitize_html(html: str) -> str:
    """安全清洗：剥离外链脚本、外链资源、危险的跨域访问。"""
    # 移除外链 <script src=...>
    html = re.sub(r"<script[^>]*\bsrc\s*=[^>]*>.*?</script>", "", html, flags=re.IGNORECASE | re.DOTALL)
    # 移除 <link rel=stylesheet href=...>（外链样式）
    html = re.sub(r"<link[^>]*\bhref\s*=[^>]*>", "", html, flags=re.IGNORECASE)
    # 移除 @import 与 url() 外链
    html = re.sub(r"@import\s+[^;]+;", "", html, flags=re.IGNORECASE)
    html = re.sub(r"url\(\s*['\"]?https?://[^)]+\)", "none", html, flags=re.IGNORECASE)
    # 跨域访问由宿主的 sandbox 与 CSP 限制，不用字符串替换破坏合法 JavaScript。
    return html


def _extract(html_doc: str) -> tuple[str, str, str] | None:
    """从模型输出解析 (title, caption, html)。"""
    title = "自定义可视化"
    caption = "模型生成的可交互 HTML 组件"
    m_title = re.search(r"TITLE:\s*(.+)", html_doc)
    if m_title:
        title = m_title.group(1).strip()[:60]
    m_cap = re.search(r"CAPTION:\s*(.+)", html_doc)
    if m_cap:
        caption = m_cap.group(1).strip()[:120]
    # 提取 ```html ... ``` 代码块；若无围栏，退而提取 <html>...</html>
    m_code = re.search(r"```html\s*(.*?)```", html_doc, re.IGNORECASE | re.DOTALL)
    if m_code:
        html = m_code.group(1).strip()
    else:
        m_html = re.search(r"(<html[\s\S]*</html>)", html_doc, re.IGNORECASE)
        if m_html:
            html = m_html.group(1).strip()
        else:
            return None
    if "<" not in html:
        return None
    return title, caption, html


class _DocumentShape(HTMLParser):
    def __init__(self) -> None:
        super().__init__()
        self.opened: set[str] = set()
        self.closed: set[str] = set()
        self.scripts = 0

    def handle_starttag(self, tag, attrs):
        self.opened.add(tag)
        if tag == "script":
            self.scripts += 1

    def handle_endtag(self, tag):
        self.closed.add(tag)
        if tag == "script":
            self.scripts -= 1


def validate_canvas(spec: dict[str, Any]) -> dict[str, Any]:
    """Canvas has an HTML contract, separate from parameterized native widgets."""
    html = spec.get("html")
    if spec.get("kind") != "html_canvas" or not isinstance(html, str) or not html.strip() or len(html) > _MAX_HTML_LEN:
        raise ValueError("未生成有效的 HTML Canvas")
    shape = _DocumentShape()
    shape.feed(html)
    if not {"html", "body"} <= shape.opened & shape.closed or shape.scripts != 0:
        raise ValueError("HTML 文档未完整闭合，请重新生成完整组件")
    return {**spec, "html": _sanitize_html(html),
            "title": str(spec.get("title") or "交互式可视化")[:120],
            "caption": str(spec.get("caption") or "模型生成的交互式示意")[:600],
            "height": max(120, min(1000, int(spec.get("height", 420))))}


def _template_fallback(tpl_key: str, query: str) -> dict[str, Any] | None:
    """模板兜底：模型不可用/失败时，用预制模板 HTML 构造 spec。失败返回 None。"""
    html = get_template_html(tpl_key, query)
    meta = template_meta(tpl_key)
    if not html:
        return None
    html = _sanitize_html(html)
    if not html or len(html) > _MAX_HTML_LEN:
        return None
    title = meta[0] if meta else "自定义可视化"
    caption = (meta[1] if meta else "模板兜底组件") + "（模板兜底）"
    return {
        "kind": "html_canvas",
        "title": title,
        "caption": caption,
        "html": html,
        "height": 420,
        "fallback_template": tpl_key,
        "generation_source": "template",
    }


async def _model_generate(
    query: str,
    context_hint: str,
    model_client: OpenAICompatibleClient,
    tpl_key: str | None,
) -> dict[str, Any] | None:
    """模型生成路径：命中模板时把模板 HTML 作为脚手架示例注入 prompt。失败返回 None。"""
    system = _SYSTEM_PROMPT
    if tpl_key:
        ref_html = get_template_html(tpl_key, query) or ""
        meta = template_meta(tpl_key)
        ref_title = meta[0] if meta else ""
        # 截断参考 HTML，避免 prompt 过长（前 3000 字符已足够展示风格与交互骨架）
        system += _SCAFFOLD_SUFFIX.format(ref_title=ref_title, ref_html=ref_html[:3000])
    user = f"可视化需求：{query}\n"
    if context_hint:
        user += f"上下文：{context_hint}\n"
    user += "\n请生成组件。"
    messages = [
        ModelMessage(role="system", content=system),
        ModelMessage(role="user", content=user),
    ]
    for attempt in range(2):
        try:
            raw = await model_client.complete(
                messages, response_format=None, thinking=False, temperature=0.2,
                timeout=90 if attempt == 0 else 60,
            )
        except RuntimeError as exc:
            if str(exc) != "model_output_incomplete":
                return None
            raw = ""
        except Exception as exc:
            logging.getLogger(__name__).warning("Canvas model request failed: %s (status=%s)",
                type(exc).__name__, getattr(getattr(exc, "response", None), "status_code", None))
            return None
        parsed = _extract(raw or "")
        try:
            if parsed is None:
                raise ValueError("未收到完整 HTML 文档")
            title, caption, html = parsed
            return validate_canvas({"kind": "html_canvas", "title": title, "caption": caption,
                "html": html, "height": 420, "generation_source": "model"})
        except ValueError as exc:
            if attempt == 0:
                # One bounded repair for malformed output; network failures remain user-retryable.
                messages.append(ModelMessage(role="user", content=(
                    f"上次输出未通过完整性检查：{exc}。请根据原需求重新生成更精简的完整文档。"
                    "减少装饰和说明，保留核心交互，务必闭合 script、body 和 html。仍按 TITLE/CAPTION/html 代码块格式输出。")))
    return None


async def build(
    query: str,
    context_hint: str,
    model_client: OpenAICompatibleClient,
) -> dict[str, Any] | None:
    """生成一个 html_canvas 组件 spec。失败返回 None。

    优先级：模型生成（带模板脚手架）> 模板兜底（模型失败/关闭且命中模板）> None。
    """
    if not query.strip():
        return None
    tpl_key = match_template(query)

    # 1) 模型可用：尝试模型生成（命中模板时注入脚手架示例）
    if model_client.enabled:
        spec = await _model_generate(query, context_hint, model_client, tpl_key)
        if spec is not None:
            return spec
        # 模型生成失败 → 落到模板兜底

    # 2) 模板兜底：模型关闭 或 模型生成失败
    if tpl_key:
        return _template_fallback(tpl_key, query)

    # 3) 既无模型命中也无模板兜底
    return None
