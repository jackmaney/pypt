#!/usr/bin/python
# -*- coding: utf-8 -*-
import jinja2
from sys import version_info
from subprocess import Popen, PIPE
from getpass import getuser
from textwrap import dedent
import os
import re


def get_input(input_msg):

    if version_info >= (3, 0):
        return input(input_msg)
    else:
        return raw_input(input_msg)


def get_username():
    '''Get git config values.'''
    username = ''

    # use try-catch to prevent crashes if user doesn't install git
    try:
        # run git config --global <key> to get username
        git_command = ['git', 'config', '--global', 'user.name']
        p = Popen(git_command, stdout=PIPE, stderr=PIPE)
        output, err = p.communicate()

        # turn stdout into unicode and strip it
        username = output.decode('utf-8').strip()

        # if user doesn't set global git config name, then use getuser()
        if not username:
            username = getuser()
    except OSError:
        # if git command is not found, then use getuser()
        username = getuser()

    return username


def get_email():

    try:
        git_command = ['git', 'config', '--global', 'user.email']
        p = Popen(git_command, stdout=PIPE, stderr=PIPE)
        output, err = p.communicate()

        email = output.decode('utf-8').strip()

        if not email:
            return None

    except OSError:

        return None


def main():

    setup_kwargs = {}
    requirements_file = None
    requirements_list = None
    find_packages = None
    packages_list = None

    fields = [
        {"name": "Name", "default": os.path.relpath(".", "..")},
        {"name": "Version", "default": "0.0.0"},
        {"name": "Description",
            "default": "%s is a package" % os.path.relpath(".", "..")},
        {"name": "License", "default": "MIT"},
        {"name": "Author", "default": get_username()},
        {"name": "Author Email", "arg":"author_email", "default":get_email()},
        {"name": "Requirements", "description": dedent("""
        Would you like to read your requirements from a [f]ile?
        Would you like to [s]pecify your requirements manually?
        Or would you like to [n]ot specify any requirements?
        [f/s/n] """)},
        {"name": "Packages", "description": dedent("""
        Would you like to use [f]ind_packages from setuptools to find the packages
        included within your distribution?
        Would you like to [s]pecify the packages yourself?
        Or would you like to [n]ot specify any packages?
        [f/s/n] """)}
    ]

    for field in fields:

        if "default" in field:

            if field["default"]:
                user_input = get_input("{} ({}): ".format(field["name"],
                                                          field["default"]))
            else:
                user_input = get_input("{}: ".format(field["name"]))

            if not user_input:
                user_input = field["default"]

            if user_input:
                arg = field["name"].lower()

                if "arg" in field:
                    arg = field["arg"]

                setup_kwargs[arg] = "'%s'" % user_input

        elif field["name"] == "Requirements":
            user_input = None

            while user_input is None or \
                    user_input.lower() not in ["f", "s", "n"]:

                user_input = get_input("{}:\n{}".format(field["name"],
                                                        field["description"]))

                if user_input.lower() == "f":

                    file_name = get_input(
                        "Great! Which file?\n[requirements.txt]")

                    if not file_name:
                        file_name = "requirements.txt"

                    requirements_file = file_name

                elif user_input.lower() == "s":

                    req_list = get_input(
                        "Please specify a comma-delimited \
list of requirements:\n")

                    requirements_list = ["'%s'" % x for x in
                                         re.split("\s*,\s*", req_list) if x]

        elif field["name"] == "Packages":
            user_input = None

            while user_input is None or \
                    user_input.lower() not in ["f", "s", "n"]:
                user_input = get_input("{}:\n{}".format(field["name"],
                                                        field["description"]))

                if user_input.lower() == "f":

                    find_packages = True

                elif user_input.lower() == "s":

                    p_list = get_input(
                        "Please specify a comma-delimited list of packages in \
your distribution:\n")

                    packages_list = [x for x in
                                     re.split("\s*,\s*", p_list) if x]

    # Set up Jinja2 template engine
    env = jinja2.Environment(loader=jinja2.PackageLoader('pip_create',
                                                         'templates'),
                             extensions=['jinja2.ext.do'])

    template = env.get_template("base.j2")

    setup_content = template.render(setup_kwargs=setup_kwargs,
                                    requirements_file=requirements_file,
                                    requirements_list=requirements_list,
                                    find_packages=find_packages,
                                    packages_list=packages_list)

    setup_content = "\n".join([x for x in setup_content.split("\n")
                               if x.strip()])

    setup_content = setup_content.replace("\\n", "")

    with open('setup.py', 'w') as setup_file:
        setup_file.write(setup_content)


if __name__ == '__main__':
    main()
