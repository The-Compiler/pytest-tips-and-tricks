from __future__ import annotations

import pathlib
from typing import Iterator, Any

import yaml
import pytest

from rpncalc.rpn_v3 import RPNCalculator, Config


class YamlException(Exception):
    """Custom exception for error reporting."""


def pytest_collect_file(
    parent: pytest.Collector,
    file_path: pathlib.Path,
) -> pytest.Collector | None:
    """Hook into pytest to collect test*.yml files."""
    if (
        file_path.suffix == ".yml"
        and file_path.name.startswith("test")
    ):
        return YamlFile.from_parent(parent, path=file_path)
    return None


class YamlFile(pytest.File):
    """Internal representation of a YAML test file."""

    def collect(self) -> Iterator[YamlItem]:
        with self.path.open("r") as f:
            raw = yaml.safe_load(f)

        for spec in raw:
            name = spec["name"]
            yield YamlItem.from_parent(self, name=name, spec=spec)


class YamlItem(pytest.Item):
    """Internal representation of a single test."""

    def __init__(self, name: str, parent: YamlFile, spec: dict[str, Any]):
        super().__init__(name, parent)
        self.spec = spec

    def runtest(self) -> None:
        """Run the test, raise exceptions on issues."""
        rpn = RPNCalculator(Config())
        try:
            inputs = self.spec["inputs"]
            stack = self.spec["stack"]
        except KeyError as e:
            raise YamlException(f"Missing key: {e}")

        for inp in inputs:
            rpn.evaluate(inp)

        assert rpn.stack == stack

    def repr_failure(self, excinfo: pytest.ExceptionInfo) -> str:
        """Called when self.runtest() raises an exception."""
        if isinstance(excinfo.value, YamlException):
            return f"Invalid YAML: {excinfo.value}"
        return super().repr_failure(excinfo)

    def reportinfo(self) -> tuple[str, int, str]:
        """Return the path/linenumber/text to show."""
        return self.fspath, 0, f"usecase: {self.name}"
