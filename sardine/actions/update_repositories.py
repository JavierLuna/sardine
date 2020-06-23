from sardine.actions.base import BaseAction
from sardine.resolvers.manifest.local import LocalManifestResolver
from sardine.resolvers.repository.remote import RemoteRepositoryResolver


class UpdateRepositories(BaseAction):

    @classmethod
    def execute(cls, *args, **kwargs):
        manifest = LocalManifestResolver.load_manifest()
        different_repositories = {declaration.repository_name for declaration in manifest.values()}
        for repository in different_repositories:
            if RemoteRepositoryResolver.repository_already_cloned(
                    RemoteRepositoryResolver.get_repository_path(repository)):
                print(f"Updating '{repository}'...")
                RemoteRepositoryResolver.update(repository)
