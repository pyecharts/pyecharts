#!/usr/bin/env python
# coding=utf-8
from __future__ import unicode_literals

import random

from pyecharts import HeatMap
from test.constants import X_TIME, Y_WEEK


def test_heatmap_default():
    data = [
        [i, j, random.randint(0, 50)] for i in range(24) for j in range(7)]
    heatmap = HeatMap("热力图示例")
    heatmap.add("热力图直角坐标系", X_TIME, Y_WEEK, data, is_visualmap=True,
                visual_text_color="#000", visual_orient='horizontal',
                xaxis_name='XNAME', yaxis_name='YNAME',
                yaxis_name_pos='end', yaxis_name_gap=5)
    heatmap.render()


def test_heatmap_calendar():
    import datetime
    begin = datetime.date(2017, 1, 1)
    end = datetime.date(2017, 12, 31)
    data = [[str(begin + datetime.timedelta(days=i)),
             random.randint(1000, 25000)]
            for i in range((end - begin).days + 1)]
    heatmap = HeatMap("日历热力图示例", "某人 2017 年微信步数情况", width=1100)
    heatmap.add("", data, is_calendar_heatmap=True,
                visual_text_color='#000', visual_range_text=['', ''],
                visual_range=[1000, 25000], calendar_cell_size=['auto', 30],
                is_visualmap=True, calendar_date_range="2017",
                visual_orient="horizontal", visual_pos="center",
                visual_top="80%", is_piecewise=True)
    heatmap.render()
