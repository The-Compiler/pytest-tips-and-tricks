import pytest
import pathlib


@pytest.fixture
def tmp_homedir(tmp_path, monkeypatch):
    monkeypatch.setenv("HOME", str(tmp_path))
    return tmp_path


@pytest.mark.usefixtures("tmp_homedir")
class TestHomeDir:
    def test_empty(self):
        assert not list(pathlib.Path.home().iterdir())
