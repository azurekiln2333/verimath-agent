"""Exact results and invalid-input boundaries for the multivariable teaching case."""
import asyncio
import math

import pytest
import mpmath as mp

from app.tools.calculus import CalculateCalculusTool, calculate


def test_circle_vertical_tangent_is_not_a_finite_slope():
    result = calculate(dict(operation="implicit_tangent", variables=["x", "y"],
                            expression="x^2+y^2-2*y", point=["1", "1"]))
    assert result["verified"] and result["at_point"] == ["2", "0"]
    assert result["vertical"] and result["dy_dx"] is None
    assert result["equation"] == "2*x - 2 = 0"
    assert result["tangent_direction"] == ["0", "2"]


def test_polar_jacobian_and_integral_agree_with_independent_cartesian_quadrature():
    jac = calculate(dict(operation="jacobian", variables=["r", "theta"],
                         mapping=["r*cos(theta)", "r*sin(theta)"]))
    assert jac["verified"] and jac["exact"] == "r" and jac["area_factor"] == "Abs(r)"
    result = calculate(dict(operation="integrate", variables=["r", "theta"], expression="r^3",
        limits=[dict(variable="r", lower="0", upper="2*sin(theta)"),
                dict(variable="theta", lower="0", upper="pi")]))
    independent = mp.quad(lambda y: mp.quad(lambda x: x*x+y*y,
        [-mp.sqrt(2*y-y*y), mp.sqrt(2*y-y*y)]), [0, 1, 2])
    assert result["exact"] == "3*pi/2"
    assert abs(result["numeric"] - independent) < 1e-8
    assert abs(float(independent) - 3*math.pi/2) < 1e-10


def test_translated_polar_coordinates_are_also_valid():
    result = calculate(dict(operation="integrate", variables=["r", "theta"],
        expression="(r^2+2*r*sin(theta)+1)*r",
        limits=[dict(variable="r", lower="0", upper="1"),
                dict(variable="theta", lower="0", upper="2*pi")]))
    assert result["exact"] == "3*pi/2"


@pytest.mark.parametrize("expression", ["__import__('os')", "x.__class__", "sin(x, x)",
                                      "10^1000", "x+unknown", "1/0"])
def test_model_expression_cannot_execute_code_or_escape_bounds(expression):
    with pytest.raises((ValueError, SyntaxError)):
        calculate(dict(operation="gradient", variables=["x"], expression=expression))


def test_tangent_rejects_off_curve_point_and_reports_singular_point():
    with pytest.raises(ValueError, match="不在"):
        calculate(dict(operation="implicit_tangent", variables=["x", "y"],
                       expression="x^2+y^2-2*y", point=["0", "1"]))
    zero = calculate(dict(operation="implicit_tangent", variables=["x", "y"],
                          expression="x^2+y^2", point=["0", "0"]))
    assert not zero["verified"] and zero["status"] == "undecidable"
    infinite = calculate(dict(operation="gradient", variables=["x"], expression="sqrt(x)", point=["0"]))
    assert not infinite["verified"]


def test_integration_rejects_bounds_that_use_already_integrated_variable():
    with pytest.raises(ValueError, match="界限"):
        calculate(dict(operation="integrate", variables=["x", "y"], expression="x*y",
            limits=[dict(variable="x", lower="0", upper="y"),
                    dict(variable="y", lower="0", upper="x")]))


def test_registered_tool_uses_bounded_child_process():
    result = asyncio.run(CalculateCalculusTool().run(operation="gradient", variables=["x", "y"],
                                                    expression="x^2+y^2-2*y", point=["1", "1"]))
    assert result.summary["at_point"] == ["2", "0"] and result.summary["verified"]


def test_actual_increment_keeps_linear_term_and_matches_direct_substitution():
    result = calculate(dict(operation="evaluate", variables=["h", "k"], expression="(2+h)^2+k^2-4"))
    assert result['expanded'] == 'h**2 + 4*h + k**2'
    evaluated = calculate(dict(operation="evaluate", variables=["x", "y"],
                              expression="(x-1)^2+(y-2)^2-4", point=["4", "2"]))
    assert evaluated['exact'] == '5' and evaluated['numeric'] == 5
    assert evaluated['checked_point'] == {'x': '4', 'y': '2'}
    assert '尚未代入' in result['scope'] and 'checked_point' in evaluated['scope']


@pytest.mark.parametrize('point', [["0"], ["x", "0"], ["0", "0"]])
def test_evaluate_rejects_bad_coordinates_and_undefined_values(point):
    with pytest.raises(ValueError):
        calculate(dict(operation='evaluate', variables=['x', 'y'], expression='1/x+y', point=point))


def test_evaluate_runs_through_the_registered_bounded_tool():
    result = asyncio.run(CalculateCalculusTool().run(operation='evaluate', variables=['h', 'k'],
                         expression='(2+h)^2+k^2-4', point=['1', '0']))
    assert result.summary['numeric'] == 5 and result.summary['verified']
