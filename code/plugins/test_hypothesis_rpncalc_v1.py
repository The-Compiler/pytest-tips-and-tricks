from hypothesis import given, strategies as st
from rpncalc.rpn_v1 import RPNCalculator

@given(st.text())
def test_random_strings(s):
    rpn = RPNCalculator()
    rpn.evaluate(s)
