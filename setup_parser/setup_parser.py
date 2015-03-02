import ast

from warnings import warn


def get_literal(node):
    """
    A simple helper function for grabbing certain literals (numbers, strings,
    variable names, lists, and dicts) from ``ast.Node`` objects.

    Mostly used for pretty printing and debugging.
    """
    result = None

    if isinstance(node, ast.Str):
        result = "'{}'".format(node.s)
    elif isinstance(node, node.Num):
        result = node.n
    elif isinstance(node, ast.Name):
        result = node.id
    elif isinstance(node, ast.List):
        result = [get_literal(x) for x in node.elts]
    elif isinstance(node, ast.Dict):
        result = {
                  get_literal(k): get_literal(v)
                  for k, v in zip(node.keys, node.values)
                 }

    return result


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
