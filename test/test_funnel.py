#!/usr/bin/env python
# coding=utf-8
from __future__ import unicode_literals

from pyecharts import Funnel
from test.constants import CLOTHES

prices = [20, 40, 60, 80, 100, 120]


def test_funnel_labelpos_inside():
    funnel = Funnel("漏斗图示例")
    funnel.add("商品", CLOTHES, prices, is_label_show=True,
               label_pos="inside", label_text_color="#fff")
    funnel.render()


def test_funnel_other_style():
    funnel = Funnel("漏斗图示例", title_pos='center')
    funnel.add("商品", CLOTHES, prices, is_label_show=True, label_pos="outside",
               legend_orient='vertical', legend_pos='left')
    funnel.render()
