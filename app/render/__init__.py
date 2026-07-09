"""后端渲染辅助：LaTeX 静态检查（无浏览器环境下可断言）。"""

from app.render.latex_lint import LatexIssue, lint_latex

__all__ = ["LatexIssue", "lint_latex"]
