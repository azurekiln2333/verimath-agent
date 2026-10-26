"""教学脚手架回归测试：步骤校验 / 误概念诊断 / 帮助阶梯 / 过程证据。

这一层的测试全在约束"别把错的判成对的"：
- 校验器误报"正确"比没有校验器更糟；
- 帮助阶梯在对的时候不给答案、该给答案的时候别刁难学生。
"""

from __future__ import annotations

import pytest

from app.coach import LadderState, ProcessStore, LearningEvent, decide, diagnose
from app.coach.ladder import detect_signals, level_instruction
from app.verify import (
    StepVerifierError,
    check_steps,
    expressions_equivalent,
    fraction_of,
    substitution_is_zero,
)


# ------------------------------------------------------------------ 步骤校验


@pytest.mark.parametrize("a,b", [
    ("x^2 - 1", "(x-1)(x+1)"),
    ("(x+1)^2", "x^2 + 2x + 1"),
    ("3(x-2)", "3x - 6"),
    ("x(x+1)", "x^2 + x"),
    (r"\frac{1}{2}x + \frac{1}{2}x", "x"),
    ("2x + 3", "2*x + 3"),
])
def test_equivalent_expressions_are_ok(a, b):
    assert expressions_equivalent(a, b).status == "ok"


@pytest.mark.parametrize("a,b", [
    ("x^2 - 1", "x^2 + 1"),
    ("(x+1)^2", "x^2 + 1"),
    ("2x + 3", "2x - 3"),
    ("sqrt(x^2)", "x"),        # x<0 时不成立：必须判错，不能判对
])
def test_non_equivalent_expressions_report_mismatch(a, b):
    result = expressions_equivalent(a, b)
    assert result.status == "mismatch"
    assert result.counterexample, "不一致时必须给出反例点，否则学生无法自行验证"


def test_check_steps_points_at_first_error():
    checks = check_steps(["x^2 - 1", "(x-1)(x+1)", "x^2 + 2x + 1"])
    assert checks[0].status == "ok"
    assert checks[1].status == "mismatch"
    assert checks[1].index == 1


def test_mathematical_typography_preserves_step_results():
    checks = check_steps(['x² − 1', '(x − 1)(x + 1)', 'x² + 2x + 1'])
    assert [check.status for check in checks] == ['ok', 'mismatch']


@pytest.mark.parametrize('written,plain', [('x³', 'x^3'), ('x¹²', 'x^12'), ('2⁻³', '1/8')])
def test_unicode_exponents_keep_their_mathematical_meaning(written, plain):
    assert expressions_equivalent(written, plain).status == 'ok'


def test_check_steps_requires_two_steps():
    with pytest.raises(StepVerifierError):
        check_steps(["x + 1"])


def test_unknown_symbol_is_undecidable_not_wrong():
    result = expressions_equivalent("alpha + 1", "alpha + 1")
    # 纯符号在采样点上无法求值：允许无法判定，但绝不判错
    assert result.status in {"ok", "undecidable"}


def test_fraction_literal_precision():
    assert fraction_of("3/4") == fraction_of("0.75")


def test_substitution_checks_solution():
    assert substitution_is_zero("x^2 - 4", {"x": "2"})
    assert not substitution_is_zero("x^2 - 4", {"x": "3"})


def test_latex_sqrt_and_frac_normalized():
    # Left side excludes negative real x, while the right side is defined there.
    result = expressions_equivalent(r"\sqrt{x} \cdot \sqrt{x}", "x")
    assert result.status == "mismatch"
    assert "定义域" in result.detail


def test_sampling_agreement_is_not_reported_as_a_proof():
    polynomial = "x*(x+2.7)*(x+1.3)*(x+0.4)*(x-0.35)*(x-0.8)*(x-1.7)*(x-2.4)*(x-3.1)"
    result = expressions_equivalent(polynomial, "0")
    assert result.status == "sampled"
    assert "尚未证明" in result.detail


def test_symbolic_verifier_unavailable_reports_only_sampling(monkeypatch):
    monkeypatch.setattr("app.verify.steps._sympy_equivalent", lambda *args: None)
    assert expressions_equivalent("x+x", "2*x").status == "sampled"


def test_cancellation_of_denominator_does_not_erase_domain_restriction():
    result = expressions_equivalent("x/x", "1")
    assert result.status == "mismatch" and result.counterexample == {"x": 0.0}


# ------------------------------------------------------------------ 误概念


def test_misconception_flags_p_value_confusion():
    ids = {m.id for m in diagnose("p值是不是代表H0为真的概率")}
    assert "p_is_h0_prob" in ids


def test_misconception_does_not_fire_on_plain_method_question():
    ids = {m.id for m in diagnose("两组成绩比较用什么检验")}
    assert "t_power_universal" not in ids


def test_misconception_detects_sqrt_square_pattern():
    ids = {m.id for m in diagnose("√(x^2)=x 对吗")}
    assert "square_root_squared" in ids


def test_misconception_misses_are_allowed():
    assert diagnose("什么是正态分布") == []


# ------------------------------------------------------------------ 帮助阶梯


def test_proof_starts_at_l0_and_escalates_when_stuck():
    state = LadderState()
    first = decide(state, "证明 x^2-1=(x-1)(x+1)")
    assert first.level == 0
    assert not first.advanced
    stuck = decide(state, "我不知道怎么下手")
    assert stuck.level == 1 and stuck.advanced
    again = decide(state, "还是不懂")
    assert again.level == 2 and again.advanced


def test_conceptual_question_does_not_require_restating():
    decision = decide(LadderState(), "什么是置信区间")
    assert decision.level >= 2, "概念题不该让学生先复述题意"
    assert level_instruction(decision)


def test_atomic_proposition_question_gets_direct_answer():
    decision = decide(LadderState(), "p值是不是H0为真的概率")
    assert decision.level == 4


def test_ladder_never_exceeds_max():
    state = LadderState(level=4, turns_at_level=1)
    for msg in ["不知道", "还是不懂", "直接说答案"] * 3:
        assert decide(state, msg).level <= 4


def test_ladder_state_caps_advance():
    state = LadderState(level=4)
    assert state.advance() == 4


def test_signals_detected():
    sig = detect_signals("我还是不懂，可以给我完整解答吗？")
    assert sig["stuck"] and sig["request_full"]


# ------------------------------------------------------------------ 过程证据

def test_process_store_records_and_profiles(tmp_path):
    store = ProcessStore(tmp_path / "p.sqlite")
    store.save_ladder("s1", 2, 1)
    assert store.load_ladder("s1") == (2, 1)
    store.record(LearningEvent(session_id="s1", route="concept", ladder_level=2,
                               misconception_ids=["p_is_h0_prob"], stuck=False))
    store.record(LearningEvent(session_id="s1", route="concept", ladder_level=4,
                               misconception_ids=["p_is_h0_prob"], stuck=True,
                               requested_full=True))
    profile = store.profile("s1")
    assert profile["turns"] == 2
    assert profile["dependency"] == pytest.approx(0.75)
    assert profile["independent_rate"] == pytest.approx(0.5)
    assert profile["recurring_misconceptions"] == [{"id": "p_is_h0_prob", "count": 2}]


def test_process_store_empty_profile_is_safe(tmp_path):
    store = ProcessStore(tmp_path / "p.sqlite")
    profile = store.profile("nobody")
    assert profile["turns"] == 0 and profile["dependency"] == 0.0
