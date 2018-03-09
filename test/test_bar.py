#!/usr/bin/env python
# coding=utf-8
from __future__ import unicode_literals

import random

from pyecharts import Bar
from test.constants import CLOTHES

clothes_v1 = [5, 20, 36, 10, 75, 90]
clothes_v2 = [10, 25, 8, 60, 20, 80]


def test_bar_stack():
    bar = Bar("柱状图数据堆叠示例")
    bar.add("商家A", CLOTHES, clothes_v1, is_stack=True)
    bar.add("商家B", CLOTHES, clothes_v2, is_stack=True)
    bar.chart_id = 'id_chart_id'
    html_content = bar._repr_html_()
    assert 'id_chart_id' == bar.chart_id
    assert "dataZoom" not in html_content
    assert "stack_" in html_content


def test_bar_marks():
    bar = Bar("标记线和标记点示例")
    bar.add("商家A", CLOTHES, clothes_v1, mark_point=["average"])
    bar.add("商家B", CLOTHES, clothes_v2, mark_line=["min", "max"])
    assert '"average"' in bar._repr_html_()


def test_bar_convert_xy_axis():
    bar = Bar("x 轴和 y 轴交换")
    bar.add("商家A", CLOTHES, clothes_v1)
    bar.add("商家B", CLOTHES, clothes_v2, is_convert=True)
    assert "average" not in bar._repr_html_()


def test_bar_histogram():
    bar = Bar("直方图示例")
    bar.add("", CLOTHES * 2, clothes_v1 + clothes_v2, bar_category_gap=0)
    bar.render()


def test_bar_rotate_label():
    days = ["{}天".format(i) for i in range(20)]
    days_v1 = [random.randint(1, 20) for _ in range(20)]
    bar = Bar("坐标轴标签旋转示例")
    bar.add("", days, days_v1, xaxis_interval=0, xaxis_rotate=30,
            yaxis_rotate=30)
    assert "stack_" not in bar._repr_html_()


def test_bar_waterfall():
    months = ["{}月".format(i) for i in range(1, 8)]
    months_v1 = [0, 100, 200, 300, 400, 220, 250]
    months_v2 = [1000, 800, 600, 500, 450, 400, 300]
    bar = Bar("瀑布图示例")
    bar.add("", months, months_v1, label_color=['rgba(0,0,0,0)'],
            is_stack=True)
    bar.add("月份", months, months_v2, is_label_show=True, is_stack=True,
            label_pos='inside')
    bar.render()


def test_bar_datazoom_undefined():
    days = ["{}天".format(i) for i in range(30)]
    days_v1 = [random.randint(1, 30) for _ in range(30)]
    bar = Bar("Bar - datazoom 默认 示例")
    bar.add("", days, days_v1, is_label_show=True, is_datazoom_show=True)
    html_content = bar._repr_html_()
    assert "dataZoom" in html_content
    assert ': "slider"' in html_content
    assert ': "inside"' not in html_content


def test_bar_datazoom_slider():
    days = ["{}天".format(i) for i in range(30)]
    days_v1 = [random.randint(1, 30) for _ in range(30)]
    bar = Bar("Bar - datazoom 示例")
    bar.add("", days, days_v1, is_datazoom_show=True,
            datazoom_type='slider', datazoom_range=[10, 25])
    html_content = bar._repr_html_()
    assert "dataZoom" in html_content
    assert ': "slider"' in html_content
    assert ': "inside"' not in html_content


def test_bar_datazoom_inside():
    days = ["{}天".format(i) for i in range(30)]
    days_v1 = [random.randint(1, 30) for _ in range(30)]
    bar = Bar("Bar - datazoom - inside 示例")
    bar.add("", days, days_v1, is_datazoom_show=True,
            datazoom_type='inside', datazoom_range=[10, 25])
    html_content = bar._repr_html_()
    assert "dataZoom" in html_content
    assert ': "inside"' in html_content
    assert ': "slider"' not in html_content


def test_bar_datazoom_both():
    days = ["{}天".format(i) for i in range(30)]
    days_v1 = [random.randint(1, 30) for _ in range(30)]
    bar = Bar("Bar - datazoom - both 示例")
    bar.add("", days, days_v1, is_datazoom_show=True,
            datazoom_type='both', datazoom_range=[10, 25],
            is_toolbox_show=False)
    html_content = bar._repr_html_()
    assert "dataZoom" in html_content
    assert ': "inside"' in html_content
    assert ': "slider"' in html_content
