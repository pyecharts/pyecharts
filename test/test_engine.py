# coding=utf8

from __future__ import unicode_literals

from pyecharts.conf import PyEchartsConfig

from nose.tools import eq_
from mock import patch, MagicMock


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


@patch('pyecharts.engine.EchartsEnvironment')
def test_template_render(fake_creator):
    fake_render = MagicMock(
        return_value='OK'
    )
    fake_get_template = MagicMock(
        return_value=MagicMock(
            render=fake_render
        )
    )
    fake_env = MagicMock(
        get_template=fake_get_template
    )
    fake_creator.return_value = fake_env

    from pyecharts.engine import render

    test_pills = dict(canIGet='The Pills Back',
                      orCanINot='Get them back')
    render('tmp', **test_pills)
    fake_get_template.assert_called_with('tmp')
    fake_render.assert_called_with(**test_pills)
