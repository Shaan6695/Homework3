from app.commands import Command

class SubtractCommand(Command):
    def __init__(self, a, b):
        super().__init__()
        self.a = a
        self.b = b

    def execute(self):
        result = self.a - self.b
        print(f"The difference between {self.a} and {self.b} is: {result}")

# Example usage:
# subtract_cmd = SubtractCommand(8, 3)
# subtract_cmd.execute()
