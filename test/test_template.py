#!/usr/bin/env python
# coding=utf-8
from __future__ import unicode_literals
import codecs


from nose.tools import eq_, raises
from pyecharts.template import (
    freeze_js,
    write_utf8_html_file,
    ensure_echarts_is_in_the_front)


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


def test_echarts_postion_in_dependency_list():
    test_sequence = set(['guangdong', 'shanghai', 'echarts'])
    result = ensure_echarts_is_in_the_front(test_sequence)
    eq_(result[0], 'echarts')


def test_echarts_postion_with_one_element_set():
    test_sequence = set(['echarts'])
    result = ensure_echarts_is_in_the_front(test_sequence)
    eq_(result[0], 'echarts')


@raises(Exception)
def test_echarts_postion_with_nothing():
    test_sequence = set()
    ensure_echarts_is_in_the_front(test_sequence)
