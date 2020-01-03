import random

from pyecharts import options as opts
from pyecharts.charts import HeatMap, Page
from pyecharts.faker import Collector, Faker

C = Collector()


@C.funcs
def heatmap_base() -> HeatMap:
    value = [[i, j, random.randint(0, 50)] for i in range(24) for j in range(7)]
    c = (
        HeatMap()
        .add_xaxis(Faker.clock)
        .add_yaxis("series0", Faker.week, value)
        .set_global_opts(
            title_opts=opts.TitleOpts(title="HeatMap-基本示例"),
            visualmap_opts=opts.VisualMapOpts(),
        )
    )
    return c


@C.funcs
def heatmap_with_label_show() -> HeatMap:
    value = [[i, j, random.randint(0, 50)] for i in range(24) for j in range(7)]
    c = (
        HeatMap()
        .add_xaxis(Faker.clock)
        .add_yaxis(
            "series0",
            Faker.week,
            value,
            label_opts=opts.LabelOpts(is_show=True, position="inside"),
        )
        .set_global_opts(
            title_opts=opts.TitleOpts(title="HeatMap-Label 显示"),
            visualmap_opts=opts.VisualMapOpts(),
        )
    )
    return c


Page().add(*[fn() for fn, _ in C.charts]).render()
