"""Exercise a real built image, including first-run indexing and restart storage."""
from __future__ import annotations

import argparse
import json
import subprocess
import time
import uuid


def docker(*arguments: str, check: bool = True) -> subprocess.CompletedProcess[str]:
    return subprocess.run(["docker", *arguments], check=check, capture_output=True, text=True)


def request(container: str, path: str, payload: dict | None = None):
    script = (
        "import json,urllib.request;"
        f"p={json.dumps(json.dumps(payload, ensure_ascii=True))} if {payload is not None!r} else None;"
        f"r=urllib.request.Request('http://127.0.0.1:8765{path}',"
        "data=p.encode() if p else None,headers={'Content-Type':'application/json'});"
        "print(urllib.request.urlopen(r,timeout=30).read().decode())"
    )
    return docker("exec", container, "python", "-c", script).stdout


def wait_ready(container: str) -> None:
    for _ in range(60):
        try:
            if json.loads(request(container, "/healthz"))["status"] == "ok":
                return
        except (subprocess.CalledProcessError, ValueError, KeyError):
            pass
        time.sleep(1)
    raise RuntimeError("Container did not become healthy within 60 seconds")


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("image")
    args = parser.parse_args()
    suffix = uuid.uuid4().hex[:12]
    container = f"verimath-smoke-{suffix}"
    volume = f"verimath-smoke-data-{suffix}"
    docker("volume", "create", volume)
    try:
        docker("run", "-d", "--name", container, "-e", "MODEL_ENABLED=false",
               "--mount", f"type=volume,source={volume},target=/data", args.image)
        wait_ready(container)
        assert "VeriMath" in request(container, "/dashboard")
        first = json.loads(request(container, "/api/panel/status"))
        assert first["corpus"]["chunks"] > 0, "Bundled corpus was not indexed"
        chat = json.loads(request(container, "/api/panel/chat", {
            "query": "What is the central limit theorem?", "session_id": suffix,
            "use_model": False,
        }))
        assert chat["content"], "Offline chat returned no content"
        docker("restart", container)
        wait_ready(container)
        restored = json.loads(request(container, "/api/panel/status"))
        assert restored["corpus"]["chunks"] == first["corpus"]["chunks"]
        assert restored["records"]["chat_count"] == 1, "Chat data did not survive restart"
        print(json.dumps({"image": args.image, "chunks": restored["corpus"]["chunks"],
                          "restart_preserved_chat": True, "status": "passed"}))
    except Exception:
        print(docker("logs", "--tail", "100", container, check=False).stdout)
        raise
    finally:
        docker("rm", "-f", container, check=False)
        docker("volume", "rm", volume, check=False)


if __name__ == "__main__":
    main()
