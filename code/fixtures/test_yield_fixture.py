import pytest
from typing import Iterator

class Client:

    def connect(self):
        print("Connecting...")

    def disconnect(self):
        print("Disconnecting...")

# fixtures/test_yield_fixture.py

@pytest.fixture
def connected_client() -> Iterator[Client]:
    client = Client()
    client.connect()
    yield client
    client.disconnect()

def test_client(connected_client: Client):
    print("in the test")
