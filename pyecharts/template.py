#!/usr/bin/env python
#coding=utf-8
from __future__ import unicode_literals

import os
import re
import sys
import codecs
from jinja2 import Environment, FileSystemLoader

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
    "安徽": "anhui: '//oog4yfyu0.bkt.clouddn.com/anhui'",
    "澳门": "aomen: '//oog4yfyu0.bkt.clouddn.com/aomen'",
    "北京": "beijing: '//oog4yfyu0.bkt.clouddn.com/beijing'",
    "重庆": "chongqing: '//oog4yfyu0.bkt.clouddn.com/chongqing'",
    "福建": "fujian: '//oog4yfyu0.bkt.clouddn.com/fujian'",
    "甘肃": "gansu: '//oog4yfyu0.bkt.clouddn.com/gansu'",
    "广西": "guangxi: '//oog4yfyu0.bkt.clouddn.com/guangxi'",
    "贵州": "guizhou: '//oog4yfyu0.bkt.clouddn.com/guizhou'",
    "海南": "hainan: '//oog4yfyu0.bkt.clouddn.com/hainan'",
    "河北": "hebei: '//oog4yfyu0.bkt.clouddn.com/hebei'",
    "黑龙江": "heilongjiang: '//oog4yfyu0.bkt.clouddn.com/heilongjiang'",
    "河南": "henan: '//oog4yfyu0.bkt.clouddn.com/henan'",
    "湖北": "hubei: '//oog4yfyu0.bkt.clouddn.com/hubei'",
    "湖南": "hunan: '//oog4yfyu0.bkt.clouddn.com/hunan'",
    "江苏": "jiangsu: '//oog4yfyu0.bkt.clouddn.com/jiangsu'",
    "江西": "jiangxi: '//oog4yfyu0.bkt.clouddn.com/jiangxi'",
    "吉林": "jilin: '//oog4yfyu0.bkt.clouddn.com/jilin'",
    "辽宁": "liaoning: '//oog4yfyu0.bkt.clouddn.com/liaoning'",
    "内蒙古": "neimenggu: '//oog4yfyu0.bkt.clouddn.com/neimenggu'",
    "宁夏": "ningxia: '//oog4yfyu0.bkt.clouddn.com/ningxia'",
    "青海": "qinghai: '//oog4yfyu0.bkt.clouddn.com/qinghai'",
    "山东": "shandong: '//oog4yfyu0.bkt.clouddn.com/shandong'",
    "上海": "shanghai: '//oog4yfyu0.bkt.clouddn.com/shanghai'",
    "山西": "shanxi: '//oog4yfyu0.bkt.clouddn.com/shanxi'",
    "四川": "sichuan: '//oog4yfyu0.bkt.clouddn.com/sichuan'",
    "台湾": "taiwan: '//oog4yfyu0.bkt.clouddn.com/taiwan'",
    "天津": "tianjin: '//oog4yfyu0.bkt.clouddn.com/tianjin'",
    "香港": "xianggang: '//oog4yfyu0.bkt.clouddn.com/xianggang'",
    "新疆": "xinjiang: '//oog4yfyu0.bkt.clouddn.com/xinjiang'",
    "西藏": "xizang: '//oog4yfyu0.bkt.clouddn.com/xizang'",
    "云南": "yunnan: '//oog4yfyu0.bkt.clouddn.com/yunnan'",
    "浙江": "zhejiang: '//oog4yfyu0.bkt.clouddn.com/zhejiang'"
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


# Single Singleton Instance for jinja2
JINJA2_ENV = Environment(
    loader=FileSystemLoader(get_resource_dir('templates')),
    keep_trailing_newline=True,
    trim_blocks=True,
    lstrip_blocks=True)


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
