import subprocess

# fixtures/test_builtin_capfd.py
def test_output(capfd):
    subprocess.run(["ls"])
    out, err = capfd.readouterr()
    assert out == "..."
