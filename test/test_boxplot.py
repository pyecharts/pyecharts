#!/usr/bin/env python
# coding=utf-8
from __future__ import unicode_literals

from pyecharts import Boxplot


def test_boxplot_one_legend():
    boxplot = Boxplot("箱形图")
    x_axis = ['expr1', 'expr2', 'expr3', 'expr4', 'expr5']
    y_axis = [
        [850, 740, 900, 1070, 930, 850, 950, 980, 980, 880,
         1000, 980, 930, 650, 760, 810, 1000, 1000, 960, 960],
        [960, 940, 960, 940, 880, 800, 850, 880, 900, 840,
         830, 790, 810, 880, 880, 830, 800, 790, 760, 800],
        [880, 880, 880, 860, 720, 720, 620, 860, 970, 950,
         880, 910, 850, 870, 840, 840, 850, 840, 840, 840],
        [890, 810, 810, 820, 800, 770, 760, 740, 750, 760,
         910, 920, 890, 860, 880, 720, 840, 850, 850, 780],
        [890, 840, 780, 810, 760, 810, 790, 810, 820, 850,
         870, 870, 810, 740, 810, 940, 950, 800, 810, 870]
    ]
    _yaxis = boxplot.prepare_data(y_axis)
    boxplot.add("boxplot", x_axis, _yaxis)
    boxplot.render()


def test_boxplot_two_legend():
    boxplot = Boxplot("箱形图")
    x_axis = ['expr1', 'expr2']
    y_axis1 = [
        [850, 740, 900, 1070, 930, 850, 950, 980, 980, 880,
         1000, 980, 930, 650, 760, 810, 1000, 1000, 960, 960],
        [960, 940, 960, 940, 880, 800, 850, 880, 900, 840,
         830, 790, 810, 880, 880, 830, 800, 790, 760, 800],
    ]
    y_axis2 = [
        [890, 810, 810, 820, 800, 770, 760, 740, 750, 760,
         910, 920, 890, 860, 880, 720, 840, 850, 850, 780],
        [890, 840, 780, 810, 760, 810, 790, 810, 820, 850,
         870, 870, 810, 740, 810, 940, 950, 800, 810, 870]
    ]
    boxplot.add("category1", x_axis, boxplot.prepare_data(y_axis1))
    boxplot.add("category2", x_axis, boxplot.prepare_data(y_axis2))
    html_content = boxplot._repr_html_()
    assert "category1" in html_content
    assert "category2" in html_content
