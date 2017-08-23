#!/usr/bin/env python
# coding=utf-8
from __future__ import unicode_literals

from pyecharts import Liquid


def test_liquid():

    # liquid_0
    liquid = Liquid("水球图示例")
    liquid.add("Liquid", [0.6])
    liquid.render()

    # liquid_1
    liquid = Liquid("水球图示例")
    liquid.add("Liquid", [0.6, 0.5, 0.4, 0.3], is_liquid_outline_show=False)
    liquid.render()

    # liquid_2
    liquid = Liquid("水球图示例")
    liquid.add("Liquid", [0.6, 0.5, 0.4, 0.3], is_liquid_animation=False, shape='diamond')
    liquid.render()
