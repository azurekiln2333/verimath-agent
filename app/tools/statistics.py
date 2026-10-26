"""Expose the existing statistical kernel; the model explains its results."""
from __future__ import annotations

import asyncio
import json

from app.stats import tests as stats
from app.tools.base import ToolResult


class CalculateStatisticsTool:
    name = "calculate_statistics"

    def schema(self):
        sample = {"type": "array", "items": {"type": "number"}, "minItems": 2, "maxItems": 2000}
        return {"type": "function", "function": {
            "name": self.name,
            "description": "根据用户明确提供的样本计算检验、置信区间和效应量。支持 Welch 独立样本、配对、单样本 t 检验和 Pearson 相关。不得编造或自行补齐数据。返回的 assumptions 为尚未验证的前提；解释时保留这些限制，不得只报告 p 值。",
            "parameters": {"type": "object", "properties": {
                "method": {"type": "string", "enum": ["welch_t", "paired_t", "one_sample_t", "pearson"]},
                "a": sample, "b": sample,
                "mu0": {"type": "number", "description": "单样本检验的明确原假设均值"},
                "alternative": {"type": "string", "enum": ["two-sided", "greater", "less"]},
                "ci_level": {"type": "number", "minimum": 0.8, "maximum": 0.999},
            }, "required": ["method", "a"]},
        }}

    async def run(self, method, a, b=None, mu0=None, alternative="two-sided", ci_level=0.95):
        if method == "one_sample_t":
            if mu0 is None:
                raise ValueError("单样本检验需要明确 mu0")
            args = (a, mu0)
        else:
            if b is None:
                raise ValueError("该方法需要第二组样本 b")
            args = (a, b)
        result = await asyncio.to_thread(getattr(stats, method), *args,
                                         alternative=alternative, ci_level=ci_level)
        data = result.as_dict()
        # Degenerate data cannot be reported as a successful, finite estimate.
        content = json.dumps(data, ensure_ascii=False, allow_nan=False)
        return ToolResult(content=content, summary={"method": method, "p_value": data["p_value"],
                                                   "effect_size": data["effect_size"], "ci": data["ci"]})
