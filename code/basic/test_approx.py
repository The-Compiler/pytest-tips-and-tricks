import pytest
from rpncalc.utils import calc

# basic/test_approx.py
def test_add():
    res = calc(0.2, 0.1, '+')
    assert res == pytest.approx(0.3)
