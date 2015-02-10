import abc
from util import get_input


class Question(object):

    __metaclass__ = abc.ABCMeta

    def __init__(self, name, template_vars):

        self.name = name
        self.message = self._get_message()
        self.template_vars = template_vars

    def _get_message(self):

        return "{}: ".format(self.name)

    def ask(self):

        user_input = get_input(self.message)
        self.process(user_input)

    @abc.abstractmethod
    def process(self, user_input):
        pass
