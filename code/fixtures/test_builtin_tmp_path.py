from pathlib import Path
import pytest
from rpncalc.utils import Config


@pytest.fixture
def config():
    return Config()


@pytest.fixture
def config_path(tmp_path: Path) -> Path:
    lines = ["[rpncalc]", "prompt = rpn>"]
    path = tmp_path / "calc.ini"
    path.write_text("\n".join(lines))
    return path

def test_config_load(
    config_path: Path, config: Config
):
    print(config_path)
    assert False  # to show output


def test_config_save(tmp_path: Path, config: Config):
    ...
