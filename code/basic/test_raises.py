from rpncalc.utils import calc

import pytest

# basic/test_raises.py

def test_zero_division():
    with pytest.raises(ZeroDivisionError):
        calc(3, 0, '/')
