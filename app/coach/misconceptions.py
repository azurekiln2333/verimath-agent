"""误概念诊断：从学生的自然语言里识别"哪一步想错了"，而不是只判对错。

为什么值得单独做一层：研究反复显示，判对错只会强化错误推理——
学生答对但方法错时，直接说"对了"等于把错误固化。真正有价值的反馈是
**命名错误类型 + 给一个只揭穿该类错误、不揭穿答案的追问**（见 §追问生成）。

实现取舍：用可审计的关键词/正则规则表，而不是小模型分类器。
- 规则表可以被教师阅读和修改，符合"教师审核"的产品定位；
- 命中即给出可复现解释，演示时不依赖网络；
- 规则必然有漏网，因此每个误概念都带 confidence，且低置信度不参与
  "帮助阶梯"降级（见 coaching.py）。

规则写法：每条规则声明 required（至少命中一个）与 forbidden（命中则否决），
避免"t 检验"这个词一出现就误报"把 t 检验当万能工具"。
"""

from __future__ import annotations

import re
from dataclasses import dataclass, field


@dataclass(frozen=True)
class Misconception:
    """一条误概念规则。

    id      稳定标识，前端用于去重与统计（写进学习档案）
    name    学生看得懂的中文名
    domain  stats / probability / algebra / inference
    why     为什么这是错的（一句话，直击要害）
    probe   针对性的苏格拉底式追问（只问、不答）
    required/forbidden  触发条件
    """

    id: str
    name: str
    domain: str
    why: str
    probe: str
    required: tuple[str, ...] = ()
    forbidden: tuple[str, ...] = ()
    max_len: int | None = None     # 只在长问题里触发（短问句容易误触）


# 关键词一律小写匹配；中文不需要词边界，英文用负向断言避免子串误伤
_RULES: tuple[Misconception, ...] = (
    Misconception(
        id="p_is_h0_prob",
        name="把 p 值当成 H₀ 为真的概率",
        domain="inference",
        why="p 值是「假定 H₀ 成立时，观察到当前或更极端结果的概率」，"
            "不是「H₀ 为真的概率」。方向恰好相反。",
        probe="如果 H₀ 是真的，我们做很多次实验，p 值大体上会怎么分布？"
              "为什么这个分布的形状正好说明 p 值不是「H₀ 为真的概率」？",
        required=("p值", "p 值", "p<", "p <", "p-值"),
        forbidden=("h0为真时", "h0 为真时", "零假设成立时", "h0成立时"),
        max_len=24,
    ),
    Misconception(
        id="p_is_error_rate",
        name="把 p=0.03 理解为「3% 的概率判断错了」",
        domain="inference",
        why="p=0.03 说的是「H₀ 成立时出现这种数据的可能性小」，"
            "不是「这次判断犯错的概率」。错误率要看 α 与第二类错误的选择。",
        probe="假设全世界有 1000 个研究，其中 900 个 H₀ 其实是真的。"
              "单靠 p<0.05 这一条，你能算出「判错的比例」吗？还缺什么信息？",
        required=("p值", "p 值"),
        forbidden=(),
        max_len=None,
    ),
    Misconception(
        id="fail_to_reject_means_equal",
        name="「不显著」= 证明没有差异",
        domain="inference",
        why="不显著只说明当前样本下没有足够证据拒绝 H₀；"
            "样本小、噪声大时，真实差异也可能检测不到。这是「证据不足」，不是「证明无」。",
        probe="如果两组真的差 0.1，但每组只有 5 个人，结果「不显著」。"
              "此时更合理的结论是「没有差异」，还是「证据不够」？怎么区分这两种情况？",
        required=("不显著", "没有显著"),
        forbidden=("功效", "样本量", "证据不足", "证据不足"),
    ),
    Misconception(
        id="clt_raw_data",
        name="以为中心极限定理让原始数据变成正态",
        domain="probability",
        why="CLT 说的是「和 / 均值的抽样分布」趋近正态，不是原始数据本身趋近正态。"
            "原始数据完全可以一直偏态。",
        probe="如果总体是严重的指数分布，抽 100 个样本、每个样本 n=50。"
              "哪条分布会接近正态：原始 5000 个数据，还是 100 个样本均值？为什么？",
        required=("中心极限定理", "clt"),
        forbidden=("原始数据不变", "原始数据不会", "均值的分布", "样本均值"),
        max_len=None,
    ),
    Misconception(
        id="n30_magic",
        name="把「n>30」当成正态近似的万能门槛",
        domain="probability",
        why="n>30 只是常见经验规则，前提是总体分布不太极端。"
            "重尾或强偏态时，30 远远不够；反过来，总体接近正态时 n=10 也许可以。",
        probe="你能不能构造一个总体：它的均值在 n=100 时抽样分布依然明显偏斜？"
              "提示：想想极端值出现的概率。",
        required=("大于30", ">30", "≥30", "n=30", "样本量30", "大样本"),
        forbidden=("经验规则", "不是定理", "误区"),
    ),
    Misconception(
        id="ci_prob_contains",
        name="把 95% 置信区间理解为「参数在其中概率 95%」",
        domain="inference",
        why="频率学派下参数是固定的，区间是随机的。95% 指的是"
            "「重复抽样得到的区间中，约 95% 会覆盖真值」。所以一个已经算出的区间，"
            "要么覆盖、要么不覆盖。",
        probe="如果某位实验者已经算完区间，他还能说「有 95% 的概率参数在里面」吗？"
              "这里的 95% 到底是对谁说的？",
        required=("置信区间", "95区间", "95%区间"),
        forbidden=("覆盖了", "覆盖真值"),
    ),
    Misconception(
        id="correlation_causation",
        name="把相关当作因果",
        domain="stats",
        why="相关只说明两者同向变化，可能有第三变量、反向因果或纯巧合。"
            "因果需要实验或更强的识别假设。",
        probe="如果冰淇淋销量和溺水人数高度相关，你能说「吃冰淇淋导致溺水」吗？"
              "还有哪种解释同样能产生这条相关？",
        required=("相关", "相关系数"),
        forbidden=("因果", "混淆变量", "第三变量", "相关性分析", "相关关系是什么"),
    ),
    Misconception(
        id="t_power_universal",
        name="默认 t 检验适用于所有两组比较",
        domain="stats",
        why="t 检验需要近正态或较大样本；配对设计与独立两组用的也不一样；"
            "方差差得远时要用 Welch。选检验前先看设计。",
        probe="在选检验之前，你能不能先回答三个问题：两组是独立还是配对？"
              "观测是连续还是等级？样本量大概多少？",
        required=("两组", "均值比较", "比较均值"),
        forbidden=("配对", "welch", "mann", "wilcoxon", "非参数",
                   "用什么", "应该用", "该用", "选什么", "怎么选",
                   "是不是一定", "都能用", "都可以", "都用"),
    ),
    Misconception(
        id="det_zero_means",
        name="「行列式为 0 = 矩阵为 0」",
        domain="algebra",
        why="行列式为 0 只说明矩阵不可逆（行/列线性相关，把空间压扁），"
            "矩阵本身完全可以非零。",
        probe="举一个 2×2 的、元素都不是 0、但行列式恰好为 0 的矩阵。"
              "它在几何上把平面变成了什么？",
        required=("行列式为0", "行列式=0", "det=0", "det = 0", "行列式为零"),
        forbidden=("矩阵为0", "零矩阵"),
    ),
    Misconception(
        id="square_root_squared",
        name="√(x²) = x",
        domain="algebra",
        why="√(x²) = |x|。x 为负时，两侧符号相反。",
        probe="把 √(x²) 看成「x 到原点的距离」。距离可能是负数吗？"
              "那 x = -3 时，根号里的 9 开出来后等于几？",
        required=(),
        forbidden=(),
        max_len=None,
    ),
    Misconception(
        id="mean_of_means",
        name="忽略各组样本量直接把组均值平均",
        domain="stats",
        why="各组样本量不同时，总体均值要按样本量加权，否则会被小样本组带偏。",
        probe="A 组 100 人、均值 80；B 组 2 人、均值 100。"
              "把两组合并后，均值更接近 80 还是 90？为什么？",
        required=("平均", "均值"),
        forbidden=("加权", "权重", "样本量不同"),
    ),
)


def _has(text: str, keywords: tuple[str, ...]) -> bool:
    return any(k in text for k in keywords)


def diagnose(text: str) -> list[Misconception]:
    """返回问题里命中的误概念（按规则表顺序，去重）。

    只做"提及级"判断：学生提到 p 值与概率的关系，才提示 p 值的误读。
    不试图判断学生究竟懂不懂 —— 那是教学现场的事，机器只负责问对的问题。
    """
    q = (text or "").lower()
    hits: list[Misconception] = []
    for rule in _RULES:
        if rule.required and not _has(q, rule.required):
            continue
        if rule.id == "square_root_squared":
            # 只有真正写出 √(x²)=x 这种式子时才触发，不因出现"根号"就报
            if not re.search(r"√\s*\(?\s*[a-z]\s*\^\s*2\s*\)?\s*=", q):
                continue
        if rule.forbidden and _has(q, rule.forbidden):
            continue
        if rule.max_len is not None and len(q) > rule.max_len:
            continue
        hits.append(rule)
    return hits


def render_misconceptions(hits: list[Misconception]) -> str:
    """把命中结果渲染成教学旁注（不打断主回答，放在回答末尾）。"""
    if not hits:
        return ""
    lines = ["**🔍 这条问题里有一个容易混淆的点**", ""]
    for m in hits:
        lines.append(f"- **{m.name}** —— {m.why}")
        lines.append(f"  > {m.probe}")
    return "\n".join(lines)


__all__ = ["Misconception", "diagnose", "render_misconceptions"]
