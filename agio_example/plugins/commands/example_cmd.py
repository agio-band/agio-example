import click
from pathlib import Path

from agio.core.events import emit
from agio.core.plugins.base_command import ACommandPlugin


class SimpleCommand(ACommandPlugin):
    name = 'example_cmd'
    command_name = 'example'
    arguments = [
        # use click "argument" and "option" functions to set up command arguments
        click.option("-a", "--arg-a", is_flag=True, help='Bool flag'),
        click.option("-b", "--arg-b", help='String argument'),
        click.option('-c', '--arg-c', help='Path Argument',
                     type=click.Path(exists=True, dir_okay=True, resolve_path=True),
                     default=Path.cwd().absolute().as_posix()
                     ),
    ]
    allow_extra_args = True
    # catch all arguments and get it in __extra_args__ value

    def execute(self, arg_a: bool, arg_b: str, arg_c: str, __extra_args__: list = None):
        print('='*50)
        print('Simple Command')
        print(f'arg_a: {arg_a}')
        print(f'arg_b: {repr(arg_b)}')
        print(f'arg_c: {arg_c}')
        print('Extra args:', __extra_args__)
        print('='*50)
        emit('example.command.event1', 1)
        emit('example.command.event2', 2)
