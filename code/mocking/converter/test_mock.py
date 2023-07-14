import pytest
import pytest_mock
import requests

from rpncalc.convert import Converter

# mocking/converter/test_mock.py

@pytest.fixture(autouse=True)
def mock_requests_get(mocker: pytest_mock.MockerFixture):
    data = {"success": True, "result": 2}
    mock_get = mocker.patch.object(requests, "get", autospec=True)
    mock_get(Converter.API_URL).json.return_value = data
    yield mock_get
    mock_get.assert_called_with(
        Converter.API_URL,
        params={"from": "EUR", "to": "CHF"},
        headers={"User-Agent": Converter.USER_AGENT})


@pytest.fixture
def converter() -> Converter:
    return Converter()


def test_eur2chf(converter: Converter):
    assert converter.eur2chf(1) == 2

def test_chf2eur(converter: Converter):
    assert converter.chf2eur(1) == 0.5
