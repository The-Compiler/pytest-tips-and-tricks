from rpncalc.utils import calc

def test_add():
    res = calc(1, 3, "+")
    assert res == 4
