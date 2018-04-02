import pyecharts.constants as constants
import pyecharts.exceptions as exceptions


class CallbackManager:
    def __init__(self):
        self.functions = {}

    def add_a_python_function(self, a_function):
        if not constants.PY35_ABOVE:
            raise exceptions.JavascriptNotSupported(constants.ERROR_MESSAGE)

        self.functions[a_function.__name__] = a_function
        return constants.FUNCTION_SIGNATURE.format(a_function.__name__)

    def has_functions(self):
        return len(self.functions) > 0

    def __del__(self):
        self.functions.clear()


def unescape_js_function(options_json):
    unescaped_json = options_json.replace(constants.FUNCTION_LEFT_ESCAPE, '')
    json_with_function_names = unescaped_json.replace(
        constants.FUNCTION_RIGHT_ESCAPE, ''
    )
    return json_with_function_names
