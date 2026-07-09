import pytest

from app.skills.method_selector import extract_features, recommend_method, render_recommendation
from app.skills.exercise import generate_exercise, render_exercise
from app.skills.registry import list_skills, SKILL_REGISTRY


@pytest.mark.parametrize("query,expect", [
    ("两组不同学生的连续成绩比较，分布近似正态", "Welch"),
    ("同一批人前后测的连续成绩，分布偏态", "Wilcoxon"),
    ("同一批人前后测的连续成绩，近似正态", "配对样本 t"),
    ("三组不同班级的连续成绩比较，正态", "ANOVA"),
    ("三组不同班级的连续成绩比较，偏态", "Kruskal-Wallis"),
    ("两个分类变量是否有关联，独立性检验", "卡方"),
    ("想用连续因变量预测，需要控制协变量", "线性回归"),
    ("因变量是否阳性的二分类，做预测建模", "Logistic"),
])
def test_method_selector_decision_tree(query, expect):
    rec = recommend_method(extract_features(query))
    assert rec.confident, f"{query} should be confident"
    assert expect in rec.primary, (query, rec.primary)


def test_method_selector_insufficient_info_asks():
    rec = recommend_method(extract_features("用什么统计方法"))
    assert rec.confident is False
    assert rec.missing
    text = render_recommendation(rec)
    assert "因变量" in text


def test_method_selector_two_groups_needs_pairing():
    # 只说两组、连续、比较，但没说独立/配对 -> 必须追问
    rec = recommend_method(extract_features("两组连续成绩的比较"))
    assert rec.confident is False
    assert any("样本结构" in m for m in rec.missing)


@pytest.mark.parametrize("topic", ["中心极限定理", "t检验两组均值", "随便什么"])
def test_exercise_self_check_passes_latex(topic):
    ex = generate_exercise(topic)
    assert ex.self_check_ok, ex.self_check_issues
    rendered = render_exercise(ex)
    assert "提示" in rendered
    assert "原创" in rendered


def test_registry_lists_two_skills():
    skills = list_skills()
    names = {s["name"] for s in skills}
    assert {"method_selector", "exercise"} <= names
    assert len(SKILL_REGISTRY) >= 2
