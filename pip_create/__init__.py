#!/usr/bin/python
# -*- coding: utf-8 -*-
import jinja2
import _version
from questions import question_list, template_vars

__version__ = _version.__version__


def main():

    for question in question_list:
        question.ask()

    # Set up Jinja2 template engine
    env = jinja2.Environment(loader=jinja2.PackageLoader('pip_create',
                                                         'templates'),
                             extensions=['jinja2.ext.do'])

    template = env.get_template("base.j2")

    setup_content = template.render(template_vars)

    setup_content = "\n".join([x for x in setup_content.split("\n")
                               if x.strip()])

    setup_content = setup_content.replace("\\n", "")

    with open('setup.py', 'w') as setup_file:
        setup_file.write(setup_content)


if __name__ == '__main__':
    main()
