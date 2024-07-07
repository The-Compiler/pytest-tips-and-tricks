import pytest

@pytest.fixture
def exchange_data() -> dict:
    rates = [{"alias": "chf", "rate": 2}]
    return {"data": {"alias": "eur", "rates": rates}}