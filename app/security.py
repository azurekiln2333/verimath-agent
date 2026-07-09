from __future__ import annotations

import base64
import hmac
import time
from dataclasses import dataclass
from hashlib import sha256

from starlette.datastructures import Headers

from app.settings import Settings


@dataclass(frozen=True)
class VerificationResult:
    ok: bool
    reason: str = ""


class SignatureVerifier:
    """AK/SK verifier compatible with Huawei-style HMAC(ts) signing."""

    def __init__(self, settings: Settings) -> None:
        self.settings = settings

    def verify(self, headers: Headers) -> VerificationResult:
        if not self.settings.enforce_signature:
            return VerificationResult(ok=True)
        access_key = headers.get("accessKey", "")
        sign = headers.get("sign", "")
        ts = headers.get("ts", "")
        if not (access_key and sign and ts):
            return VerificationResult(False, "missing accessKey/sign/ts headers")
        if access_key != self.settings.access_key:
            return VerificationResult(False, "invalid accessKey")
        try:
            timestamp_ms = int(ts)
        except ValueError:
            return VerificationResult(False, "invalid timestamp")
        delta = abs(time.time() - timestamp_ms / 1000)
        if delta > self.settings.signature_window_seconds:
            return VerificationResult(False, "timestamp outside replay window")
        expected = base64.b64encode(
            hmac.new(
                self.settings.secret_key.encode("utf-8"),
                ts.encode("utf-8"),
                sha256,
            ).digest()
        ).decode("utf-8")
        if not hmac.compare_digest(expected, sign):
            return VerificationResult(False, "invalid signature")
        return VerificationResult(ok=True)

