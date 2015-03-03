import git
import os


current = os.path.abspath(os.getcwd())
parent = os.path.abspath(os.pardir)

repo = None

while True:

    try:
        repo = git.Repo(current)
        break
    except git.exc.InvalidGitRepositoryError:
        if current == parent:
            break

        current = parent
        parent = os.path.abspath(os.path.join(current, os.pardir))

from get_origin import get_origin
from git_config import git_config
