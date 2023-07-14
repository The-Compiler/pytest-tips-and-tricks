import pytest

class Client:
    def connect(self):
        print("connect")

    def disconnect(self):
        print("disconnect")

# fixtures/test_fixture_finalizer.py
@pytest.fixture
def connected_client(request: pytest.FixtureRequest) -> Client:
    client = Client()
    client.connect()
    request.addfinalizer(client.disconnect)
    return client

def test_one(client):
    pass

def test_two(client):
    pass

def test_three(client):
    pass
