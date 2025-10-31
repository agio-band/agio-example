from agio.core.plugins.base_command import ACommandPlugin, ASubCommand
import click


class SubCommand1(ASubCommand):
    command_name = "cmd1"

    def execute(self,  **kwargs):
        click.secho(f'Command 1', fg='yellow')


class SubCommand2(ASubCommand):
    command_name = "cmd2"

    def execute(self,  **kwargs):
        click.secho(f'Command 2', fg='yellow')


class ExampleSubCommand(ACommandPlugin):
    name = 'example_sub_cmd'
    command_name = "subcmd"
    subcommands = [
        SubCommand1,
        SubCommand2,
    ]
    help = 'Example sub commands'
    allow_empty_root_command = True

    def execute(self, **kwargs):
        click.secho(f'Root Command', fg='yellow')