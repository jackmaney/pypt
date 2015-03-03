import git
from . import repo
from warnings import warn


def git_config(section, option):

    result = None

    if repo is not None:

        try:
            result = repo.config_reader().get(section, option)

        except git.exc.NoOptionError:
            warn("No '{}.{}' git configuration found for this repo".format(
                section, option
            ))

    return result
