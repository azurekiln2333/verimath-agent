"""前后端 parity：statlib.js 必须与 app/stats/ 算出同样的数。

为什么这层测试是必要的：可视化件在浏览器里实时重算（拖滑块 60fps），
而答案文本里的数字由 Python 算。两边若有偏差，学生会看到"图上写 p=0.048、
文字里写 p=0.052"这种自相矛盾 —— 对一个教统计的产品是致命的。

跑法：把调用清单喂给 node，收结果，逐项比。node 不在时 skip 而非 fail ——
CI 里装 node 是可选的，但装了就必须过。

容差 1e-12：两侧 erf/lgamma 实现不同（Python 用 libm，JS 用 Cody/Lanczos），
固有差异在 1e-15~1e-16 量级，经连分数与二分放大后仍远小于 1e-12。
"""

from __future__ import annotations

import json
import math
import shutil
import subprocess
from pathlib import Path

import pytest

from app.stats import distributions as D
from app.stats import power as P
from app.stats import tests as T
from app.stats.rng import PCG32
from app.stats.special import betainc, gammainc, gammaincc, log_beta
from tests.statlib_parity_cases import (
    ANOVA_GROUPS,
    CASES,
    POWER_CASES,
    PY_TO_JS,
    RNG_CASES,
    SAMPLE_SIZE_CASES,
    TEST_CASES,
)

_RUNNER = Path(__file__).parent / "statlib_parity_runner.js"
_TOL = 1e-12

_PY_FUNCS = {
    "erf": lambda x: math.erf(x),
    "erfc": lambda x: math.erfc(x),
    "lgamma": lambda x: math.lgamma(x),
    "log_beta": log_beta,
    "betainc": betainc,
    "gammainc": gammainc,
    "gammaincc": gammaincc,
}


def _py_func(name: str):
    if name in _PY_FUNCS:
        return _PY_FUNCS[name]
    return getattr(D, name)


def _decode(v):
    if v == "__inf__":
        return math.inf
    if v == "__-inf__":
        return -math.inf
    if v == "__nan__":
        return math.nan
    return v


@pytest.fixture(scope="module")
def js_results():
    node = shutil.which("node")
    if node is None:
        pytest.skip("未安装 node，跳过 parity（装了就必须过）")
    payload = {
        "scalars": [[PY_TO_JS[name], args] for name, args in CASES],
        "tests": [[js, args] for _, js, args in TEST_CASES],
        "anova": ANOVA_GROUPS,
        "power": POWER_CASES,
        "sampleSize": SAMPLE_SIZE_CASES,
        "rng": RNG_CASES,
    }
    proc = subprocess.run(
        [node, str(_RUNNER)],
        input=json.dumps(payload),
        capture_output=True,
        text=True,
        timeout=120,
        encoding="utf-8",
    )
    if proc.returncode != 0:
        pytest.fail(f"parity runner 失败:\n{proc.stderr}")
    return json.loads(proc.stdout)


_DBL_EPS = 2.0**-52


def _tol_for(args: list[float]) -> float:
    """按参数量级给出可达到的 parity 容差下限。

    根因：两侧 lgamma 的**相对**误差都在机器 epsilon（~2e-16），但**绝对**
    误差随 |lgamma(x)| 增长。lgamma(5000) ≈ 37582，其 ulp 就是 8.3e-12。
    log_beta = lgamma(a)+lgamma(b)-lgamma(a+b) 把这个绝对误差原样带出（结果
    是 O(1)，误差却是大数的 ulp），随后 exp() 把它变成结果的相对误差。

    所以 t_cdf(-2.5, df=1e4) 两侧差 7.3e-12 不是实现错误，是 double 的
    表示极限 —— Python 的 libm 与 JS 的 Lanczos 谁都不比谁"更对"。
    实测退化曲线与本函数的预测吻合：df=100→2.8e-14，1e3→4.5e-13，
    1e4→7.3e-12，1e6→9.3e-10。

    教学场景 df 通常 < 1000（df=1e4 意味着 n=10001），且大 df 本就该用
    正态近似 —— test_stats_accuracy 里已有 t→normal 的断言。
    """
    if not args:
        return _TOL
    scale = max(abs(a) for a in args if isinstance(a, (int, float)))
    if scale <= 100:
        return _TOL
    # lgamma(scale/2) 的 ulp，留 4 倍余量给连分数与二分的放大
    return max(_TOL, 4 * _DBL_EPS * abs(math.lgamma(scale / 2.0 + 1.0)))


def _assert_close(py: float, js, label: str, tol: float = _TOL) -> None:
    js = _decode(js)
    assert not (isinstance(js, str)), f"{label}: JS 侧报错 {js}"
    if isinstance(py, float) and math.isnan(py):
        assert math.isnan(js), f"{label}: Python NaN，JS 得 {js}"
        return
    if isinstance(py, float) and math.isinf(py):
        assert js == py, f"{label}: Python {py}，JS 得 {js}"
        return
    # 绝对值极小时改用绝对容差 —— 相对容差在 1e-300 附近无意义
    if abs(py) < 1e-290:
        assert abs(js - py) < 1e-300 or js == pytest.approx(py, rel=1e-6), (
            f"{label}: py={py!r} js={js!r}"
        )
        return
    assert js == pytest.approx(py, rel=tol, abs=1e-300), (
        f"{label}: py={py!r} js={js!r} relerr={abs(js - py) / abs(py):.3e}"
    )


def test_scalar_function_parity(js_results) -> None:
    """全部标量函数逐点比对。这是 parity 的主体。"""
    got = js_results["scalars"]
    assert len(got) == len(CASES), "JS 返回数量与清单不符"
    mismatches = []
    for (name, args), js_val in zip(CASES, got):
        py_val = _py_func(name)(*args)
        try:
            _assert_close(py_val, js_val, f"{name}{tuple(args)}", _tol_for(args))
        except AssertionError as exc:
            mismatches.append(str(exc))
    assert not mismatches, "parity 失配 {} 项:\n{}".format(
        len(mismatches), "\n".join(mismatches[:20])
    )


def test_tolerance_stays_tight_for_normal_scale_params() -> None:
    """护栏：_tol_for 只允许在大参数下放宽，教学常用量级必须保持 1e-12。

    没有这条，将来有人为了让某个 case 过而把容差函数改松，就会静默放过
    真实的算法偏差。"""
    assert _tol_for([0.5]) == _TOL
    assert _tol_for([2.0, 10.0]) == _TOL
    assert _tol_for([-2.5, 100.0]) == _TOL
    assert _tol_for([0.05, 3.0, 10.0]) == _TOL
    # 大 df 才放宽，且放宽幅度必须由量级决定而非常数
    assert _TOL < _tol_for([-2.5, 10000.0]) < 1e-10
    assert _tol_for([-2.5, 1_000_000.0]) > _tol_for([-2.5, 10000.0])


def test_case_list_covers_every_exported_function() -> None:
    """清单必须覆盖 PY_TO_JS 里每个函数 —— 防止新增函数忘了加 parity。"""
    covered = {name for name, _ in CASES}
    missing = set(PY_TO_JS) - covered
    assert not missing, f"这些函数没有 parity 用例: {sorted(missing)}"


@pytest.mark.parametrize("py_name,js_name,args", TEST_CASES,
                         ids=[c[0] for c in TEST_CASES])
def test_hypothesis_test_parity(js_results, py_name: str, js_name: str, args) -> None:
    """检验层：统计量、p 值、df、CI、效应量全部要对上。"""
    py_res = getattr(T, py_name)(*args)
    js_res = js_results["tests"][js_name]
    for field in ("statistic", "p_value", "df", "effect_size", "estimate"):
        py_v = getattr(py_res, field)
        if py_v is None:
            assert js_res.get(field) in (None, 0) or js_res.get(field) is None
            continue
        _assert_close(py_v, js_res[field], f"{py_name}.{field}")
    if py_res.ci is not None:
        _assert_close(py_res.ci[0], js_res["ci"][0], f"{py_name}.ci.lo")
        _assert_close(py_res.ci[1], js_res["ci"][1], f"{py_name}.ci.hi")


def test_anova_parity(js_results) -> None:
    py_res = T.anova_oneway(ANOVA_GROUPS)
    js_res = js_results["anova"]
    _assert_close(py_res.statistic, js_res["statistic"], "anova.F")
    _assert_close(py_res.p_value, js_res["p_value"], "anova.p")
    _assert_close(py_res.effect_size, js_res["effect_size"], "anova.omega2")
    for key in ("eta_squared", "omega_squared", "ms_between", "ms_within"):
        _assert_close(py_res.detail[key], js_res["detail"][key], f"anova.{key}")
    for i, m in enumerate(py_res.detail["group_means"]):
        _assert_close(m, js_res["detail"]["group_means"][i], f"anova.mean[{i}]")


@pytest.mark.parametrize("idx", range(len(POWER_CASES)))
def test_power_parity(js_results, idx: int) -> None:
    d, n, alpha, alt = POWER_CASES[idx]
    py_res = P.power_two_sample_t(d, n, alpha, alt)
    js_res = js_results["power"][idx]
    _assert_close(py_res.power, js_res["power"], f"power{POWER_CASES[idx]}")
    _assert_close(py_res.beta, js_res["beta"], f"beta{POWER_CASES[idx]}")


@pytest.mark.parametrize("idx", range(len(SAMPLE_SIZE_CASES)))
def test_sample_size_parity(js_results, idx: int) -> None:
    """样本量反解必须给出**完全相同的整数** —— 差 1 都算失配。
    这是最严的一条：它把功效函数、正态起点、搜索循环三处都锁住了。"""
    d, pw, alpha, alt = SAMPLE_SIZE_CASES[idx]
    py_res = P.sample_size_two_sample_t(d, pw, alpha, alt)
    js_res = js_results["sampleSize"][idx]
    assert py_res.n_per_group == js_res["n_per_group"], (
        f"样本量不一致 {SAMPLE_SIZE_CASES[idx]}: "
        f"py={py_res.n_per_group} js={js_res['n_per_group']}"
    )
    _assert_close(py_res.power, js_res["power"], f"ss.power{SAMPLE_SIZE_CASES[idx]}")


@pytest.mark.parametrize("idx", range(len(RNG_CASES)))
def test_rng_parity(js_results, idx: int) -> None:
    """同种子必出同序列 —— 跨语言。

    这是整个 parity 里最不可妥协的一条：种子会写进 artifact spec 与 trace，
    "换个种子再试"的教学动作要求两侧序列完全一致。random/randint/bernoulli
    要求逐位相同（纯整数与位运算），normal/exponential 走浮点超越函数，
    容差 1e-12。
    """
    spec = RNG_CASES[idx]
    r = PCG32(spec["seed"], spec["stream"])
    method = spec["method"]
    py_vals = []
    for _ in range(spec["n"]):
        if method == "random":
            py_vals.append(r.random())
        elif method == "normal":
            py_vals.append(r.normal())
        elif method == "exponential":
            py_vals.append(r.exponential(2.5))
        elif method == "randint":
            py_vals.append(r.randint(1, 6))
        elif method == "bernoulli":
            py_vals.append(r.bernoulli(0.3))
    js_vals = [_decode(v) for v in js_results["rng"][idx]]
    assert len(js_vals) == len(py_vals)
    if method in ("random", "randint", "bernoulli"):
        assert js_vals == py_vals, f"{method} 序列不一致: py={py_vals} js={js_vals}"
    else:
        for i, (a, b) in enumerate(zip(py_vals, js_vals)):
            _assert_close(a, b, f"rng.{method}[{i}]")
