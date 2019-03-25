#!/usr/bin/env python
# coding=utf-8
from __future__ import unicode_literals

import math
import random
from test.constants import CLOTHES, WEEK

from pyecharts import Line

clothes_v1 = [5, 20, 36, 10, 10, 100]
clothes_v2 = [55, 60, 16, 20, 15, 80]


def test_line_user_define_markpoint():
    line = Line("折线图示例")
    line.add(
        "商家A",
        CLOTHES,
        clothes_v1,
        mark_point=["average", {"coord": ["裤子", 10], "name": "这是我想要的第一个标记点"}],
    )
    line.add(
        "商家B",
        CLOTHES,
        clothes_v2,
        is_smooth=True,
        mark_point=[{"coord": ["袜子", 80], "name": "这是我想要的第二个标记点"}],
    )
    html_content = line._repr_html_()
    assert '"value": 80' in html_content
    assert '"value": 10' in html_content


def test_line_user_define_marks():
    line = Line("折线图示例")
    line.add(
        "商家A",
        CLOTHES,
        clothes_v1,
        mark_point=["average", "max", "min"],
        symbol_size=50,
        mark_point_symbol="diamond",
        mark_point_textcolor="#40ff27",
    )
    line.add(
        "商家B",
        CLOTHES,
        clothes_v2,
        mark_point=["average", "max", "min"],
        mark_point_symbol="arrow",
        mark_point_symbolsize=40,
    )
    assert '"symbolSize":50' not in line._repr_html_()


def test_line_type_step():
    line = Line("折线图-阶梯图示例")
    line.add("商家A", CLOTHES, clothes_v1, is_step=True, is_label_show=True)
    assert '"step": true' in line._repr_html_()


def test_line_type_fill():
    line = Line("折线图-面积图示例")
    line.add(
        "商家A",
        CLOTHES,
        clothes_v1,
        is_fill=True,
        line_opacity=0.2,
        area_opacity=0.4,
        symbol=None,
    )
    line.add(
        "商家B",
        CLOTHES,
        clothes_v2,
        is_fill=True,
        area_color="#000",
        area_opacity=0.3,
        is_smooth=True,
    )
    assert '"step": true' not in line._repr_html_()


def test_line_mark_point_raw():
    line = Line()
    line.add(
        "商家A",
        CLOTHES,
        clothes_v1,
        mark_point_raw=[
            {"name": "rawData", "symbol": "pin", "coord": ["衬衫", 5], "value": 5}
        ],
    )
    assert line.options.get("series")[0]["markLine"]["data"] == []
