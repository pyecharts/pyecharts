# coding=utf-8
from __future__ import unicode_literals

import codecs
import datetime
import os
import json


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


class UnknownTypeEncoder(json.JSONEncoder):
    """
    UnknownTypeEncoder`类用于处理数据的编码，使其能够被正常的序列化
    """

    def default(self, obj):
        if isinstance(obj, (datetime.datetime, datetime.date)):
            return obj.isoformat()
        else:
            # Pandas and Numpy lists
            try:
                return obj.astype(float).tolist()
            except Exception:
                try:
                    return obj.astype(str).tolist()
                except Exception:
                    return json.JSONEncoder.default(self, obj)


def json_dumps(data, indent=0):
    """ json 序列化编码处理

    :param data: 字典数据
    :param indent: 缩进量
    """
    return json.dumps(data, indent=indent, cls=UnknownTypeEncoder)


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
