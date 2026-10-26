"""Run symbolic work outside the web event loop, with a killable deadline."""
from __future__ import annotations

import asyncio
import json
import os
from pathlib import Path
import subprocess
import sys
from weakref import WeakKeyDictionary

_slots = WeakKeyDictionary()


async def run_compute(operation: str, arguments: dict, *, timeout: float = 15):
    loop = asyncio.get_running_loop()
    slots = _slots.setdefault(loop, asyncio.Semaphore(2))
    async with asyncio.timeout(timeout):
        async with slots:
            process = await asyncio.create_subprocess_exec(
                sys.executable, "-m", "app.bounded_compute", operation,
                cwd=Path(__file__).resolve().parents[1],
                stdin=asyncio.subprocess.PIPE, stdout=asyncio.subprocess.PIPE,
                stderr=asyncio.subprocess.DEVNULL,
                creationflags=subprocess.CREATE_NO_WINDOW if os.name == "nt" else 0,
            )
            try:
                output, _ = await process.communicate(json.dumps(arguments).encode())
                if process.returncode:
                    raise ValueError("计算进程未能完成，请简化输入")
                result = json.loads(output)
                if "error" in result:
                    raise ValueError(result["error"])
                return result["result"]
            finally:
                if process.returncode is None:
                    process.kill()
                await process.wait()


async def _worker(operation: str, arguments: dict):
    from dataclasses import asdict

    if operation == "verify_steps":
        from app.verify import check_steps
        return [asdict(check) for check in check_steps(arguments["steps"])]
    if operation == "linalg":
        from app.linalg.tool import LinalgStepSolveTool
        return asdict(await LinalgStepSolveTool()._run_inline(**arguments))
    if operation == "calculus":
        from app.tools.calculus import calculate
        return calculate(arguments)
    raise ValueError("未知计算类型")


if __name__ == "__main__":
    try:
        value = asyncio.run(_worker(sys.argv[1], json.loads(sys.stdin.buffer.read())))
        envelope = {"result": value}
    except Exception as exc:
        envelope = {"error": str(exc)[:200]}
    sys.stdout.write(json.dumps(envelope, allow_nan=False))
