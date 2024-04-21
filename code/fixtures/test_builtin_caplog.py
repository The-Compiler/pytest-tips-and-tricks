import logging


def test_output(caplog):
    logging.warning("Something failed")
    assert caplog.messages == ["Something failed"]
