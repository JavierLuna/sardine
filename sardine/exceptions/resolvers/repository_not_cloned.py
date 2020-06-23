from sardine.exceptions.sardine_exception import SardineException

class RepositoryNotCloned(SardineException):

    def __init__(self, repository_name: str):
        super().__init__(f"Repository '{repository_name}' not found.")

