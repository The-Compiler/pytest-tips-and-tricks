import pytest
from rpncalc.utils import Config


@pytest.fixture(params=[">", "rpn>"])
def config(request: pytest.FixtureRequest):
    return Config(prompt=request.param)

def test_init(config: Config):
    print(config.prompt)
    assert False
