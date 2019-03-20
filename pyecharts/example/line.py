# coding=utf-8

import pyecharts.options as opts
from pyecharts.charts import Bar, Line
from pyecharts.example.commons import CLOTHES, gen_random_data
from pyecharts.render import make_snapshot


def line_base() -> Line:
    c = Line()
    c.add_xaxis(CLOTHES).add_yaxis(
        "series0", gen_random_data(len(CLOTHES))
    ).add_yaxis("series1", gen_random_data(len(CLOTHES)))
    return c


line_base().render()
