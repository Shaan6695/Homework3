from app.commands import Command

class MultiplyCommand(Command):
    def __init__(self, a, b):
        super().__init__()
        self.a = a
        self.b = b

    def execute(self):
        result = self.a * self.b
        print(f"The product of {self.a} and {self.b} is: {result}")

# Example usage:
# multiply_cmd = MultiplyCommand(4, 7)
# multiply_cmd.execute()
