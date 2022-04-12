# encoding: utf-8
"""
@file: test.grid.py
@desc:
@author: guozhen3
@time: 2022/2/18
"""

from nose.tools import assert_equal

from pyecharts import options as opts
from pyecharts.charts import Bar, Grid, Line
from test_overlap import test_chart_for_grid


def test_grid_control_axis_index():
    bar = test_chart_for_grid()
    gc = Grid().add(
        bar, opts.GridOpts(pos_left="5%", pos_right="20%"), is_control_axis_index=True
    )
    expected_idx = (0, 1, 2)
    for idx, series in enumerate(gc.options.get("series")):
        assert_equal(series.get("yAxisIndex"), expected_idx[idx])
    gc.render("grid_test.html")


test_grid_control_axis_index()
