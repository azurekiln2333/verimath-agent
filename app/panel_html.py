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

from pathlib import Path

_STATIC_DIR = Path(__file__).resolve().parent / "static"

PANEL_HTML = (_STATIC_DIR / "panel.html").read_text(encoding="utf-8")
