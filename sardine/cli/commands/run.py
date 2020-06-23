from sardine.cli.commands.base import BaseCommand
from sardine.cli.commands.stack_specific import StackSpecificCommand

from sardine.actions.download_repositories import DownloadRepositories
from sardine.actions.execute_stack import ExecuteStack

class RunCommand(StackSpecificCommand):
    """
    Runs a stack
    """
    __command_name__ = 'run'

    @classmethod
    def attach_args(cls, arggroup):
        super(RunCommand, cls).attach_args(arggroup)
        arggroup.add_argument("-d", "--detached", action='store_true', default=False)


    @classmethod
    def execute(cls, args):
       DownloadRepositories.execute()
       ExecuteStack.execute(args.stack, detached=args.detached)
