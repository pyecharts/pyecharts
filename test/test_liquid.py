#!/usr/bin/env python
# coding=utf-8
from __future__ import unicode_literals

from pyecharts import Liquid


def test_liquid():
    # liquid default
    liquid = Liquid("水球图示例")
    liquid.add("Liquid", [0.6])
    liquid.render()

    # liquid multiple data
    liquid = Liquid("水球图示例")
    liquid.add("Liquid", [0.6, 0.5, 0.4, 0.3], is_liquid_outline_show=False)
    assert "diamond" not in liquid._repr_html_()

    # liquid shape diamond
    liquid = Liquid("水球图示例")
    liquid.add("Liquid", [0.6, 0.5, 0.4, 0.3], is_liquid_animation=False,
               shape='diamond')
    assert "diamond" in liquid._repr_html_()
