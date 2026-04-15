import pytest
from typing import Iterator


class Client:
    def connect(self):
        print("\nConnecting...")

    def disconnect(self):
        print("\nDisconnecting...")


# exercise: [yield]

@pytest.fixture(scope="function")
def connected_client() -> Iterator[Client]:
    client = Client()
    client.connect()
    yield client
    client.disconnect()

@pytest.fixture
def connected_client_skip() -> Iterator[Client]:
    client = Client()
    pytest.skip("Client not available")
    client.connect()
    yield client
    client.disconnect()

def test_client_1(connected_client: Client):
    print("in the test 1")

def test_client_2(connected_client: Client):
    print("in the test 2")
