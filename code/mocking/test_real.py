import pytest

from rpncalc.utils import Config
from rpncalc.rpn_v3 import RPNCalculator


@pytest.fixture
def rpn() -> RPNCalculator:
    return RPNCalculator(Config())

def test_convert(rpn: RPNCalculator):
    rpn.stack = [10]
    rpn.evaluate("eur2chf")
    rpn.evaluate("chf2eur")
    assert rpn.stack[-1] == 10
