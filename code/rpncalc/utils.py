import pathlib
import configparser


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
        with path.open("r") as f:
            parser.read_file(f)
        self.prompt = parser["rpncalc"]["prompt"]

    def save(self, path: pathlib.Path) -> None:
        parser = configparser.ConfigParser()
        parser["rpncalc"] = {"prompt": self.prompt}
        with path.open("w") as f:
            parser.write(f)

    def load_cwd(self) -> bool:
        ini = pathlib.Path.cwd() / "rpncalc.ini"
        if ini.exists():
            self.load(ini)
            return True
        return False
