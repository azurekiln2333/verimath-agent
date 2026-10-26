FROM python:3.11-slim

WORKDIR /app

ENV PYTHONDONTWRITEBYTECODE=1 \
    PYTHONUNBUFFERED=1 \
    DATA_DIR=/data \
    CORPUS_WHITELIST=/corpus \
    CORPUS_AUTO_INDEX=true

# Read dependencies from the project metadata so CI and the image stay aligned.
COPY pyproject.toml ./
RUN python -c "import subprocess,sys,tomllib; p=tomllib.load(open('pyproject.toml','rb'))['project']; subprocess.check_call([sys.executable,'-m','pip','install','--no-cache-dir',*p['dependencies'],*p['optional-dependencies']['linalg']])"

COPY app ./app
COPY scripts ./scripts
COPY corpus/curated/public_main/ /corpus/

RUN mkdir -p /corpus /data

ARG VCS_REF=unknown
ARG VERSION=0.1.0
LABEL org.opencontainers.image.title="VeriMath Agent" \
      org.opencontainers.image.source="https://github.com/azurekiln2333/verimath-agent" \
      org.opencontainers.image.version=$VERSION \
      org.opencontainers.image.revision=$VCS_REF

EXPOSE 8765
HEALTHCHECK --interval=30s --timeout=5s --start-period=30s --retries=3 \
    CMD python -c "import urllib.request;urllib.request.urlopen('http://127.0.0.1:8765/healthz',timeout=3)" || exit 1

ENTRYPOINT ["python", "-m", "scripts.container_entrypoint"]
CMD ["python", "-m", "uvicorn", "app.main:app", "--host", "0.0.0.0", "--port", "8765"]
