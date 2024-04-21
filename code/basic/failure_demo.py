def test_eq_text():
    assert "spam" == "eggs"


def test_eq_similar_text():
    assert "foo 1 bar" == "foo 2 bar"


def test_eq_long_text():
    a = "1" * 100 + "a" + "2" * 100
    b = "1" * 100 + "b" + "2" * 100
    assert a == b


def test_eq_list():
    assert [0, 1, 2] == [0, 1, 3]


def test_eq_dict():
    assert {"a": 0, "b": 1} == {"a": 0, "b": 2}


def test_eq_set():
    assert {0, 10, 11, 12} == {0, 20, 21}


def test_eq_longer_list():
    assert [1, 2] == [1, 2, 3]


def test_not_in_text_single():
    text = "single foo line"
    assert "foo" not in text
