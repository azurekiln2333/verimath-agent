from app.model_client import OpenAICompatibleClient
from app.settings import Settings


def test_model_client_respects_explicit_disable_flag():
    settings = Settings(model_api_key="test-key", model_enabled=False)
    assert OpenAICompatibleClient(settings).enabled is False


def test_model_client_enabled_when_flag_and_key_are_present():
    settings = Settings(model_api_key="test-key", model_enabled=True)
    assert OpenAICompatibleClient(settings).enabled is True


def test_model_client_enabled_by_default_when_key_is_present(monkeypatch):
    monkeypatch.delenv("MODEL_ENABLED", raising=False)
    settings = Settings(model_api_key="test-key")
    assert OpenAICompatibleClient(settings).enabled is True


def test_model_client_without_key_stays_unavailable(monkeypatch):
    monkeypatch.delenv("MODEL_ENABLED", raising=False)
    settings = Settings(model_api_key="")
    assert OpenAICompatibleClient(settings).enabled is False


def test_model_pool_is_reused_and_closed_with_explicit_output_budget(monkeypatch):
    import asyncio
    import json
    import httpx
    from app.model_client import ModelMessage

    calls = []

    def handle(request):
        body = json.loads(request.content)
        assert body["max_tokens"] == 512
        calls.append(body)
        return httpx.Response(200, json={"choices": [{"message": {"content": "回答"}, "finish_reason": "stop"}]})

    monkeypatch.setattr(httpx, "AsyncHTTPTransport", lambda **kwargs: httpx.MockTransport(handle))

    async def run():
        client = OpenAICompatibleClient(Settings(model_enabled=True, model_api_key="test", model_max_output_tokens=512))
        await client.start()
        pool = client._http
        await client.start()
        assert client._http is pool
        assert (await client.chat([ModelMessage("user", "问")])).content == "回答"
        assert await client.complete([ModelMessage("user", "问")]) == "回答"
        await client.aclose()
        assert client._http is None and pool.is_closed
        assert len(calls) == 2
    asyncio.run(run())


def test_truncated_model_stream_is_not_marked_completed(monkeypatch):
    import asyncio
    import httpx
    import pytest

    def handle(request):
        return httpx.Response(200, text='data: {"choices":[{"delta":{"content":"部分"}}]}\n\n')

    monkeypatch.setattr(httpx, "AsyncHTTPTransport", lambda **kwargs: httpx.MockTransport(handle))

    async def run():
        client = OpenAICompatibleClient(Settings(model_enabled=True, model_api_key="test"))
        await client.start()
        try:
            events = client.stream_chat([])
            assert (await anext(events)).text == "部分"
            with pytest.raises(RuntimeError, match="model_stream_incomplete"):
                await anext(events)
        finally:
            await client.aclose()
    asyncio.run(run())
