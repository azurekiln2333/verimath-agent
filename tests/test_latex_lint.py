from app.render.latex_lint import lint_latex


def test_clean_formula_has_no_issues():
    text = r"方差是 \(\sigma^2\)，积分 \[\int_0^1 x\,dx\]。"
    assert lint_latex(text) == []


def test_bare_command_flagged():
    text = r"期望是 \frac{1}{n}\sum x_i 这样。"
    kinds = {i.kind for i in lint_latex(text)}
    assert "bare_command" in kinds


def test_command_in_code_fence_flagged():
    text = "```\n\\frac{a}{b}\n```"
    kinds = {i.kind for i in lint_latex(text)}
    assert "command_in_code" in kinds


def test_command_in_inline_code_flagged():
    text = "用 `\\frac{a}{b}` 表示比值。"
    kinds = {i.kind for i in lint_latex(text)}
    assert "command_in_code" in kinds


def test_unbalanced_inline_delimiter_flagged():
    text = r"这里 \(x^2 缺右括号。"
    kinds = {i.kind for i in lint_latex(text)}
    assert "unbalanced_inline" in kinds


def test_unbalanced_display_delimiter_flagged():
    text = r"公式 \[x^2 没有闭合。"
    kinds = {i.kind for i in lint_latex(text)}
    assert "unbalanced_display" in kinds
