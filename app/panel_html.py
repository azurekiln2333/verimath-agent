# -*- coding: utf-8 -*-
"""面板 HTML 装配器（Q2 批准：单字符串拆分为静态文件，2026-08 收口）。

源码在 app/static/ 下三个文件：
- panel.html：页面骨架（结构 + 资源引用）
- panel.css ：样式（原 <style> 块，1487 行）
- panel.js  ：脚本（原两个内联 <script> 块合并，1521 行）

本模块只做读取，PANEL_HTML 契约不变（端点 / 与 /dashboard 及既有测试依赖）。
CSS/JS 走 /static 静态托管；开发期改文件后刷新即可，无需重启（静态目录直读）。
"""
from __future__ import annotations

import hashlib
import re
from pathlib import Path

_STATIC_DIR = Path(__file__).resolve().parent / "static"

# 给 /static/ 引用加内容指纹。
# 为什么需要：改完样式表刷新页面，浏览器若仍命中旧缓存，用户看到的是
# "改了没生效"——旧 CSS 与旧 JS 并存时最难排查（例如裁切规则还在生效）。
# 用内容哈希而不是版本号：只有真改过的文件才换 URL，未改动的继续走缓存。
_STATIC_REF = re.compile(r'(src|href)="/static/([^"?#]+)"')


def _with_cache_bust(html: str) -> str:
    def stamp(match: "re.Match[str]") -> str:
        attr, rel = match.group(1), match.group(2)
        path = _STATIC_DIR / rel
        if not path.is_file():
            return match.group(0)
        digest = hashlib.sha1(path.read_bytes()).hexdigest()[:8]
        return f'{attr}="/static/{rel}?v={digest}"'

    return _STATIC_REF.sub(stamp, html)


PANEL_HTML = _with_cache_bust((_STATIC_DIR / "panel.html").read_text(encoding="utf-8"))
