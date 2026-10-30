"""Safe model diagnostics: retain status codes without exposing keys or response bodies."""
from __future__ import annotations

import httpx


_HINTS = {
    "authentication_failed": "模型接口鉴权失败，请检查服务端模型密钥及对应接口地址。",
    "access_denied": "模型接口拒绝访问，请检查密钥的模型权限。",
    "model_not_found": "模型或接口路径不存在，请检查接口地址和模型名称。",
    "invalid_request": "模型接口拒绝了请求，请检查模型名称以及思考、工具调用参数是否受支持。",
    "rate_limited": "模型接口请求受限或额度不足，请检查额度或稍后重试。",
    "upstream_error": "上游模型服务异常，请稍后重试。",
    "timeout": "等待模型响应超时，请检查服务器到模型接口的连接，或关闭深度思考后重试。",
    "connection_error": "无法连接模型接口，请检查服务器网络和接口地址。",
    "incomplete_output": "模型返回的内容不完整，请重试或调整模型输出上限。",
    "execution_error": "模型调用失败，请查看服务端诊断日志。",
}


def model_error_hint(code: str) -> str:
    return _HINTS.get(code, _HINTS["execution_error"])


class ModelRequestError(RuntimeError):
    def __init__(self, details: dict) -> None:
        self.details = details
        super().__init__(details["message"])


def describe_model_error(exc: Exception) -> dict:
    if isinstance(exc, ModelRequestError):
        return exc.details
    status = None
    if isinstance(exc, httpx.HTTPStatusError):
        status = exc.response.status_code
        code = {401: "authentication_failed", 403: "access_denied", 404: "model_not_found",
                400: "invalid_request", 422: "invalid_request", 429: "rate_limited"}.get(
                    status, "upstream_error" if status >= 500 else "execution_error")
    elif isinstance(exc, (TimeoutError, httpx.TimeoutException)):
        code = "timeout"
    elif isinstance(exc, (httpx.RequestError, ConnectionError)):
        code = "connection_error"
    elif isinstance(exc, (RuntimeError, ValueError)) and str(exc) in {
        "model_stream_incomplete", "model_output_incomplete", "model_output_empty",
    }:
        code = "incomplete_output"
    else:
        code = "execution_error"
    hint = model_error_hint(code)
    if status is not None:
        hint = f"HTTP {status}：{hint}"
    return {"code": code, "message": "agent_timeout" if code == "timeout" else type(exc).__name__,
            "error_type": type(exc).__name__, "http_status": status, "user_message": hint}
