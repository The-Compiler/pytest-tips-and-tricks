import pytest
import sys


@pytest.mark.skipif(
    # condition
    sys.platform == "win32",
    # text shown with -v
    reason="Linux only",
)
def test_linux():
    pass

@pytest.mark.xfail(
    # condition optional
    reason="see #1234",
)
def test_new_api():
    pass


# exercise: [skip-xfail]
