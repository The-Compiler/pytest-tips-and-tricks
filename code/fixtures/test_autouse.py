import pytest
import pathlib


class TestEmptyHomedir:
    @pytest.fixture(autouse=True)
    def tmp_homedir(self, tmp_path, monkeypatch):
        monkeypatch.setenv("HOME", str(tmp_path))
        return tmp_path

    def test_a(self, tmp_homedir):
        assert not list(tmp_homedir.iterdir())

    def test_b(self):
        assert not list(pathlib.Path.home().iterdir())
