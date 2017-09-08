# coding=utf-8
from __future__ import unicode_literals

import os
import codecs


from nose.tools import eq_
from pyecharts.utils import (
    freeze_js,
    write_utf8_html_file,
    get_resource_dir
)


def test_get_resource_dir():
    path = get_resource_dir('templates')
    expected = os.path.join(os.getcwd(), '..', 'pyecharts', 'templates')
    eq_(path, os.path.abspath(expected))


def test_freeze_js():
    html_content = """
        </style>
        <!-- build -->
        <script src="js/echarts/echarts.min.js"></script>
        <script src="js/echarts/echarts-wordcloud.min.js"></script>
        <!-- endbuild -->
    </head><body>"""

    html_content = freeze_js(html_content)
    assert 'exports.echarts' in html_content
    assert 'echarts-wordcloud' in html_content


def test_write_utf8_html_file():
    content = "柱状图数据堆叠示例"
    file_name = 'test.html'
    write_utf8_html_file(file_name, content)
    with codecs.open(file_name, 'r', 'utf-8') as f:
        actual_content = f.read()
        eq_(content, actual_content)
