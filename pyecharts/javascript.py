import pyecharts.constants as constants
import pyecharts.exceptions as exceptions


CUSTOM_FUNCTIONS = {}
# to escape javascript function in
# json dump
FUNCTION_LEFT_ESCAPE = '"-=>'
FUNCTION_RIGHT_ESCAPE = '<=-"'
FUNCTION_SIGNATURE = '-=>%s<=-'


def clear():
    CUSTOM_FUNCTIONS.clear()


def add_a_new_function(afunc):
    if not constants.PY35_ABOVE:
        raise exceptions.JavascriptNotSupported(constants.ERROR_MESSAGE)
    CUSTOM_FUNCTIONS[afunc.__name__] = afunc
    return FUNCTION_SIGNATURE % afunc.__name__


def unescape_js_function(options_json):
    unescaped_json = options_json.replace(FUNCTION_LEFT_ESCAPE, '')
    json_with_function_names = unescaped_json.replace(
        FUNCTION_RIGHT_ESCAPE, '')
    return json_with_function_names


def has_functions():
    return len(CUSTOM_FUNCTIONS) > 0


def compile():
    try:
        from pyecharts_javascripthon import Python2Javascript
    except ImportError:
        raise exceptions.ExtensionMissing(constants.ERROR_MESSAGE)

    content = []
    for func in CUSTOM_FUNCTIONS:
        javascript_function = Python2Javascript.translate(
            CUSTOM_FUNCTIONS[func])
        content.append(javascript_function)
    return ''.join(content)
