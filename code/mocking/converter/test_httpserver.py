import pytest
import pytest_httpserver
import urllib.parse
from rpncalc.convert import Converter


@pytest.fixture
def server_url(
    httpserver: pytest_httpserver.HTTPServer, exchange_data: dict
):
    url_path = urllib.parse.urlparse(Converter.API_URL).path

    req = httpserver.expect_request(
        url_path, query_string=Converter.PARAMS,
        headers=Converter.HEADERS,
    )
    req.respond_with_json(exchange_data)

    yield httpserver.url_for(url_path)
    httpserver.check()


@pytest.fixture
def converter(
    server_url: str,  # e.g. http://localhost:41475/v1/currencies/...
    monkeypatch: pytest.MonkeyPatch,
) -> Converter:
    conv = Converter()
    monkeypatch.setattr(conv, "API_URL", server_url)
    return conv

def test_eur2chf(converter: Converter):
    assert converter.eur2chf(1) == 2

def test_chf2eur(converter: Converter):
    assert converter.chf2eur(1) == 0.5