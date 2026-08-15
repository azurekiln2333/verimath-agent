# GRILLING_REPORT.md — 小艺架构重构 W1 共识落盘

日期：2026-08-15
状态：用户已确认，进入实施

## 1. 最终设计树

```
交付物定位
├── 主产品 A：逐步解答 + 验算证明（学生贴题 → 步骤展示 + SymPy/Fraction 复算凭证）★W1
├── 副产品 B：课件/讲义生成（A 的排版扩展，七段式结构）★W3
└── 建模项目报告 C：仅保留最小 projects/ 状态机（比赛叙事用，非主产品）
架构
├── calc 确定性计算层（全系统唯一数值来源 = 数值纪律）
│   ├── stats（现有 app/stats 平移）
│   └── linalg（W1：rref/det/inverse/solve/eigen/rank/spaces；W2：Jordan/二次型）
├── skills 技能包（manifest + handler + selfcheck）
├── 回答路径收敛：5 条 → 2 条（单轮 agent loop / 多阶段 project）
└── 答疑风格：rigorous(默认)/examples/concise/discuss/caveman-lite(新增第4档)
```

## 2. 问答记录（R1）

| # | 问题 | 用户裁决 |
|---|------|---------|
| Q1 | 核心交付物 | **A 逐步解答+验算证明 为主，B 课件/讲义 为副**；C 不作主产品 |
| Q2 | 删除清单 | 听推荐：删 `enhance_with_model`、`_attach_tier2_artifact`、`learning_path` 路由、`panel_html.py` 单字符串、`.tmp_*` 日志 |
| Q3 | SymPy 安装 | 听推荐：装进 venv，pyproject 加 `[linalg]` optional |
| Q4 | caveman-lite 默认值 | 听推荐：不改默认（rigorous 仍默认），加第 4 档面板可选 |
| Q5 | 线代范围 | 听推荐：W1 核心（rref/det/inverse/eigen/rank/基础解系/列空间），W2 高代扩展（Jordan/二次型） |
| Q6 | 笔记评测集 | 听推荐：W1 用高代目录，50 条起步，概率论留 W2 |
| Q7 | 验收标准 | 听推荐：38 现有测试全绿 + linalg parity（每算子≥3例）+ 出题验算闭环测试 + eval seeds ≥50 + demo 脚本 3 个，写入 docs/acceptance_w1.md |
| Q8 | projects/StageRunner | 听推荐：保最小版（SQLite 状态表 + 一个门） |

## 3. 共识摘要

1. 差异化核心 = "LLM 解释、代码计算"：回答中数值断言必须来自 calc 工具，禁止模型口算。
2. 主产品是逐步解答+验算凭证，不是聊天；课件是其排版变体。
3. 数值纪律：出题答案必须过 SymPy/Fraction 复算，不一致回喂重生成，≤3 轮，仍败回退模板。
4. caveman-lite 只压缩连接性文字，数学内容（公式/条件/边界）永不压缩。
5. 冗余路径收敛后，行为以现有测试 + eval 基线守护，先建基线再动主链（W2）。

## 4. 被否决的备选方案

- 交付物"三线并做"（A+B+C 全量）：W1-W3 工期不容，C 降为最小状态机。
- 直接引入开源逐步求解库（mathy 等）：无高星成熟库，RL 方向不可用；改为 SymPy 内核 + 自写 StepRecorder。
- 用笔记微调模型：无必要不可行；笔记仅作评测集来源。
- caveman-lite 作默认风格：教学场景严谨优先，否决。
