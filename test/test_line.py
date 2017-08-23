#!/usr/bin/env python
# coding=utf-8
from __future__ import unicode_literals

from pyecharts import Line


def test_line():

    # line_0
    attr = ["衬衫", "羊毛衫", "雪纺衫", "裤子", "高跟鞋", "袜子"]
    v1 = [5, 20, 36, 10, 10, 100]
    v2 = [55, 60, 16, 20, 15, 80]
    line = Line("折线图示例")
    line.add("商家A", attr, v1, mark_point=["average"])
    line.add("商家B", attr, v2, is_smooth=True, mark_line=["max", "average"])
    line.render()

    # line_0_1
    line = Line("折线图示例")
    line.add("商家A", attr, v1, mark_point=["average", "max", "min"],
             mark_point_symbol='diamond', mark_point_textcolor='#40ff27')
    line.add("商家B", attr, v2, mark_point=["average", "max", "min"],
             mark_point_symbol='arrow', mark_point_symbolsize=40)
    line.render()

    # line_1
    line = Line("折线图-数据堆叠示例")
    line.add("商家A", attr, v1, is_stack=True, is_label_show=True)
    line.add("商家B", attr, v2, is_stack=True, is_label_show=True)
    line.render()

    # line_2
    line = Line("折线图-阶梯图示例")
    line.add("商家A", attr, v1, is_step=True, is_label_show=True)
    line.render()

    # line_3
    line = Line("折线图-面积图示例")
    line.add("商家A", attr, v1, is_fill=True, line_opacity=0.2, area_opacity=0.4, symbol=None)
    line.add("商家B", attr, v2, is_fill=True, area_color='#000', area_opacity=0.3, is_smooth=True)
    line.render()

    # line_3_1
    import math, random
    line = Line("折线图示例")
    line.add("商家A", attr, [math.log10(random.randint(1, 99999)) for _ in range(6)])
    line.add("商家B", attr, [math.log10(random.randint(1, 99999999)) for _ in range(6)], yaxis_type="log")
    line.render()

    # line_4
    attr = ['周一', '周二', '周三', '周四', '周五', '周六', '周日']
    line = Line("折线图示例")
    line.add("最高气温", attr, [11, 11, 15, 13, 12, 13, 10], mark_point=["max", "min"], mark_line=["average"])
    line.add("最低气温", attr, [1, -2, 2, 5, 3, 2, 0], mark_point=["max", "min"], mark_line=["average"])
    line.render()
