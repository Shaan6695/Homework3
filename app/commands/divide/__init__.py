from app.commands import Command

class DivideCommand(Command):
    def __init__(self, a, b):
        super().__init__()
        self.a = a
        self.b = b

    def execute(self):
        if self.b == 0:
            print("Error: Cannot divide by zero")
        else:
            result = self.a / self.b
            print(f"The division of {self.a} by {self.b} is: {result}")

# Example usage:
# divide_cmd = DivideCommand(10, 2)
# divide_cmd.execute()
