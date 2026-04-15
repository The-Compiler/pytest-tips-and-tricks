import pytest


def test_sub(subtests: pytest.Subtests):
    for i in range(5):
        with subtests.test("part 1", i=i):
            assert i % 2 == 0

    for i in range(10, 15):
        with subtests.test("part 2", i=i):
            assert i % 2 == 0
