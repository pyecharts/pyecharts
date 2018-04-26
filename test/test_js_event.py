#!/usr/bin/env python
# coding=utf-8
from __future__ import unicode_literals

import pyecharts.echarts.events as events
from pyecharts import Bar
from pyecharts_javascripthon.dom import alert


def on_click():
    alert("点击事件触发")


def test_mouse_click():
    bar = Bar("我的第一个图表", "这里是副标题")
    bar.add(
        "服装", ["衬衫", "羊毛衫", "雪纺衫", "裤子", "高跟鞋", "袜子"], [5, 20, 36, 10, 75, 90]
    )
    bar.on(events.MOUSE_CLICK, on_click)
    assert "function on_click(" in bar._repr_html_()
