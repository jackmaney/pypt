import os
import jinja2

base_dir = os.path.abspath(os.path.realpath(os.path.dirname(__file__)))

template_dirs = [
    x for x in os.listdir(base_dir)
    if os.path.isdir(os.path.join(base_dir, x))
    and all([
        os.path.isfile(os.path.join(base_dir, x, y))
        and y.endswith(".j2")
        for y in os.listdir(os.path.join(base_dir, x))
    ])
]


def get_template(template_type, template_name="base.j2", extensions=None):
    if template_type not in template_dirs:
        raise ValueError(
            "No templates of type '{}' found (in {})".format(
                template_type, base_dir))

    loader_dir = os.path.join(base_dir, template_type)

    if extensions is None:
        extensions = []

    env = jinja2.Environment(
        loader=jinja2.FileSystemLoader(loader_dir),
        extensions=extensions)

    return env.get_template(template_name)
