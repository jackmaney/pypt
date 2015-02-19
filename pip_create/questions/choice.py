from question import Question
from ..util import get_input


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

        user_input = None

        while not user_input:

            user_input = get_input(self.message)

            if not user_input and self.default:
                user_input = self.default

            if user_input in self.choices and user_input in self.follow_ups:
                self.follow_ups[user_input].ask()
                break
            elif user_input in self.choices:
                break
            else:
                user_input = None

    def process(self):
        # All processing is done by follow-up questions
        pass
