"""
Usage: pypt init [options]

    -h --help
    -i --interactive   Interactive mode (without this flag, defaults are used)
"""

from docopt import docopt
from ..questions import question_list, template_vars
from .._version import __version__

import jinja2


def init(argv):

    args = docopt(__doc__, argv=argv)

    if args["--interactive"]:

        print "pypt version {}\n".format(__version__)
        for question in question_list:
            question.ask()

    else:

        for question in question_list:
            question.process()

    # Set up Jinja2 template engine
    env = jinja2.Environment(loader=jinja2.PackageLoader('pypt',
                                                         'templates'),
                             extensions=['jinja2.ext.do'])

    template = env.get_template("base.j2")

    setup_content = template.render(template_vars)

    setup_content = "\n".join([x for x in setup_content.split("\n")
                               if x.strip()])

    setup_content = setup_content.replace("\\n", "")

    with open('setup.py', 'w') as setup_file:
        setup_file.write(setup_content)
