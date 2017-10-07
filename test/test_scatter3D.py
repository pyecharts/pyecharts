#!/usr/bin/env python
# coding=utf-8
from __future__ import unicode_literals

from pyecharts import Scatter3D
from test.constants import RANGE_COLOR


def test_scatter3d():
    import random
    data = [
        [random.randint(0, 100),
         random.randint(0, 100),
         random.randint(0, 100)] for _ in range(80)
    ]
    scatter3d = Scatter3D("3D 散点图示例", width=1200, height=600)
    scatter3d.add("", data, is_visualmap=True,
                  visual_range_color=RANGE_COLOR)
    scatter3d.render()
