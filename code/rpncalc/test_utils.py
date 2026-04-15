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
def example_ini(ini_path: Path) -> Path:
    # creates rpncalc.ini with pathlib
    ini_path.write_text(
        "[rpncalc]\n"
        "prompt = rpn>\n")
    return ini_path


# exercise: [load-save]

def test_config_load(
    example_ini: Path, config: Config
):
    # call config.load(...), ensure that the prompt is set to "rpn>"
    ...


def test_config_save(
    ini_path: Path, config: Config
):
    # call config.save(...), ensure that
    # the ini file is written correctly
    ...


# exercise: [cwd]


# exercise: [implicit]
