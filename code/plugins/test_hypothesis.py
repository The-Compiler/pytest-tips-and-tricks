from __future__ import annotations

from hypothesis import given
from hypothesis.strategies import text


def decode(inp: list[tuple[int, str]]) -> str:
    out = ""
    for count, character in inp:
        out += count * character
    return out


# exercise: [hypothesis]

def encode(input_string: str) -> list[tuple[int, str]]:
    count = 1; prev = ""; out = []
    for character in input_string:
        if character != prev:
            if prev:
                entry = (count, prev)
                out.append(entry)
            count = 1
            prev = character
        else:
            count += 1
    entry = (count, character)
    out.append(entry)
    return out


@given(text())
def test_decode_inverts_encode(s: str):
    assert decode(encode(s)) == s
