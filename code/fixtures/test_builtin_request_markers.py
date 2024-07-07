import pytest

from rpncalc.utils import Config


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