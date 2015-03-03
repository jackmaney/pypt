from question import Question

import re
import six


class SetupQuestion(Question):

    def __init__(self, name, template_vars,
                 default=None, key_name=None, message=None):
        self.default = default
        if key_name:
            self.key_name = key_name
        else:
            self.key_name = name.lower()

        super(SetupQuestion, self).__init__(name, template_vars, message)

    def _get_message(self):

        if self.default:
            return "{} ({}): ".format(self.name, self.default)
        else:
            return super(SetupQuestion, self)._get_message()

    def process(self):

        if "setup_kwargs" not in self.template_vars:
            self.template_vars["setup_kwargs"] = {}

        if not self.user_input and self.default:
            self.user_input = self.default

        if self.user_input:
            self.template_vars["setup_kwargs"][
                self.key_name] = "'{}'".format(self.user_input)


class VariableQuestion(SetupQuestion):

    def __init__(self, name, template_vars, variable_name,
                 default=None, key_name=None, message=None):

        self.variable_name = variable_name
        super(VariableQuestion, self).__init__(name, template_vars,
                                               default=default,
                                               key_name=key_name,
                                               message=message)

    def process(self):

        if not self.user_input and self.default:
            self.user_input = self.default

        if self.user_input:

            if isinstance(self.user_input, six.string_types):
                self.template_vars[self.variable_name] = "'{}'".format(
                    self.user_input)
            else:
                self.template_vars[self.variable_name] = self.user_input


class ListVariableQuestion(VariableQuestion):

    def process(self):

        if not self.user_input and self.default:
            self.user_input = self.default

        if self.user_input:
            result = "[{}]".format(",".join([
                "'{}'".format(x.strip()) for x in
                re.split("\s*,\s*", self.user_input) if x]))
            result = re.sub("\s+", "", result)
            self.template_vars[self.variable_name] = result
