import asyncio
import json

import httpx
import pytest

from app.model_errors import describe_model_error
from app.settings import Settings
from scripts.check_model import check_model


@pytest.mark.parametrize("error,code", [
    (httpx.ReadTimeout("private-key"), "timeout"),
    (httpx.ConnectError("private-key"), "connection_error"),
    (RuntimeError("model_output_incomplete"), "incomplete_output"),
    (RuntimeError("private-key"), "execution_error"),
])
def test_diagnostics_classify_failures_without_echoing_exception_details(error, code):
    details = describe_model_error(error)
    assert details["code"] == code
    assert "private-key" not in json.dumps(details)


@pytest.mark.parametrize("status", [200, 401, 429])
def test_container_model_probe_checks_streaming_and_never_prints_key(monkeypatch, status):
    calls = []

    def handle(request):
        body = json.loads(request.content)
        calls.append(body)
        assert body["stream"] and body["thinking"] == {"type": "disabled"}
        if status != 200:
            return httpx.Response(status, text="private-key provider body")
        return httpx.Response(200, text='data: {"choices":[{"delta":{"content":"你好"},"finish_reason":"stop"}]}\n\ndata: [DONE]\n\n')

    async def run():
        transport = httpx.MockTransport(handle)
        monkeypatch.setattr("app.model_client.httpx.AsyncClient", lambda **kwargs: original(transport=transport))
        result = await check_model(Settings(model_enabled=True, model_api_key="private-key",
                                           model_api_base="https://private-key@model.invalid/v1?token=private-key"))
        assert result["ok"] is (status == 200)
        assert result["api_host"] == "model.invalid"
        assert "private-key" not in json.dumps(result)
        if status != 200:
            assert result["http_status"] == status
        assert len(calls) == 1

    original = httpx.AsyncClient
    asyncio.run(run())


def test_container_model_probe_handles_missing_key_without_network():
    result = asyncio.run(check_model(Settings(model_enabled=True, model_api_key="")))
    assert not result["ok"] and result["code"] == "not_configured" and not result["key_present"]
