import pytest

from rpncalc.utils import Config


# exercise: [request]

@pytest.fixture
def config(request: pytest.FixtureRequest) -> Config:
    marker = request.node.get_closest_marker("long_prompt")
    if marker is None:
        return Config(prompt=">")
    return Config(prompt="rpn>")


def test_normal(config: Config):
    assert config.prompt == ">"


@pytest.mark.long_prompt
def test_marker(config: Config):
    assert config.prompt == "rpn>"


class ServerConfig:

    def __init__(self, filename: str = "test.json", strict: bool = False):
        self.filename = filename
        self.strict = strict


@pytest.fixture
def server_config(request: pytest.FixtureRequest) -> ServerConfig:
    marker = request.node.get_closest_marker("config_args")
    if marker is None:
        return ServerConfig()
    return ServerConfig(*marker.args, **marker.kwargs)
