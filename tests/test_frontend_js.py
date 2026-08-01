"""把 JS 侧的测试挂进 pytest，让 `pytest` 一条命令覆盖前后端。

不重复实现断言 —— 断言写在 tests/*_runner.js 里（那边能直接 require
被测模块），这里只负责跑它、把失败输出转述给 pytest。
"""

from __future__ import annotations

import shutil
import subprocess
from pathlib import Path

import pytest

_HERE = Path(__file__).parent
_ROOT = _HERE.parent


def _run_node(script: Path) -> subprocess.CompletedProcess:
    node = shutil.which("node")
    if node is None:
        pytest.skip("未安装 node，跳过前端测试（装了就必须过）")
    return subprocess.run(
        [node, str(script)],
        capture_output=True,
        text=True,
        timeout=120,
        cwd=str(_ROOT),
        encoding="utf-8",
    )


def test_plot_js_pure_functions() -> None:
    """plot.js 的坐标映射、刻度算法、分箱与绘图冒烟测试。"""
    proc = _run_node(_HERE / "plot_runner.js")
    assert proc.returncode == 0, f"plot.js 测试失败:\n{proc.stdout}\n{proc.stderr}"
    assert "OK" in proc.stdout


def test_statlib_js_loads_without_dom() -> None:
    """statlib.js 必须能在无 DOM 环境加载 —— parity 测试与 node 端复用都靠这点。"""
    script = _HERE / "statlib_smoke.js"
    proc = _run_node(script)
    assert proc.returncode == 0, f"statlib.js 冒烟失败:\n{proc.stdout}\n{proc.stderr}"


def test_widgets_render_headlessly() -> None:
    """用 DOM 桩把每个 widget 真渲染一遍。

    抓的是真缺陷而不是语法：NaN 坐标（在浏览器里表现为静默空白图）、
    save/restore 失衡、缺 aria-label、参数变化后崩溃。
    已用注入变异验证过这些断言确实会失败。
    """
    proc = _run_node(_HERE / "widgets_runner.js")
    assert proc.returncode == 0, f"widgets.js 测试失败:\n{proc.stdout}\n{proc.stderr}"
    assert "OK" in proc.stdout


def test_widget_registries_match_between_python_and_js() -> None:
    """两侧 widget 注册表必须一一对应。

    少了 JS 实现 → 后端过校验、前端白屏。
    多了 JS 实现 → 模型永远不会选它（后端会拒），是死代码。
    """
    from app.artifacts import WIDGET_REGISTRY

    script = _HERE / "widget_kinds.js"
    proc = _run_node(script)
    assert proc.returncode == 0, f"读取 JS 注册表失败:\n{proc.stderr}"
    js_kinds = set(proc.stdout.strip().split(","))
    py_kinds = set(WIDGET_REGISTRY)
    assert js_kinds == py_kinds, (
        f"注册表不匹配\n  仅 Python 有: {sorted(py_kinds - js_kinds)}"
        f"\n  仅 JS 有: {sorted(js_kinds - py_kinds)}"
    )


def test_planner_specs_match_js_control_ranges(tmp_path: Path) -> None:
    """planner 的每个 spec 都要能被 JS 控件正确接住。

    这个测试是补一个真实漏掉的 bug：planner 给 seed=20240607，
    而滑块范围 1..999，<input type=range> 静默夹到 999 —— 界面正常，
    但滑块值与渲染值不符，且「恢复初始参数」回不到初始图。

    之前的 widgets_runner 用自己写的 spec（seed 恰好在范围内），测不出来。
    """
    import json

    from app.artifacts.planner import _RULES, plan_artifact

    payload = []
    for rule_name, _pattern, factory in _RULES:
        spec = factory("")
        payload.append({"rule": rule_name, "spec": spec.as_dict()})
    assert payload, "应至少有一条规则"

    spec_file = tmp_path / "planner_specs.json"
    spec_file.write_text(json.dumps(payload, ensure_ascii=False), encoding="utf-8")

    node = shutil.which("node")
    if node is None:
        pytest.skip("未安装 node")
    proc = subprocess.run(
        [node, str(_HERE / "controls_parity_runner.js"), str(spec_file)],
        capture_output=True, text=True, timeout=120, cwd=str(_ROOT), encoding="utf-8",
    )
    assert proc.returncode == 0, (
        f"planner spec 与 JS 控件不一致:\n{proc.stdout}\n{proc.stderr}"
    )


def test_js_sources_have_no_syntax_errors() -> None:
    """对每个前端 JS 文件做一次语法检查。"""
    node = shutil.which("node")
    if node is None:
        pytest.skip("未安装 node")
    static = _ROOT / "app" / "static"
    targets = [p for p in static.glob("*.js")]
    assert targets, "app/static 下应有 JS 源文件"
    for path in targets:
        proc = subprocess.run(
            [node, "--check", str(path)],
            capture_output=True, text=True, timeout=60, encoding="utf-8",
        )
        assert proc.returncode == 0, f"{path.name} 语法错误:\n{proc.stderr}"
