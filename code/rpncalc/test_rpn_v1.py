import pytest

from rpncalc.rpn_v1 import RPNCalculator


def test_complex_example():
    rpn = RPNCalculator()

    rpn.evaluate("1")
    assert rpn.stack == [1]
    rpn.evaluate("2")
    assert rpn.stack == [1, 2]
    rpn.evaluate("+")
    assert rpn.stack == [3]
    rpn.evaluate("5")
    assert rpn.stack == [3, 5]
    rpn.evaluate("*")
    assert rpn.stack == [15]


def test_stack_push():
    rpn = RPNCalculator()
    rpn.evaluate("1")
    rpn.evaluate("2")
    assert rpn.stack == [1, 2]

@pytest.mark.parametrize("op, expected", [
    ("+", 3), ("-", -1), ("*", 2), ("/", 0.5),
])
def test_operations(op, expected):
    rpn = RPNCalculator()
    rpn.stack = [1, 2]
    rpn.evaluate(op)
    assert rpn.stack == [expected]


@pytest.mark.skip(reason="TODO: Error handling")
def test_unknown_operator():
    rpn = RPNCalculator()
    rpn.stack = [1, 2]

    rpn.evaluate("**")
    # FIXME how do we test that this printed an error?


@pytest.mark.skip(reason="TODO: Error handling")
def test_division_by_zero():
    rpn = RPNCalculator()
    rpn.stack = [1, 0]

    rpn.evaluate("/")
    # FIXME how do we test that this printed an error?


@pytest.mark.skip(reason="TODO: Error handling")
def test_not_enough_operands():
    rpn = RPNCalculator()
    rpn.stack = [1]

    rpn.evaluate("+")
    # FIXME how do we test that this printed an error?


@pytest.mark.skip(reason="FIXME: Should this be possible?")
def test_float_input():
    rpn = RPNCalculator()
    rpn.evaluate("1.5")
