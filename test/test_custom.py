#!/usr/bin/env python
# coding=utf-8
from __future__ import unicode_literals
from random import randint

from pyecharts import Bar, Line, Scatter, EffectScatter
from pyecharts import Grid, Timeline, Overlap, Page
from test.constants import CLOTHES, WEEK


def test_page_grid_timeline_overlap():
    # Grid
    v1 = [5, 20, 36, 10, 75, 90]
    v2 = [10, 25, 8, 60, 20, 80]
    bar = Bar("柱状图示例", height=720, width=1200, title_pos="65%")
    bar.add("商家A", CLOTHES, v1, is_stack=True)
    bar.add("商家B", CLOTHES, v2, is_stack=True, legend_pos="80%")
    line = Line("折线图示例")
    line.add("最高气温", WEEK, [11, 11, 15, 13, 12, 13, 10],
             mark_point=["max", "min"], mark_line=["average"])
    line.add("最低气温", WEEK, [1, -2, 2, 5, 3, 2, 0],
             mark_point=["max", "min"], mark_line=["average"],
             legend_pos="20%")
    v1 = [5, 20, 36, 10, 75, 90]
    v2 = [10, 25, 8, 60, 20, 80]
    scatter = Scatter("散点图示例", title_top="50%", title_pos="65%")
    scatter.add("scatter", v1, v2, legend_top="50%", legend_pos="80%")
    es = EffectScatter("动态散点图示例", title_top="50%")
    es.add("es", [11, 11, 15, 13, 12, 13, 10], [1, -2, 2, 5, 3, 2, 0],
           effect_scale=6, legend_top="50%", legend_pos="20%")

    grid = Grid()
    grid.add(bar, grid_bottom="60%", grid_left="60%")
    grid.add(line, grid_bottom="60%", grid_right="60%")
    grid.add(scatter, grid_top="60%", grid_left="60%")
    grid.add(es, grid_top="60%", grid_right="60%")

    # Timeline
    bar_1 = Bar("2012 年销量", "数据纯属虚构")
    bar_1.add("春季", CLOTHES, [randint(10, 100) for _ in range(6)])
    bar_1.add("夏季", CLOTHES, [randint(10, 100) for _ in range(6)])
    bar_1.add("秋季", CLOTHES, [randint(10, 100) for _ in range(6)])
    bar_1.add("冬季", CLOTHES, [randint(10, 100) for _ in range(6)])

    bar_2 = Bar("2013 年销量", "数据纯属虚构")
    bar_2.add("春季", CLOTHES, [randint(10, 100) for _ in range(6)])
    bar_2.add("夏季", CLOTHES, [randint(10, 100) for _ in range(6)])
    bar_2.add("秋季", CLOTHES, [randint(10, 100) for _ in range(6)])
    bar_2.add("冬季", CLOTHES, [randint(10, 100) for _ in range(6)])

    bar_3 = Bar("2014 年销量", "数据纯属虚构")
    bar_3.add("春季", CLOTHES, [randint(10, 100) for _ in range(6)])
    bar_3.add("夏季", CLOTHES, [randint(10, 100) for _ in range(6)])
    bar_3.add("秋季", CLOTHES, [randint(10, 100) for _ in range(6)])
    bar_3.add("冬季", CLOTHES, [randint(10, 100) for _ in range(6)])

    bar_4 = Bar("2015 年销量", "数据纯属虚构")
    bar_4.add("春季", CLOTHES, [randint(10, 100) for _ in range(6)])
    bar_4.add("夏季", CLOTHES, [randint(10, 100) for _ in range(6)])
    bar_4.add("秋季", CLOTHES, [randint(10, 100) for _ in range(6)])
    bar_4.add("冬季", CLOTHES, [randint(10, 100) for _ in range(6)])

    bar_5 = Bar("2016 年销量", "数据纯属虚构", height=720, width=1200)
    bar_5.add("春季", CLOTHES, [randint(10, 100) for _ in range(6)])
    bar_5.add("夏季", CLOTHES, [randint(10, 100) for _ in range(6)])
    bar_5.add("秋季", CLOTHES, [randint(10, 100) for _ in range(6)])
    bar_5.add("冬季", CLOTHES, [randint(10, 100) for _ in range(6)],
              is_legend_show=True)

    timeline = Timeline(is_auto_play=True, timeline_bottom=0)
    timeline.add(bar_1, '2012 年')
    timeline.add(bar_2, '2013 年')
    timeline.add(bar_3, '2014 年')
    timeline.add(bar_4, '2015 年')
    timeline.add(bar_5, '2016 年')

    # Overlap
    attr = ["{}月".format(i) for i in range(1, 13)]
    v1 = [2.0, 4.9, 7.0, 23.2, 25.6, 76.7, 135.6, 162.2, 32.6, 20.0, 6.4, 3.3]
    v2 = [2.6, 5.9, 9.0, 26.4, 28.7, 70.7, 175.6, 182.2, 48.7, 18.8, 6.0, 2.3]
    v3 = [2.0, 2.2, 3.3, 4.5, 6.3, 10.2, 20.3, 23.4, 23.0, 16.5, 12.0, 6.2]

    bar = Bar(height=720, width=1200)
    bar.add("蒸发量", attr, v1)
    bar.add("降水量", attr, v2, yaxis_formatter=" ml", yaxis_max=250)
    line = Line()
    line.add("平均温度", attr, v3, yaxis_formatter=" °C")

    overlap = Overlap()
    overlap.add(bar)
    overlap.add(line, yaxis_index=1, is_add_yaxis=True)

    page = Page()
    page.add(grid)
    page.add(timeline)
    page.add(overlap)
    page.render()
