from ..question import Question


class Series(list):

    def __init__(self, question_list=None, template_vars=None):

        if question_list is None:
            question_list = []

        if not all([isinstance(x, Question) for x in question_list]):
            raise ValueError("question_list must be a list of Questions!")

        names = [x.name for x in question_list]

        if len(set(names)) != len(question_list):
            raise ValueError("Questions must have distinct names!")

        self.template_vars = template_vars

        super(list, self).__init__(question_list)

    def ask(self):

        for q in self:
            q.ask()

    def process(self):

        for q in self:
            q.process()

    def get_question_by_name(self, name):

        if name not in [x.names for x in self]:
            return None
        else:
            return [x for x in self if x.names == name][0]


import init
