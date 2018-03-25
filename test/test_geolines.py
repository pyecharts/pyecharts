#!/usr/bin/env python
# coding=utf-8
from __future__ import unicode_literals

from nose.tools import assert_raises

from pyecharts import GeoLines, Style
from pyecharts.datasets.coordinates import search_coordinates_by_keyword

style = Style(
    title_top="#fff",
    title_pos="center",
    width=1200,
    height=600,
    background_color="#404a59"
)

style_geo = style.add(
    is_label_show=True,
    line_curve=0.2,
    line_opacity=0.6,
    legend_text_color="#eee",
    legend_pos="right",
    geo_effect_symbol="plane",
    geo_effect_symbolsize=15,
    label_color=['#a6c84c', '#ffa022', '#46bee9'],
    label_pos="right",
    label_formatter="{b}",
    label_text_color="#eee",
    legend_selectedmode="single",
)


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
    lines = GeoLines("GeoLines 示例", **style.init_style)
    lines.add("从广州出发", data_guangzhou, **style_geo)
    lines.add("从北京出发", data_beijing, **style_geo)
    lines.print_echarts_options()
    lines.render()


def test_with_full_example():
    line_data = [
        ["广州", "上海"],
        ["广州", "北京"],
        ["广州", "南京"],
        ['广州', 'A市']
    ]

    lines = GeoLines("GeoLines 示例", **style.init_style)

    with assert_raises(ValueError):
        lines.add("从广州出发", line_data, **style_geo)

    assert 0 == len(search_coordinates_by_keyword('A市'))

    lines.add_coordinate('A市', 119.3, 26.08)
    lines.add("从广州出发", line_data, **style_geo)
    lines.render()
