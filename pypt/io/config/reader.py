from .file import global_config_file, local_config_file
from .. import get_template

import commentjson
import os


def read_config():

    result = None

    if os.path.exists(local_config_file) and os.path.isfile(local_config_file):
        result = from_file(local_config_file)
    elif os.path.exists(global_config_file) and \
            os.path.isfile(global_config_file):
        result = from_file(global_config_file)

    return result


def from_string(string):

    return commentjson.loads(string)


def from_file(file_name=global_config_file):

    with open(file_name) as f:
        result = f.read()

    return from_string(result)


def from_template(template_type, template_vars=None,
                  template_name="base.j2", extensions=None):

    template = get_template(template_type, template_name=template_name,
                            extensions=extensions)

    if template_vars is None:
        template_text = template.render()
    else:
        template_text = template.render(template_vars)

    return from_string(template_text)
