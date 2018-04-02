import pyecharts.constants as constants
import pyecharts.exceptions as exceptions


class CallbackManager:

    def __init__(self):
        self.functions = {}

    def add(self, a_function):
        if not constants.PY35_ABOVE:
            raise exceptions.JavascriptNotSupported(constants.ERROR_MESSAGE)

        self.functions[a_function.__name__] = a_function
        return constants.FUNCTION_SIGNATURE.format(a_function.__name__)

    def contains(self, a_function):
        return a_function.__name__ in self.functions

    def has_functions(self):
        return len(self.functions) > 0

    def clear(self):
        self.functions.clear()

    def __repr__(self):
        if not self.has_functions():
            return ''

        try:
            from pyecharts_javascripthon import Python2Javascript
        except ImportError:
            raise exceptions.ExtensionMissing(constants.ERROR_MESSAGE)

        content = []
        for func in self.functions:
            javascript_function = Python2Javascript.translate(
                self.functions[func]
            )
            content.append(javascript_function)
        return ''.join(content)


def unescape_js_function(options_json):
    unescaped_json = options_json.replace(constants.FUNCTION_LEFT_ESCAPE, '')
    json_with_function_names = unescaped_json.replace(
        constants.FUNCTION_RIGHT_ESCAPE, ''
    )
    return json_with_function_names


GLOBAL_CALLBACKS = CallbackManager()
