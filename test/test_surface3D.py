#!/usr/bin/env python
# coding=utf-8
from __future__ import unicode_literals

import math
from test.constants import RANGE_COLOR

from nose.tools import eq_

from pyecharts import Surface3D


def create_surface3d_data():
    for t0 in range(-30, 30, 1):
        y = t0 / 10
        for t1 in range(-30, 30, 1):
            x = t1 / 10
            z = math.sin(x * x + y * y) * x / 3.14
            yield [x, y, z]


def test_surface3d_default():
    _data = list(create_surface3d_data())
    surface3d = Surface3D("3D 曲面图示例", width=1200, height=600)
    surface3d.add(
        "",
        _data,
        is_visualmap=True,
        visual_range_color=RANGE_COLOR,
        visual_range=[-3, 3],
        grid3d_rotate_sensitivity=5,
    )
    assert "lambert" not in surface3d._repr_html_()


def test_surface3d_must_use_canvas():
    surface3d = Surface3D()
    eq_(surface3d.renderer, "canvas")
