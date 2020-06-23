from abc import abstractmethod
from abc import ABCMeta

class BaseCommand():
    __command_name__ = ''

    @classmethod
    def attach_args(cls, arggroup):
        pass

    @classmethod
    def execute(cls, args):
        raise NotImplementedError("Base commands must implement this method")
