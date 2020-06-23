import argparse
from typing import Type, Dict

from sardine.cli.commands.update import UpdateCommand
from sardine.cli.commands.run import RunCommand
from sardine.cli.commands.base import BaseCommand
from sardine.cli.commands.stop import StopCommand

all_commands = [UpdateCommand, RunCommand, StopCommand]

def get_registered_commands() -> Dict[str, Type[BaseCommand]]:
    return {command.__command_name__: command for command in all_commands}

def parse_args(registered_commands: Dict[str, Type[BaseCommand]]):
    parser = argparse.ArgumentParser()
    subparsers = parser.add_subparsers(help="commands", dest="command")
    for command_name, command in registered_commands.items():
        command_subparser = subparsers.add_parser(command_name, help=command.__doc__)
        command.attach_args(command_subparser)
    return parser.parse_args()

def main():
    registered_commands = get_registered_commands()
    args = parse_args(registered_commands)
    registered_commands[args.command].execute(args)


if __name__ == '__main__':
    main()
