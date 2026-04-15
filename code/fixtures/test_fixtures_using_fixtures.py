import pytest
from rpncalc.utils import Config
from rpncalc.rpn_v2 import RPNCalculator


@pytest.fixture
def config() -> Config:
    return Config()

@pytest.fixture
def rpn(config: Config) -> RPNCalculator:
    return RPNCalculator(config)

def test_config(config: Config):
    assert config.prompt == ">"

def test_rpn(rpn: RPNCalculator):
    assert rpn.stack == []
