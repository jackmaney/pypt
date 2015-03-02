import ast

from warnings import warn


class SetupKwargsVisitor(ast.NodeVisitor):

    def visit_Call(self, node):

        if isinstance(node.func, ast.Name) and node.func.id == "setup":
            return {kw.arg: kw.value for kw in node.keywords}


def get_setup_kwargs(setup_file="setup.py"):
    try:
        with open(setup_file) as f:
            setup_text = f.read()
    except IOError:
        warn("Could not open file '{}'".format(setup_file))

        return None

    return SetupKwargsVisitor().visit(ast.parse(setup_text))
