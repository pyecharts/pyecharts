#!/usr/bin/env python
# coding=utf-8
from __future__ import unicode_literals

import math
import random
from test.constants import WEEK, X_TIME

from pyecharts import Polar


def test_polar_type_scatter_one():
    data = [(i, random.randint(1, 100)) for i in range(101)]
    polar = Polar("极坐标系-散点图示例")
    polar.add(
        "",
        data,
        boundary_gap=False,
        type="scatter",
        is_splitline_show=False,
        is_axisline_show=True,
    )
    assert '"type": "scatter"' in polar._repr_html_()


def test_polar_type_effectscatter():
    data = [(i, random.randint(1, 100)) for i in range(10)]
    polar = Polar("极坐标系-动态散点图示例", width=1200, height=600)
    polar.add("", data, type="effectScatter", effect_scale=10, effect_period=5)
    assert '"type": "effectScatter"' in polar._repr_html_()


def test_polar_type_barradius():
    polar = Polar("极坐标系-堆叠柱状图示例", width=1200, height=600)
    polar.add(
        "A", [1, 2, 3, 4, 3, 5, 1], radius_data=WEEK, type="barRadius", is_stack=True
    )
    polar.add(
        "B", [2, 4, 6, 1, 2, 3, 1], radius_data=WEEK, type="barRadius", is_stack=True
    )
    polar.add(
        "C", [1, 2, 3, 4, 1, 2, 5], radius_data=WEEK, type="barRadius", is_stack=True
    )
    polar.render()


def test_polar_type_barangle():
    polar = Polar("极坐标系-堆叠柱状图示例", width=1200, height=600)
    polar.add(
        "", [1, 2, 3, 4, 3, 5, 1], angle_data=WEEK, type="barAngle", is_stack=True
    )
    polar.add(
        "", [2, 4, 6, 1, 2, 3, 1], anglle_data=WEEK, type="barAngle", is_stack=True
    )
    polar.add(
        "", [1, 2, 3, 4, 1, 2, 5], angle_data=WEEK, type="barAngle", is_stack=True
    )
    polar.render()


def test_polar_draw_love():
    data = []
    for i in range(101):
        theta = i / 100 * 360
        r = 5 * (1 + math.sin(theta / 180 * math.pi))
        data.append([r, theta])
    hour = [i for i in range(1, 25)]
    polar = Polar("极坐标系示例", width=1200, height=600)
    polar.add("Love", data, angle_data=hour, boundary_gap=False, start_angle=0)
    polar.render()


def test_polar_draw_flower():
    data = []
    for i in range(361):
        t = i / 180 * math.pi
        r = math.sin(2 * t) * math.cos(2 * t)
        data.append([r, i])
    polar = Polar("极坐标系示例", width=1200, height=600)
    polar.add("Flower", data, start_angle=0, symbol=None, axis_range=[0, None])
    polar.render()


def test_polar_draw_color_flower():
    data = []
    for i in range(361):
        t = i / 180 * math.pi
        r = math.sin(2 * t) * math.cos(2 * t)
        data.append([r, i])
    polar = Polar("极坐标系示例", width=1200, height=600)
    polar.add(
        "Color-Flower",
        data,
        start_angle=0,
        symbol=None,
        axis_range=[0, None],
        area_color="#f71f24",
        area_opacity=0.6,
    )
    polar.render()


def test_polar_draw_snail():
    data = []
    for i in range(5):
        for j in range(101):
            theta = j / 100 * 360
            alpha = i * 360 + theta
            r = math.pow(math.e, 0.003 * alpha)
            data.append([r, theta])
    polar = Polar("极坐标系示例")
    polar.add(
        "",
        data,
        symbol_size=0,
        symbol="circle",
        start_angle=-25,
        is_radiusaxis_show=False,
        area_color="#f3c5b3",
        area_opacity=0.5,
        is_angleaxis_show=False,
    )
    polar.render()


def test_polor_custom_type():
    def render_item(params, api):
        values = [api.value(0), api.value(1)]
        coord = api.coord(values)
        size = api.size([1, 1], values)
        return {
            "type": "sector",
            "shape": {
                "cx": params.coordSys.cx,
                "cy": params.coordSys.cy,
                "r0": coord[2] - size[0] / 2,
                "r": coord[2] + size[0] / 2,
                "startAngle": coord[3] - size[1] / 2,
                "endAngle": coord[3] + size[1] / 2,
            },
            "style": api.style({"fill": api.visual("color")}),
        }

    polar = Polar("自定义渲染逻辑示例", width=1200, height=600)
    polar.add(
        "",
        [
            [random.randint(0, 6), random.randint(1, 24), random.randint(1, 24)]
            for _ in range(100)
        ],
        render_item=render_item,
        type="custom",
        angle_data=X_TIME,
        radius_data=WEEK,
        is_visualmap=True,
        visual_range=[0, 30],
    )
    html_content = polar._repr_html_()
    assert "function render_item(params, api) {" in html_content
    assert '"type": "custom"' in html_content
