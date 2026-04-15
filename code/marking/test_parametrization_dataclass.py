from dataclasses import dataclass
import pytest
from rpncalc.utils import calc


@dataclass
class CalcCase:
    name: str
    a: int
    b: int
    result: int
    op: str = "+"

    def __str__(self) -> str:
        return self.name


@pytest.mark.parametrize("cc", [
    CalcCase("add", a=1, b=2, result=3),
    CalcCase("add-neg", a=-2, b=-3, result=-5),
    CalcCase("sub", a=2, b=1, op="-", result=1),
], ids=str)
def test_calc(cc: CalcCase):
    assert calc(cc.a, cc.b, cc.op) == cc.result
