import pytest
from typing import Iterator


class Client:
    def connect(self):
        print("\nConnecting...")

    def disconnect(self):
        print("\nDisconnecting...")


@pytest.fixture(scope="function")
def connected_client() -> Iterator[Client]:
    client = Client()
    client.connect()
    yield client
    client.disconnect()

def test_client(connected_client: Client):
    print("in the test")
