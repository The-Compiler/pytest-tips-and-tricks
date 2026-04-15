def test_ok():
    pass


def test_bad():
    1/0


def test_custom(record_property):
    record_property("example_key", 1)
