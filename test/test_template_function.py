# coding=utf8

from pyecharts.utils import get_resource_dir
from pyecharts import Bar
from pyecharts.engine import EchartsEnvironment, configure

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
    configure(jshost='http://localhost/echarts')
    tpl = ECHARTS_ENV.from_string('{{ echarts_js_dependencies(bar) }}')
    bar = create_demo_bar()
    html = tpl.render(bar=bar)
    assert '<script type="text/javascript" src="http://localhost/echarts/echarts.min.js"></script>' == html


def test_echarts_js_dependencies_embed():
    configure(jshost=get_resource_dir('templates', 'js', 'echarts'))
    tpl = ECHARTS_ENV.from_string('{{ echarts_js_dependencies_embed("echarts.min") }}')
    bar = create_demo_bar()
    html = tpl.render(bar=bar)
    assert len(html) > 0

    # echarts_js_dependencies equals echarts_js_dependencies_embed when use local host.
    tpl2 = ECHARTS_ENV.from_string('{{ echarts_js_dependencies("echarts.min") }}')
    html2 = tpl2.render(bar=bar)
    assert len(html2) > 0
    assert html == html2


def test_echarts_js_container():
    tpl = ECHARTS_ENV.from_string('{{ echarts_container(bar) }}')
    bar = create_demo_bar('id_demo_chart')
    html = tpl.render(bar=bar)
    assert '<div id="id_demo_chart" style="width:800px;height:400px;"></div>' == html

    bar.width = 1024
    bar.height = 768
    html = tpl.render(bar=bar)
    assert '<div id="id_demo_chart" style="width:1024px;height:768px;"></div>' == html

    bar.width = '1024px'
    bar.height = '768px'
    html = tpl.render(bar=bar)
    assert '<div id="id_demo_chart" style="width:1024px;height:768px;"></div>' == html


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
