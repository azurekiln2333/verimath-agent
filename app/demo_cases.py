"""演示案例包：把学生真实的学习现场固化成可一键回放的脚本。

为什么需要它：决赛现场最怕三件事 —— 网络抖动、模型延迟、演示跑偏。
这里把每个案例拆成「输入 + 期望发生的教学动作」，案例本身不依赖模型：
帮助阶梯、误概念、推导核对、函数图像都是确定性路径，断网也能演。

案例分四组，对应用户最关心的四个差异化机制：
    ladder    帮助阶梯：同一道题，学生越卡，帮助级别越高
    verify    推导核对：错误出在哪一步，反例是什么
    viz       可视化：函数图像 / 统计分布
    photo     拍照问疑：手写题 → 文本 → 继续追问

每个案例都标注 triggers（点哪里能看到），方便彩排时按图索骥。
"""

from __future__ import annotations

from dataclasses import asdict, dataclass, field
from typing import Any

from app.coach.ladder import LadderState, decide
from app.coach.misconceptions import diagnose
from app.ocr.service import cluster_texts
from app.verify import check_steps


@dataclass
class DemoCase:
    id: str
    group: str
    title: str
    question: str
    expect: str
    checks: list[str] = field(default_factory=list)
    note: str = ""


CASES: tuple[DemoCase, ...] = (
    # ---------------------------------------------------------- 帮助阶梯
    DemoCase(
        id="ladder-01",
        group="ladder",
        title="同一道题，三次「不懂」",
        question="证明 x^2 - 1 = (x-1)(x+1)",
        expect="先解释证明的切入点；追问「还是不懂」时承接前文换一种解释；"
               "要求「展开完整步骤」时给出可核对的推导。帮助等级仅作参考。",
        checks=[
            "连续追问会带着前面的问答重新调用模型",
            "解释与当前卡点相关，侧栏追问沿用本轮回答",
            "明确要求完整步骤后，不被帮助等级限制",
        ],
        note="演示要点：观察模型能否承接具体卡点；等级变化不代表回答深度的硬上限。",
    ),
    DemoCase(
        id="ladder-02",
        group="ladder",
        title="概念提问不刁难",
        question="什么是置信区间",
        expect="先简短解释置信区间，再按需生成覆盖率演示；追问围绕本轮具体内容展开。",
        checks=["侧栏阶梯显示 L2", "出现「生成可视化」按钮（覆盖率演示）"],
        note="概念题直接讲解；需要时可继续要求换例子或展开步骤。",
    ),
    DemoCase(
        id="ladder-03",
        group="ladder",
        title="求证式提问直接澄清",
        question="p值0.03是不是代表H0为真的概率",
        expect="先明确回答「不是」，再讲清 p 值的条件概率含义；侧栏提示「把 p 值当成 H0 为真的概率」这一误概念。",
        checks=["答案开头给出明确的是/否", "侧栏出现误概念卡片"],
        note="这是学生最常见的误读，答错会直接影响后续所有推断。",
    ),
    # ---------------------------------------------------------- 推导核对
    DemoCase(
        id="verify-01",
        group="verify",
        title="错误推导当场被定位",
        question="x^2 - 1 / (x-1)(x+1) / x^2 + 2x + 1",
        expect="第 1 步等价 ✓，第 2 步不等价 ✗，并给出具体反例点。",
        checks=["侧栏「推导核对」页：第 1→2 步绿色，第 2→3 步红色", "反例行给出一组具体数值"],
        note="演示时先让学生自己说「哪一步错了」，再点核对。",
    ),
    DemoCase(
        id="verify-02",
        group="verify",
        title="正确推导全程通过",
        question="(x+1)^2 / x^2 + 2x + 1 / x^2 + x + x + 1",
        expect="两步都判等价，并提醒「每步成立 ≠ 整个推导正确」。",
        checks=["全部绿色", "顶部提示检查起止点是否回答了原问题"],
        note="",
    ),
    # ---------------------------------------------------------- 可视化
    DemoCase(
        id="viz-calculus",
        group="viz",
        title="从圆的切线到换元积分",
        question="设 D={(x,y):x^2+y^2≤2y}。①说明并画出区域 D，求边界在 P=(1,1) 处的切线。"
                 "②计算二重积分 ∬_D(x^2+y^2)dxdy，并解释坐标变换为何改变面积元。请简洁地串起关键步骤。",
        expect="用工具核对切线 x=1、雅可比 r 与积分 3π/2；回答后可追问梯度、点积和换元，按需由模型生成交互图。",
        checks=["活动记录包含微积分核对", "回答下出现推荐追问", "点击生成可视化后仍能继续聊天"],
        note="推荐追问和图形由模型结合本轮上下文生成。案例入口只填入题目，不预置答案。",
    ),
    DemoCase(
        id="viz-01",
        group="viz",
        title="二次函数：Δ 与交点",
        question="y = x^2 - 2x - 3 的图像长什么样？顶点和与 x 轴交点在哪",
        expect="画出学生给的这条曲线，标出顶点 (1,-4)、对称轴 x=1、两个根 -1 与 3；"
               "拖动 a/b/c 实时变化。",
        checks=["图标题就是 y = x² - 2x - 3", "图下注释给出 Δ=16"],
        note="再换 y=-x^2+4x-4 演示 Δ=0 的相切情形。",
    ),
    DemoCase(
        id="viz-02",
        group="viz",
        title="中心极限定理：样本均值为何收敛",
        question="中心极限定理为什么样本均值近似正态？画出来看看",
        expect="抽样分布模拟，拖动 n 看到均值的分布逐步收窄并逼近钟形，同时强调原始数据不变。",
        checks=["出现抽样分布图", "侧栏误概念提示「以为 CLT 让原始数据变正态」"],
        note="",
    ),
    # ---------------------------------------------------------- 拍照问疑
    DemoCase(
        id="photo-01",
        group="photo",
        title="拍手写题直接进入辅导",
        question="（点击输入框左侧的相机图标，上传一张题目截图）",
        expect="识别出的文本填入输入框，先让学生核对；确认后发送，进入正常的帮助阶梯。",
        checks=["识别结果进入输入框而不是直接发送", "提示「先核对一遍」"],
        note="识别结果只存本地 .data/ocr 且已脱敏。",
    ),
    DemoCase(
        id="photo-02",
        group="photo",
        title="共性疑问聚类（教师视角）",
        question="（接口：POST /api/coach/clusters）",
        expect="把最近上传的疑问按知识点聚成若干组，指出哪类疑问出现最多。",
        checks=["返回 clusters，按规模降序", "代表句已脱敏"],
        note="对应申报书里的「隐性学情 → 教师可用的证据」。",
    ),
)


def list_cases() -> list[dict[str, Any]]:
    return [asdict(c) for c in CASES]


def run_case(case_id: str) -> dict[str, Any]:
    """在服务端跑一遍该案例的确定性部分，返回可验证的观测结果。

    不做模型调用 —— 现场断网也能检查机制是否成立。
    """
    case = next((c for c in CASES if c.id == case_id), None)
    if case is None:
        raise KeyError(case_id)
    out: dict[str, Any] = {"id": case.id, "title": case.title, "observations": []}

    if case.id.startswith("ladder"):
        state = LadderState()
        rounds = [case.question]
        if case.id == "ladder-01":
            rounds += ["我不知道怎么下手", "还是不懂，再讲讲", "直接告诉我答案吧"]
        for q in rounds:
            hits = diagnose(q)
            d = decide(state, q, hits)
            out["observations"].append({
                "query": q, "level": d.level, "level_name": d.level_name,
                "reason": d.reason, "advanced": d.advanced,
                "misconceptions": [m.id for m in hits],
            })
    elif case.id.startswith("verify"):
        steps = [s.strip() for s in case.question.split(" / ")]
        checks = check_steps(steps)
        out["observations"].append({
            "steps": steps,
            "checks": [{"index": c.index, "status": c.status,
                        "counterexample": c.counterexample} for c in checks],
        })
    elif case.id.startswith("photo"):
        out["observations"].append({
            "note": "拍照案例需要真实图片；聚类接口可直接用 POST /api/coach/clusters 演示。",
        })
    else:
        out["observations"].append({"note": "可视化案例在页面上直接提问即可，无需预跑。"})
    return out


def group_of(case_id: str) -> str:
    case = next((c for c in CASES if c.id == case_id), None)
    return case.group if case else ""


__all__ = ["CASES", "DemoCase", "group_of", "list_cases", "run_case"]
