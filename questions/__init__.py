from default import SetupQuestion, VariableQuestion, ListVariableQuestion
from choice import ChoiceQuestion
from util import get_username, get_email
from textwrap import dedent
import os

__all__ = ["template_vars", "question_list"]

template_vars = {
    "setup_kwargs": {},
    "requirements_file": None,
    "requirements_list": None,
    "find_packages": None,
    "packages_list": None,
}

name = SetupQuestion(name="Name", default=os.path.relpath(".", os.pardir),
                     template_vars=template_vars)

version = SetupQuestion(name="Version", default="0.0.0",
                        template_vars=template_vars)

description = SetupQuestion(name="Description",
                            default="{} is a package".format(
                                os.path.relpath(".", os.pardir)),
                            template_vars=template_vars)

long_desc_file = VariableQuestion(name="long_desc_file",
                                  template_vars=template_vars,
                                  message="Great! Which file?\n[README.rst]",
                                  default="README.rst",
                                  variable_name="readme_file")

ld_description = "Would you like to pull in a long description from a file \
(usually a README)?"

long_description = ChoiceQuestion(name="Long Description",
                                  template_vars=template_vars,
                                  choices=["y", "n"],
                                  description=ld_description,
                                  default="n",
                                  follow_ups={"y": long_desc_file})

license = SetupQuestion(name="License", default="MIT",
                        template_vars=template_vars)

author = SetupQuestion(name="Author", default=get_username(),
                       template_vars=template_vars)

email = SetupQuestion(name="Author Email", default=get_email(),
                      key_name="author_email", template_vars=template_vars)

req_find = VariableQuestion(name="find_requirements",
                            template_vars=template_vars,
                            default="requirements.txt",
                            message="Great! Which file?\n[requirements.txt]",
                            variable_name="requirements_file")

req_list = ListVariableQuestion(name="req_list",
                                message="Please specify a comma-delimited list \
of requirements:\n", template_vars=template_vars,
                                variable_name="requirements_list")

req_description = dedent("""
        Would you like to read your requirements from a [f]ile?
        Would you like to [s]pecify your requirements manually?
        Or would you like to [n]ot specify any requirements?""")


requirements = ChoiceQuestion(name="Requirements", template_vars=template_vars,
                              choices=["f", "s", "n"],
                              description=req_description,
                              follow_ups={"f": req_find, "s": req_list},
                              default="n")


find_packages = VariableQuestion(name="find_packages", message="",
                                 template_vars=template_vars,
                                 default=True,
                                 variable_name="find_packages")

package_list = ListVariableQuestion(name="package_list",
                                    message="Please specify a comma-delimited \
list of packages in your distribution:\n", template_vars=template_vars,
                                    variable_name="packages_list")

package_description = dedent("""
    Would you like to use [f]ind_packages from setuptools to find the packages
    included within your distribution?
    Would you like to [s]pecify the packages yourself?
    Or would you like to [n]ot specify any packages?""")

packages = ChoiceQuestion(name="Packages", template_vars=template_vars,
                          description=package_description,
                          choices=["f", "s", "n"], default="n",
                          follow_ups={"f": find_packages, "s": package_list})

question_list = [name, version, description,
                 long_description, license, author, email,
                 requirements, packages]
