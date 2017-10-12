#!/usr/bin/env python
# coding=utf-8
from __future__ import unicode_literals

from pyecharts import Funnel


def test_funnel():
    # label_pos 'inside'
    attr = ["衬衫", "羊毛衫", "雪纺衫", "裤子", "高跟鞋", "袜子"]
    value = [20, 40, 60, 80, 100, 120]
    funnel = Funnel("漏斗图示例")
    funnel.add("商品", attr, value, is_label_show=True, label_pos="inside",
               label_text_color="#fff")
    funnel.render()

    # label_pos 'outside'&legend_orient 'vertical'
    funnel = Funnel("漏斗图示例", title_pos='center')
    funnel.add("商品", attr, value, is_label_show=True, label_pos="outside",
               legend_orient='vertical', legend_pos='left')
    funnel.render()
