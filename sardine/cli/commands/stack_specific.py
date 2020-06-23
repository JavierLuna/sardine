from sardine.cli.commands.base import BaseCommand

class StackSpecificCommand(BaseCommand):
    @classmethod
    def attach_args(cls, arggroup):
        arggroup.add_argument("stack", help="Target stack")
