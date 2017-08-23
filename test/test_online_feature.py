# coding=utf-8
from __future__ import unicode_literals

import pyecharts.constants as constants
from pyecharts import Bar, Page
from pyecharts.template import online
from nose.tools import eq_


DEFAULT_HOST = 'https://chfw.github.io/jupyter-echarts/echarts'


def test_online():
    old_host = constants.CONFIGURATION['HOST']
    online()
    eq_(constants.CONFIGURATION['HOST'], DEFAULT_HOST)
    constants.CONFIGURATION['HOST'] = old_host


def test_online_with_chart():
    old_host = constants.CONFIGURATION['HOST']
    online()
    attr = ["衬衫", "羊毛衫", "雪纺衫", "裤子", "高跟鞋", "袜子"]
    v1 = [5, 20, 36, 10, 75, 90]
    v2 = [10, 25, 8, 60, 20, 80]
    bar = Bar("柱状图数据堆叠示例")
    bar.add("商家A", attr, v1, is_stack=True)
    bar.add("商家B", attr, v2, is_stack=True)
    html = bar._repr_html_()
    assert DEFAULT_HOST in html
    constants.CONFIGURATION['HOST'] = old_host


def test_chart_with_custom_host():
    local_host = 'http://localhost:8000'
    attr = ["衬衫", "羊毛衫", "雪纺衫", "裤子", "高跟鞋", "袜子"]
    v1 = [5, 20, 36, 10, 75, 90]
    bar = Bar("柱状图数据堆叠示例", jshost=local_host)
    bar.add("商家A", attr, v1, is_stack=True)
    html = bar._repr_html_()
    assert local_host in html
    assert constants.CONFIGURATION['HOST'] != local_host


def test_in_event_of_overly_configured_custom_url_is_precedent():
    old_host = constants.CONFIGURATION['HOST']
    local_host = 'http://localhost:8000'
    online()
    attr = ["衬衫", "羊毛衫", "雪纺衫", "裤子", "高跟鞋", "袜子"]
    v1 = [5, 20, 36, 10, 75, 90]
    v2 = [10, 25, 8, 60, 20, 80]
    bar = Bar("柱状图数据堆叠示例", jshost=local_host)
    bar.add("商家A", attr, v1, is_stack=True)
    bar.add("商家B", attr, v2, is_stack=True)
    html = bar._repr_html_()
    assert DEFAULT_HOST not in html
    assert local_host in html
    constants.CONFIGURATION['HOST'] = old_host


def test_online_with_page():
    old_host = constants.CONFIGURATION['HOST']
    online()
    page = Page()
    attr = ["衬衫", "羊毛衫", "雪纺衫", "裤子", "高跟鞋", "袜子"]
    v1 = [5, 20, 36, 10, 75, 90]
    bar = Bar("柱状图数据堆叠示例")
    bar.add("商家A", attr, v1, is_stack=True)
    page.add(bar)

    html = page._repr_html_()
    assert DEFAULT_HOST in html
    constants.CONFIGURATION['HOST'] = old_host


def test_page_with_custom_host():
    local_host = 'http://localhost:8000'
    page = Page(jshost=local_host)
    attr = ["衬衫", "羊毛衫", "雪纺衫", "裤子", "高跟鞋", "袜子"]
    v1 = [5, 20, 36, 10, 75, 90]
    bar = Bar("柱状图数据堆叠示例")
    bar.add("商家A", attr, v1, is_stack=True)
    page.add(bar)

    html = page._repr_html_()
    assert local_host in html
    assert constants.CONFIGURATION['HOST'] != local_host
