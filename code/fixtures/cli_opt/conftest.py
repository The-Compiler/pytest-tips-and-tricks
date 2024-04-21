import pytest


def pytest_addoption(parser: pytest.Parser) -> None:
    parser.addoption("--server-ip", type=str)

@pytest.fixture
def server_ip(request: pytest.FixtureRequest) -> str:
    return request.config.option.server_ip
