import ast


class SetupParser(object):

    def __init__(self, setup_file="setup.py"):
        self.setup_file = setup_file

        with open(setup_file) as f:
            self.setup_text = f.read()

        self.setup_parsed = ast.parse(self.setup_text)

        self.raw_setup_args = None

        self.pretty_setup_args = None

        self.variables = None

    def get_setup_args(self):

        for node in ast.walk(self.setup_parsed):

            ast.dump(node)

            if isinstance(node, ast.Call) and \
                    isinstance(node.func, ast.Name) and \
                    node.func.id == "setup":

                self.raw_setup_args = {
                    kw.arg: kw.value for kw in node.keywords
                }

                self.pretty_setup_args = {
                    x: get_literal(self.raw_setup_args.get(x))
                    for x in self.raw_setup_args
                }


def get_literal(node):
    """
    A simple helper function for grabbing certain literals (numbers, strings,
    variable names, lists, and dicts) from ``ast.Node`` objects.

    Mostly used for pretty printing and debugging.
    """
    result = node

    if isinstance(node, ast.Str):
        result = "{}".format(node.s)

    elif isinstance(node, ast.Num):

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

    elif isinstance(node, ast.Call):

        arg_list = [get_literal(x) for x in node.args]
        arg_list += ["{}={}".format(kw.arg, get_literal(kw.value))
                     for kw in node.keywords
                     ]
        if node.starargs:
            arg_list.append("*{}".format(node.starargs.id))
        if node.kwargs:
            arg_list.append("**{}".format(node.kwargs.id))

        result = "{}({})".format(node.func.id, ",".join(arg_list))

    return result
