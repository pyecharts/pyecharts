# coding=utf-8
from __future__ import unicode_literals

import os
import codecs

from nose.tools import eq_

from pyecharts.utils import (
    write_utf8_html_file,
    get_resource_dir,
    merge_js_dependencies,
)
from pyecharts.utils import remove_key_with_none_value


def test_get_resource_dir():
    path = get_resource_dir("templates")
    expected = os.path.join(os.getcwd(), "..", "pyecharts", "templates")
    eq_(path, os.path.abspath(expected))


def test_write_utf8_html_file():
    content = "柱状图数据堆叠示例"
    file_name = "test.html"
    write_utf8_html_file(file_name, content)
    with codecs.open(file_name, "r", "utf-8") as f:
        actual_content = f.read()
        eq_(content, actual_content)


class MockChart(object):
    """
    A mock class for a Chart and Page
    """

    def __init__(self, js_dependencies):
        self.js_dependencies = js_dependencies


def test_merge_js_dependencies_with_one_chart():
    # Prepare some kinds of charts or page.

    base_chart = MockChart(["echarts"])

    # One chart or page
    eq_(["echarts"], merge_js_dependencies(base_chart))
    # A map chart
    ch1 = MockChart(["echarts", "fujian", "zhengjiang", "anhui"])
    eq_(
        ["echarts", "fujian", "zhengjiang", "anhui"],
        merge_js_dependencies(ch1),
    )


def test_merge_js_dependencies_with_multiple_charts():
    base_chart = MockChart(["echarts"])
    map_chart = MockChart(["echarts", "fujian"])
    three_d_chart = MockChart(["echarts", "echartsgl"])
    # Multiple charts
    eq_(["echarts", "fujian"], merge_js_dependencies(base_chart, map_chart))
    eq_(
        ["echarts", "echartsgl", "fujian"],
        merge_js_dependencies(base_chart, map_chart, three_d_chart),
    )


def test_merge_js_dependencies_with_mixed_chart_and_string():
    map_chart = MockChart(["echarts", "fujian"])

    eq_(["echarts", "zhejiang"], merge_js_dependencies("echarts", "zhejiang"))
    eq_(
        ["echarts", "zhejiang"], merge_js_dependencies(["echarts", "zhejiang"])
    )
    eq_(["echarts", "fujian"], merge_js_dependencies("echarts", map_chart))


class MockPoint(object):
    def __init__(self, x, y):
        self.x = x
        self.y = y


def test_remove_key_with_none_value():
    fixture = {
        "a": 1,
        "b": None,
        "nested": {"ac": 1, "bc": None, "nested": {"a": 1, "b": None}},
        "array": [
            1,
            {"nested": {"ac": 1, "bc": None, "nested": {"a": 1, "b": None}}},
            {"normal": 1, "empty_string": ""},
        ],
    }
    actual_result = remove_key_with_none_value(fixture)
    expected = {
        "a": 1,
        "array": [1, {"nested": {"ac": 1, "nested": {"a": 1}}}, {"normal": 1}],
        "nested": {"ac": 1, "nested": {"a": 1}},
    }
    eq_(actual_result, expected)
