# coding=utf8
"""
Test cases for jinja2 template functions
"""

from __future__ import unicode_literals
from nose.tools import raises

from pyecharts.utils import get_resource_dir
from pyecharts import Bar, Map
from pyecharts.engine import BaseEnvironment, EchartsEnvironment
from pyecharts.conf import PyEchartsConfig

ECHARTS_ENV = EchartsEnvironment()


def create_demo_bar(chart_id_demo=None):
    attr = ["衬衫", "羊毛衫", "雪纺衫", "裤子", "高跟鞋", "袜子"]
    v1 = [5, 20, 36, 10, 75, 90]
    v2 = [10, 25, 8, 60, 20, 80]
    bar = Bar("柱状图数据堆叠示例")
    bar.add("商家A", attr, v1, is_stack=True)
    bar.add("商家B", attr, v2, is_stack=True)
    if chart_id_demo:
        bar._chart_id = chart_id_demo
    return bar


def test_echarts_js_dependencies():
    env = EchartsEnvironment(
        pyecharts_config=PyEchartsConfig(jshost='http://localhost/echarts')
    )
    tpl = env.from_string('{{ echarts_js_dependencies(bar) }}')
    bar = create_demo_bar()
    html = tpl.render(bar=bar)
    assert '<script type="text/javascript" src="http://localhost/echarts/echarts.min.js"></script>' == html  # flake8: noqa


def test_echarts_js_dependencies_embed():
    env = EchartsEnvironment(
        pyecharts_config=PyEchartsConfig(
            jshost=get_resource_dir('templates', 'js', 'echarts')
        )
    )
    tpl = env.from_string('{{ echarts_js_dependencies_embed("echarts") }}')
    bar = create_demo_bar()
    html = tpl.render(bar=bar)
    assert len(html) > 0

    # no longer echarts_js_dependencies equals echarts_js_dependencies_
    # embed when use local host.
    # because the js files is either in python path or user path
    # hence it could not be simply judged.


def test_echarts_js_container():
    tpl = ECHARTS_ENV.from_string('{{ echarts_container(bar) }}')
    bar = create_demo_bar('id_demo_chart')
    html = tpl.render(bar=bar)
    assert '<div id="id_demo_chart" style="width:800px;height:400px;"></div>' == html  # flake8: noqa

    bar.width = 1024
    bar.height = 768
    html = tpl.render(bar=bar)
    assert '<div id="id_demo_chart" style="width:1024px;height:768px;"></div>' == html  # flake8: noqa

    bar.width = '1024px'
    bar.height = '768px'
    html = tpl.render(bar=bar)
    assert '<div id="id_demo_chart" style="width:1024px;height:768px;"></div>' == html  # flake8: noqa


def test_echarts_js_content():
    tpl = ECHARTS_ENV.from_string('{{ echarts_js_content(bar) }}')
    bar = create_demo_bar()
    html = tpl.render(bar=bar)
    assert len(html) > 0


def test_echarts_js_content_wrap():
    tpl = ECHARTS_ENV.from_string('{{ echarts_js_content_wrap(bar) }}')
    bar = create_demo_bar()
    html = tpl.render(bar=bar)
    assert len(html) > 0


@raises(TypeError)
def test_create_environment_without_config():
    be = BaseEnvironment()


def test_echarts_js_in_first():
    value = [20, 190, 253, 77, 65]
    attr = ['汕头市', '汕尾市', '揭阳市', '阳江市', '肇庆市']
    map = Map("广东地图示例", width=1200, height=600)
    map.add("", attr, value, maptype='广东', is_visualmap=True,
            visual_text_color='#000')
    env = EchartsEnvironment(
        pyecharts_config=PyEchartsConfig(jshost='http://localhost/echarts')
    )
    tpl = env.from_string('{{ echarts_js_dependencies(m) }}')
    html = tpl.render(m=map)
    echarts_js_pos = html.find('echarts.min.js')
    guangdong_js_pos = html.find('guangdong.js')
    assert echarts_js_pos > -1
    assert guangdong_js_pos > -1
    assert echarts_js_pos < guangdong_js_pos
