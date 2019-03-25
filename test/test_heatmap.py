#!/usr/bin/env python
# coding=utf-8
from __future__ import unicode_literals

import random
from test.constants import X_TIME, Y_WEEK

from pyecharts import HeatMap


def test_heatmap_default():
    data = [[i, j, random.randint(0, 50)] for i in range(24) for j in range(7)]
    heatmap = HeatMap("热力图示例")
    heatmap.add(
        "热力图直角坐标系",
        X_TIME,
        Y_WEEK,
        data,
        is_visualmap=True,
        visual_text_color="#000",
        visual_orient="horizontal",
        xaxis_name="XNAME",
        yaxis_name="YNAME",
        yaxis_name_pos="end",
        yaxis_name_gap=5,
    )
    html_content = heatmap._repr_html_()
    assert "Saturday" in html_content
    assert "Monday" in html_content


def test_heatmap_display_yaxis_label():
    data = [[i, j, random.randint(0, 50)] for i in range(24) for j in range(7)]
    heatmap = HeatMap()
    heatmap.add(
        "热力图直角坐标系",
        X_TIME,
        Y_WEEK,
        data,
        is_visualmap=True,
        is_label_show=False,
        visual_text_color="#000",
        visual_orient="horizontal",
    )
    html_content = heatmap._repr_html_()
    assert r'"formatter": "{value} "' not in html_content
    assert "Saturday" in html_content
    assert "Monday" in html_content


def test_heatmap_yaxis_formatter():
    data = [[i, j, random.randint(0, 50)] for i in range(24) for j in range(7)]
    heatmap = HeatMap()
    heatmap.add(
        "热力图直角坐标系",
        X_TIME,
        Y_WEEK,
        data,
        is_visualmap=True,
        is_label_show=False,
        visual_text_color="#000",
        visual_orient="horizontal",
        yaxis_formatter="",
    )
    html_content = heatmap._repr_html_()
    assert r'"formatter": "{value} "' in html_content
    assert "Saturday" in html_content
    assert "Monday" in html_content
