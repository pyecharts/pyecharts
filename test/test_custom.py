#!/usr/bin/env python
#coding=utf-8

from pyecharts import Bar, Line

def test_custom():

    # custom_0
    attr = ['A', 'B', 'C', 'D', 'E', 'F']
    v1 = [10, 20, 30, 40, 50, 60]
    v2 = [15, 25, 35, 45, 55, 65]
    v3 = [38, 28, 58, 48, 78, 68]
    bar = Bar("Line - Bar 示例")
    bar.add("bar", attr, v1)
    line = Line()
    line.add("line", v2, v3)
    bar.custom(line.get_series())
    bar.show_config()
    bar.render()