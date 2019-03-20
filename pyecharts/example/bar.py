# coding=utf-8

import pyecharts.options as opts
from pyecharts.charts import Bar
from pyecharts.example.commons import CLOTHES, gen_random_data
from pyecharts.render import make_snapshot


def bar_base() -> Bar:
    c = Bar()
    c.add_xaxis(CLOTHES).add_yaxis(
        "series0", gen_random_data(len(CLOTHES))
    ).add_yaxis("series1", gen_random_data(len(CLOTHES)))
    return c


def bar_title() -> Bar:
    c = bar_base()
    c.set_global_opts(title_opts=opts.TitleOpts(title="我是主标题", subtitle="我是副标题"))
    c.add_js_funcs("var fn = function() { console.log('hello'); }")
    return c


def bar_reversal_axis() -> Bar:
    c = bar_title()
    c.reversal_axis()
    return c


def bar_datazoom() -> Bar:
    c = bar_title()
    c.set_global_opts(datazoom_opts=opts.DataZoomOpts())
    return c


bar_datazoom().render()
# make_snapshot(bar_reversal_axis().render(), "bar_reversal.png")
# make_snapshot(bar_base().render(), "bar_base.png")
# make_snapshot(bar_title().render(), "bar_title.png")
