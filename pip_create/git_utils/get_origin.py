from . import repo
import urllib
from urlparse import urlparse
from sys import version_info


def url_parse(url):
    if version_info >= (3, 0):
        return urllib.parse(url)
    else:
        return urlparse(url)


def get_origin():
    if repo is None:
        raise ValueError("No repo found!")

    for remote in repo.remotes:

        if remote.name == "origin":
            parsed = url_parse(remote.url)

            if parsed.hostname and parsed.netloc and \
                    parsed.hostname != parsed.netloc:
                return parsed.geturl().replace(parsed.netloc, parsed.hostname)
            else:
                return remote.url

    return None
