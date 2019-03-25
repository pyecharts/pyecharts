#!/usr/bin/env python
# coding=utf-8
from __future__ import unicode_literals

from test.constants import CLOTHES

from pyecharts import Funnel

prices = [20, 40, 60, 80, 100, 120]


def test_funnel_other_style():
    funnel = Funnel("漏斗图示例", title_pos="center")
    funnel.add(
        "商品",
        CLOTHES,
        prices,
        is_label_show=True,
        label_pos="outside",
        legend_orient="vertical",
        legend_pos="left",
    )
    funnel.render()
