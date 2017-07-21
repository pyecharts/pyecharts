#!/usr/bin/env python
#coding=utf-8

from pyecharts import Bar, Line, Scatter, EffectScatter

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

    # custom_1
    v1 = [10, 20, 30, 40, 50, 60]
    v2 = [30, 30, 30, 30, 30, 30]
    v3 = [50, 50, 50, 50, 50, 50]
    v4 = [10, 10, 10, 10, 10, 10]
    es = EffectScatter("Scatter - EffectScatter 示例")
    es.add("es", v1, v2)
    scatter = Scatter()
    scatter.add("scatter", v1, v3)
    es.custom(scatter.get_series())
    es_1 = EffectScatter()
    es_1.add("es_1", v1, v4, symbol='pin', effect_scale=5)
    es.custom(es_1.get_series())
    es.show_config()
    es.render()
