import pytest

@pytest.mark.parametrize("i", range(20))
def test_good_1(i):
    pass

def test_bad():
    assert False

@pytest.mark.parametrize("i", range(20))
def test_good_2(i):
    pass
