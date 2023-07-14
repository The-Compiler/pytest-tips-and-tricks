import pytest
from rpncalc.utils import Config

# fixtures/test_fixture_param.py

@pytest.fixture(params=[
    ">",
    "rpn>",
])
def config(request):
    c = Config(prompt=request.param)
    return c

def test_init(config):
    print(config.prompt)
    assert False
