# coding=utf-8
import random

from example.commons import Collector, Faker
from pyecharts import options as opts
from pyecharts.charts import Page, Scatter3D

C = Collector()


@C.funcs
def scatter3d_base() -> Scatter3D:
    data = [
        [random.randint(0, 100), random.randint(0, 100), random.randint(0, 100)]
        for _ in range(80)
    ]
    c = (
        Scatter3D()
        .add("", data)
        .set_global_opts(
            title_opts=opts.TitleOpts("Scatter3D-基本示例"),
            visualmap_opts=opts.VisualMapOpts(range_color=Faker.visual_color),
        )
    )
    return c


Page().add(*[fn() for fn, _ in C.charts]).render()
