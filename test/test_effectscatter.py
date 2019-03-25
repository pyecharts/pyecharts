#!/usr/bin/env python
# coding=utf-8
from __future__ import unicode_literals

from pyecharts import EffectScatter


def test_effectscatter_splitline():
    es = EffectScatter("动态散点图各种图形示例")
    es.add("", [10], [10])
    assert es.options["xAxis"][0]["splitLine"]["show"] is True
