import pytest
from rpncalc.convert import Converter

from responses import RequestsMock, matchers

@pytest.fixture(autouse=True)
def patch_requests_get(
    responses: RequestsMock, exchange_data: dict
) -> None:
    responses.get(
        Converter.API_URL,
        json=exchange_data,
        match=[
            matchers.query_param_matcher(Converter.PARAMS),
            matchers.header_matcher(Converter.HEADERS),
        ],
    )


@pytest.fixture
def responses():
    # NOTE: Normally you would use the `responses` fixture from the
    # pytest-responses plugin instead of hand-rolling it like here.
    #
    # However, the plugin assumes that it's responsible for all requests (and
    # all of them should be mocked using it).
    #
    # Since we want to demonstrate other ways too, we avoid installing it.
    with RequestsMock() as rm:
        yield rm


@pytest.fixture
def converter() -> Converter:
    return Converter()


def test_eur2chf(converter: Converter):
    assert converter.eur2chf(1) == 2


def test_chf2eur(converter: Converter):
    assert converter.chf2eur(1) == 0.5