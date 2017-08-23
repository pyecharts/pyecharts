#!/usr/bin/env python
# coding=utf-8
from __future__ import unicode_literals

from pyecharts import HeatMap


def test_heatmap():

    # heatmap_0
    import random
    x_axis = ["12a", "1a", "2a", "3a", "4a", "5a", "6a", "7a", "8a", "9a", "10a", "11a",
              "12p", "1p", "2p", "3p", "4p", "5p", "6p", "7p", "8p", "9p", "10p", "11p"]
    y_axis = ["Saturday", "Friday", "Thursday", "Wednesday", "Tuesday", "Monday", "Sunday"]
    data = [[i, j, random.randint(0, 50)] for i in range(24) for j in range(7)]
    heatmap = HeatMap("热力图示例")
    heatmap.add("热力图直角坐标系", x_axis, y_axis, data, is_visualmap=True,
                visual_text_color="#000", visual_orient='horizontal')
    heatmap.render()
