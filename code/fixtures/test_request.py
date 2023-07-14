import pytest

@pytest.fixture
def db(request):
    marker = request.node.get_marker("database")
    db = somelib.setup_db(name=marker.kwargs['name'])
    db.blah()
    return db


@pytest.mark.database(name='test')
def test_foo(db):
    assert db.get('foo') == 'bar'


@pytest.mark.database(name='production')
def test_bar(db):
    assert db.get('foo') == 'baz'
