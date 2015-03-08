from .file import local_config_file, global_config_file
from .reader import from_file
from .. import get_template, git_utils, __version__

import os
from copy import deepcopy
import collections


# http://stackoverflow.com/a/18394648/554546
def _update(orig_dict, new_dict):

    for key, val in new_dict.iteritems():
        if isinstance(val, collections.Mapping):
            _update(orig_dict.get(key, {}), val)
        elif isinstance(val, list):
            orig_dict[key] = (orig_dict[key] + val)
        else:
            orig_dict[key] = new_dict[key]


def write_default_config(global_config=True):

    if global_config:
        config_file = global_config_file
    else:
        config_file = local_config_file

    author = git_utils.git_config("user", "name")
    email = git_utils.git_config("user", "email")

    template_vars = {
        "pypt_version": __version__,
        "init": {
            "setup": {
                "author": author,
                "author_email": email,
                "version": "0.0.0"
            }
        }
    }

    if not global_config:
        origin = git_utils.get_origin()

        if origin is not None:
            template_vars["init"]["setup"]["url"] = origin

    template = get_template("config")

    template_text = template.render(
        {k: v for k, v in template_vars.items() if v is not None})

    with open(config_file, "w") as f:
        f.write(template_text)


def write_config(config_data, global_config=True):

    if global_config:
        config_file = global_config_file
    else:
        config_file = local_config_file

    if not os.path.exists(config_file):
        write_default_config(global_config=global_config)

    old_config_data = from_file(config_file)

    new_config_data = deepcopy(config_data)
    _update(old_config_data, new_config_data)

    template = get_template("config")

    template_text = template.render(old_config_data)

    with open(config_file, "w") as f:
        f.write(template_text)
