import pytest
import time
from rpncalc.rpn_v2 import RPNCalculator, Config


@pytest.fixture(scope="module")
def rpn_instance() -> RPNCalculator:
    time.sleep(2)
    return RPNCalculator(Config())


@pytest.fixture
def rpn(
    rpn_instance: RPNCalculator,
) -> RPNCalculator:
    rpn_instance.stack.clear()
    return rpn_instance


def test_a(rpn: RPNCalculator):
    rpn.stack.append(42)
    assert rpn.stack == [42]


def test_b(rpn: RPNCalculator):
    assert not rpn.stack
