# coding=utf-8

import os

from pyecharts.datasets import FILENAMES


class OrderedSet:
    def __init__(self, *args):
        self._values = dict()
        self.items = []
        for a in args:
            self.add(a)

    def add(self, item):
        if not self._values.get(item, False):
            self._values.update({item: True})
            self.items.append(item)


def filter_js_func(fn: str) -> str:
    return "__-o-__{}__-o-__".format(fn)


def produce_require_dict(js_dependencies, js_host) -> dict:
    confs, libraries = [], []
    for name in js_dependencies.items:
        confs.append("'{}':'{}/{}'".format(name, js_host, FILENAMES[name]))
        libraries = ["'{}'".format(name)]
    return dict(config_items=confs, libraries=libraries)


def get_resource_dir(*paths):
    """
    Return absolute path for a directory or file inside the project.
    :param paths: paths relative to project root dir.
    :return:
    """
    project_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
    resource_path = os.path.join(project_dir, *paths)
    return resource_path


def write_utf8_html_file(file_name, html_content):
    """

    :param file_name:
    :param html_content:
    :return:
    """
    with open(file_name, "w+", encoding="utf-8") as html_file:
        html_file.write(html_content)


def _flat(obj):
    if hasattr(obj, "js_dependencies"):
        return list(obj.js_dependencies)

    if isinstance(obj, (list, tuple, set)):
        return obj

    return (obj,)  # tuple


def _expand(dict_generator):
    return dict(list(dict_generator))


def _clean_dict(mydict):
    for key, value in mydict.items():
        if value is not None:
            if isinstance(value, dict):
                value = _expand(_clean_dict(value))

            elif isinstance(value, (list, tuple, set)):
                value = list(_clean_array(value))

            elif isinstance(value, str) and not value:
                # delete key with empty string
                continue

            yield (key, value)


def _clean_array(myarray):
    for value in myarray:
        if isinstance(value, dict):
            yield _expand(_clean_dict(value))

        elif isinstance(value, (list, tuple, set)):
            yield list(_clean_array(value))

        else:
            yield value


def remove_key_with_none_value(incoming_dict):
    return _expand(_clean_dict(incoming_dict))


def is_ascii(s):
    return all(ord(c) < 128 for c in s)
