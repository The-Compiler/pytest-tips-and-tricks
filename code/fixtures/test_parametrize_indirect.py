import pytest
from rpncalc.utils import Config


@pytest.fixture
def config(request):
    c = Config(prompt=request.param)
    return c

@pytest.mark.parametrize(
    "config, length", [
        (">", 1), ("rpn>", 5),
    ],
    indirect=["config"],
)
def test_prompt(config: Config, length: int):
    assert len(config.prompt) == length
