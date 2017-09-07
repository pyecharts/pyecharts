#!/usr/bin/env python
# coding=utf-8
from __future__ import unicode_literals

from pyecharts import HeatMap
from test.constants import X_TIME, Y_WEEK


def test_heatmap():
    import random
    data = [[i, j, random.randint(0, 50)] for i in range(24) for j in range(7)]
    heatmap = HeatMap("热力图示例")
    heatmap.add("热力图直角坐标系", X_TIME, Y_WEEK, data, is_visualmap=True,
                visual_text_color="#000", visual_orient='horizontal')
    heatmap.render()
