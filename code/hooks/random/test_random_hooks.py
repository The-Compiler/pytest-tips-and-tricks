import pytest
import re

pytest_plugins = ["pytester"]


@pytest.fixture(autouse=True)
def copy_conftest(pytester: pytest.Pytester) -> None:
    """Copy the conftest.py file to the pytester temp folder."""
    pytester.copy_example("conftest.py")
    # Avoid warnings from pytest-asyncio
    pytester.makeini("[pytest]\nasyncio_default_fixture_loop_scope = function")


def test_help(pytester: pytest.Pytester):
    """Check if the custom option was registered correctly."""
    result = pytester.runpytest("--help")
    result.stdout.fnmatch_lines(["*--shuffle*"])


def test_report_header(pytester: pytest.Pytester):
    """Check if the custom header is displayed when the option is used."""
    result = pytester.runpytest("--shuffle")
    result.stdout.fnmatch_lines(["Test shuffling enabled!"])


def test_report_header_no_arg(pytester: pytest.Pytester):
    """Check if the custom header is not displayed when the option is not used."""
    result = pytester.runpytest()
    result.stdout.no_fnmatch_line("Test shuffling enabled!")


@pytest.mark.parametrize("shuffle", [False, True])
def test_items_shuffled(pytester: pytest.Pytester, shuffle: bool):
    """Check if the test items are shuffled when the option is used."""
    pytester.makepyfile(
        """
        import pytest

        @pytest.mark.parametrize("i", range(100))
        def test_a(i):
            pass
        """
    )
    pytest_args = ["--shuffle"] if shuffle else []
    result = pytester.runpytest(*pytest_args, "--collect-only")
    ids = [int(n) for n in re.findall(r"test_a\[(\d+)\]", str(result.stdout))]

    # shuffle == True  -> the order *is not* test_a[0] ... test_a[99]
    # shuffle == False -> the order *is* test_a[0] ... test_a[99]
    assert (ids == list(range(100))) != shuffle
