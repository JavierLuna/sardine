from sardine.cli.commands.base import BaseCommand
from sardine.actions.update_repositories import UpdateRepositories

class UpdateCommand(BaseCommand):
    """
    Updates all registered stack repositories.
    """
    __command_name__ = 'update'

    @classmethod
    def execute(cls, args):
        UpdateRepositories.execute()
