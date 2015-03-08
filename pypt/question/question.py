from ..io import get_input


class Question(object):

    def __init__(self, name, series=None, message=None, default=None, key=None,
                 update_function=None, do_not_ask=False,
                 quote_user_input=True):

        self.name = name
        self._series = series
        if series is not None:
            self.series = series

        self.user_input = None
        self.default = default

        if message is not None:
            self.message = message
        else:
            self.message = self._get_message()

        self.key = key
        self.update_function = update_function
        self.do_not_ask = do_not_ask
        self.quote_user_input = quote_user_input

    def _get_message(self):

        if self.default:
            return "{} ({}): ".format(self.name, self.default)
        else:
            return "{}: ".format(self.name)

    @property
    def series(self):
        return self._series

    @series.setter
    def series(self, s):
        if s and self not in s and self.name not in [x.name for x in s]:
            s.append(self)
        self._series = s

    def ask(self):

        if not self.do_not_ask and self.message:
            self.user_input = get_input(self.message)

        self.process()

    def process(self):

        if not self.user_input and self.default:
            self.user_input = self.default

        if self.user_input and self.series and \
                self.key and self.series.template_vars:
            if self.quote_user_input:
                self.user_input = '"{}"'.format(self.user_input)

            if hasattr(self.update_function, "__call__"):
                self.update_function(self)
            else:
                value = self.series.template_vars.get(self.key)

                if isinstance(value, list):
                    value.append(self.user_input)
                    self.series.template_vars[self.key] = value
                else:
                    self.series.template_vars[self.key] = self.user_input
