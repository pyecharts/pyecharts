# coding=utf-8
from __future__ import unicode_literals

from future.utils import viewitems

import os
import sys
import codecs

PY3 = sys.version_info[0] == 3

if PY3:
    string_type = str
else:
    string_type = basestring


__all__ = [
    "get_resource_dir",
    "write_utf8_html_file",
    "to_css_length",
    "merge_js_dependencies",
]


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
    with codecs.open(file_name, "w+", encoding="utf-8") as f:
        f.write(html_content)


def to_css_length(x):
    """
    Return the standard length string of css.
    It's compatible with number values in old versions.

    :param x:
    :return:
    """
    if isinstance(x, (int, float)):
        return "{}px".format(x)

    else:
        return x


def _flat(obj):
    """
    :param obj:
    :return: Return a list
    """
    if hasattr(obj, "js_dependencies"):
        return list(obj.js_dependencies)

    if isinstance(obj, (list, tuple, set)):
        return obj

    return obj,  # tuple


def merge_js_dependencies(*chart_or_name_list):
    """
    Merge multiple dependencies to a total list.
    This will ensure the order and unique in the items.

    :param chart_or_name_list:
    :return: A list containing dependency items.
    """
    front_required_items = ["echarts"]
    front_optional_items = ["echartsgl"]
    dependencies = []
    fist_items = set()

    def _add(_item):
        if _item in front_required_items:
            pass
        elif _item in front_optional_items:
            fist_items.add(_item)
        elif _item not in dependencies:
            dependencies.append(_item)

    for d in chart_or_name_list:
        for _d in _flat(d):
            _add(_d)
    fol = [x for x in front_optional_items if x in fist_items]
    return front_required_items + fol + dependencies


def _expand(dict_generator):
    return dict(list(dict_generator))


def _clean(mydict):
    for key, value in viewitems(mydict):
        if value is not None:
            if isinstance(value, dict):
                if value:
                    value = _expand(_clean(value))
                else:
                    # delete key with empty dictionary
                    continue
                if not value:
                    # detete empty dictionary after cleanning
                    continue
            elif isinstance(value, (list, tuple, set)):
                if value:
                    value = list(_clean_array(value))
                else:
                    # delete key with empty array
                    continue
            elif isinstance(value, string_type) and not value:
                # delete key with empty string
                continue
            yield (key, value)


def _clean_array(myarray):
    for value in myarray:
        if isinstance(value, dict):
            yield _expand(_clean(value))

        elif isinstance(value, (list, tuple, set)):
            yield list(_clean_array(value))

        else:
            yield value


def remove_key_with_none_value(incoming_dict):
    return _expand(_clean(incoming_dict))
