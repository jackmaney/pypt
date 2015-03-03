from question import Question
from ..io import get_input


class ChoiceQuestion(Question):

    def __init__(self, name, template_vars, description,
                 choices, follow_ups, default=None, message=None):
        self.description = description

        if not choices:
            raise ValueError("choices parameter must be a list of strings")

        if default and default not in choices:
            raise ValueError(
                "default ({}) not found in the list of choices ({})".format(
                    default, ",".join(choices)
                ))

        for choice in choices:
            if choice != default and choice not in follow_ups:
                raise ValueError(
                    "Non-default choice {} needs a follow-up question".format(
                        default
                    ))
        self.choices = choices
        self.default = default
        self.follow_ups = follow_ups

        super(ChoiceQuestion, self).__init__(name, template_vars, message)

    def _get_message(self):

        choice_str = "[{}]".format(",".join(self.choices))

        if self.default:
            choice_str += "({}): ".format(self.default)
        else:
            choice_str += ": "

        return "{}:\n{}\n{}".format(self.name, self.description, choice_str)

    def ask(self):

        while not self.user_input:

            self.user_input = get_input(self.message)

            if not self.user_input and self.default:
                self.user_input = self.default

            if self.user_input in self.choices and \
                    self.user_input in self.follow_ups:

                self.follow_ups[self.user_input].ask()
                break
            elif self.user_input in self.choices:
                break
            else:
                self.user_input = None

    def process(self):
        # The only way this should be called directly is to bypass
        # asking the follow-up questions and just process the default
        # follow-up.

        if self.default in self.follow_ups:
            self.follow_ups[self.default].process()
