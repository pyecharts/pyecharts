# coding=utf-8
from __future__ import unicode_literals

from test.constants import RANGE_COLOR

from nose.tools import eq_

from pyecharts import Scatter3D


def test_scatter3d_must_use_canvas():
    scatter3d = Scatter3D()
    eq_(scatter3d.renderer, "canvas")
