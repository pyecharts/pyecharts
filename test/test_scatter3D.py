#!/usr/bin/env python
# coding=utf-8
from __future__ import unicode_literals

from pyecharts import Scatter3D


def test_scatter3d():

    # scatter3D_0
    import random
    data = [
        [random.randint(0, 100), random.randint(0, 100), random.randint(0, 100)] for _ in range(80)
    ]
    range_color = ['#313695', '#4575b4', '#74add1', '#abd9e9', '#e0f3f8', '#ffffbf',
                   '#fee090', '#fdae61', '#f46d43', '#d73027', '#a50026']
    scatter3d = Scatter3D("3D 散点图示例", width=1200, height=600)
    scatter3d.add("", data, is_visualmap=True, visual_range_color=range_color)
    scatter3d.render()
