# coding=utf-8
from example.commons import Collector
from pyecharts import options as opts
from pyecharts.charts import Gauge, Page

C = Collector()


@C.funcs
def gauge_base() -> Gauge:
    c = (
        Gauge()
        .add("", [("完成率", 66.6)])
        .set_global_opts(title_opts=opts.TitleOpts(title="Gauge-基本示例"))
    )
    return c


Page().add(*[fn() for fn, _ in C.charts]).render()
