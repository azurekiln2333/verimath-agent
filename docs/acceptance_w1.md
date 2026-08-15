# W1 验收报告（docs/acceptance_w1.md）

日期：2026-08-15
范围：线代计算内核 + 出题验算闭环 + caveman-lite 风格（GRILLING_REPORT Q7 约定项）

## 验收清单

| 项 | 约定 | 实测 | 结论 |
|---|------|------|------|
| 现有测试回归 | 38 个旧测试不因 W1 失败 | 729 passed / 5 failed；5 个失败经 git worktree 在干净 HEAD 上复现 4 个，第 5 个（`test_artifact_host_is_outside_the_streaming_bubble`）由工作区既有的未提交面板重设计导致（`app/panel_html.py` 工作区 diff 3108 行，非 W1 改动；W1 仅加 1 个按钮 + 2 条 i18n） | 通过（零新增失败；5 个旧伤列入 W2 重构范围） |
| linalg parity 测试 | 每算子 ≥3 例，Fraction 内核 vs SymPy 独立复算 | `tests/test_linalg_ops.py` 29 例：rref/rank 5、det 5、inverse 3、solve 4、eigen 4、spaces 2、步骤记录 2；全部通过，verified 标志全部为真 | 通过 |
| 出题验算闭环 | 坏答案回喂重试 ≤3 轮，仍败回退模板 | `tests/test_exercise_verify.py` 4 例：坏→好重试、3 败回退模板、无 answer_check 放行、重试计数；全部通过 | 通过 |
| eval seeds | ≥50 条 | `eval/seeds_linalg.jsonl` 50 条（det 12 / rank 8 / inverse 10 / rref 10 / solve 10），答案全部由内核 Fraction 计算 | 通过 |
| demo 脚本 | 3 个 | `scripts/demo_linalg.py`：3x3 求逆、2x2 特征值（含可对角化判定）、含自由变量方程组（通解+基础解系），逐步输出 + SymPy 复算凭证 | 通过 |

## 交付物清单

- `app/linalg/`：matrix.py（FracMatrix + Step）、ops.py（rref/rank/det/inverse/solve/eigen/null_space/column_space，全部带 SymPy 复算凭证）、tool.py（`linalg_step_solve` 工具 + `verify_answer` 出题验算）
- `app/tools/handlers.py`：工具注册（第 6 个工具）
- `app/skills/exercise.py`：`generate_exercise_with_model` 升级为验算闭环（≤3 轮回喂，模板兜底）
- `app/main.py`：数值纪律硬规则进 Agent system prompt；`caveman` 风格注册（第 4 档，非默认）
- `app/panel_html.py`：风格按钮"极简/Terse"（中英 i18n）
- `pyproject.toml`：`[linalg]` optional 依赖（sympy>=1.13）
- `eval/seeds_linalg.jsonl`、`scripts/gen_linalg_seeds.py`、`scripts/demo_linalg.py`

## 已知遗留（进入 W2）

1. 5 个基线失败测试（面板重设计未完成 + prompt 文案断言漂移），随 W2 面板静态化一起收口。
2. `verify_answer` 支持 det/rank/inverse/rref 四算子；solve/eigen 答案结构复杂，W2 再接。
3. 工作区存在本会话之外的未提交改动（`app/static/icons.js`、`_css_check.py`），提交前需与负责人确认归属。
