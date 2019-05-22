from git import Repo

class RepositoryException(Exception):
    pass

def clone(url, local_path="/tmp/tmp_repo"):
    if "github" in url:
        clone_from_github(url, local_path)

def clone_from_github(url, local_path="/tmp/tmp_repo"):
    try:
        Repo.clone_from(url, local_path)
    except:
        raise RepositoryException("Не удалось клонировать репозиторий {0} в директорию {1}."
                                  .format(url, local_path))
