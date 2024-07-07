import logging


def test_output(caplog):
    logging.warning("Something failed")
    assert caplog.messages == ["Something failed"]


def test_record_tuples(caplog):
    logging.warning("Something failed")
    assert caplog.record_tuples == [
        ("root", logging.WARNING, "Something failed")
    ]