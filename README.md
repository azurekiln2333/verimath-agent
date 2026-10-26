# VeriMath Agent · 数学与统计学习导师

## 镜像部署与自动更新

GitHub 和 CNB 按版本标签构建并发布镜像。
服务器使用 `docker-compose.yml` 拉取镜像。
默认同时启动 Watchtower，每 10 分钟检查更新。
镜像自带 Python、静态页面和默认知识库语料。
首次启动会自动建立空数据库的知识索引。

完整步骤见 [镜像部署文档](deploy/README.md)。
服务器只需 Compose 文件、`.env.docker` 和数据目录。
源码构建使用单独的 `docker-compose.build.yml`。

技术栈：Python 3.11+、FastAPI、Uvicorn、SQLite、SymPy，
以及原生 HTML、CSS 和 JavaScript。
大模型通过兼容 Chat Completions 的 HTTP API 接入。

这是一个本地验证用的云 A2A Remote Agent 脚手架，目标是先跑通协议、会话、流式回答、取消任务、清上下文和白名单 RAG 采集，再迁移到公网 HTTPS 接入小艺开放平台。

## 当前能力

- `GET /healthz`：健康检查。
- `POST /a2a`：统一 JSON-RPC 入口。
- 已支持方法：`initialize`、`notifications/initialized`、`message/stream`、`tasks/cancel`、`clearContext` / `clearContextRPC`。
- `message/stream` 使用 SSE 返回 `status`、`message`、`final` 事件。
- 内置 5 个轻量 Agent：课程规划、概念答疑、统计方法选择、练习讲评、合规守门。
- RAG 只允许白名单目录，默认排除 `.pem`、`.pyc`、环境目录、压缩包、可执行文件和未支持格式。

## 本地运行

先创建本地虚拟环境并安装依赖。不要全局安装。

```powershell
cd xiaoyi-a2a-stat-tutor
py -m venv .venv
.\.venv\Scripts\python.exe -m pip install -e ".[test]"
.\.venv\Scripts\python.exe -m uvicorn app.main:app --reload --host 127.0.0.1 --port 8765
```

浏览器打开本地面板：

```text
http://127.0.0.1:8765/dashboard
```

如果 `8765` 被占用，可以把启动命令端口改成 `8766`，然后打开 `http://127.0.0.1:8766/dashboard`。

面板会把助手回答渲染为 Markdown，并通过 MathJax CommonHTML 渲染 LaTeX 公式。已支持标题、列表、粗体、引用、代码块、表格、链接、行内公式和独立公式，后续可直接迁移到 App WebView 或小艺平台的展示层。

发送问题时，面板会显示分阶段状态：检索知识库、调用模型、整理 Markdown 与公式、保存聊天记录。

面板左侧提供回答偏好：`严谨`、`举例`、`简洁`。默认是严谨模式，面向理学专业学生，要求模型说明定义、条件、公式、适用边界和常见误区。

面板聊天会自动保存到 `.data/a2a.sqlite`，左侧“最近聊天”会显示最近记录。离线评测运行会保存到 `.data/eval_runs.jsonl`，左侧“测试记录”会显示最近评测摘要。

默认安装使用 SQLite Keyword RAG，避免 Windows 本地缺少 C++ 编译工具时被 Chroma/HNSW 阻塞。以后需要向量库时再单独安装：

```powershell
.\.venv\Scripts\python.exe -m pip install -e ".[vector]"
```

另开终端模拟小艺请求：

```powershell
.\.venv\Scripts\python.exe scripts\a2a_client.py --query "两组成绩比较应该用什么统计方法？"
```

轻量并发烟测：

```powershell
.\.venv\Scripts\python.exe scripts\load_smoke.py --concurrency 20
```

离线跑 140 条评测种子集：

```powershell
.\.venv\Scripts\python.exe scripts\run_eval.py
```

## 模型配置

默认模型配置为 DeepSeek 官方 OpenAI-compatible 接口：

```powershell
$env:MODEL_API_BASE = "https://api.deepseek.com"
$env:MODEL_NAME = "deepseek-v4-flash"
$env:DEEPSEEK_API_KEY = "只在本机终端里填写，不写入文件"
$env:MODEL_ENABLED = "true"
```

默认启用模型：配置 `MODEL_API_KEY` 或 `DEEPSEEK_API_KEY` 后，普通聊天会调用模型，由模型决定是否使用工具。需要离线调试时可显式设置 `MODEL_ENABLED=false`，或关闭面板设置中的「使用模型」。未配置密钥或模型调用失败时保留规则回答作为降级；自动化测试单独关闭真实模型调用。

项目启动时会自动读取本地 `.env`，但 `.env` 已被 `.gitignore` 排除，不要提交密钥。

## 构建本地资料索引

只会读取 `CORPUS_WHITELIST` 指定的白名单目录。首次执行前请确认里面都是自有或已授权资料。
公开本地语料不要直接把原始 `corpus/public_index` 或 `corpus/papers/kconrad_md` 塞进白名单；
先整理成 `corpus/curated/public_main` 再入库，避免导航卡、英文原文和主讲义混成一类文本。

```powershell
Copy-Item .env.example .env
.\.venv\Scripts\python.exe scripts\curate_public_corpus.py
.\.venv\Scripts\python.exe scripts\build_corpus.py
```

当前建议的本地白名单示例：

```env
CORPUS_WHITELIST=corpus/curated/public_main
```

`scripts\build_corpus.py` 默认只索引 `main,public` 两类 `ingest_policy`。如果要单独构建题卷副库，可显式指定：

```powershell
.\.venv\Scripts\python.exe scripts\build_corpus.py --include-policies exam --db-path .data\exam.sqlite
```

## 重要边界

- 本地 POC 不能直接上架，正式接入小艺前需要公网 HTTPS、AK/SK 鉴权、限流、监控、隐私协议和内容审核材料。
- 不把 Z-Library、Sci-Hub、百度文库、组卷网等未授权内容放入公开知识库。
- 不承诺天工计划激励收益，具体档位和口径必须以华为最新后台/官方页面为准。
