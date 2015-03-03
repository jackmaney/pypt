from subprocess import call
import jinja2
import tempfile
import os
import re

EDITOR = os.getenv("EDITOR", "vim")


def process_temp_file(template_name, template_data=None):
    env = jinja2.Environment(
        loader=jinja2.PackageLoader(
            'pypt',
            'templates/temp_file'), extensions=['jinja2.ext.do'])

    template = env.get_template(template_name)

    if template_data is None:
        content = template.render()
    else:
        content = template.render(template_data)

    result = None

    with tempfile.NamedTemporaryFile(suffix=".tmp") as tmp:
        tmp.write(content)
        tmp.flush()

        call([EDITOR, tmp.name])

        with open(tmp.name) as f:
            result = f.read().splitlines()

    if result is not None:
        result = [x for x in result if x.strip() and not re.match(r"^\s*#", x)]

    return result
