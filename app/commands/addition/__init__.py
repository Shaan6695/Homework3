from app.commands import Command

class AddCommand(Command):
    def __init__(self, a, b):
        super().__init__()
        self.a = a
        self.b = b

    def execute(self):
        result = self.a + self.b
        print(f"The sum of {self.a} and {self.b} is: {result}")

# Example usage:
# add_cmd = AddCommand(5, 3)
# add_cmd.execute()
