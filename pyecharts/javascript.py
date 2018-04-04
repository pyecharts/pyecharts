# coding=utf-8
import json
import types
import datetime

import pyecharts.constants as constants
import pyecharts.exceptions as exceptions


CUSTOM_FUNCTIONS = {}
# to escape javascript function in
# json dump
FUNCTION_LEFT_ESCAPE = '"-=>'
FUNCTION_RIGHT_ESCAPE = '<=-"'
FUNCTION_SIGNATURE = '-=>{0}<=-'


def clear():
    CUSTOM_FUNCTIONS.clear()


def add_a_new_function(afunc):
    if not constants.PY35_ABOVE:
        raise exceptions.JavascriptNotSupported(constants.ERROR_MESSAGE)

    CUSTOM_FUNCTIONS[afunc.__name__] = afunc
    return FUNCTION_SIGNATURE.format(afunc.__name__)


def unescape_js_function(options_json):
    unescaped_json = options_json.replace(FUNCTION_LEFT_ESCAPE, '')
    json_with_function_names = unescaped_json.replace(
        FUNCTION_RIGHT_ESCAPE, ''
    )
    return json_with_function_names


def has_functions():
    return len(CUSTOM_FUNCTIONS) > 0


def translate_python_functions():
    try:
        from pyecharts_javascripthon import Python2Javascript
    except ImportError:
        raise exceptions.ExtensionMissing(constants.ERROR_MESSAGE)

    content = []
    for func in CUSTOM_FUNCTIONS:
        javascript_function = Python2Javascript.translate(
            CUSTOM_FUNCTIONS[func]
        )
        content.append(javascript_function)
    return ''.join(content)


class UnknownTypeEncoder(json.JSONEncoder):
    """
    UnknownTypeEncoder`类用于处理数据的编码，使其能够被正常的序列化
    """

    def default(self, obj):
        if isinstance(obj, (datetime.datetime, datetime.date)):
            return obj.isoformat()
        if isinstance(obj, types.FunctionType):
            return add_a_new_function(obj)
        else:
            # Pandas and Numpy lists
            try:
                return obj.astype(float).tolist()

            except Exception:
                try:
                    return obj.astype(str).tolist()

                except Exception:
                    return json.JSONEncoder.default(self, obj)


def translate_options(data, indent=0):
    """ json 序列化编码处理

    :param data: 字典数据
    :param indent: 缩进量
    """
    options_in_json = json.dumps(data, indent=indent, cls=UnknownTypeEncoder)
    if has_functions():
        options_with_js_functions = unescape_js_function(options_in_json)
        return options_with_js_functions

    else:
        return options_in_json
