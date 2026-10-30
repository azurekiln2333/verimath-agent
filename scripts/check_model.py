"""Check the container's actual model configuration without printing secrets."""
from __future__ import annotations

import asyncio
import json
import time
from urllib.parse import urlsplit

from app.model_client import ModelMessage, OpenAICompatibleClient
from app.model_errors import describe_model_error
from app.settings import Settings, settings


async def check_model(config: Settings) -> dict:
    client = OpenAICompatibleClient(config)
    report = {"ok": False, "api_host": urlsplit(config.model_api_base).hostname,
              "model": config.model_name, "model_enabled": config.model_enabled,
              "key_present": bool(config.model_api_key), "thinking_enabled": config.model_thinking,
              "probe": "streaming_greeting_without_thinking"}
    if not client.enabled:
        report.update(code="not_configured", user_message="请启用模型并配置接口地址与密钥。")
        return report
    started = time.monotonic()
    try:
        text = ""
        async with asyncio.timeout(25):
            async for event in client.stream_chat([ModelMessage("user", "你好，请只回答你好。")],
                                                   thinking=False, max_tokens=128):
                if event.type == "delta":
                    text += event.text
        if not text.strip():
            raise ValueError("model_output_empty")
        report.update(ok=True, code="ok", user_message="模型鉴权与流式回答正常。")
    except Exception as exc:
        report.update(describe_model_error(exc))
    finally:
        await client.aclose()
    report["elapsed_seconds"] = round(time.monotonic() - started, 2)
    return report


def main() -> None:
    result = asyncio.run(check_model(settings))
    print(json.dumps(result, ensure_ascii=False, indent=2))
    raise SystemExit(0 if result["ok"] else 1)


if __name__ == "__main__":
    main()
