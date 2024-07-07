import pathlib
import configparser
import os


def calc(a, b, op):
    if op == "+":
        return a + b
    elif op == "-":
        return a - b
    elif op == "*":
        return a * b
    elif op == "/":
        return a / b
    raise ValueError("Invalid operator")


class Config:
    def __init__(self, prompt=">"):
        self.prompt = prompt

    def __repr__(self) -> str:
        return f"Config(prompt={self.prompt!r})"

    def load(self, path: pathlib.Path) -> None:
        parser = configparser.ConfigParser()
        parser.read(path)
        self.prompt = parser["rpncalc"]["prompt"]

    def save(self, path: pathlib.Path) -> None:
        parser = configparser.ConfigParser()
        parser["rpncalc"] = {"prompt": self.prompt}
        with path.open("w") as f:
            parser.write(f)

    def load_env(self) -> None:
        var = "RPNCALC_CONFIG_DIR"
        config_dir = os.environ.get(var)
        if not config_dir:
            return
        path = pathlib.Path(config_dir)
        ini_path = path / "rpncalc.ini"
        if not ini_path.exists():
            raise FileNotFoundError(
                f"{ini_path} not found")
        self.load(ini_path)