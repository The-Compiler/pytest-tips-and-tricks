def test_output(capsys):
    print("Hello World")
    out, err = capsys.readouterr()
    assert out == "Hello World\n"
