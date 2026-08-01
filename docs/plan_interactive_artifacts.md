# 交互式可视化件 + Agent 核心重构 实施计划

## 一、这个计划要解决什么

**新功能**：Gemini 式交互可视化。拖动 μ、σ 看正态分布变形，选偏态总体看 CLT
把样本均值分布拉正态，拖 α 看功效怎么涨。走**分层**路线：预置件为主，
代码沙箱兜底（Tier 1 / Tier 2）。

**顺手补掉的硬伤**：一个统计学导师**不会算统计量**。当前 `app/` 里没有任何
统计计算，t 值、p 值、功效全靠 LLM 口算。交互可视化的本质就是
「参数 → 计算 → 图形」的实时闭环，所以计算层是它的地基，也是补这个硬伤的入口。

**同时要动的架构债**（用户已确认纳入范围）：

| 位置 | 问题 |
|---|---|
| `app/agents/router.py:42` | `route()` 是一串 `if any(k in q ...)`，加能力要改路由代码 |
| `app/agents/router.py:83` | `_concept()` 只有「中心极限定理」有正文，其余落通用占位模板 |
| `app/skills/exercise.py:21` | 整个题库 2 个模板（`clt`、`t_test`） |
| `app/skills/registry.py` | `SKILL_REGISTRY` 只被 `/api/panel/status` 展示，路由不消费，是死的 |
| `app/learning_store.py` | 只写不读，画像数据无消费方 |
| `app/panel_html.py` | 1155 行单个 Python 字符串，再加内容会爆到不可维护 |

LLM 当前的角色是「润色规则骨架」（`main.py:650` `build_model_messages`），
所以模型再强也突破不了骨架的天花板 —— 这是「没有逻辑」的根因。

## 二、参考的行业架构

这个方向已经标准化，不用自己发明协议：

- **MCP Apps（SEP-1865，状态 Final）**：`ui://` 预声明 UI 资源、工具通过 metadata
  引用、**强制 iframe 沙箱**、UI 与宿主走标准 JSON-RPC 双向通信、所有上行消息可审计。
- **MCP-UI**（Postman / HuggingFace / Shopify / Goose / ElevenLabs 已采用）：
  `rawHtml`（srcdoc 注入）/ `externalUrl` / `remoteDom` 三种内容类型；
  `tool` / `intent` / `prompt` / `notify` / `link` 五类上行动作。
- 两者共同的安全底线：**沙箱隔离 + 结构化事件是唯一上行通道**。

本计划直接借用这套形状：预声明件 + spec 引用（对应 Tier 1）、
sandbox iframe + 白名单 postMessage 动作（对应 Tier 2）。

## 三、目标架构

```
用户提问
   │
   ▼
┌─────────────────────────────────────────────────────┐
│ Agent Core（Phase 5 重构）                          │
│  Capability 声明式注册表                            │
│  ├─ LLMRouter    模型可用：structured output 选能力 │
│  └─ KeywordRouter 模型不可用：现有关键词逻辑兜底    │
└─────────────────────────────────────────────────────┘
   │
   ▼
┌─────────────────────────────────────────────────────┐
│ Tool Layer（Phase 0 + 5）                           │
│  stat_compute(func, args)   ← 新：权威统计计算      │
│  rag_retrieve(query)        ← 已有                  │
│  make_artifact(spec)        ← 新：Tier 1            │
│  write_artifact_code(intent)← 新：Tier 2            │
└─────────────────────────────────────────────────────┘
   │
   ▼
┌─────────────────────────────────────────────────────┐
│ Artifact Channel（Phase 2）                         │
│  面板 SSE：新增 event: artifact                     │
│  A2A：artifacts 字段 + 三级降级                     │
└─────────────────────────────────────────────────────┘
   │
   ├──► Tier 1：预置渲染器（statlib.js + canvas 原语）
   │      确定性 · 可评测 · 离线可用 · 永不渲染失败
   │
   └──► Tier 2：sandbox iframe + 调试台
          表达力无限 · 错误捕获 → AI 自修复回路
```

## 四、关键技术决策（先讲 Why）

### 4.1 计算层必须前后端各一份

拖动滑块要 60fps 重绘，**不可能每帧打后端**，所以前端必须能算。
但 LLM 答案里的数值（「p = 0.032」）必须是算出来的而非编的，评测集要能离线
断言精度，所以后端也必须能算。两份，且**逐函数对齐精度**。

- `app/stats/`（Python）— 权威层：LLM 工具调用、artifact 初始数据、单元测试基准
- `app/static/statlib.js` — 交互层：滑块实时重算

### 4.2 不引入 scipy

当前依赖是 fastapi / httpx / pymupdf / python-docx。scipy 会带上 numpy 整套，
Windows 上有 wheel 体积和编译工具链问题 —— README 里已经因为 chromadb/HNSW
需要 C++ 工具链而踩过坑，默认才退到 SQLite Keyword RAG。已确认本机 venv 无 scipy。

教学所需的分布函数用高精度有理逼近纯 Python 实现约 300 行，可精确测试。
以后要做真实数据分析再加 `[science]` optional-dependency。

**精度目标（写进测试，不是口头承诺）**：

| 函数 | 算法 | 目标精度 |
|---|---|---|
| `norm_cdf` | Cody / Hart 有理逼近 | \|ε\| < 1e-15 |
| `norm_ppf` | Acklam 逆正态 + 一步 Halley 精化 | 机器精度 |
| `t_cdf` `chi2_cdf` `f_cdf` | 不完全 beta / gamma，Lentz 连分数 | \|ε\| < 1e-12 |

> Abramowitz-Stegun 7.1.26 精度不够（只对 erf 到 1e-7），不采用。

**这是统计学导师的底线**：教学工具算错数比不算更糟，因为学生会把错的当标准答案。
测试方式是硬编码一张从 scipy 离线取的基准值表，断言 1e-10 级一致。

### 4.3 随机数必须可复现

教学场景的真实需求：学生看到有趣的模拟结果要能「再来一次一样的」，
也要能「换个种子看是不是巧合」。所以**不用 `Math.random()`**，
用带种子的 PCG32，前后端同算法同种子出同序列，`seed` 进 spec、进 trace，可完整重放。

Gemini / Claude Artifacts 都没做这件事（刷新就变），但统计教学必需。

### 4.4 不引入 D3 / Plotly / Chart.js

项目已有 vendor 本地化先例（katex / markdown-it / dompurify 都在
`app/static/vendor/`）。但 Plotly 3MB+，D3 API 面太大。

统计教学的图形需求很窄：坐标轴、曲线、直方图、阴影区域、散点、文本标注。
手写 canvas 原语约 200 行，完全可控。

**更关键的理由**：这套原语会注入给 Tier 2 的沙箱复用。
**给 LLM 一个小而稳的绘图 API，比让它自由用 D3 可靠得多** ——
生成失败率会显著下降，因为 API 面小到可以完整写进 prompt。

### 4.5 Tier 1 的 spec 契约：LLM 只填参数，不写代码

用 Pydantic 定义（项目已用 pydantic v2），JSON Schema 自动导出喂给 LLM
做 structured output：

```python
class WidgetSpec(BaseModel):
    widget: Literal["distribution-explorer", "clt-simulator", ...]
    title: str
    params: list[ParamSpec]        # 滑块 / 下拉 / 开关
    seed: int | None = None
    annotations: list[str] = []    # "68-95-99.7", "critical-region", ...
    teaching_note: str             # 这个件要讲什么
    misconception: str | None      # 显式绑定的误解 ID
```

**校验失败 → 降级到最接近的默认件或纯文本**。这就是「永不渲染失败」的来源：
LLM 不可能输出坏代码，因为它根本不输出代码。

### 4.6 Tier 2 沙箱安全（唯一的真实风险面，必须严格）

**iframe 属性**：`sandbox="allow-scripts"`，**绝对不加 `allow-same-origin`**。
两者同时出现时 iframe 内脚本可以移除自己父级的 sandbox 属性，等于完全没有沙箱。
这是最常见的致命配置错误。

**注入到生成 HTML 的 CSP**：

```
default-src 'none'; script-src 'unsafe-inline';
style-src 'unsafe-inline'; img-src data:; connect-src 'none'
```

`connect-src 'none'` 是关键：即使生成的代码里有 `fetch`，也发不出去。
一条规则同时解决「数据外泄」和「离线不可用」两个问题。

**后端静态检查**（新建 `app/render/artifact_lint.py`，复用 `latex_lint.py`
的模式与风格 —— 返回 issue 列表、不真执行、供离线断言）：

- 禁：`<script src=`、`import(`、`eval(`、`new Function`、`fetch(`、
  `XMLHttpRequest`、`WebSocket`、`Worker`、`localStorage`、`document.cookie`、
  `top.`、`parent.`
- 尺寸上限 64KB；必须含 `<canvas>` 或 `<svg>`（可视化件的最低要求）
- 有 issue 就不渲染，直接走「让 AI 修」回路

**postMessage 校验**：宿主用 `event.source === iframe.contentWindow` 判断来源。
**不能用 origin 校验** —— srcdoc + sandbox 的 origin 是 `null`，这是容易搞错的点。

上行动作白名单：`ready` / `error` / `log` / `resize` / `param-change` / `request-compute`。

### 4.7 `request-compute`：沙箱不给网络，但给受控计算 RPC

沙箱里的代码**不允许也不需要**自己实现 normal cdf —— LLM 手写的分布函数一定不准。
它只能通过 `request-compute` 请求宿主代理调用权威 `statlib`。

一个设计同时拿到三件事：安全（无网络）、离线可用（无 CDN）、数值正确（走权威层）。

### 4.8 调试回路（你点名要的"可以调试"）

```
生成 → lint → 渲染 → 运行时错误捕获 → 调试台显示
                              │
                    ┌─────────┴─────────┐
                    ▼                   ▼
              [让 AI 修]           [手动编辑代码]
                    │                   │
      code+error+stack → LLM → patch → 重渲染 (v2)
                    │
              最多自动修 2 次（防烧 token 死循环）
```

iframe 内注入的 error harness 要抓四类：

1. `window.onerror`
2. `window.addEventListener('unhandledrejection')`
3. 包裹 `console.error / warn / log`
4. **首屏 `ready` 超时（3s 没 ready = 白屏）** ——
   语法错误导致的白屏**不会**触发 `onerror`，只能靠超时兜住

**手动编辑**也要有：调试台带代码编辑区（`textarea` 够用，不引 Monaco，
保持零依赖），改完点「重新运行」。这才是完整的「可以调试」。

版本历史存 `artifact_store`，可 v1/v2/v3 切换对比。
全部挂现有 `trace_store` 的 span 机制（`start_tool_run("artifact_generate")`），
不新造观测设施。

### 4.9 小艺平台渲染能力：我不确定，所以做三级降级

**必须诚实说明**：我没有小艺开放平台富文本 / HTML 渲染能力的文档，搜索也没找到。
所以不能假设它支持交互 iframe。设计上做**能力协商 + 三级降级**：

| 宿主能力 | 呈现方式 |
|---|---|
| 本地面板 / WebView | 完整交互 iframe |
| 只支持图片 | 服务端渲染静态 SVG（纯 Python 字符串拼接，无 headless browser），给几帧关键参数对比图 |
| 只支持纯文本 | 降级为文字描述 + 关键数值表 |

`initialize` 时读客户端 capabilities，或用 `ARTIFACT_MODE` 环境变量强制。

SVG 降级是纯 Python、零依赖、可单元测试 —— 附带好处是**没有浏览器的评测环境
也能验证可视化的数值正确性**。

### 4.10 先拆前端，否则后面每一步都在往巨型字符串里塞代码

`app/panel_html.py` 已经 1155 行单个 Python 字符串。加 artifact 展示区 +
调试台 + 10 个件的渲染器会爆到 5000+ 行，不可维护。

拆成：`app/static/panel/{index.html,panel.css,panel.js}` +
`app/static/widgets/*.js`，`panel_html.py` 退化成薄壳或改 `FileResponse`。

`tests/test_panel.py` 断言了 HTML 内容（`"function renderMarkdown" in response.text`
等 14 条），要同步改成读取静态文件。这是 Phase 0 的一部分，不能拖。

## 五、分阶段实施

整体约 6600 行新代码。**这不是一次对话能完成的**，建议一个 Phase 一轮，
每个 Phase 结束都能独立跑测试、独立 demo。

### Phase 0：地基 —— 统计计算层 + 前端拆分

不碰 LLM，纯离线可测。

| 文件 | 内容 |
|---|---|
| `app/stats/special.py` | `erf` `erfc` `lgamma` `betainc` `gammainc`（Lentz 连分数） |
| `app/stats/distributions.py` | norm / t / chi2 / f / binom / poisson / exp / beta 的 `pdf` `cdf` `ppf` |
| `app/stats/tests.py` | `welch_t` `student_t` `paired_t` `chi2_indep` `anova_oneway` `pearson` `spearman` |
| `app/stats/power.py` | 功效 / 样本量反解 |
| `app/stats/rng.py` | PCG32 可复现 PRNG + 采样器（Box-Muller、逆变换、拒绝采样） |
| `app/static/panel/*` | 从 `panel_html.py` 拆出 html / css / js |

测试：`tests/test_stats_accuracy.py`（硬编码 scipy 基准值表，断言 1e-10）、
`tests/test_rng_reproducible.py`（同种子同序列）、改造 `tests/test_panel.py`。

**验收**：`pytest` 全绿；面板功能与拆分前完全一致（无回归）。

### Phase 1：前端计算层 + 第一个件

| 文件 | 内容 |
|---|---|
| `app/static/statlib.js` | 与 Phase 0 逐函数对齐的 JS 版 + PCG32 |
| `app/static/plot.js` | canvas 绘图原语（约 200 行）：坐标轴、曲线、直方图、阴影、散点、标注 |
| `app/static/widgets/distribution-explorer.js` | 第一个件：拖 μ σ 看密度变形 |

测试：`tests/fixtures/statlib_parity.json`（一张输入输出表），
Python 和 Node 各自断言同一张表 —— Node v24 已确认可用。

**验收**：面板能手动挂出一个能拖的正态分布图；前后端计算一致。

### Phase 2：Artifact 通道打通

| 文件 | 内容 |
|---|---|
| `app/artifacts/spec.py` | Pydantic `WidgetSpec` + JSON Schema 导出 |
| `app/artifacts/store.py` | 版本历史（v1/v2/v3） |
| `app/artifacts/svg.py` | 纯 Python SVG 降级渲染 |
| `app/main.py` | SSE 新增 `event: artifact`；A2A 加 `artifacts` 字段 + 三级降级 |

**验收**：一句「画个正态分布让我拖 μ」端到端出交互图；
`ARTIFACT_MODE=svg` 时降级为静态图；`=text` 时降级为数值表。

### Phase 3：剩余 9 个件

按「能纠正哪个具体统计学误解」排序 —— 你已确认全都要：

| 件 | 纠正的误解 |
|---|---|
| `clt-simulator` | 「原始数据会变正态」/「n>30 就保证正态近似」（README 已点名） |
| `hypothesis-test-visualizer` | p 值的含义、α 与功效的权衡 |
| `ci-coverage-simulator` | 「95% CI 意味着参数有 95% 概率在里面」 |
| `power-sample-size` | 样本量 / 效应量 / α / power 四角关系 |
| `regression-playground` | 离群点与杠杆点的影响、R² 的误读 |
| `p-hacking-demo` | 多重比较、选择性报告 —— 与 `guard.py` 的 `statistical_integrity` 呼应 |
| `lln-vs-clt` | 大数定律与 CLT 的混淆 |
| `bootstrap-visualizer` | 重抽样分布的含义 |
| `bayes-updating` | 先验 → 后验的更新直觉 |

**验收**：每个件有独立 spec 样例 + SVG 降级 + 一条 golden 集意图样本。

### Phase 4：Tier 2 代码沙箱 + 调试回路

| 文件 | 内容 |
|---|---|
| `app/render/artifact_lint.py` | 静态安全检查（4.6 的禁用清单） |
| `app/static/panel/sandbox.js` | iframe 沙箱 + harness 注入 + postMessage 协议 |
| `app/static/panel/devtools.js` | 调试台：错误列表 / 代码编辑 / 版本切换 / 让 AI 修 |
| `app/main.py` | `/api/artifact/compute` 代理端点（`request-compute` 落地） |

测试：`tests/test_artifact_lint.py` —— **恶意代码样本必须被拦**
（`fetch`、`<script src>`、`eval`、`parent.` 各一条）。

**验收**：故意让 LLM 生成一段有 bug 的可视化，调试台抓到错误，
点「让 AI 修」后 v2 正常渲染；手动改代码也能重跑。

### Phase 5：路由与 Agent 核心重构

```python
@dataclass(frozen=True)
class Capability:
    name: str
    description: str            # 给 LLM 看，用于意图选择
    keywords: tuple[str, ...]   # 离线兜底
    handler: Callable
    tools: tuple[str, ...]      # 这个能力可用哪些工具
    produces_artifact: bool
```

- `app/agents/capabilities.py` — 注册表，升级现有 `SKILL_REGISTRY`（让它真正被消费，不再是死的）
- `app/agents/router.py` — `LLMRouter`（structured output 选能力）+ `KeywordRouter`（现有逻辑保留为兜底）
- `app/model_client.py` — 加 `complete_with_tools`（DeepSeek 兼容 OpenAI function calling）
- `learning_store` 开始被读：根据画像推荐「下一个该看哪个件」

**为什么重构放最后**：Phase 0–4 可以先在现有路由上挂一个 `visualize` 分支跑通。
先用垂直切片验证功能、再重构承载它的骨架，比先重构空骨架风险低得多。

**接缝预留**：Phase 0–4 期间所有 handler 都按 `Capability` 的形状写
（同签名、同返回类型），Phase 5 只换路由分派，不改 handler 内部。

## 六、测试与评测闭环

项目已有 `eval/golden.jsonl` + `scripts/eval_gate.py` 红绿灯，可视化必须进这个闭环，
否则会变成「看起来能跑但没人知道对不对」的功能。

| 测试 | 断言什么 |
|---|---|
| `test_stats_accuracy.py` | 对齐硬编码 scipy 基准值，1e-10 |
| `test_statlib_parity.py` | 前后端同函数同输入结果一致（Python + Node 各跑一遍同一张 fixture） |
| `test_rng_reproducible.py` | 同种子出同序列，跨语言一致 |
| `test_artifact_lint.py` | 恶意代码样本必须被拦 |
| `test_widget_spec.py` | spec 校验通过 / LLM 输出畸形时正确降级 |
| `test_artifact_svg.py` | SVG 降级路径的数值正确性（无浏览器环境可跑） |
| `eval/golden.jsonl` | 可视化意图样本：路由到 `visualize` + 选对件 |

## 七、风险与不确定项

**我确认过的**：
- Node v24.14.0 可用（跑 JS parity 测试）
- venv 无 scipy（所以基准值表必须离线取好硬编码，不能运行时依赖）
- 项目已有 vendor 本地化先例，离线策略成立

**我没有验证、需要你确认或后续查证的**：
1. **小艺平台是否支持渲染交互 HTML** —— 没找到文档。三级降级是为此做的保险，
   但如果平台完全不支持，Tier 2 就只在本地面板/WebView 有意义。
2. **DeepSeek `deepseek-v4-flash` 的 structured output / function calling 支持程度** ——
   Phase 5 的 LLM 路由依赖这个。若不稳，退回「JSON mode + 严格校验 + 关键词兜底」。
3. **`.tmp_*` 临时文件与 `debug_etsu.html`**（项目根目录 20 个左右）——
   看着是上一轮调试残留。要不要清掉是你的决定，我不会主动删。

**明确的取舍**：
- 手写绘图原语 = 少依赖、可控、Tier 2 生成成功率高；代价是图形样式没有 D3 丰富
- 纯 Python 统计 = 零编译依赖、可测；代价是不支持大规模数值计算（教学场景够用）
- Tier 1 为主 = 稳定可评测；代价是预置清单外的需求要落到 Tier 2，质量取决于模型

## 八、建议的起手式

Phase 0 是纯地基、零 LLM 依赖、完全可测，且**它是后面所有 Phase 的前提**
（前端拆分不做，后面每步都在往 1155 行字符串里塞代码；计算层不做，
可视化就只能画假数据）。

建议这一轮先把 Phase 0 做完并跑绿测试，再决定 Phase 1 的节奏。
