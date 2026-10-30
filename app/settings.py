from __future__ import annotations

import os
from dataclasses import dataclass, field
from pathlib import Path


DEFAULT_CORPUS_PATHS = (
    r"E:\windows_ext\Desktop\个人\学习\概率论",
    r"E:\windows_ext\Desktop\个人\学习\数分高代",
)


def load_local_env(path: Path = Path(".env")) -> None:
    if not path.exists() or not path.is_file():
        return
    for raw_line in path.read_text(encoding="utf-8").splitlines():
        line = raw_line.strip()
        if not line or line.startswith("#") or "=" not in line:
            continue
        key, value = line.split("=", 1)
        key = key.strip()
        value = value.strip().strip('"').strip("'")
        if key and key not in os.environ:
            os.environ[key] = value


def _env_bool(name: str, default: bool = False) -> bool:
    fallback = "true" if default else "false"
    return os.getenv(name, fallback).lower() in {"1", "true", "yes", "on"}


def _split_paths(value: str | None) -> list[Path]:
    if not value:
        return [Path(path) for path in DEFAULT_CORPUS_PATHS]
    return [Path(part.strip()) for part in value.split(";") if part.strip()]


load_local_env()


@dataclass(frozen=True)
class Settings:
    app_name: str = "xiaoyi-a2a-stat-tutor"
    app_version: str = "0.1.1"
    data_dir: Path = field(default_factory=lambda: Path(os.getenv("DATA_DIR", ".data")))
    corpus_paths: tuple[Path, ...] = field(
        default_factory=lambda: tuple(_split_paths(os.getenv("CORPUS_WHITELIST")))
    )
    enforce_signature: bool = field(default_factory=lambda: _env_bool("A2A_ENFORCE_SIGNATURE"))
    access_key: str = field(default_factory=lambda: os.getenv("A2A_ACCESS_KEY", ""))
    secret_key: str = field(default_factory=lambda: os.getenv("A2A_SECRET_KEY", ""))
    signature_window_seconds: int = field(
        default_factory=lambda: int(os.getenv("A2A_SIGNATURE_WINDOW_SECONDS", "900"))
    )
    model_api_base: str = field(
        default_factory=lambda: os.getenv("MODEL_API_BASE", "https://api.deepseek.com")
    )
    model_api_key: str = field(
        default_factory=lambda: (os.getenv("MODEL_API_KEY") or os.getenv("DEEPSEEK_API_KEY", "")).strip()
    )
    model_name: str = field(default_factory=lambda: os.getenv("MODEL_NAME", "deepseek-v4-flash"))
    # 可独立指定视觉模型；留空时复用已验证支持图片的聊天模型与同一 API。
    ocr_model_name: str = field(default_factory=lambda: os.getenv("OCR_MODEL_NAME", "").strip())
    model_enabled: bool = field(default_factory=lambda: _env_bool("MODEL_ENABLED", default=True))
    model_max_output_tokens: int = field(default_factory=lambda: int(os.getenv("MODEL_MAX_OUTPUT_TOKENS", "8192")))
    agent_timeout_seconds: float = field(default_factory=lambda: float(os.getenv("AGENT_TIMEOUT_SECONDS", "180")))
    # DeepSeek 思考模式：默认开启。reasoning_content 与 content 同级返回，
    # 工具调用轮次需把 reasoning_content 回传给 API（否则 400）。
    model_thinking: bool = field(default_factory=lambda: _env_bool("MODEL_THINKING", default=True))
    # 思考强度：high（普通默认）/ max（复杂 agent 请求）。low/medium 映射为 high。
    model_reasoning_effort: str = field(
        default_factory=lambda: os.getenv("MODEL_REASONING_EFFORT", "high")
    )
    max_history_turns: int = field(default_factory=lambda: int(os.getenv("MAX_HISTORY_TURNS", "8")))
    retrieval_limit: int = field(default_factory=lambda: int(os.getenv("RETRIEVAL_LIMIT", "4")))
    # 多轮上下文拼装进模型时的 token 预算（字符数近似，不引 tiktoken）。
    # 与 max_history_turns 配合：轮数先截断，再按 token 预算二次裁剪，避免长对话超模型窗口。
    context_token_budget: int = field(
        default_factory=lambda: int(os.getenv("CONTEXT_TOKEN_BUDGET", "4000"))
    )

    @property
    def sqlite_path(self) -> Path:
        return self.data_dir / "a2a.sqlite"

    @property
    def trace_sqlite_path(self) -> Path:
        return self.data_dir / "trace.sqlite"


settings = Settings()
