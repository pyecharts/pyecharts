# coding=utf-8
from __future__ import unicode_literals

from pyecharts import Map
import pyecharts.echarts.events as events
from pyecharts_javascripthon.dom import alert

from test.utils import get_default_rendering_file_content


def on_click(params):
    alert(params.name)


def test_map_show_label():
    # show label
    value = [155, 10, 66, 78]
    attr = ["福建", "山东", "北京", "上海"]
    map = Map("全国地图示例", width=1200, height=600)
    map.add("", attr, value, maptype="china", is_label_show=True)
    map.on(events.MOUSE_CLICK, on_click)
    map.render()
    content = get_default_rendering_file_content()
    assert "function on_click(params) {" in content
    assert '("click", on_click);' in content
