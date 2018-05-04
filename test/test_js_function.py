#!/usr/bin/env python
# coding=utf-8
from __future__ import unicode_literals

from pyecharts import Geo, Style


def geo_formatter(params):
    return params.name + " : " + params.value[2]


def test_geo_formatter_func():
    style = Style(
        title_color="#fff",
        title_pos="center",
        width=1200,
        height=600,
        background_color="#404a59",
    )
    data = [("汕头市", 50), ("汕尾市", 60), ("揭阳市", 35), ("阳江市", 44), ("肇庆市", 72)]
    geo = Geo("广东城市空气质量", "data from pm2.5", **style.init_style)
    attr, value = geo.cast(data)
    geo.add(
        "",
        attr,
        value,
        maptype="广东",
        type="effectScatter",
        tooltip_formatter=geo_formatter,
        is_random=True,
        effect_scale=5,
        is_legend_show=False,
    )
    assert "function geo_formatter(" in geo._repr_html_()
