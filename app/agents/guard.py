from __future__ import annotations

from dataclasses import dataclass


@dataclass(frozen=True)
class GuardResult:
    allowed: bool
    reason: str = ""
    safe_answer: str = ""


class ContentGuard:
    COPYRIGHT_KEYWORDS = (
        "z-library",
        "zlibrary",
        "sci-hub",
        "百度文库",
        "文库会员",
        "文库下载",
        "组卷网会员",
        "组卷网题库",
        "破解",
        "付费资料",
        "付费教材",
        "整本教材",
        "整本整理",
        "没有授权",
        "未授权",
        "爬下来",
    )
    ACADEMIC_MISUSE_KEYWORDS = (
        "代写",
        "帮我考试",
        "考试答案",
        "可能考的答案",
        "泄题",
        "直接给答案不要过程",
        "最终答案",
        "不要过程",
        "老师要求独立完成",
        "写完整论文",
        "绕过查重",
        "查重",
        "论文造假",
        "编数据",
        "编一些数据",
    )
    STATISTICAL_MISUSE_KEYWORDS = (
        "写成因果结论",
        "解释成显著",
        "删掉不显著",
        "只报显著",
        "不报不显著",
        "换检验直到显著",
        "直到显著",
        "结果不符合假设",
    )
    HIGH_RISK_KEYWORDS = (
        "推荐用药",
        "保证赚钱",
    )
    PRIVACY_KEYWORDS = (
        "身份证",
        "手机号",
        "学生成绩",
        "敏感信息",
        "隐私数据",
    )

    def check(self, query: str) -> GuardResult:
        normalized = query.lower()
        if any(keyword in normalized for keyword in self.COPYRIGHT_KEYWORDS):
            return GuardResult(
                allowed=False,
                reason="copyright_risk",
                safe_answer=(
                    "我不能提供未授权资料的下载、破解或整本复制。"
                    "可以改为帮你整理知识点框架、生成原创练习题，或基于你有权使用的资料做学习辅导。"
                ),
            )
        if any(keyword in normalized for keyword in self.ACADEMIC_MISUSE_KEYWORDS):
            return GuardResult(
                allowed=False,
                reason="academic_integrity",
                safe_answer=(
                    "我不能代写作业、作弊或编造数据。"
                    "我可以带你分步骤理解题意、检查思路、给出相似练习和评分标准。"
                ),
            )
        if any(keyword in normalized for keyword in self.STATISTICAL_MISUSE_KEYWORDS):
            return GuardResult(
                allowed=False,
                reason="statistical_integrity",
                safe_answer=(
                    "我不能帮你把统计结果写成误导性结论，也不能协助 p-hacking 或选择性报告。"
                    "可以改为帮你写严谨表述：同时报告效应量、置信区间、p 值、模型假设、稳健性检查和局限性。"
                ),
            )
        privacy_risk = "上传" in normalized and any(
            keyword in normalized for keyword in self.PRIVACY_KEYWORDS
        )
        if any(keyword in normalized for keyword in self.HIGH_RISK_KEYWORDS) or privacy_risk:
            return GuardResult(
                allowed=False,
                reason="high_risk_or_privacy",
                safe_answer=(
                    "这个请求涉及高风险决策或个人敏感信息，我不能直接给医疗/金融承诺性结论，也不能建议上传未脱敏隐私数据。"
                    "可以改为提供统计分析框架、风险提示、脱敏清单和需要咨询专业人士的问题列表。"
                ),
            )
        return GuardResult(allowed=True)
