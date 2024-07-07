from __future__ import annotations

import pytest

from rpncalc.rpn_v2 import RPNCalculator
from rpncalc.utils import Config


def test_complex_example():
    rpn = RPNCalculator(Config())

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
    rpn = RPNCalculator(Config())
    rpn.evaluate("1")
    rpn.evaluate("2")
    assert rpn.stack == [1, 2]


@pytest.mark.parametrize(
    "op, expected",
    [
        ("+", 3),
        ("-", -1),
        ("*", 2),
        ("/", 0.5),
    ],
)
def test_operations(op, expected):
    rpn = RPNCalculator(Config())
    rpn.stack = [1, 2]
    rpn.evaluate(op)
    assert rpn.stack == [expected]


@pytest.mark.parametrize("n", [1.5, -1])
def test_number_input(n):
    rpn = RPNCalculator(Config())
    rpn.evaluate(str(n))
    assert rpn.stack == [n]


@pytest.mark.parametrize(
    "op", ["**", "+-"])
def test_unknown_operator(op: str):
    rpn = RPNCalculator(Config())
    rpn.stack = [1, 2]
    rpn.evaluate(op)