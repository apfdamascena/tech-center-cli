import click
import os
class ComplexCLI(click.MultiCommand):
    def list_commands(self, ctx):
        commands = []
        for filename in os.listdir(os.path.join(os.path.dirname(__file__), "commands")):
            if filename.endswith(".py") and not filename.startswith("__"):
                commands.append(filename.replace('.py',''))
        commands.sort()
        return commands

    def get_command(self, ctx, name):
        try:
            module = __import__(f"techcenter.commands.{name}", None, None, ["cli"])
        except ImportError:
            return
        return module.cli

@click.command(cls=ComplexCLI)
def cli():
    """Hablas comigo Tech Center"""
    pass