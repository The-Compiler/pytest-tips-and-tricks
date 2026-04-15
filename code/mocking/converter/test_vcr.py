import pytest
from rpncalc.convert import Converter


@pytest.fixture
def converter() -> Converter:
    return Converter()


@pytest.mark.vcr
def test_eur2chf(converter: Converter):
    assert converter.eur2chf(1) == pytest.approx(0.9, rel=1e-1)


@pytest.mark.vcr
def test_chf2eur(converter: Converter):
    assert converter.chf2eur(1) == pytest.approx(1.1, rel=1e-1)
