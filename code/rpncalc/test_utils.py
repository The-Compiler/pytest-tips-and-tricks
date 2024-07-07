from pathlib import Path

import pytest

from rpncalc.utils import Config


@pytest.fixture
def config():
    return Config()


@pytest.fixture
def ini_path(tmp_path: Path) -> Path:
    return tmp_path / "rpncalc.ini"

@pytest.fixture
def config_path(ini_path: Path) -> Path:
    contents = (
        "[rpncalc]\n"
        "prompt = rpn>"
    )
    ini_path.write_text(contents)
    return ini_path


def test_config_load(config_path: Path, config: Config):
    # call config.load(...), ensure that the prompt is set to "rpn>"
    ...


def test_config_save(ini_path: Path, config: Config):
    # call config.save(...), ensure that the ini file is written correctly
    ...


