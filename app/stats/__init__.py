"""统计计算层：纯 Python、零第三方依赖的权威计算。

分三块：
- distributions  分布的 pdf / cdf / sf / ppf
- tests          假设检验（返回统计量、p 值、置信区间、效应量）
- power          功效与样本量
- rng            可复现随机数与采样器

与 app/static/statlib.js 逐函数对齐，跨语言 parity 由测试保证。
"""

from app.stats import distributions, power, rng, tests

__all__ = ["distributions", "power", "rng", "tests"]
