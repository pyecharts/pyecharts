# coding=utf-8
from pyecharts import options as opts
from pyecharts.charts import Boxplot, Page

from example.commons import Faker

charts = []


def collect_charts(fn):
    charts.append((fn, fn.__name__))
    return fn
