# VeriMath Agent 镜像部署

GitHub 和 CNB 负责构建镜像。服务器只拉取镜像。
默认 Compose 同时启动应用和 Watchtower。
Watchtower 每 600 秒检查一次正式版镜像。

## 技术栈

后端使用 Python 3.11、FastAPI 和 Uvicorn。
前端使用原生 HTML、CSS 和 JavaScript。
数据保存在 SQLite。数学核验使用 SymPy。
模型通过兼容 Chat Completions 的 HTTP 接口调用。
服务器不运行模型权重。

## 镜像与发布规则

| 来源 | 镜像 |
|---|---|
| CNB | `docker.cnb.cool/azurekiln/verimath-agent:latest` |
| GitHub | `ghcr.io/azurekiln2333/verimath-agent:latest` |

普通提交和 PR 运行测试。
推送 `v*` 标签后，两端先测试，再构建镜像。
构建后的镜像还要通过启动与持久化检查。
检查通过后，流水线才上传镜像。

发布标签必须匹配 `pyproject.toml` 中的版本。
例如，版本 `0.1.0` 对应标签 `v0.1.0`。
正式版同时发布版本标签、提交标签和 `latest`。
预发布版本不更新 `latest`。
因此，普通代码提交不会立即更新服务器。

## 服务器首次部署

服务器需要 Docker Engine 和 Compose 插件。
2 核 2GB 可用于小规模使用。保持一个应用进程。
当前流水线发布 `linux/amd64` 镜像，适用于 x86_64 服务器。

首次发布 GHCR 镜像后，在 GitHub 的 Package settings 中
选择 Change visibility → Public。
公开代码仓库不会自动把 GHCR 镜像改为公开。
CNB 仓库也需要设为公开，才能按下述方式免登录下载与拉取。

从仓库下载以下两个文件。
也可直接从本地复制这两个文件。

```text
/opt/verimath-agent/
├── docker-compose.yml
├── .env.docker.example
├── .env.docker
└── data/                  # 首次启动后创建
```

公开仓库可以这样下载配置。
私有仓库应先登录仓库，或直接复制文件。

```bash
mkdir -p /opt/verimath-agent
cd /opt/verimath-agent
curl -fL https://cnb.cool/azurekiln/verimath-agent/-/raw/main/docker-compose.yml -o docker-compose.yml
curl -fL https://cnb.cool/azurekiln/verimath-agent/-/raw/main/.env.docker.example -o .env.docker.example
cp .env.docker.example .env.docker
nano .env.docker
```

已有 `.env.docker` 时，保留原文件。
至少填写以下模型配置。

```dotenv
MODEL_ENABLED=true
MODEL_API_BASE=https://你的模型接口/v1
MODEL_NAME=服务商支持的模型ID
MODEL_API_KEY=有效密钥
```

接口地址是否需要 `/v1`，以服务商说明为准。
代码中的思考参数面向 DeepSeek 接口。
切换其他服务商时，先验证参数兼容性。
识图还要求 `OCR_MODEL_NAME` 对应模型支持图片。

启动应用与自动更新服务。

```bash
docker compose --env-file .env.docker pull
docker compose --env-file .env.docker up -d --no-build
docker compose --env-file .env.docker ps
docker compose --env-file .env.docker logs --tail=100 xiaoyi
curl http://127.0.0.1:8765/healthz
```

镜像包含运行环境、静态页面和整理后的默认语料。
首次启动会给空数据库自动建立知识索引。
后续启动保留已有知识索引与聊天数据。
服务器无需 Python、Node、源码或 Dockerfile。

默认只监听主机的 `127.0.0.1:8765`。
可通过宿主机 Nginx 或 Caddy 提供 HTTPS 入口。
临时直连时，可设置 `VERIMATH_BIND_HOST=0.0.0.0`。
更改后重新运行 `up -d`。

面板目前没有应用内登录。
公网反向代理应对全部路径设置访问鉴权。
仅打开 A2A 签名开关，不能保护面板 API。

## Watchtower 自动更新

默认跟随 `VERIMATH_IMAGE` 指定的镜像标签。
当正式发布更新 `latest` 后，Watchtower 拉取新镜像。
它重建应用容器，并保留 `./data` 挂载。
应用更新期间会短暂停机。

Watchtower 只处理同时匹配以下条件的容器。

- `com.centurylinklabs.watchtower.enable=true`
- scope 与当前 Compose 项目名称一致

Watchtower 自身不参与自动更新。
清理选项只删除被替换的镜像。
它不会删除宿主机的 `data/`。

可在 `.env.docker` 中调整检查间隔。

```dotenv
WATCHTOWER_POLL_INTERVAL=600
```

查看自动更新日志或暂停自动更新。

```bash
docker compose --env-file .env.docker logs --tail=100 watchtower
docker compose --env-file .env.docker stop watchtower
```

再次运行 `up -d` 可恢复 Watchtower。
固定 `VERIMATH_IMAGE=...:v0.1.0` 可锁定版本。
锁定版本后不会自动切换到其他版本标签。

Watchtower 沿用容器原有配置。
它不会重新读取服务器上的 Compose 或环境文件。
修改密钥、端口、挂载或环境变量后，执行以下命令。

```bash
docker compose --env-file .env.docker up -d --no-build
```

## 私有镜像的拉取凭据

私有镜像需要服务器与 Watchtower 都能认证。
从仓库额外复制 `deploy/docker-compose.private.yml`。
为服务器创建具有镜像读取权限的专用令牌。

```bash
mkdir -p registry-auth
docker --config ./registry-auth login docker.cnb.cool --username cnb
```

在 `.env.docker` 中追加以下配置。

```dotenv
REGISTRY_AUTH_FILE=./registry-auth/config.json
```

拉取并启动。文件路径以主 Compose 文件为基准。

```bash
docker --config ./registry-auth compose --env-file .env.docker -f docker-compose.yml -f deploy/docker-compose.private.yml pull
docker --config ./registry-auth compose --env-file .env.docker -f docker-compose.yml -f deploy/docker-compose.private.yml up -d --no-build
```

此配置把专用认证文件只读挂载给 Watchtower。
认证文件不要使用宿主机专用的 `credsStore`。
容器中通常没有对应的凭据助手。
更新令牌后，重建 Watchtower 以重新加载认证文件。

GHCR 镜像同样可用。
将 `VERIMATH_IMAGE` 改为 GHCR 地址。
随后登录 `ghcr.io`，并使用上面的启动方式。

## 自定义知识库

默认使用镜像内的 `/corpus`。
可额外使用 `deploy/docker-compose.corpus.yml`。
在 `.env.docker` 中设置 `VERIMATH_CORPUS_DIR`。
此路径会只读挂载到 `/corpus`。

```dotenv
VERIMATH_CORPUS_DIR=./corpus
```

```bash
docker compose --env-file .env.docker -f docker-compose.yml -f deploy/docker-compose.corpus.yml up -d --no-build
```

已有索引不会在镜像更新时被自动替换。
更新语料后，可以手动全量重建索引。
此命令会替换已有知识片段，包括面板添加的笔记。
先备份数据，再执行。

```bash
docker compose --env-file .env.docker exec xiaoyi python -m scripts.build_corpus
```

## 迁移旧数据与回退

旧源码版默认把数据写入 `.data/`。
新 Compose 把宿主机 `./data/` 挂载到 `/data`。
迁移前停止旧应用，再复制完整目录。
SQLite 的 WAL 文件也要一起保留。

升级前可停止应用并备份配置与数据。

```bash
docker compose --env-file .env.docker stop xiaoyi
tar -czf verimath-backup.tar.gz data .env.docker
docker compose --env-file .env.docker up -d --no-build
```

回退时，把 `VERIMATH_IMAGE` 改为旧版本标签。
随后重新执行 `pull` 和 `up -d --no-build`。
如果版本包含不兼容的数据迁移，应恢复配套备份。

## 本地构建

仅开发者需要本地构建。
合并开发配置后，应用自动更新会被关闭。
Watchtower 也不会默认启动。

```bash
docker compose --env-file .env.docker -f docker-compose.yml -f docker-compose.build.yml up -d --build
```

## 发布新版本

先修改 `pyproject.toml` 中的版本。
完成测试并提交代码，再创建匹配的标签。

```bash
git tag v0.1.0
git push origin main v0.1.0
git push cnb main v0.1.0
```

GitHub 使用 `.github/workflows/build-and-release.yml`。
CNB 使用 `.cnb.yml`，由平台提供构建令牌。
两端分别发布 GHCR 与 CNB 镜像。
服务器默认从 CNB 拉取。

不要把模型密钥配置到构建变量中。
模型密钥只保存在服务器的 `.env.docker`。
`.dockerignore` 只放行运行代码与整理后的语料。
本地环境、聊天数据库和原始 PDF 不会进入镜像。
