#!/usr/bin/env python
# coding=utf-8
from __future__ import unicode_literals

import math
import random

from pyecharts import Polar
from test.constants import WEEK


def test_polar_type_scatter_one():
    data = [(i, random.randint(1, 100)) for i in range(101)]
    polar = Polar("极坐标系-散点图示例")
    polar.add("", data, boundary_gap=False, type='scatter',
              is_splitline_show=False, is_axisline_show=True)
    assert '"type": "scatter"' in polar._repr_html_()


def test_polar_type_scatter_more():
    data_1 = [(10, random.randint(1, 100)) for i in range(300)]
    data_2 = [(11, random.randint(1, 100)) for i in range(300)]
    polar = Polar("极坐标系-散点图示例", width=1200, height=600)
    polar.add("", data_1, type='scatter')
    polar.add("", data_2, type='scatter')
    polar.render()


def test_polar_type_effectscatter():
    data = [(i, random.randint(1, 100)) for i in range(10)]
    polar = Polar("极坐标系-动态散点图示例", width=1200, height=600)
    polar.add("", data, type='effectScatter', effect_scale=10,
              effect_period=5)
    assert '"type": "effectScatter"' in polar._repr_html_()


def test_polar_type_barradius():
    polar = Polar("极坐标系-堆叠柱状图示例", width=1200, height=600)
    polar.add("A", [1, 2, 3, 4, 3, 5, 1], radius_data=WEEK,
              type='barRadius', is_stack=True)
    polar.add("B", [2, 4, 6, 1, 2, 3, 1], radius_data=WEEK,
              type='barRadius', is_stack=True)
    polar.add("C", [1, 2, 3, 4, 1, 2, 5], radius_data=WEEK,
              type='barRadius', is_stack=True)
    polar.render()


def test_polar_type_barangle():
    polar = Polar("极坐标系-堆叠柱状图示例", width=1200, height=600)
    polar.add("", [1, 2, 3, 4, 3, 5, 1], radius_data=WEEK,
              type='barAngle', is_stack=True)
    polar.add("", [2, 4, 6, 1, 2, 3, 1], radius_data=WEEK,
              type='barAngle', is_stack=True)
    polar.add("", [1, 2, 3, 4, 1, 2, 5], radius_data=WEEK,
              type='barAngle', is_stack=True)
    polar.render()


def test_polar_draw_love():
    data = []
    for i in range(101):
        theta = i / 100 * 360
        r = 5 * (1 + math.sin(theta / 180 * math.pi))
        data.append([r, theta])
    hour = [i for i in range(1, 25)]
    polar = Polar("极坐标系示例", width=1200, height=600)
    polar.add("Love", data, angle_data=hour,
              boundary_gap=False, start_angle=0)
    polar.render()


def test_polar_draw_flower():
    data = []
    for i in range(361):
        t = i / 180 * math.pi
        r = math.sin(2 * t) * math.cos(2 * t)
        data.append([r, i])
    polar = Polar("极坐标系示例", width=1200, height=600)
    polar.add("Flower", data, start_angle=0,
              symbol=None, axis_range=[0, None])
    polar.render()


def test_polar_draw_color_flower():
    data = []
    for i in range(361):
        t = i / 180 * math.pi
        r = math.sin(2 * t) * math.cos(2 * t)
        data.append([r, i])
    polar = Polar("极坐标系示例", width=1200, height=600)
    polar.add("Color-Flower", data, start_angle=0, symbol=None,
              axis_range=[0, None], area_color="#f71f24", area_opacity=0.6)
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
    polar.add("", data, symbol_size=0, symbol='circle', start_angle=-25,
              is_radiusaxis_show=False, area_color="#f3c5b3",
              area_opacity=0.5, is_angleaxis_show=False)
    polar.render()
