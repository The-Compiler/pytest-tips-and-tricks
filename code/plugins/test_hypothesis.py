from __future__ import annotations

from hypothesis import given
from hypothesis.strategies import text


def decode(lst: list[tuple[int, str]]) -> str:
    s = ""
    for count, character in lst:
        s += count * character
    return s


def encode(input_string: str) -> list[tuple[int, str]]:
    count = 1; prev = ""; lst = []
    for character in input_string:
        if character != prev:
            if prev:
                entry = (count, prev)
                lst.append(entry)
            count = 1
            prev = character
        else:
            count += 1
    entry = (count, character)
    lst.append(entry)
    return lst


@given(text())
def test_decode_inverts_encode(s: str):
    assert decode(encode(s)) == s