import pytest
import logging


def test_output(caplog: pytest.LogCaptureFixture):
    logging.warning("Something failed")
    assert caplog.messages == ["Something failed"]


def test_record_tuples(caplog: pytest.LogCaptureFixture):
    logging.warning("Something failed")
    assert caplog.record_tuples == [
        ("root", logging.WARNING, "Something failed"),
    ]
