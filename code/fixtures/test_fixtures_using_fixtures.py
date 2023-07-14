import pytest
from rpncalc.utils import Config
from rpncalc.rpn_v2 import RPNCalculator

# fixtures/test_fixtures_using_fixtures.py
@pytest.fixture
def config() -> Config:
    return Config()

@pytest.fixture
def rpn(config: Config) -> RPNCalculator:
    return RPNCalculator(config)

def test_default_config(config: Config):
    assert config.prompt == "> "

def test_rpn(rpn: RPNCalculator):
    assert rpn.stack == []
