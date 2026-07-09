from __future__ import annotations

import argparse
import asyncio
import time

import httpx


async def run_one(
    client: httpx.AsyncClient,
    url: str,
    query: str,
    use_model: bool,
    index: int,
) -> tuple[int, bool, float]:
    payload = {
        "jsonrpc": "2.0",
        "id": f"load-{index}",
        "method": "message/stream",
        "params": {
            "taskId": f"load-task-{index}",
            "message": {"content": query},
            "useModel": use_model,
        },
    }
    start = time.perf_counter()
    response = await client.post(url, json=payload)
    latency = time.perf_counter() - start
    return response.status_code, "event: final" in response.text, latency


async def run(url: str, query: str, concurrency: int, timeout: float, use_model: bool) -> int:
    start = time.perf_counter()
    limits = httpx.Limits(
        max_connections=max(concurrency + 5, 10),
        max_keepalive_connections=max(concurrency, 5),
    )
    async with httpx.AsyncClient(timeout=timeout, limits=limits) as client:
        results = await asyncio.gather(
            *(run_one(client, url, query, use_model, index) for index in range(concurrency))
        )
    total = time.perf_counter() - start
    ok_count = sum(1 for status, has_final, _ in results if status == 200 and has_final)
    max_latency = max((latency for _, _, latency in results), default=0.0)
    print(f"ok_count {ok_count}")
    print(f"use_model {str(use_model).lower()}")
    print(f"elapsed_all_seconds {total:.3f}")
    print(f"max_latency_seconds {max_latency:.3f}")
    return 0 if ok_count == concurrency else 1


def main() -> int:
    parser = argparse.ArgumentParser(description="Lightweight local A2A streaming load smoke test.")
    parser.add_argument("--url", default="http://127.0.0.1:8765/a2a")
    parser.add_argument("--query", default="中心极限定理是什么？")
    parser.add_argument("--concurrency", type=int, default=20)
    parser.add_argument("--timeout", type=float, default=15.0)
    parser.add_argument(
        "--use-model",
        action="store_true",
        help="Call the configured model during the smoke test. Default is offline router only.",
    )
    args = parser.parse_args()
    if args.concurrency < 1:
        parser.error("--concurrency must be >= 1")
    return asyncio.run(run(args.url, args.query, args.concurrency, args.timeout, args.use_model))


if __name__ == "__main__":
    raise SystemExit(main())
