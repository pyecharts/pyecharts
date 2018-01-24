#!/usr/bin/env python
# coding=utf-8
from __future__ import unicode_literals

from pyecharts import Line
from test.constants import CLOTHES, WEEK


clothes_v1 = [5, 20, 36, 10, 10, 100]
clothes_v2 = [55, 60, 16, 20, 15, 80]


def test_line_marks():
    line = Line("折线图示例")
    line.add("商家A", CLOTHES, clothes_v1, mark_point=["average"])
    line.add("商家B", CLOTHES, clothes_v2, is_smooth=True,
             mark_line=["max", "average"])
    line.render()


def test_line_user_define_markpoint():
    line = Line("折线图示例")
    line.add("商家A", CLOTHES, clothes_v1,
             mark_point=["average", {
                 "coord": ["裤子", 10], "name": "这是我想要的第一个标记点"}])
    line.add("商家B", CLOTHES, clothes_v2, is_smooth=True,
             mark_point=[{
                 "coord": ["袜子", 80], "name": "这是我想要的第二个标记点"}])
    line.render()


def test_line_user_define_marks():
    line = Line("折线图示例")
    line.add("商家A", CLOTHES, clothes_v1,
             mark_point=["average", "max", "min"], symbol_size=50,
             mark_point_symbol='diamond', mark_point_textcolor='#40ff27')
    line.add("商家B", CLOTHES, clothes_v2,
             mark_point=["average", "max", "min"],
             mark_point_symbol='arrow', mark_point_symbolsize=40)
    assert '"symbolSize":50' not in line._repr_html_()


def test_line_negative_value():
    line = Line("折线图示例")
    line.add("最高气温", WEEK, [11, 11, 15, 13, 12, 13, 10],
             mark_point=["max", "min"], mark_line=["average"])
    line.add("最低气温", WEEK, [1, -2, 2, 5, 3, 2, 0],
             mark_point=["max", "min"], mark_line=["average"])
    line.render()


def test_line_type_stack():
    line = Line("折线图-数据堆叠示例")
    line.add("商家A", CLOTHES, clothes_v1, is_stack=True, is_label_show=True)
    line.add("商家B", CLOTHES, clothes_v2, is_stack=True, is_label_show=True)
    line.render()


def test_line_type_step():
    line = Line("折线图-阶梯图示例")
    line.add("商家A", CLOTHES, clothes_v1, is_step=True, is_label_show=True)
    assert '"step": true' in line._repr_html_()


def test_line_type_fil():
    line = Line("折线图-面积图示例")
    line.add("商家A", CLOTHES, clothes_v1, is_fill=True, line_opacity=0.2,
             area_opacity=0.4, symbol=None)
    line.add("商家B", CLOTHES, clothes_v2, is_fill=True, area_color='#000',
             area_opacity=0.3, is_smooth=True)
    assert '"step": true' not in line._repr_html_()


def test_line_log_yaxis():
    import math
    import random
    line = Line("折线图示例")
    line.add("商家A", CLOTHES,
             [math.log10(random.randint(1, 99999)) for _ in range(6)])
    line.add("商家B", CLOTHES,
             [math.log10(random.randint(1, 99999999)) for _ in range(6)],
             yaxis_type="log")
    line.render()
