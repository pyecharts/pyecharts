#!/usr/bin/env python
# coding=utf-8
from __future__ import unicode_literals

from pyecharts import Pie, Style
from test.constants import CLOTHES


def test_pie_default():
    v1 = [11, 12, 13, 10, 10, 10]
    pie = Pie("饼图示例")
    pie.add("", CLOTHES, v1, is_label_show=True)
    pie.render()


def test_pie_legend():
    v1 = [11, 12, 13, 10, 10, 10]
    pie = Pie("饼图-圆环图示例", title_pos='center')
    pie.add("", CLOTHES, v1, radius=[40, 75], label_text_color=None,
            is_label_show=True, legend_orient='vertical', legend_pos='left')
    pie.render()


def test_pie_type_rose():
    v1 = [11, 12, 13, 10, 10, 10]
    v2 = [19, 21, 32, 20, 20, 33]
    pie = Pie("饼图-玫瑰图示例", title_pos='center', width=900)
    pie.add("商品A", CLOTHES, v1, center=[25, 50], is_random=True,
            radius=[30, 75], rosetype='radius')
    pie.add("商品B", CLOTHES, v2, center=[75, 50], is_random=True,
            radius=[30, 75], rosetype='area',
            is_legend_show=False, is_label_show=True)
    pie.render()


def test_pie_type_radius():
    pie = Pie("饼图示例", title_pos='center', width=1000, height=600)
    pie.add("", ['A', 'B', 'C', 'D', 'E', 'F'], [335, 321, 234, 135, 251, 148],
            radius=[40, 55], is_label_show=True)
    pie.add("", ['H', 'I', 'J'], [335, 679, 204], radius=[0, 30],
            legend_orient='vertical', legend_pos='left')
    pie.render()


def test_pie_multiple():
    import random
    attr = ['A', 'B', 'C', 'D', 'E', 'F']
    pie = Pie("饼图示例", width=1000, height=600)
    pie.add("", attr, [random.randint(0, 100) for _ in range(6)],
            radius=[50, 55], center=[25, 50], is_random=True)
    pie.add("", attr, [random.randint(20, 100) for _ in range(6)],
            radius=[0, 45], center=[25, 50], rosetype='area')
    pie.add("", attr, [random.randint(0, 100) for _ in range(6)],
            radius=[50, 55], center=[65, 50], is_random=True)
    pie.add("", attr, [random.randint(20, 100) for _ in range(6)],
            radius=[0, 45], center=[65, 50], rosetype='radius')
    pie.render()


def test_pie_multiple_movie():
    pie = Pie('各类电影中"好片"所占的比例', "数据来着豆瓣", title_pos='center')
    style = Style()
    pie_style = style.add(
        label_pos="center",
        is_label_show=True,
        label_text_color=None
    )

    pie.add("", ["剧情", ""], [25, 75], center=[10, 30],
            radius=[18, 24], **pie_style)
    pie.add("", ["奇幻", ""], [24, 76], center=[30, 30],
            radius=[18, 24], **pie_style)
    pie.add("", ["爱情", ""], [14, 86], center=[50, 30],
            radius=[18, 24], **pie_style)
    pie.add("", ["惊悚", ""], [11, 89], center=[70, 30],
            radius=[18, 24], **pie_style)
    pie.add("", ["冒险", ""], [27, 73], center=[90, 30],
            radius=[18, 24], **pie_style)
    pie.add("", ["动作", ""], [15, 85], center=[10, 70],
            radius=[18, 24], **pie_style)
    pie.add("", ["喜剧", ""], [54, 46], center=[30, 70],
            radius=[18, 24], **pie_style)
    pie.add("", ["科幻", ""], [26, 74], center=[50, 70],
            radius=[18, 24], **pie_style)
    pie.add("", ["悬疑", ""], [25, 75], center=[70, 70],
            radius=[18, 24], **pie_style)
    pie.add("", ["犯罪", ""], [28, 72], center=[90, 70],
            radius=[18, 24], legend_top="center", **pie_style)
    pie.render()
