# coding=utf-8
from __future__ import unicode_literals

import os
import re
import sys
import json
import codecs
import datetime

PY2 = sys.version_info[0] == 2

JS_PATTERN = re.compile(r'<!-- build -->(.*)<!-- endbuild -->',
                        re.IGNORECASE | re.MULTILINE | re.DOTALL)
JS_SRC_PATTERN = re.compile(r'src=\"(.*?)\"')


def freeze_js(html_content):
    """

    :param html_content:
    :return:
    """
    matches = JS_PATTERN.finditer(html_content)

    if not matches:
        return html_content

    for match in reversed(tuple(matches)):
        # JS file block
        src_matches = JS_SRC_PATTERN.findall(match.group(1))

        js_content = ""
        for src in src_matches:
            src = src.strip()
            src = src.split('/')
            file_path = os.path.join(
                get_resource_dir('templates'), *src)

            with codecs.open(file_path, "r", "utf-8") as f:
                js_content += f.read() + '\n'
        # Replace matched string with inline JS
        fmt = '<script type="text/javascript">{}</script>'
        js_content = fmt.format(js_content)
        html_content = (html_content[:match.start()] + js_content +
                        html_content[match.end():])

    return html_content


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
    if PY2:
        html = html_content.encode('utf-8')
        with open(file_name, "w+") as fout:
            fout.write(html)
    else:
        with open(file_name, "w+", encoding="utf-8") as fout:
            fout.write(html_content)


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
