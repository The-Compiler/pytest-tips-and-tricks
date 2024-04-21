from rpncalc.utils import calc, Config
from rpncalc.convert import Converter


class RPNCalculator:
    def __init__(self, config):
        self.converter = Converter()
        self.config = config
        self.stack = []

    def get_inputs(self):
        inp = input(self.config.prompt + " ")
        return inp.split()

    def run(self):
        while True:
            for inp in self.get_inputs():
                if inp == "q":
                    return
                elif inp == "p":
                    print(self.stack)
                else:
                    self.evaluate(inp)

    def _evaluate_convert(self, inp):
        try:
            amount = self.stack.pop()
        except IndexError:
            print("Not enough operands")
            return

        if inp == "eur2chf":
            res = self.converter.eur2chf(amount)
        elif inp == "chf2eur":
            res = self.converter.chf2eur(amount)

        self.stack.append(res)
        print(f"{res:.2f}")

    def evaluate(self, inp):
        try:
            self.stack.append(float(inp))
            return
        except ValueError:
            pass

        if inp in ["eur2chf", "chf2eur"]:
            self._evaluate_convert(inp)
            return
        elif inp not in ["+", "-", "*", "/"]:
            print(f"Invalid input: {inp}")
            return

        if len(self.stack) < 2:
            print("Not enough operands")
            return

        b = self.stack.pop()
        a = self.stack.pop()

        try:
            res = calc(a, b, inp)
        except ZeroDivisionError:
            print("Division by zero")
            return

        self.stack.append(res)
        print(res)


if __name__ == "__main__":
    config = Config()
    rpn = RPNCalculator(config)
    rpn.run()
