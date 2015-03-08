from . import Series
from .. import reader, writer
from ..question import Question
from ..choice import ChoiceQuestion
from textwrap import dedent
from ...git_utils import git_config, get_origin
import sys

import os
import re

__all__ = ["get_series"]


def setup_update(question):

    current_value = question.series.template_vars[
        "setup"].get(question.key)

    if isinstance(current_value, list):
        current_value.append(question.user_input)
        question.series.template_vars["setup"][
            question.key] = current_value
    else:
        question.series.template_vars.get(
            "setup")[question.key] = question.user_input


def update_comma_sep_list(question):

    question.series.template_vars[question.key] = [
        x.strip() for x in re.split("\s*,\s*", question.user_input)
        if x.strip()]


class SetupQuestion(Question):

    def __init__(self, name, *args, **kwargs):
        kwargs["update_function"] = setup_update

        if not kwargs.get("key"):
            kwargs["key"] = name.lower()
        super(SetupQuestion, self).__init__(name, *args, **kwargs)

    def process(self):
        super(SetupQuestion, self).process()
        print "{}={}".format(self.key, self.user_input)


def get_series():

    config_data = reader.read_config()

    if config_data is None:
        msg = "Warning: No configuration file found. Creating a \
    configuration file at {}".format(reader.global_config_file)
        print >> sys.stderr, msg
        writer.write_default_config()
        config_data = reader.read_config()

    config_data = config_data["init"]

    print ""
    print "config_data = {}".format(config_data)
    print ""

    print config_data.get("setup").get(
        "packages_choice", "n")

    _initial_setup_args = [
        "name", "author", "author_email", "version",
        "url", "long_description", "description"
    ]

    template_vars = {
        "setup": {
            x: config_data["setup"][x] for x in _initial_setup_args
            if x in config_data["setup"]
        },
        "requirements_file": None,
        "requirements_list": None,
        "find_packages": None,
        "package_list": None,
    }

    print ""
    print "template_vars = {}".format(template_vars)
    print ""

    series = Series(template_vars=template_vars)

    name = SetupQuestion(name="Name", default=os.path.relpath(".", os.pardir),
                         series=series)

    version = SetupQuestion(name="Version", default=config_data.get(
        "setup").get("version", "0.0.0"),
        series=series)

    description = Question(name="Description",
                                default="{} is a package".format(
                                    os.path.relpath(".", os.pardir)),
                                series=series)

    long_desc_file = Question(name="long_desc_file", series=series,
                              message="Great! Which file do you want to use for \
a long description?\n[README.rst]",
                              default=config_data.get("readme_file",
                                                      "README.rst"),
                              key="readme_file")

    ld_description = "Would you like to pull in a long description from a file \
    (usually a README)?"

    long_description = ChoiceQuestion(name="Long Description",
                                      series=series,
                                      choices=["y", "n"],
                                      description=ld_description,
                                      default=config_data.get(
                                          "long_description_from_file", "y"),
                                      follow_ups={"y": long_desc_file})

    license = SetupQuestion(name="License", default="MIT", series=series)

    author = SetupQuestion(name="Author",
                           default=config_data.get("setup").get(
                               "author", git_config("user", "name")),
                           series=series)

    email = SetupQuestion(name="Author Email",
                          default=config_data.get("setup").get(
                              "email", git_config("user", "email")),
                          key="author_email", series=series)

    url = SetupQuestion(name="URL",
                        default=config_data.get("setup").get(
                            "url", get_origin()),
                        series=series)

    req_find = Question(name="find_requirements",
                        series=series,
                        message="Great! Which file do you want to use to specify \
    requirements?\n[requirements.txt]",
                        default="requirements.txt",
                        key="requirements_file")

    req_list = Question(name="req_list",
                        message="Please specify a comma-delimited list \
    of requirements:\n", series=series,
                        key="requirements_list",
                        update_function=update_comma_sep_list,
                        quote_user_input=False)

    req_description = dedent("""
            Would you like to read your requirements from a [f]ile?
            Would you like to [s]pecify your requirements manually?
            Or would you like to [n]ot specify any requirements?""")

    requirements = ChoiceQuestion(name="Requirements", series=series,
                                  choices=["f", "s", "n"],
                                  description=req_description,
                                  follow_ups={"f": req_find, "s": req_list},
                                  default=config_data.get(
                                      "setup").get("requirements_choice", "n"))

    find_packages = Question(name="find_packages", series=series, default=True,
                             do_not_ask=True, key="find_packages",
                             quote_user_input=False)

    package_list = Question(name="package_list",
                            message="Please specify a comma-delimited \
list of packages in your distribution:\n", series=series,
                            key="package_list",
                            update_function=update_comma_sep_list,
                            quote_user_input=False)

    package_description = dedent("""
        Would you like to use [f]ind_packages from setuptools to find the
        packages included within your distribution?
        Would you like to [s]pecify the packages yourself?
        Or would you like to [n]ot specify any packages?""")

    packages = ChoiceQuestion(name="Packages", series=series,
                              description=package_description,
                              choices=["f", "s", "n"],
                              default=config_data.get("setup").get(
                                  "packages_choice", "n"),
                              follow_ups={"f": find_packages,
                                          "s": package_list})

    series.extend([name, version, description,
                   long_description, license, author, email, url,
                   requirements, packages])

    return series
