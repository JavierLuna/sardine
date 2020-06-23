from sardine.cli.commands.stack_specific import StackSpecificCommand
from sardine.actions.stop_stack import StopStack

class StopCommand(StackSpecificCommand):
    """
    Stop a stack
    """
    __command_name__ = 'stop'


    @classmethod
    def execute(cls, args):
        StopStack.execute(args.stack)
