#!/usr/bin/env python
# coding=utf-8
from __future__ import unicode_literals

from pyecharts import Line


def test_line():
    # line default markLine&markPoint
    attr = ["衬衫", "羊毛衫", "雪纺衫", "裤子", "高跟鞋", "袜子"]
    v1 = [5, 20, 36, 10, 10, 100]
    v2 = [55, 60, 16, 20, 15, 80]
    line = Line("折线图示例")
    line.add("商家A", attr, v1, mark_point=["average"])
    line.add("商家B", attr, v2, is_smooth=True, mark_line=["max", "average"])
    line.render()

    # line user-define markPoint
    line = Line("折线图示例")
    line.add("商家A", attr, v1,
             mark_point=["average", {
                 "coord": ["裤子", 10], "name": "这是我想要的第一个标记点"}])
    line.add("商家B", attr, v2, is_smooth=True,
             mark_point=[{
                 "coord": ["袜子", 80], "name": "这是我想要的第二个标记点"}])
    line.render()

    # line user-define markLine&markPoint
    line = Line("折线图示例")
    line.add("商家A", attr, v1, mark_point=["average", "max", "min"],
             mark_point_symbol='diamond', mark_point_textcolor='#40ff27')
    line.add("商家B", attr, v2, mark_point=["average", "max", "min"],
             mark_point_symbol='arrow', mark_point_symbolsize=40)
    line.render()

    # line user-define markLine&markPoint
    attr = ['周一', '周二', '周三', '周四', '周五', '周六', '周日']
    line = Line("折线图示例")
    line.add("最高气温", attr, [11, 11, 15, 13, 12, 13, 10],
             mark_point=["max", "min"], mark_line=["average"])
    line.add("最低气温", attr, [1, -2, 2, 5, 3, 2, 0],
             mark_point=["max", "min"], mark_line=["average"])
    line.render()


def test_line_type():
    # line is_stack
    attr = ["衬衫", "羊毛衫", "雪纺衫", "裤子", "高跟鞋", "袜子"]
    v1 = [5, 20, 36, 10, 10, 100]
    v2 = [55, 60, 16, 20, 15, 80]
    line = Line("折线图-数据堆叠示例")
    line.add("商家A", attr, v1, is_stack=True, is_label_show=True)
    line.add("商家B", attr, v2, is_stack=True, is_label_show=True)
    line.render()

    # line is_step
    line = Line("折线图-阶梯图示例")
    line.add("商家A", attr, v1, is_step=True, is_label_show=True)
    assert '"step": true' in line._repr_html_()

    # line is_fill
    line = Line("折线图-面积图示例")
    line.add("商家A", attr, v1, is_fill=True, line_opacity=0.2,
             area_opacity=0.4, symbol=None)
    line.add("商家B", attr, v2, is_fill=True, area_color='#000',
             area_opacity=0.3, is_smooth=True)
    assert '"step": true' not in line._repr_html_()

    # line yAxis type 'log'
    import math
    import random
    line = Line("折线图示例")
    line.add("商家A", attr,
             [math.log10(random.randint(1, 99999)) for _ in range(6)])
    line.add("商家B", attr,
             [math.log10(random.randint(1, 99999999)) for _ in range(6)],
             yaxis_type="log")
    line.render()
