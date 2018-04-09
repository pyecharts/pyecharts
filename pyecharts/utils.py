# coding=utf-8
from __future__ import unicode_literals

import codecs
import os
import operator
import sys

PY2 = sys.version_info[0] == 2


def get_resource_dir(*paths):
    """

    :param path:
    :return:
    """
    current_path = os.path.dirname(__file__)
    resource_path = os.path.join(current_path, *paths)
    return resource_path


def write_utf8_html_file(file_name, html_content):
    """

    :param file_name:
    :param html_content:
    :return:
    """
    with codecs.open(file_name, 'w+', encoding='utf-8') as f:
        f.write(html_content)


def to_css_length(x):
    """
    Return the standard length string of css.
    It's compatible with number values in old versions.

    :param x:
    :return:
    """
    if isinstance(x, (int, float)):
        return '{}px'.format(x)

    else:
        return x


def merge_js_dependencies(*chart_or_name_list):
    """
    Merge multiple dependencies to a total list.
    This will ensure the order and unique in the items.

    :param chart_or_name_list:
    :return: A list containing dependency items.
    """
    front_must_items = ['echarts']  # items which must be included.
    front_optional_items = ['echartsgl']
    dependencies = []
    fist_items = set()

    def _add(_items):
        if _items in front_must_items:
            pass
        elif _items in front_optional_items:
            fist_items.add(_items)
        elif _items not in dependencies:
            dependencies.append(_items)

    for d in chart_or_name_list:
        if hasattr(d, 'js_dependencies'):
            for x in d.js_dependencies:
                _add(x)
        elif isinstance(d, (list, tuple, set)):
            for x in d:
                _add(x)
        else:
            _add(d)
    # items which should be included in front part.
    fol = [x for x in front_optional_items if x in fist_items]
    return front_must_items + fol + dependencies


# ------- Lazy Module ------#

def proxy_method(func):
    def inner(self, *args):
        if self._wrapped is None:
            self._setup()
        return func(self._wrapped, *args)

    return inner


class LazyObject(object):
    _wrapped = None

    def __init__(self, func):
        self.__dict__['_setupfunc'] = func

    __getattr__ = proxy_method(getattr)

    def __setattr__(self, key, value):
        if key == '_wrapped':
            self.__dict__['_wrapped'] = value
        else:
            if self._wrapped is None:
                self._setup()
            setattr(self._wrapped, key, value)

    def _setup(self):
        self._wrapped = self._setupfunc()

    __getitem__ = proxy_method(operator.getitem)

    if PY2:
        __str__ = proxy_method(str)
        __unicode__ = proxy_method(unicode)  # NOQA: unicode undefined on PY3
        __nonzero__ = proxy_method(bool)
    else:
        __bytes__ = proxy_method(bytes)
        __str__ = proxy_method(str)
        __bool__ = proxy_method(bool)
