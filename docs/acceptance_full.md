# 全量验收报告（docs/acceptance_full.md）

日期：2026-08-16（W1 验收 2026-08-15 之后的全量收口）
范围：W1 线代内核 + W2 高代扩展 + W3 GateCraft 化 + 面板静态拆分 + 评测集 + 冗余清理（GRILLING_REPORT 全项）

## 0. 一句话

把 xiaoyi-a2a-stat-tutor 重构为 GateCraft 理念的数理统计学习导师：
**LLM 解释、代码计算、一切数值经内核复算并出凭证**。四层结构全部落地：
测试 802 全绿，双评测 gate 绿，答案基准 65/65。

## 1. 验收清单

| 项 | 约定 | 实测 | 结论 |
|---|------|------|------|
| 全量测试回归 | 旧测试不因 W1/W2/面板拆分失败 | **802 passed / 0 failed**（772 基线 + W2 30 例） | 通过 |
| linalg parity | 每算子 ≥3 例，Fraction 内核 vs SymPy 独立复算 | test_linalg_ops.py 29 例 + test_linalg_w2.py 30 例；全部 verified | 通过 |
| W2 Jordan | 块结构/过渡矩阵/相似不变量复算 | 8 用例：不可对角化 2x2、可对角化、幂零 3x3、混合块、复数根 ±i、教材例、不可约特征多项式（λ³-2 友矩阵） | 通过 |
| W2 二次型 | 标准形/惯性指数/符号差/正定性 | 12 用例：正定/负定/不定/半正定/零矩阵/3x3/表达式路径（Hessian/2）/非对称拒绝 | 通过 |
| verify_answer 扩展 | 新算子可验算 | jordan（相似不变量，块序无关）、quadratic_form（"p,q" 或关键词）、solve 解型扩展（唯一/无解/无穷特解回代） | 通过 |
| 评测集 | ≥50 条 + 笔记来源 | seeds_linalg.jsonl **65 条**（内核答案基准 65/65）；seeds_gaodai.jsonl **36 条**（高代笔记来源，自检全过） | 通过 |
| 双 gate | golden + 高代 无退化 | golden 30 条：route 1.0 / retrieval 1.0 / guard 1.0 [GREEN]；gaodai 36 条：三项全 1.0 [GREEN] | 通过 |
| demo 脚本 | 可复现冒烟 | demo_linalg.py（5 算子）、gen_linalg_seeds.py、gen_gaodai_seeds.py（幂等）、run_linalg_eval.py、run_eval.py、eval_gate.py | 通过 |
| 面板静态拆分 | 单字符串 → app/static/ | panel.html(396) + panel.css(1487) + panel.js(1521)；panel_html.py 降为只读装配器；测试改读静态文件 | 通过 |
| 冗余清理 | Q2 批准清单 | enhance_with_model/_attach_tier2_artifact/learning_path 已删（上一会话，含 9 个 .tmp_* 日志）；本会话：.tmp_vendor 缓存目录、out.log、_css_check.py、面板单字符串 | 通过 |

## 2. 交付物清单

### W2 高代扩展
- app/linalg/ops.py：+jordan()（特征多项式→核维数序列→块结构→J→广义特征向量链 P→相似不变量复算）、+quadratic_form()（对称矩阵/表达式→特征值→Gram-Schmidt 正交对角化→标准形→秩/p/q/符号差→正定性，SymPy is_positive_definite 复算）；eigen 复算升级为逐 λ 判零（三层验证）
- app/linalg/tool.py：_OPERATIONS +2；run() 支持 expression；verify_answer +_verify_jordan/_verify_qf；_verify_solve 支持无解/无穷解
- app/linalg/__init__.py：导出 +2
- app/skills/solution_writer.py：离线直答 +2 算子；SOLUTION_GUIDE 更新
- app/skills/registry.py：solution 关键词 +17（jordan/若尔当/若当/标准形/二次型/惯性指数/符号差/正定/负定/半正定/配方法/施密特/线性相关/基变换/过渡矩阵/线性方程组/对角化）
- app/skills/exercise.py、app/skills/courseware.py：answer_check 算子枚举 +2
- scripts/demo_linalg.py：demo 3→5 算子

### 评测集（笔记来源，GRILLING_REPORT Q6）
- scripts/gen_gaodai_seeds.py：从 腾讯云/知识库语料/高等代数 19 篇笔记提取 36 条 golden 格式查询；tags 前缀进语料；幂等重建（source 前缀 gaodai_notes:）；生成时自检路由一致性 + 检索命中
- eval/seeds_gaodai.jsonl：36 条（计算类→solution、概念类→concept，含标签驱动查询）
- scripts/run_linalg_eval.py：答案基准回归端
- scripts/gen_linalg_seeds.py：+W2 手工精选（jordan ×7、quadratic_form ×8）；expected 格式与验算器对齐
- eval/golden.jsonl：learning_path 4 条改 concept/method_selection（Q2 删路由后意图落盘）；g-concept-10 贝叶斯 must_retrieve=false
- .env：CORPUS_WHITELIST 改为 我的笔记库 + 腾讯云/知识库语料（旧路径指向不存在的 个人/学习 目录）；语料重建 1411 chunks

### 面板静态拆分（Q2 批准）
- app/static/panel.html、panel.css、panel.js：单字符串 3409 行 → 三文件
- app/panel_html.py：只读装配器（PANEL_HTML 契约不变）
- tests/test_panel_artifacts.py、tests/test_panel.py：断言改读静态文件 + /static 端点

### 文档
- 本文件；docs/acceptance_w1.md（W1 验收，保留）

## 3. 数值纪律与防幻觉（GateCraft 核心）

1. 一切矩阵/统计数值由 app/linalg、app/stats 内核（Fraction 精确）计算；
2. 每个 LinalgResult 带 SymPy 独立复算凭证（verified 标志），不一致绝不标 verified；
3. 出题/课件 answer_check 过 verify_answer，≤3 轮回喂重生成，仍败回退模板；
4. Agent system prompt 硬规则：禁止模型口算数值，必须调用 linalg_step_solve；
5. 验算凭证渲染进步骤 Markdown（✅ 已用 SymPy 独立复算）。

## 4. 复现命令

    # 全量测试
    .venv\Scripts\python.exe -m pytest tests -q
    # 评测 gate（双集）
    .venv\Scripts\python.exe -m scripts.eval_gate --input eval/golden.jsonl
    .venv\Scripts\python.exe -m scripts.eval_gate --input eval/seeds_gaodai.jsonl
    # 答案基准 + 种子再生
    .venv\Scripts\python.exe scripts\run_linalg_eval.py
    .venv\Scripts\python.exe scripts\gen_linalg_seeds.py
    .venv\Scripts\python.exe scripts\gen_gaodai_seeds.py
    # 演示
    .venv\Scripts\python.exe scripts\demo_linalg.py
    # 服务
    .venv\Scripts\python.exe -m uvicorn app.main:app --port 8765

## 5. 已知边界（诚实声明）

1. **配方法未实现为独立算法**：二次型标准形走正交对角化（特征值路径），配方法仅作关键词路由；对有理数系数的教学例等价。
2. **Jordan 的 P 构造**：广义特征向量链失败时回退 SymPy jordan_form 的 P；J 与 verified 不依赖 P（相似不变量独立复算）。
3. **不可约特征多项式**（如 λ³-2 友矩阵）：J 与块结构正确且 verified，但 P 可能含复杂根式/复数（SymPy 输出）。
4. **贝叶斯主题不在本地语料**：golden g-concept-10 诚实标注 must_retrieve=false。
5. **语料白名单已改**（.env CORPUS_WHITELIST）：旧的 个人/学习 目录不再入库，以 我的笔记库 + 腾讯云/知识库语料 为准（与 ADP 比赛版知识库对齐）。
6. **面板静态拆分后** JS/CSS 走 /static；本地开发改文件后硬刷新即可。

## 6. 提交归属说明

- app/static/icons.js 新增 10 个图标（person/chevron_right/check_circle/...）：上一会话面板重设计的组成部分，随本次提交入库。
- _css_check.py（localhost:8000 CSS 调试脚本）：一次性调试产物，已删除。
- 工作区未提交改动全部归属本项目重构，统一提交。