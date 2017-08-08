#!/usr/bin/env python
#coding=utf-8
from __future__ import unicode_literals

import os
import re
import codecs

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
            file_path = os.path.join(
                get_resource_dir('templates'), src.strip())

            with codecs.open(file_path, "r", "utf-8") as f:
                js_content += f.read() + '\n'
        # Replace matched string with inline JS
        fmt = '<script type="text/javascript">{}</script>'
        js_content = fmt.format(js_content)
        html_content = (html_content[:match.start()] + js_content +
                        html_content[match.end():])

    return html_content


_mapindex = {
    "广东": "guangdong: '//oog4yfyu0.bkt.clouddn.com/guangdong'",
}


def get_map(map_name):
    """

    :param map_name:
    :return:
    """
    _location_js = _mapindex.get(map_name, "")
    _location = ""
    try:
        _location = _location_js.split(":")[0]
    except:
        pass
    return dict(
        location_js=_location_js,
        location=_location
        )


def get_resource_dir(folder):
    """

    :param folder:
    :return:
    """
    current_path = os.path.dirname(__file__)
    resource_path = os.path.join(current_path, folder)
    return resource_path
