import pytest
from rpncalc.utils import calc


@pytest.mark.parametrize("a, b, expected", [
    (1, 2, 3),  # 1 + 2 = 3
    (2, 3, 6),  # 2 + 3 = 6 (?)
    (3, 4, 7),  # 3 + 4 = 7
    (4, 5, 9),  # 4 + 5 = 9
])
def test_add(a: int, b: int, expected: int):
    assert calc(a, b, "+") == expected

@pytest.mark.parametrize(
    "op", ["+", "-", "*", "/", "@"])
def test_smoke(op: str):
    calc(1, 2, op)


@pytest.mark.parametrize("a", [1, 2])
@pytest.mark.parametrize("b", [3, 4])
def test_permutations(a: int, b: int):
    assert calc(a, b, "+") == a + b


# exercise: [parametrize]
