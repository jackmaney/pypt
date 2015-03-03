"""
Usage:  pypt [--version] [--help]
        pypt <command> [<args>...]

Commands:
    init    Set up a new Python package (setup.py, MANIFEST.in, etc)
    config  Get/set configuration options
"""

from _version import __version__
from docopt import docopt
from command import commands


def main(argv=None):

    args = docopt(__doc__, version=__version__, options_first=True, argv=argv)

    command_argv = [args["<command>"]] + args["<args>"]

    if args["<command>"] in commands:
        cmd = commands[args["<command>"]]
        cmd(command_argv)
    elif args["<command>"] in ["help", None]:
        main(argv=["--help"])
