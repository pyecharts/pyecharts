# encoding: utf-8
"""
@file: test_overlap.py
@desc:
@author: guozhen3
@time: 2022/2/18
"""

from unittest.mock import patch

from nose.tools import assert_equal, assert_in

from pyecharts import options as opts
from pyecharts.charts import Bar, Grid, Line


def test_chart_for_grid():
    x_data = ["{}月".format(i) for i in range(1, 13)]
    bar = (
        Bar()
            .add_xaxis(x_data)
            .add_yaxis(
            "蒸发量",
            [2.0, 4.9, 7.0, 23.2, 25.6, 76.7, 135.6, 162.2, 32.6, 20.0, 6.4, 3.3],
            yaxis_index=0,
            color='red'
        )
            .add_yaxis(
            "降水量",
            [2.6, 5.9, 9.0, 26.4, 28.7, 70.7, 175.6, 182.2, 48.7, 18.8, 6.0, 2.3],
            yaxis_index=1,
            color='green'
        )
            .extend_axis(yaxis=opts.AxisOpts(name="蒸发量", type_="value", position="right"))
            .extend_axis(yaxis=opts.AxisOpts(type_="value", name="温度", position="left"))
            .set_global_opts(
            yaxis_opts=opts.AxisOpts(name="降水量", position="right", offset=80)
        )
    )

    line = (
        Line()
            .add_xaxis(x_data)
            .add_yaxis(
            "平均温度",
            [2.0, 2.2, 3.3, 4.5, 6.3, 10.2, 20.3, 23.4, 23.0, 16.5, 12.0, 6.2],
            yaxis_index=2,
            color="blue",
            label_opts=opts.LabelOpts(is_show=False),
        )
    )

    bar.overlap(line)
    assert_equal(bar.colors[:3], ['red', 'green', 'blue'])
    bar.render("overlap_test_after_colors_update.html")
    return bar


if __name__ == "__main__":
    test_chart_for_grid()
