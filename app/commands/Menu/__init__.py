import sys
from app.commands import Command


class MenuCommand(Command):
    def execute(self):
        sys.exit("Menu")