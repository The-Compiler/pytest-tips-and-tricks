# mocking/test_fake.py

import pytest

from rpncalc.utils import Config
from rpncalc.rpn_v3 import RPNCalculator

class FakeConverter:

    RATE = 2

    def eur2chf(self, amount: float) -> float:
        return amount * self.RATE

    def chf2eur(self, amount: float) -> float:
        return amount / self.RATE


@pytest.fixture
def rpn(monkeypatch: pytest.MonkeyPatch) -> RPNCalculator:
    rpn = RPNCalculator(Config())
    monkeypatch.setattr(rpn, "converter", FakeConverter())
    return rpn

def test_convert(rpn: RPNCalculator):
    rpn.stack = [10]
    rpn.evaluate("eur2chf")
    assert rpn.stack == [20]
