#!/usr/bin/env python
# coding=utf-8
from __future__ import unicode_literals

import re
import os
import sys
import codecs


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


def get_resource_dir(folder):
    """

    :param folder:
    :return:
    """
    current_path = os.path.dirname(__file__)
    resource_path = os.path.join(current_path, folder)
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
