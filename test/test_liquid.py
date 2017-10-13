#!/usr/bin/env python
# coding=utf-8
from __future__ import unicode_literals

from pyecharts import Liquid


def test_liquid_default():
    liquid = Liquid("水球图示例")
    liquid.add("Liquid", [0.6])
    liquid.render()


def test_liquid_multiple_data():
    liquid = Liquid("水球图示例")
    liquid.add("Liquid", [0.6, 0.5, 0.4, 0.3], is_liquid_outline_show=False)
    assert "diamond" not in liquid._repr_html_()


def test_liquid_diamond_shape():
    liquid = Liquid("水球图示例")
    liquid.add("Liquid", [0.6, 0.5, 0.4, 0.3], is_liquid_animation=False,
               shape='diamond')
    assert "diamond" in liquid._repr_html_()
