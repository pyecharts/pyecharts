#!/usr/bin/env python
# coding=utf-8
from __future__ import unicode_literals

from pyecharts import Bar


def test_bar():

    # bar_0
    attr = ["衬衫", "羊毛衫", "雪纺衫", "裤子", "高跟鞋", "袜子"]
    v1 = [5, 20, 36, 10, 75, 90]
    v2 = [10, 25, 8, 60, 20, 80]
    bar = Bar("柱状图数据堆叠示例")
    bar.add("商家A", attr, v1, is_stack=True)
    bar.add("商家B", attr, v2, is_stack=True)
    bar.render()

    # bar_1
    bar = Bar("标记线和标记点示例")
    bar.add("商家A", attr, v1, mark_point=["average"])
    bar.add("商家B", attr, v2, mark_line=["min", "max"])
    bar.render()

    # bar_2
    bar = Bar("x 轴和 y 轴交换")
    bar.add("商家A", attr, v1)
    bar.add("商家B", attr, v2, is_convert=True)
    bar.render()

    # bar_3
    attr = ["{}月".format(i) for i in range(1, 13)]
    v1 = [2.0, 4.9, 7.0, 23.2, 25.6, 76.7, 135.6, 162.2, 32.6, 20.0, 6.4, 3.3]
    v2 = [2.6, 5.9, 9.0, 26.4, 28.7, 70.7, 175.6, 182.2, 48.7, 18.8, 6.0, 2.3]
    bar = Bar("柱状图示例")
    bar.add("蒸发量", attr, v1, mark_line=["average"], mark_point=["max", "min"])
    bar.add("降水量", attr, v2, mark_line=["average"], mark_point=["max", "min"],
            is_datazoom_show=True, datazoom_range=[20, 60], datazoom_type='inside')
    bar.render()

    # bar_3_1
    bar = Bar("柱状图示例")
    bar.add("蒸发量", attr, v1, mark_line=["average"], mark_point=["max", "min"])
    bar.add("降水量", attr, v2, mark_line=["average"], mark_point=["max", "min"],
            is_datazoom_show=True, datazoom_range=[50, 80])
    bar.render()

    # bar_4
    import random

    attr = ["{}天".format(i) for i in range(30)]
    v1 = [random.randint(1, 30) for _ in range(30)]
    bar = Bar("Bar - datazoom - slider 示例")
    bar.add("", attr, v1, is_label_show=True, is_datazoom_show=True)
    bar.render()

    # bar_5
    attr = ["{}天".format(i) for i in range(30)]
    v1 = [random.randint(1, 30) for _ in range(30)]
    bar = Bar("Bar - datazoom - inside 示例")
    bar.add("", attr, v1, is_datazoom_show=True, datazoom_type='inside', datazoom_range=[10, 25])
    bar.render()

    # bar_6
    attr = ["{}天".format(i) for i in range(20)]
    v1 = [random.randint(1, 20) for _ in range(20)]
    bar = Bar("坐标轴标签旋转示例")
    bar.add("", attr, v1, xaxis_interval=0, xaxis_rotate=30, yaxis_rotate=30)
    bar.render()
