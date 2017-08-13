#coding=utf-8
from __future__ import unicode_literals

from random import randint

from pyecharts.timeline import Timeline
from pyecharts import Bar, Pie

def test_timeline():

    attr = ["衬衫", "羊毛衫", "雪纺衫", "裤子", "高跟鞋", "袜子"]
    bar_1 = Bar("2012 年销量", "数据纯属虚构")
    bar_1.add("春季", attr, [randint(10, 100) for _ in range(6)])
    bar_1.add("夏季", attr, [randint(10, 100) for _ in range(6)])
    bar_1.add("秋季", attr, [randint(10, 100) for _ in range(6)])
    bar_1.add("冬季", attr, [randint(10, 100) for _ in range(6)])

    bar_2 = Bar("2013 年销量", "数据纯属虚构")
    bar_2.add("春季", attr, [randint(10, 100) for _ in range(6)])
    bar_2.add("夏季", attr, [randint(10, 100) for _ in range(6)])
    bar_2.add("秋季", attr, [randint(10, 100) for _ in range(6)])
    bar_2.add("冬季", attr, [randint(10, 100) for _ in range(6)])

    bar_3 = Bar("2014 年销量", "数据纯属虚构")
    bar_3.add("春季", attr, [randint(10, 100) for _ in range(6)])
    bar_3.add("夏季", attr, [randint(10, 100) for _ in range(6)])
    bar_3.add("秋季", attr, [randint(10, 100) for _ in range(6)])
    bar_3.add("冬季", attr, [randint(10, 100) for _ in range(6)])

    bar_4 = Bar("2015 年销量", "数据纯属虚构")
    bar_4.add("春季", attr, [randint(10, 100) for _ in range(6)])
    bar_4.add("夏季", attr, [randint(10, 100) for _ in range(6)])
    bar_4.add("秋季", attr, [randint(10, 100) for _ in range(6)])
    bar_4.add("冬季", attr, [randint(10, 100) for _ in range(6)])

    bar_5 = Bar("2016 年销量", "数据纯属虚构")
    bar_5.add("春季", attr, [randint(10, 100) for _ in range(6)])
    bar_5.add("夏季", attr, [randint(10, 100) for _ in range(6)])
    bar_5.add("秋季", attr, [randint(10, 100) for _ in range(6)])
    bar_5.add("冬季", attr, [randint(10, 100) for _ in range(6)], is_legend_show=True)

    timeline = Timeline(is_auto_play=True, timeline_bottom=0)
    timeline.add(bar_1, '2012 年')
    timeline.add(bar_2, '2013 年')
    timeline.add(bar_3, '2014 年')
    timeline.add(bar_4, '2015 年')
    timeline.add(bar_5, '2016 年')
    timeline.show_config()
    timeline.render()


def test_timeline_pie():

    attr = ["衬衫", "羊毛衫", "雪纺衫", "裤子", "高跟鞋", "袜子"]
    pie_1 = Pie("2012 年销量比例", "数据纯属虚构")
    pie_1.add("秋季", attr, [randint(10, 100) for _ in range(6)],
              is_label_show=True, radius=[30, 55], rosetype='radius')

    pie_2 = Pie("2013 年销量比例", "数据纯属虚构")
    pie_2.add("秋季", attr, [randint(10, 100) for _ in range(6)],
              is_label_show=True, radius=[30, 55], rosetype='radius')

    pie_3 = Pie("2014 年销量比例", "数据纯属虚构")
    pie_3.add("秋季", attr, [randint(10, 100) for _ in range(6)],
              is_label_show=True, radius=[30, 55], rosetype='radius')

    pie_4 = Pie("2015 年销量比例", "数据纯属虚构")
    pie_4.add("秋季", attr, [randint(10, 100) for _ in range(6)],
              is_label_show=True, radius=[30, 55], rosetype='radius')

    pie_5 = Pie("2016 年销量比例", "数据纯属虚构")
    pie_5.add("秋季", attr, [randint(10, 100) for _ in range(6)],
              is_label_show=True, radius=[30, 55], rosetype='radius')

    timeline = Timeline(is_auto_play=True, timeline_bottom=0)
    timeline.add(pie_1, '2012 年')
    timeline.add(pie_2, '2013 年')
    timeline.add(pie_3, '2014 年')
    timeline.add(pie_4, '2015 年')
    timeline.add(pie_5, '2016 年')
    timeline.show_config()
    timeline.render()
