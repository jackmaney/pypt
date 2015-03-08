"""
Usage: pypt init [options]

    -h --help
    -i --interactive   Interactive mode (without this flag, defaults are used)
"""

from docopt import docopt
from ..question.series.init import get_series
from .._version import __version__
from ..templates import get_template

import re


def init(argv):

    args = docopt(__doc__, argv=argv)

    series = get_series()

    if args["--interactive"]:

        print "pypt version {}\n".format(__version__)
        series.ask()

    else:

        series.process()

    template = get_template("init", extensions=["jinja2.ext.do"])

    setup_content = template.render(**series.template_vars)

    setup_content = "\n".join([x for x in setup_content.split("\n")
                               if x.strip()])

    setup_content = setup_content.replace("\\n", "")

    setup_content = re.sub("(?:\n\s*){3,}", "\n\n", setup_content)

    with open('setup.py', 'w') as setup_file:
        setup_file.write(setup_content)
