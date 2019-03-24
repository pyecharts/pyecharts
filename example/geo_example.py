# coding=utf-8
from pyecharts import options as opts
from pyecharts.charts import Geo
from example.commons import Faker


def geo_base():
    c = (
        Geo()
        .add("geo", [list(z) for z in zip(Faker.provinces, Faker.values())])
        .set_global_opts(visualmap_opts=opts.VisualMapOpts())
        .set_series_opts(label_opts=opts.LabelOpts(is_show=False))
    )
    return c
