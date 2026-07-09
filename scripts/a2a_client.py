from __future__ import annotations

import argparse
import json
import sys
import urllib.request
from typing import Any

if hasattr(sys.stdout, "reconfigure"):
    sys.stdout.reconfigure(encoding="utf-8")


def post_json(url: str, payload: dict[str, Any], session_id: str | None = None):
    data = json.dumps(payload, ensure_ascii=False).encode("utf-8")
    request = urllib.request.Request(
        url,
        data=data,
        headers={"Content-Type": "application/json"},
        method="POST",
    )
    if session_id:
        request.add_header("agent-session-id", session_id)
    return urllib.request.urlopen(request, timeout=120)


def initialize(url: str) -> str:
    response = post_json(
        url,
        {"jsonrpc": "2.0", "id": "init-1", "method": "initialize", "params": {}},
    )
    body = json.loads(response.read().decode("utf-8"))
    session_id = response.headers.get("agent-session-id") or body["result"]["sessionId"]
    print("initialized session:", session_id)
    return session_id


def stream_message(url: str, session_id: str, query: str) -> None:
    payload = {
        "jsonrpc": "2.0",
        "id": "msg-1",
        "method": "message/stream",
        "params": {
            "taskId": "local-demo-task",
            "message": {"role": "user", "content": query},
        },
    }
    with post_json(url, payload, session_id=session_id) as response:
        for raw_line in response:
            line = raw_line.decode("utf-8", errors="replace").rstrip()
            if line:
                print(line)


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--url", default="http://127.0.0.1:8765/a2a")
    parser.add_argument("--query", default="概率论和数理统计应该怎么学？")
    args = parser.parse_args()
    session_id = initialize(args.url)
    stream_message(args.url, session_id, args.query)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
