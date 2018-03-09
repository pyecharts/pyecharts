#!/usr/bin/env python
# coding=utf-8
from __future__ import unicode_literals

from pyecharts import Scatter


v1 = [10, 20, 30, 40, 50, 60]
v2 = [10, 20, 30, 40, 50, 60]


def test_scatter_defualt():
    scatter = Scatter("散点图示例")
    scatter.add("A", v1, v2)
    scatter.add("B", v1[::-1], v2)
    html_content = scatter._repr_html_()
    assert '"type": "value"' in html_content
    assert '"type": "category"' not in html_content


def test_scatter_xaxis_type_category():
    scatter = Scatter("散点图示例")
    scatter.add("A", ["a", "b", "c", "d", "e", "f"], v2)
    scatter.add("B", ["a", "b", "c", "d", "e", "f"], v1[::-1],
                xaxis_type="category")
    assert '"type": "category"' in scatter._repr_html_()


def test_scatter_visualmap_default():
    scatter = Scatter("散点图示例")
    scatter.add("A", v1, v2)
    scatter.add("B", v1[::-1], v2, is_visualmap=True)
    scatter.render()


def test_scatter_visualmap_type_size():
    scatter = Scatter("散点图示例")
    scatter.add("B", v1[::-1], v2, is_visualmap=True, visual_type='size',
                visual_range_size=[20, 80])
    scatter.render()


def test_scatter_draw_love():
    scatter = Scatter("散点图示例", width=800, height=480)
    v1, v2 = scatter.draw("../images/love.png")
    scatter.add("Love", v1, v2)
    scatter.render()


def test_scatter_draw__hot_red_bra():
    scatter = Scatter("散点图示例", width=1000, height=480)
    v1, v2 = scatter.draw("../images/cup.png")
    scatter.add("Cup", v1, v2)
    scatter.render()


def test_scatter_multi_dimension():
    data = [
        [28604, 77, 17096869],
        [31163, 77.4, 27662440],
        [1516, 68, 1154605773],
        [13670, 74.7, 10582082],
        [28599, 75, 4986705],
        [29476, 77.1, 56943299],
        [31476, 75.4, 78958237],
        [28666, 78.1, 254830],
        [1777, 57.7, 870601776],
        [29550, 79.1, 122249285],
        [2076, 67.9, 20194354],
        [12087, 72, 42972254],
        [24021, 75.4, 3397534],
        [43296, 76.8, 4240375],
        [10088, 70.8, 38195258],
        [19349, 69.6, 147568552],
        [10670, 67.3, 53994605],
        [26424, 75.7, 57110117],
        [37062, 75.4, 252847810]
    ]

    x_lst = [v[0] for v in data]
    y_lst = [v[1] for v in data]
    extra_data = [v[2] for v in data]
    sc = Scatter()
    sc.add("scatter", x_lst, y_lst, extra_data=extra_data, is_visualmap=True,
           visual_dimension=2, visual_orient='horizontal',
           visual_type='size', visual_range=[254830, 1154605773],
           visual_text_color='#000')
    sc.render()


def test_scatter_markline_coords():
    scatter = Scatter("散点图示例")
    scatter.add("A", v1, v2, mark_line_coords=[[10, 10], [30, 30]])
    assert '"coord": [' in scatter._repr_html_()
