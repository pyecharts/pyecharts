#!/usr/bin/env python
# coding=utf-8
from __future__ import unicode_literals

import math

from test.constants import RANGE_COLOR
from pyecharts import Line3D
from nose.tools import eq_


def create_line3d_data():
    for t in range(0, 25000):
        _t = t / 1000
        x = (1 + 0.25 * math.cos(75 * _t)) * math.cos(_t)
        y = (1 + 0.25 * math.cos(75 * _t)) * math.sin(_t)
        z = _t + 2.0 * math.sin(75 * _t)
        yield [x, y, z]


def test_line3d_default():
    _data = list(create_line3d_data())
    line3d = Line3D("3D 折线图示例", width=1200, height=600)
    line3d.add("", _data, is_visualmap=True, visual_range_color=RANGE_COLOR,
               visual_range=[0, 30], grid3d_rotate_sensitivity=5)
    line3d.render()


def test_line3d_rotate_automatically_speedup():
    _data = list(create_line3d_data())
    line3d = Line3D("3D 折线图示例", width=1200, height=600)
    line3d.add("", _data, is_visualmap=True, visual_range_color=RANGE_COLOR,
               visual_range=[0, 30], is_grid3d_rotate=True,
               grid3d_rotate_speed=180)
    line3d.render()


def test_line3d_must_use_canvas():
    line3d = Line3D("3D 折线图示例", width=1200, height=600)
    eq_(line3d.renderer, 'canvas')
