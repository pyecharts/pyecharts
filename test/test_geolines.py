#!/usr/bin/env python
# coding=utf-8
from __future__ import unicode_literals

from pyecharts import GeoLines

chart_init = {
    "title_color": "#fff",
    "title_pos": "center",
    "width": 1200,
    "height": 600,
    "background_color": '#404a59'
}


def test_geolines():
    data_guangzhou = [
        ["广州", "上海"],
        ["广州", "北京"],
        ["广州", "南京"],
        ["广州", "重庆"],
        ["广州", "兰州"],
        ["广州", "杭州"]
    ]
    data_beijing = [
        ["北京", "上海"],
        ["北京", "广州"],
        ["北京", "南京"],
        ["北京", "重庆"],
        ["北京", "兰州"],
        ["北京", "杭州"]
    ]
    lines = GeoLines(**chart_init)
    symbol = "path://M1705.06,1318.313v-89.254l-319.9-221.799l0.073-208." \
             "063c0.521-84.662-26.629-121.796-63.961-121.491c-37.332-0." \
             "305-64.482,36.829-63.961,121.491l0.073,208.063l-319.9,221." \
             "799v89.254l330.343-157.288l12.238,241.308l-134.449,92." \
             "931l0.531,42.034l175.125-42.917l175.125,42.917l0.531-42." \
             "034l-134.449-92.931l12.238-241.308L1705.06,1318.313z"
    lines.add("从广州出发", data_guangzhou, is_label_show=True, line_curve=0.2,
              geo_effect_symbol=symbol, geo_effect_symbolsize=15,
              label_color=['#a6c84c', '#ffa022', '#46bee9'],
              label_pos="right", line_opacity=0.6,
              label_formatter="{b}", label_text_color="#eee")
    lines.add("从北京出发", data_beijing, is_label_show=True, line_curve=0.2,
              geo_effect_symbol=symbol, geo_effect_symbolsize=15,
              label_pos="right", line_opacity=0.6, legend_selectedmode="single",
              label_formatter="{b}", label_text_color="#eee")
    lines.render()
