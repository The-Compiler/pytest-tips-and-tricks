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
    ("+", 3), ("-", -1),
    ("*", 2), ("/", 0.5),
])
def test_operations(op, expected):
    rpn = RPNCalculator()
    rpn.stack = [1, 2]
    rpn.evaluate(op)
    assert rpn.stack == [expected]
