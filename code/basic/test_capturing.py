def test_ok():
    print("This isn't printed")


def test_bad():
    print("This is printed")
    assert False
