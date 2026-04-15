import pytest
import requests
from pytest_mock import MockerFixture, MockType

from rpncalc.convert import Converter


@pytest.fixture
def mock_get(mocker: MockerFixture, exchange_data: dict) -> MockType:
    mock = mocker.patch.object(requests, "get", autospec=True)
    mock(Converter.API_URL).json.return_value = exchange_data
    return mock


@pytest.fixture
def converter() -> Converter:
    return Converter()


def test_eur2chf(converter: Converter, mock_get: MockType):
    assert converter.eur2chf(1) == 2
    mock_get.assert_called_with(
        Converter.API_URL,
        params=Converter.PARAMS,
        headers=Converter.HEADERS,
        timeout=Converter.TIMEOUT,
    )


def test_chf2eur(converter: Converter, mock_get: MockType):
    assert converter.chf2eur(1) == 0.5
    mock_get.assert_called_with(
        Converter.API_URL,
        params=Converter.PARAMS,
        headers=Converter.HEADERS,
        timeout=Converter.TIMEOUT,
    )
