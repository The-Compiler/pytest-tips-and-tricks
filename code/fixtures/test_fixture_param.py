import pytest
from rpncalc.utils import Config


@pytest.fixture(
    params=[
        ">",
        "rpn>",
    ]
)
def config(request):
    c = Config(prompt=request.param)
    return c

def test_init(config):
    print(config.prompt)
    assert False
