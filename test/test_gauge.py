#!/usr/bin/env python
# coding=utf-8
from __future__ import unicode_literals

from pyecharts import Gauge


def test_gauge_default():
    gauge = Gauge("仪表盘示例")
    gauge.add("业务指标", "完成率", 66.66)
    assert "66.66" in gauge._repr_html_()


def test_gauge_angle_range_and_scale_range():
    gauge = Gauge("仪表盘示例")
    gauge.add("业务指标", "完成率", 166.66, angle_range=[180, 0],
              scale_range=[0, 200], is_legend_show=False)
    assert "166.66" in gauge._repr_html_()
