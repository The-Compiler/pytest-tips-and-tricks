import pytest
import requests
from rpncalc.convert import Converter

# mocking/converter/
# test_monkeypatch.py


class FakeResponse:
    def __init__(self, data):
        self._data = data

    def raise_for_status(self):
        pass

    def json(self):
        return self._data


def fake_get(url: str, params: dict, headers: dict) -> FakeResponse:
    assert url == Converter.API_URL
    assert params == {"codes": ["EUR"]}
    assert headers == {"User-Agent": Converter.USER_AGENT}
    rates = [{"code": "chf", "rate": 2}]
    return FakeResponse({"data": [{"code": "eur", "rates": rates}]})


@pytest.fixture(autouse=True)
def patch_requests_get(monkeypatch: pytest.MonkeyPatch) -> None:
    monkeypatch.setattr(requests, "get", fake_get)


@pytest.fixture
def converter() -> Converter:
    return Converter()


def test_eur2chf(converter: Converter):
    assert converter.eur2chf(1) == 2

def test_chf2eur(converter: Converter):
    assert converter.chf2eur(1) == 0.5
