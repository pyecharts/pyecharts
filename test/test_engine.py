# coding=utf8

from __future__ import unicode_literals

from pyecharts.conf import PyEchartsConfig

from nose.tools import eq_


def test_merge_js_dependencies():
    # PyEchartsConfig.merge_js_dependencies(str1, str2,...)
    eq_(['echarts', 'fujian'],
        PyEchartsConfig.merge_js_dependencies('echarts', 'fujian'))

    # PyEchartsConfig.merge_js_dependencies(chart)
    class MockChart(object):
        def __init__(self, js_dependencies):
            self.js_dependencies = js_dependencies

    ch1 = MockChart(['echarts', 'fujian', 'zhengjiang', 'anhui'])
    eq_(
        ['echarts', 'fujian', 'zhengjiang', 'anhui'],
        PyEchartsConfig.merge_js_dependencies(ch1)
    )

    # PyEchartsConfig.merge_js_dependencies(chart1, chart2 )
    ch1 = MockChart(['echarts'])
    ch2 = MockChart(['echarts', 'beijing'])
    eq_(
        ['echarts', 'beijing'],
        PyEchartsConfig.merge_js_dependencies(ch1, ch2)
    )

    # PyEchartsConfig.merge_js_dependencies(*chart_list)

    mock_page = [ch1, ch2]
    ch1 = MockChart(['echarts'])
    ch2 = MockChart(['echarts', 'beijing'])
    eq_(
        ['echarts', 'beijing'],
        PyEchartsConfig.merge_js_dependencies(*mock_page)
    )
