#!/usr/bin/env python
#coding=utf-8
from __future__ import unicode_literals

from pyecharts import Scatter

def test_scatter():

    # scatter_0
    v1 = [10, 20, 30, 40, 50, 60]
    v2 = [10, 20, 30, 40, 50, 60]
    scatter = Scatter("散点图示例")
    scatter.add("A", v1, v2)
    scatter.add("B", v1[::-1], v2)
    scatter.show_config()
    scatter.render()

    # scatter_0_1
    scatter = Scatter("散点图示例")
    scatter.add("A", v1, v2)
    scatter.add("B", v1[::-1], v2, is_visualmap=True)
    scatter.show_config()
    scatter.render()

    # scatter_0_2
    scatter = Scatter("散点图示例")
    scatter.add("A", v1, v2)
    scatter.add("B", v1[::-1], v2, is_visualmap=True, visual_type='size', visual_range_size=[20, 80])
    scatter.show_config()
    scatter.render()

    # scatter_1
    scatter = Scatter("散点图示例")
    v1, v2 = scatter.draw("../images/pyecharts-0.png")
    scatter.add("pyecharts", v1, v2, is_random=True)
    scatter.show_config()
    scatter.render()

    # scatter_2
    scatter = Scatter("散点图示例", width=800, height=480)
    v1, v2 = scatter.draw("../images/love.png")
    scatter.add("Love", v1, v2)
    scatter.render()

    # scatter_3
    scatter = Scatter("散点图示例", width=1000, height=480)
    v1, v2 = scatter.draw("../images/cup.png")
    scatter.add("Cup", v1, v2)
    scatter.render()

    # scatter_4
    scatter = Scatter("散点图示例", width=1000, height=480)
    v1, v2 = scatter.draw("../images/cup.png")
    scatter.add("Cup", v1, v2, label_color=["#000"])
    scatter.render()
