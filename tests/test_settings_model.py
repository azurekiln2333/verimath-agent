from app.settings import Settings, load_local_env


def test_deepseek_flash_is_default_model():
    settings = Settings()
    assert settings.model_api_base == "https://api.deepseek.com"
    assert settings.model_name == "deepseek-v4-flash"


def test_settings_reads_environment_at_instantiation(monkeypatch):
    monkeypatch.setenv("MODEL_ENABLED", "true")
    monkeypatch.setenv("RETRIEVAL_LIMIT", "7")
    settings = Settings()
    assert settings.model_enabled is True
    assert settings.retrieval_limit == 7


def test_load_local_env_does_not_override_existing_env(tmp_path, monkeypatch):
    env_file = tmp_path / ".env"
    env_file.write_text(
        "MODEL_ENABLED=true\nMODEL_NAME=from-file\nDEEPSEEK_API_KEY=from-file\n",
        encoding="utf-8",
    )
    monkeypatch.setenv("MODEL_NAME", "from-shell")
    monkeypatch.delenv("MODEL_ENABLED", raising=False)
    monkeypatch.delenv("DEEPSEEK_API_KEY", raising=False)
    load_local_env(env_file)
    assert Settings().model_enabled is True
    assert Settings().model_name == "from-shell"
    assert Settings().model_api_key == "from-file"
