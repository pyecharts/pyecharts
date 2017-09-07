#!/usr/bin/env python
# coding=utf-8
from __future__ import unicode_literals

from pyecharts import Scatter


def test_scatter_xaxis_type():
    # xAxis type 'value'
    v1 = [10, 20, 30, 40, 50, 60]
    v2 = [10, 20, 30, 40, 50, 60]
    scatter = Scatter("散点图示例")
    scatter.add("A", v1, v2)
    scatter.add("B", v1[::-1], v2)
    assert '"type": "value"' in scatter._repr_html_()
    assert '"type": "category"' not in scatter._repr_html_()
    scatter.render()

    # xAxis type 'category'
    scatter = Scatter("散点图示例")
    scatter.add("A", ["a", "b", "c", "d", "e", "f"], v2)
    scatter.add("B", ["a", "b", "c", "d", "e", "f"], v1[::-1],
                xaxis_type="category")
    assert '"type": "category"' in scatter._repr_html_()
    scatter.render()


def test_scatter_visualmap():
    # visual type 'color'
    v1 = [10, 20, 30, 40, 50, 60]
    v2 = [10, 20, 30, 40, 50, 60]
    scatter = Scatter("散点图示例")
    scatter.add("A", v1, v2)
    scatter.add("B", v1[::-1], v2, is_visualmap=True)
    scatter.render()

    # visual type 'size'
    scatter = Scatter("散点图示例")
    scatter.add("A", v1, v2)
    scatter.add("B", v1[::-1], v2, is_visualmap=True, visual_type='size',
                visual_range_size=[20, 80])
    scatter.render()


def test_scatter_draw_picture():
    # draw pyecharts
    scatter = Scatter("散点图示例")
    v1, v2 = scatter.draw("../images/pyecharts-0.png")
    scatter.add("pyecharts", v1, v2, is_random=True)
    scatter.render()

    # draw love
    scatter = Scatter("散点图示例", width=800, height=480)
    v1, v2 = scatter.draw("../images/love.png")
    scatter.add("Love", v1, v2)
    scatter.render()

    # draw a hot red bra
    scatter = Scatter("散点图示例", width=1000, height=480)
    v1, v2 = scatter.draw("../images/cup.png")
    scatter.add("Cup", v1, v2)
    scatter.render()

    # draw a sexy black bra
    scatter = Scatter("散点图示例", width=1000, height=480)
    v1, v2 = scatter.draw("../images/cup.png")
    scatter.add("Cup", v1, v2, label_color=["#000"])
    scatter.render()
