"""面板侧 artifact 接线的结构性断言。

面板是一大段内联 HTML/JS，无法单元测试渲染结果，但**接线断了是静默的**：
少一个 script 标签就整块功能消失，而所有 Python 测试照样绿。
所以这里断言的是那些"断了不会报错"的连接点。
"""

from __future__ import annotations

import re
import shutil
import subprocess
from pathlib import Path

import pytest

from app.panel_html import PANEL_HTML

_ROOT = Path(__file__).parent.parent


def _panel_js() -> str:
    """面板脚本源码（app/static/panel.js，静态拆分后内联脚本已外置）。"""
    return (_ROOT / "app" / "static" / "panel.js").read_text(encoding="utf-8")


def _panel_css() -> str:
    """面板样式源码（app/static/panel.css）。"""
    return (_ROOT / "app" / "static" / "panel.css").read_text(encoding="utf-8")


def test_visualization_scripts_are_loaded_in_dependency_order() -> None:
    """statlib 必须在 plot/widgets 之前 —— 后两者在加载时就 require 它。"""
    order = [
        PANEL_HTML.index("/static/statlib.js"),
        PANEL_HTML.index("/static/plot.js"),
        PANEL_HTML.index("/static/widgets.js"),
    ]
    assert order == sorted(order), "脚本加载顺序错误：statlib 必须最先"


def test_all_visualization_scripts_exist_on_disk() -> None:
    """引用了不存在的文件 → 404 → 整块功能消失且无 Python 报错。"""
    for name in ("statlib.js", "plot.js", "widgets.js"):
        assert (_ROOT / "app" / "static" / name).is_file(), f"缺少 {name}"


def test_referenced_static_assets_all_exist() -> None:
    """把面板里所有 /static/ 引用都核对一遍。"""
    # 引用可能带内容指纹（?v=hash），核对磁盘前先剥掉查询串
    refs = set(re.findall(r'src="/static/([^"?]+)', PANEL_HTML))
    assert refs, "面板应引用静态资源"
    for ref in refs:
        assert (_ROOT / "app" / "static" / ref).is_file(), f"引用了不存在的资源: {ref}"


def test_visualizations_wait_for_complete_answer_and_user_action() -> None:
    """完整回答结束后提出候选，点击才启动独立任务。"""
    js = _panel_js()
    meta_block = js[
        js.index("if (evt.event === 'meta')"):
        js.index("} else if (evt.event === 'delta')")
    ]
    assert "renderArtifacts" not in meta_block
    assert "data.visualization_offers" in js
    tasks = (_ROOT / "app/static/artifact-tasks.js").read_text(encoding="utf-8")
    assert "action.addEventListener('click'" in tasks
    assert "post('/api/panel/artifact-jobs'" in tasks


def test_artifact_host_is_outside_the_streaming_bubble() -> None:
    """图的容器必须独立于文字气泡。

    流式阶段用 pending.textContent = acc 反复重写气泡内容，
    图若挂在气泡内会被每个 token 抹掉。
    现在它挂在「消息列」的伴随区（.msg-companion → .artifact-host）里：
    既不在气泡内，也和正文同列同宽，不再和正文分家。
    """
    js = _panel_js()
    assert "function ensureCompanion(col)" in js
    assert "const artifactHost = ensureCompanion(column)" in js
    assert "renderArtifactButton(artifactHost, offer)" in js
    assert "pending.appendChild(artifactHost)" not in js
    # 流式重写只发生在气泡本身
    assert "pending.textContent = acc" in js


def test_artifact_rendering_is_idempotent() -> None:
    """meta 与 final 都带 artifacts，重复渲染不能画出两份。"""
    assert "artifactsDone" in _panel_js(), "应有幂等标记"


def test_artifact_failure_degrades_gracefully() -> None:
    """渲染失败必须只影响图本身，并且上报。"""
    assert "artifact-error" in _panel_js() or "artifact-error" in _panel_css()
    assert "文字答案不受影响" in _panel_js()
    assert "reportRenderFail" in _panel_js()


def test_sliders_have_accessible_names() -> None:
    """无 aria-label 的 range 输入，屏幕阅读器只会读「滑块」。"""
    assert "input.setAttribute('aria-label', c.label)" in _panel_js()


def test_artifact_css_present() -> None:
    css = _panel_css()
    for cls in ("artifact-head", "artifact-caption", "artifact-controls",
                "artifact-note", "artifact-dual", "artifact-error"):
        assert f".{cls}" in css, f"缺少 {cls} 样式"


def test_slider_touch_target_and_focus_visible() -> None:
    """滑块是主要交互方式：触摸目标要够大，键盘焦点要可见。"""
    css = _panel_css()
    controls_css = css[
        css.index(".artifact-control input"):
        css.index(".artifact-reset")
    ]
    assert "min-height" in controls_css, "滑块应有最小触摸高度"
    assert "focus-visible" in controls_css, "滑块应有可见焦点样式"


def test_dual_layout_collapses_on_narrow_screens() -> None:
    """双图布局在窄屏必须堆叠，否则每张图挤成不可读的一半宽。"""
    css = _panel_css()
    assert "@media (max-width: 640px)" in css
    narrow = css[css.index("@media (max-width: 640px)"):]
    assert "artifact-dual" in narrow[:200]


def test_panel_js_has_valid_syntax() -> None:
    """panel.js 语法错误会让整个面板的 JS 全部失效。"""
    node = shutil.which("node")
    if node is None:
        pytest.skip("未安装 node")
    tmp = _ROOT / "build"
    tmp.mkdir(exist_ok=True)
    path = tmp / "_panel_syntax_check.js"
    try:
        path.write_text(_panel_js(), encoding="utf-8")
        proc = subprocess.run(
            [node, "--check", str(path)],
            capture_output=True, text=True, timeout=60, encoding="utf-8",
        )
        assert proc.returncode == 0, f"面板 JS 语法错误:\n{proc.stderr}"
    finally:
        path.unlink(missing_ok=True)
