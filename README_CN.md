# 小艺 A2A 数理统计学习导师 · 中文说明

> 本文档为 `app/` 等核心目录的中文注释版，解决“文件夹备注不完整”问题。英文原版见 `README.md`。

## 1. 项目定位

本地可验证的 **A2A Remote Agent** 脚手架，已跑通 `GET /healthz` `POST /a2a` `message/stream SSE` `tasks/cancel` `clearContext` 全链路，目标为公网 HTTPS 接入小艺开放平台。

- **技术栈**：`FastAPI + uvicorn + pydantic + httpx + sse-starlette + pymupdf + python-docx`（`pyproject.toml:6`）
- **当前版本**：`0.1.0` `requires-python >=3.11`
- **测试**：`802 passed`（`tests/`），评测集 `65/65` 答案基准

## 2. 目录中文注释

| 目录/文件 | 中文说明 | 关键内容 |
|---|---|---|
| `app/main.py` | **FastAPI 入口**，健康检查 + 统一 JSON-RPC + 面板 `/dashboard` | `app_name= xiaoyi-a2a-stat-tutor` `sessions/retriever/model_client` |
| `app/settings.py` | **配置中心**，读 `.env` 白名单/模型/A2A 鉴权 | `CORPUS_WHITELIST` `MODEL_API_BASE` `A2A_ENFORCE_SIGNATURE` |
| `app/protocol.py` | **协议层**，JSON-RPC 2.0 + SSE `sse_event` | `CLEAR_CONTEXT_METHODS` |
| `app/agents/` | **5个轻量 Agent** | `router.py:27` `TutorRouter` 分发 |
| `app/agents/router.py` | 路由器，5路由 `concept/method_selection/exercise/solution/courseware` | `route_for_query` |
| `app/artifacts/` | **可视化件** | `planner.py:1` Tier1 16规则，`spec.py:211` 8种 Widget 校验 |
| `app/linalg/` | **线代内核（亮点2）** | `matrix.py:56` `FracMatrix`，`ops.py:7` 8算子 `rref/.../quadratic_form`，`tool.py:53` `linalg_step_solve` |
| `app/tools/` | **工具注册** | `handlers.py:252` 6工具，`registry.py` 调度 |
| `app/rag/` | **白名单 RAG** | `KeywordRetriever` 排除 `.pem/.pyc` |
| `app/skills/` | **出题/方法选择/课件** | `method_selector.py` 决策树 |
| `app/static/` | **前端面板** | `panel.html/css/js` MathJax 渲染 |
| `app/stats/` | 统计计算 | 假设检验/回归 |
| `corpus/` | 语料（构建索引用） | `curated/public_main/` 129篇 已清洗 |
| `.data/` | 运行时数据 | `a2a.sqlite` / `trace.sqlite` / `eval_runs.jsonl` |
| `tests/` | 测试 | `802 passed` |
| `scripts/` | 脚本 | `build_corpus.py` `run_eval.py` `a2a_client.py` |
| `docs/` | 文档 | `acceptance_full.md` 九节 |
| `.venv/` | 虚拟环境 | 本地创建，勿提交 |

## 3. 快速开始

```powershell
cd E:\windows_ext\Desktop\智能体\xiaoyi-a2a-stat-tutor
py -m venv .venv
.\.venv\Scripts\python.exe -m pip install -e ".[test]"
.\.venv\Scripts\python.exe -m uvicorn app.main:app --reload --host 127.0.0.1 --port 8765
# 打开 http://127.0.0.1:8765/dashboard
```

## 4. 关键特性（中文要点）

### 4.1 教学脚手架（2026-10 新增，决赛差异化主线）

| 模块 | 作用 | 是否依赖模型 |
|---|---|---|
| `app/coach/ladder.py` | **帮助阶梯** L0–L4：复述 → 追问 → 提示 → 局部示范 → 完整解答。等级由确定性规则决定，模型只能在等级上限内作答 | 否 |
| `app/coach/misconceptions.py` | **误概念诊断**：10+ 条可审计规则（p 值含义、不显著=无差异、CLT、置信区间等），命中即给一个苏格拉底式追问 | 否 |
| `app/coach/store.py` | **过程证据**：每轮帮助等级、误区触发、求助信号落 SQLite，产出「帮助依赖度 / 独立推进率 / 反复误区」 | 否 |
| `app/verify/steps.py` | **逐步推导核对**：相邻两步在 9 个采样点上逐一验证，不一致时给出具体反例点；SymPy 可用时追加符号确认 | 否 |
| `app/ocr/service.py` | **拍照问疑**：DeepSeek Flash 原生识图 → 脱敏落盘 → 文本回填输入框；配套确定性聚类输出「共性疑问」 | 识图需模型 |
| `app/demo_cases.py` | **演示案例包**：9 个案例 + 一键跑确定性部分，彩排与现场断网可用 | 否 |

设计依据（研究结论，见 `docs/frontier_research_notes.md`）：普通 AI 工具能提升练习阶段的即时表现，却伴随撤去工具后的独立测试下降；
带教师设计的提示与学习保护的辅导方式没有这种损失。帮助阶梯就是把"给多少帮助"显式化、可审计化。

接口：

- `GET  /api/coach/cases`、`GET /api/coach/cases/{id}` — 演示案例
- `GET  /api/coach/profile?session_id=` — 学情画像
- `POST /api/coach/verify-steps` — 逐步核对
- `POST /api/coach/ocr`、`POST /api/coach/clusters` — 拍照问疑与共性聚类
- SSE 新增 `coach` 事件（帮助等级 + 误概念），前端渲染为侧栏卡片 + 回答下方旁注

### 4.2 原有能力

- **可视化（亮点1）**：`planner.py` 确定性选图 100%成功率，`spec.py` 9 种 `Widget` 校验（新增 `function_plot`：一次/二次/三次函数、顶点、对称轴、判别式），失败静默降级为纯文字
- **线代内核（亮点2）**：`Fraction` 精确算术 + `Step` 逐步记录 + `SymPy` 独立复算 `verified` 凭证
- **数值纪律**：`main.py` 硬规则 `linalg_step_solve` 为唯一数值权威，禁止模型口算
- **白名单 RAG**：`CORPUS_WHITELIST` 仅读授权目录，`self_note` 权重最高

## 5. 已清理

- 根目录 `_cdp_*.mjs` 372 个临时脚本 → 已归档至 `E:\windows_ext\Desktop\智能体\_归档_CDP脚本\`
- 临时文件 `_adp_state.png` `_save_body.json` 等 → 已归档
- `.venv` `__pycache__` 为缓存，勿提交

## 6. 维护

- 新增可视化：`planner.py:291` 加规则，`spec.py` 注册
- 新增算子：`linalg/ops.py:7` 实现，`linalg/tool.py:16` 注册
- 语料更新：修改 `CORPUS_WHITELIST` 后 `scripts/build_corpus.py` 重建
