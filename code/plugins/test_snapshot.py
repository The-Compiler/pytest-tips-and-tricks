from rpncalc.utils import calc
from inline_snapshot import snapshot

def test_add():
    assert calc(1, 2, "+") == snapshot(3)
