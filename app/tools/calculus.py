"""Bounded, exact calculus operations; the model chooses and explains the inputs."""
from __future__ import annotations

import ast
import json
import math
import re

from app.bounded_compute import run_compute
from app.tools.base import ToolResult


class CalculateCalculusTool:
    name = "calculate_calculus"

    def schema(self):
        expression = {"type": "string", "minLength": 1, "maxLength": 500}
        return {"type": "function", "function": {
            "name": self.name,
            "description": (
                "用符号计算核对代入与展开、梯度、隐式曲线切线、雅可比及定积分。具体微积分题应先调用本工具再给结论。"
                "表达式用 x^2、sin(theta)、pi 等普通数学形式。variables 按坐标顺序填写。"
                "gradient/implicit_tangent 用 expression，point 为对应坐标的字符串数组；"
                "evaluate 用 expression 核对代数展开与简化，可选 point 代入数值。例如核对实际增量可输入 (2+h)^2+k^2-4，variables=[h,k]。"
                "jacobian 用 mapping 字符串数组；integrate 用 expression 和 limits（由内到外）。"
                "例如 integral: expression=r^3, variables=[r,theta], limits=[{variable:r,lower:0,upper:2*sin(theta)},"
                "{variable:theta,lower:0,upper:pi}]，其中上下限均为字符串。工具只核对输入，区域与换元依据仍须解释。"
            ),
            "parameters": {"type": "object", "properties": {
                "operation": {"type": "string", "enum": ["evaluate", "gradient", "implicit_tangent", "jacobian", "integrate"]},
                "variables": {"type": "array", "items": {"type": "string", "maxLength": 20}, "minItems": 1, "maxItems": 3},
                "expression": expression,
                "point": {"type": "array", "items": expression, "minItems": 1, "maxItems": 3},
                "mapping": {"type": "array", "items": expression, "minItems": 1, "maxItems": 3},
                "limits": {"type": "array", "minItems": 1, "maxItems": 3, "items": {
                    "type": "object", "properties": {"variable": {"type": "string", "maxLength": 20},
                        "lower": expression, "upper": expression}, "required": ["variable", "lower", "upper"]}},
            }, "required": ["operation", "variables"]},
        }}

    async def run(self, **arguments):
        result = await run_compute("calculus", arguments)
        return ToolResult(json.dumps(result, ensure_ascii=False, allow_nan=False), summary=result)


def _expression(text, symbols):
    """Construct SymPy nodes from an allowlisted AST; never eval model output."""
    import sympy as sp
    from app.verify.steps import normalize

    if not isinstance(text, str) or not 0 < len(text) <= 500:
        raise ValueError("表达式需要为不超过500字的字符串")
    tree = ast.parse(normalize(text), mode="eval")
    if sum(1 for _ in ast.walk(tree)) > 180:
        raise ValueError("表达式过于复杂")
    functions = {"sin": sp.sin, "cos": sp.cos, "tan": sp.tan, "exp": sp.exp,
                 "log": sp.log, "ln": sp.log, "sqrt": sp.sqrt, "abs": sp.Abs}
    names = {**symbols, "pi": sp.pi, "e": sp.E}

    def visit(node):
        if isinstance(node, ast.Expression):
            return visit(node.body)
        if isinstance(node, ast.Constant) and type(node.value) in (int, float):
            if not math.isfinite(node.value) or abs(node.value) > 10**12:
                raise ValueError("常数超出计算范围")
            return sp.Rational(str(node.value))
        if isinstance(node, ast.Name) and node.id in names:
            return names[node.id]
        if isinstance(node, ast.UnaryOp) and isinstance(node.op, (ast.UAdd, ast.USub)):
            value = visit(node.operand)
            return -value if isinstance(node.op, ast.USub) else value
        if isinstance(node, ast.BinOp):
            left, right = visit(node.left), visit(node.right)
            if isinstance(node.op, ast.Add): return left + right
            if isinstance(node.op, ast.Sub): return left - right
            if isinstance(node.op, ast.Mult): return left * right
            if isinstance(node.op, ast.Div): return left / right
            if isinstance(node.op, ast.Pow):
                if right.is_number and (right.is_real is not True or abs(right) > 100):
                    raise ValueError("幂指数超出计算范围")
                return left ** right
        if (isinstance(node, ast.Call) and isinstance(node.func, ast.Name)
                and node.func.id in functions and len(node.args) == 1 and not node.keywords):
            return functions[node.func.id](visit(node.args[0]))
        raise ValueError("仅支持声明的变量、算术及 sin/cos/tan/exp/log/sqrt/abs")

    value = visit(tree)
    if value.has(sp.zoo, sp.nan, sp.oo, -sp.oo):
        raise ValueError("表达式含未定义或非有限值")
    return value


def calculate(arguments):
    """Runs only in the killable calculation child process."""
    import sympy as sp

    variables = arguments.get("variables", [])
    reserved = {"sin", "cos", "tan", "exp", "log", "ln", "sqrt", "abs", "pi", "e"}
    if (not isinstance(variables, list) or not 1 <= len(variables) <= 3
            or any(not isinstance(v, str) or not re.fullmatch(r"[A-Za-z][A-Za-z0-9_]{0,19}", v)
                   or v in reserved for v in variables) or len(set(variables)) != len(variables)):
        raise ValueError("请声明1至3个不重复的变量")
    symbols = {name: sp.Symbol(name, real=True) for name in variables}
    ordered = list(symbols.values())
    parse = lambda text: _expression(text, symbols)
    operation = arguments.get("operation")
    result = {"operation": operation, "verified": True,
              "scope": "仅核对所提供的表达式、点和积分界限；不自动证明区域或换元选择正确。"}

    if operation == "evaluate":
        expression = parse(arguments.get("expression"))
        expanded = sp.expand(expression)
        if "point" in arguments:
            point = arguments["point"]
            if not isinstance(point, list) or len(point) != len(variables):
                raise ValueError("代入坐标数需要与变量数一致")
            coordinates = [parse(value) for value in point]
            if any(value.free_symbols or value.is_real is not True or value.is_finite is not True for value in coordinates):
                raise ValueError("代入坐标必须为有限实数常量")
            expression = expression.subs(dict(zip(ordered, coordinates)), simultaneous=True)
            result['checked_point'] = dict(zip(variables, map(str, coordinates)))
            result['scope'] = '仅核对本表达式及 checked_point 所示坐标；不为其他数值例子背书。'
        else:
            result['scope'] = '仅核对代数展开与简化，尚未代入任何坐标。若回答包含具体点的数值例子，请另用 evaluate 的 point 参数核对。'
        exact = sp.simplify(expression)
        if exact.has(sp.zoo, sp.nan, sp.oo, -sp.oo):
            raise ValueError("代入后表达式未定义或非有限")
        result.update(expanded=str(expanded), expanded_latex=sp.latex(expanded), exact=str(exact), latex=sp.latex(exact))
        if not exact.free_symbols:
            if exact.is_real is not True or exact.is_finite is not True:
                raise ValueError("结果不是有限实数")
            numeric = float(exact.evalf())
            if not math.isfinite(numeric):
                raise ValueError("数值超出显示范围，请缩小输入")
            result['numeric'] = numeric
    elif operation == "jacobian":
        mapping = arguments.get("mapping", [])
        if len(mapping) != len(variables):
            raise ValueError("变换分量数需要与变量数一致")
        matrix = sp.Matrix([parse(item) for item in mapping]).jacobian(ordered)
        determinant = sp.trigsimp(matrix.det())
        result.update(matrix=[[str(v) for v in matrix.row(i)] for i in range(matrix.rows)],
                      matrix_latex=sp.latex(matrix), exact=str(determinant), latex=sp.latex(determinant),
                      area_factor=str(sp.Abs(determinant)))
    elif operation in {"gradient", "implicit_tangent"}:
        expression = parse(arguments.get("expression"))
        gradient = [sp.simplify(sp.diff(expression, v)) for v in ordered]
        result["gradient"] = [str(item) for item in gradient]
        if "point" in arguments:
            point = arguments["point"]
            if len(point) != len(variables):
                raise ValueError("点的坐标数需要与变量数一致")
            coordinates = [_expression(item, {}) for item in point]
            if any(v.is_real is not True or v.is_finite is not True for v in coordinates):
                raise ValueError("点的坐标必须是有限实数")
            substitutions = dict(zip(ordered, coordinates))
            normal = [sp.simplify(item.subs(substitutions)) for item in gradient]
            result["at_point"] = [str(item) for item in normal]
            if any(v.is_real is not True or v.is_finite is not True for v in normal):
                return {**result, "verified": False, "status": "undecidable",
                        "detail": "该点梯度不是已确认的有限实向量，不能据此确认切线。"}
        if operation == "implicit_tangent":
            if len(variables) != 2 or "point" not in arguments:
                raise ValueError("隐式切线需要两个变量及对应点")
            if sp.simplify(expression.subs(substitutions)) != 0:
                raise ValueError("给定点不在所输入的零等值曲线上")
            if all(v == 0 for v in normal):
                return {**result, "verified": False, "status": "undecidable",
                        "detail": "该点梯度为零，不能由这个一阶条件确定切线。"}
            equation = sp.expand(sum(v * (coordinate - location) for v, coordinate, location
                                     in zip(normal, ordered, coordinates)))
            result.update(equation=str(equation) + " = 0", equation_latex=sp.latex(equation) + "=0",
                          tangent_direction=[str(-normal[1]), str(normal[0])], vertical=normal[1] == 0,
                          dy_dx=None if normal[1] == 0 else str(sp.simplify(-normal[0] / normal[1])))
            if result["vertical"]:
                result["detail"] = f"切线为 {variables[0]}={coordinates[0]}，该点不存在有限的 dy/dx。"
    elif operation == "integrate":
        limits = arguments.get("limits", [])
        if not limits or len(limits) != len(variables) or set(item["variable"] for item in limits) != set(variables):
            raise ValueError("每个变量需要一个积分界限，顺序由内到外")
        expression = parse(arguments.get("expression"))
        integrated = set()
        steps = []
        for limit in limits:
            variable = symbols[limit["variable"]]
            lower, upper = parse(limit["lower"]), parse(limit["upper"])
            if (lower.free_symbols | upper.free_symbols) & (integrated | {variable}):
                raise ValueError("积分界限不能依赖本变量或已积掉的变量")
            expression = sp.integrate(expression, (variable, lower, upper))
            if expression.has(sp.Integral):
                return {**result, "verified": False, "status": "undecidable", "detail": "未得到闭式积分结果。"}
            integrated.add(variable)
            steps.append({"variable": str(variable), "exact": str(expression), "latex": sp.latex(expression)})
        expression = sp.simplify(expression)
        if expression.is_real is not True or expression.is_finite is not True:
            raise ValueError("积分结果不是已确认的有限实数")
        result.update(exact=str(expression), latex=sp.latex(expression), numeric=float(expression.evalf()), steps=steps)
    else:
        raise ValueError("未知微积分操作")
    return result
