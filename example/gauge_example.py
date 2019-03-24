# coding=utf-8
from pyecharts import options as opts
from pyecharts.charts import Gauge, Page

from example.commons import Faker

charts = []


def collect_charts(fn):
    charts.append((fn, fn.__name__))
    return fn


@collect_charts
def gauge_base() -> Gauge:
    c = (
        Gauge()
        .add("", [("完成率", 66.6)])
        .set_global_opts(title_opts=opts.TitleOpts(title="Gauge-基本示例"))
    )
    return c


Page().add(*[fn() for fn, _ in charts]).render()
