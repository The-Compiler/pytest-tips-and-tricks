from __future__ import annotations

import pytest

# from rpncalc.rpn_v1 import RPNCalculator
from rpncalc.rpn_v2 import RPNCalculator
from rpncalc.utils import Config


@pytest.fixture
def rpn() -> RPNCalculator:
    return RPNCalculator(Config())


# exercise: [capturing]

@pytest.mark.parametrize("op", ["@", "+-"])
def test_unknown_operator(rpn: RPNCalculator, op: str):
    rpn.stack = [1, 2]
    rpn.evaluate(op)  # FIXME how to test the printed error message?

def test_division_by_zero(rpn: RPNCalculator):
    rpn.stack = [1, 0]
    rpn.evaluate("/")  # FIXME how to test the printed error message?

@pytest.mark.parametrize("stack", [[1], []])
def test_not_enough_operands(rpn: RPNCalculator, stack: list[int]):
    rpn.stack = stack
    rpn.evaluate("+")  # FIXME how to test the printed error message?
