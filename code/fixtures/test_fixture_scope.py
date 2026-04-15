import pytest
import time
from rpncalc.rpn_v2 import RPNCalculator, Config


@pytest.fixture(scope="function")
def rpn() -> RPNCalculator:
    time.sleep(2)
    return RPNCalculator(Config())

def test_a(rpn: RPNCalculator):
    rpn.stack.append(42)
    assert rpn.stack == [42]

def test_b(rpn: RPNCalculator):
    assert not rpn.stack
