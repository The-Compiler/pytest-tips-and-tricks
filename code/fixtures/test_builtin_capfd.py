import subprocess


def test_output(capfd):
    subprocess.run(["ls"])
    out, err = capfd.readouterr()
    assert out == "..."
