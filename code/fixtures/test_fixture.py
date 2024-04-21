import pytest
from rpncalc.utils import Config
from rpncalc.rpn_v2 import RPNCalculator


@pytest.fixture
def rpn() -> RPNCalculator:
    return RPNCalculator(Config())


def test_empty_stack(rpn: RPNCalculator):
    assert rpn.stack == []
