import pytest


class Client:
    def connect(self):
        print("connect")

    def disconnect(self):
        print("disconnect")


@pytest.fixture
def connected_client(request: pytest.FixtureRequest) -> Client:
    client = Client()
    client.connect()
    request.addfinalizer(client.disconnect)
    return client


def test_one(connected_client: Client):
    pass


def test_two(connected_client: Client):
    pass


def test_three(connected_client: Client):
    pass
