from sys import version_info
from subprocess import Popen, PIPE
from getpass import getuser
from urlparse import urlparse
import git

try:
    repo = git.Repo(path=".")

except git.InvalidGitRepositoryError:
    repo = None


def get_input(input_msg):

    if version_info >= (3, 0):
        return input(input_msg)
    else:
        return raw_input(input_msg)


def url_parse(url):
    if version_info >= (3, 0):
        import urllib
        return urllib.parse(url)
    else:
        from urlparse import urlparse
        return urlparse(url)


def run_command(cmd):

    try:
        p = Popen(cmd, stdout=PIPE, stderr=PIPE)
        output, err = p.communicate()

        result = output.decode("utf-8").strip()
        return result

    except OSError:
        return None


def git_config(name):

    result = run_command(["git", "config", "--local", name])

    if result is None or result == "":
        result = run_command(["git", "config", "--global", name])

    return result


def get_origin():

    if repo is None:
        return None

    for remote in repo.remotes:

        if remote.name == "origin":
            parsed = url_parse(remote.url)

            if parsed.hostname and parsed.netloc and \
                    parsed.hostname != parsed.netloc:
                return parsed.geturl().replace(parsed.netloc, parsed.hostname)
            else:
                return remote.url
