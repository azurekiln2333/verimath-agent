from __future__ import annotations

import json

from locust import HttpUser, between, task


class A2AUser(HttpUser):
    wait_time = between(1, 3)
    session_id: str | None = None

    def on_start(self) -> None:
        response = self.client.post(
            "/a2a",
            json={"jsonrpc": "2.0", "id": "init", "method": "initialize", "params": {}},
        )
        self.session_id = response.headers.get("agent-session-id")

    @task
    def stream_method_selection(self) -> None:
        headers = {}
        if self.session_id:
            headers["agent-session-id"] = self.session_id
        payload = {
            "jsonrpc": "2.0",
            "id": "load",
            "method": "message/stream",
            "params": {
                "taskId": "load-test-task",
                "message": {"content": "两组成绩比较用什么统计方法？"},
            },
        }
        with self.client.post(
            "/a2a",
            headers={**headers, "Content-Type": "application/json"},
            data=json.dumps(payload, ensure_ascii=False),
            name="/a2a message/stream",
            catch_response=True,
        ) as response:
            if response.status_code != 200:
                response.failure(f"unexpected status {response.status_code}")
