import subprocess


def test_capsys(capsys):
    print("Hello World")
    out, err = capsys.readouterr()
    assert out == "Hello World\n"


def test_capfd(capfd):
    subprocess.run(["ls"])
    out, err = capfd.readouterr()
    assert out == "..."
