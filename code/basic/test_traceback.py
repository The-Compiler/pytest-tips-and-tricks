from rpncalc.utils import calc

def test_divide():
    # This will raise ZeroDivisionError
    assert calc(2, 0, "/") == 0

def test_good():
    pass
