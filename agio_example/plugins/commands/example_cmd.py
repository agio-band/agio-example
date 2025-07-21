import click
from pathlib import Path

from agio.core.events import emit
from agio.core.plugins.base_command import ACommandPlugin


class SimpleCommand(ACommandPlugin):
    name = 'example_cmd'
    command_name = 'example'
    arguments = [
        click.option("-a", "--arg-a", is_flag=True, help='Bool flag'),
        click.option("-b", "--arg-b", help='String argument'),
        click.option('-c', '--arg-c', help='Path Argument',
                     type=click.Path(exists=True, dir_okay=True, resolve_path=True),
                     default=Path.cwd().absolute().as_posix()
                     ),
    ]

    def execute(self, arg_a: bool, arg_b: str, arg_c: str):
        print('='*50)
        print('Simple Command')
        print(f'arg_a: {arg_a}')
        print(f'arg_b: {repr(arg_b)}')
        print(f'arg_c: {arg_c}')
        print('='*50)
        emit('example.command.event1', 1)
        emit('example.command.event2', 2)
