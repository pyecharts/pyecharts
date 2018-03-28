import sys


PY35_ABOVE = sys.version_info[0] == 3 and sys.version_info[1] > 4
CUSTOM_FUNCTIONS = {}
ERROR_MESSAGE = "You need python 3.5+ and pyecharts-javascripthon"
# to escape javascript function in
# json dump
FUNCTION_LEFT_ESCAPE = '"-=>'
FUNCTION_RIGHT_ESCAPE = '<=-"'
FUNCTION_SIGNATURE = '-=>%s<=-'


def clear():
    CUSTOM_FUNCTIONS.clear()


def add_a_new_function(afunc):
    if not PY35_ABOVE:
        raise Exception(ERROR_MESSAGE)

    CUSTOM_FUNCTIONS[afunc.__name__] = afunc
    return FUNCTION_SIGNATURE % afunc.__name__


def unescape_js_function(options_json):
    unescaped_json = options_json.replace(FUNCTION_LEFT_ESCAPE, '')
    json_with_function_names = unescaped_json.replace(
        FUNCTION_RIGHT_ESCAPE, '')
    return json_with_function_names


def isEmpty():
    return len(CUSTOM_FUNCTIONS) == 0


def compile():
    try:
        from pyecharts_javascripthon import Python2Javascript
    except ImportError:
        raise Exception(ERROR_MESSAGE)

    content = []
    for func in CUSTOM_FUNCTIONS:
        javascript_function = Python2Javascript.translate(
            CUSTOM_FUNCTIONS[func])
        content.append(javascript_function)
    return ''.join(content)
