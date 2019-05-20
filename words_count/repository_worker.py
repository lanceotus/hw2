from git import Repo

class RepositoryException(Exception):
    pass

class Repository:
    @staticmethod
    def clone(url, local_path="/tmp/tmp_repo"):
        if "github" in url:
            Repository._clone_from_github(url, local_path)

    @staticmethod
    def _clone_from_github(url, local_path="/tmp/tmp_repo"):
        try:
            Repo.clone_from(url, local_path)
        except:
            raise RepositoryException("Не удалось клонировать репозиторий {0} в директорию {1}."
                                      .format(url, local_path))
