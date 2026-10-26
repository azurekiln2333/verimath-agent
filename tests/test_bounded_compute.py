import asyncio

import pytest

from app.bounded_compute import run_compute


def test_symbolic_child_returns_step_results_without_blocking_web_loop():
    async def run():
        ticks = []

        async def heartbeat():
            for _ in range(3):
                ticks.append(True)
                await asyncio.sleep(.01)

        checks, _ = await asyncio.gather(run_compute("verify_steps", {"steps": ["x+x", "2*x"]}), heartbeat())
        assert checks[0]["status"] == "ok"
        assert len(ticks) == 3
    asyncio.run(run())


@pytest.mark.parametrize("stop", ["timeout", "cancel"])
def test_stalled_compute_process_is_killed_and_reaped(monkeypatch, stop):
    from types import SimpleNamespace

    async def run():
        started = asyncio.Event()
        state = SimpleNamespace(returncode=None, killed=False, reaped=False)

        async def communicate(data):
            started.set()
            await asyncio.Event().wait()

        def kill():
            state.killed = True
            state.returncode = -9

        async def wait():
            state.reaped = True

        state.communicate, state.kill, state.wait = communicate, kill, wait

        async def spawn(*args, **kwargs):
            return state

        monkeypatch.setattr(asyncio, "create_subprocess_exec", spawn)
        task = asyncio.create_task(run_compute("verify_steps", {"steps": []}, timeout=.05))
        await started.wait()
        if stop == "cancel":
            task.cancel()
        with pytest.raises(TimeoutError if stop == "timeout" else asyncio.CancelledError):
            await task
        assert state.killed and state.reaped
    asyncio.run(run())
