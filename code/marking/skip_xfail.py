import pytest

# decorators
@pytest.mark.skipif(
    sys.platform == "win32",
    reason="POSIX only",
)
def test_posix_property():
    ...

@pytest.mark.xfail(
    reason="not implemented",
)
class TestNewAPI:
     # test methods


# imperative (inside test)
def test_skipped():
    if not utils.server_is_reachable():
        pytest.skip("Server is unreachable")

def test_expected_to_fail():
    if utils.server_is_incompatible():
        pytest.xfail("Server version too new")
