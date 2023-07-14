from rpncalc.rpn_v3 import RPNCalculator, Config
import yaml
import pytest

class YamlException(Exception):
    """Custom exception for error reporting."""


def pytest_collect_file(parent, file_path):
    if file_path.suffix == ".yml" and file_path.name.startswith("test"):
        return YamlFile.from_parent(parent, path=file_path)


class YamlFile(pytest.File):
    def collect(self):
        with self.path.open("r") as f:
            raw = yaml.safe_load(f)

        for spec in raw:
            name = spec["name"]
            yield YamlItem.from_parent(self, name=name, spec=spec)


class YamlItem(pytest.Item):
    def __init__(self, name, parent, spec):
        super().__init__(name, parent)
        self.spec = spec

    def runtest(self):
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

    def repr_failure(self, excinfo):
        """Called when self.runtest() raises an exception."""
        if isinstance(excinfo.value, YamlException):
            return f"Invalid YAML: {excinfo.value}"
        return super().repr_failure(excinfo)

    def reportinfo(self):
        """Return the path/linenumber/text to show."""
        return self.fspath, 0, f"usecase: {self.name}"
