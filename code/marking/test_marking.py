import pytest
import time

# marking/test_marking.py

@pytest.mark.slow
@pytest.mark.webtest
def test_slow_api():
    time.sleep(1)

@pytest.mark.webtest
def test_api():
    pass

def test_fast():
    pass
