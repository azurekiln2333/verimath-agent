from app.model_client import OpenAICompatibleClient
from app.settings import Settings


def test_model_client_requires_explicit_enable_flag():
    settings = Settings(model_api_key="test-key", model_enabled=False)
    assert OpenAICompatibleClient(settings).enabled is False


def test_model_client_enabled_when_flag_and_key_are_present():
    settings = Settings(model_api_key="test-key", model_enabled=True)
    assert OpenAICompatibleClient(settings).enabled is True
