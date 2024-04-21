from rpncalc.utils import calc, Config

class RPNCalculator:
    def __init__(self, config):
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

    def evaluate(self, inp):
        try:
            self.stack.append(float(inp))
            return
        except ValueError:
            pass

        if inp not in ["+", "-", "*", "/"]:
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
