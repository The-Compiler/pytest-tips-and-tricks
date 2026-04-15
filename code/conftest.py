# exercise: [conftest]
import pytest

# exercise: [shuffle]
def pytest_addoption(parser: pytest.Parser) -> None:
    ...


def pytest_report_header(config: pytest.Config) -> list[str]:
    ...


def pytest_collection_modifyitems(
    config: pytest.Config,
    items: list[pytest.Item],
) -> None:
    ...
