from rpncalc.utils import calc

import pytest


def test_zero_division():
    with pytest.raises(ZeroDivisionError):
        calc(3, 0, "/")
