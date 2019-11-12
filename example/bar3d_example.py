import random

from pyecharts import options as opts
from pyecharts.charts import Bar3D, Page
from pyecharts.faker import Collector, Faker

C = Collector()


def generate_data():
    data = []
    for j in range(10):
        for k in range(10):
            value = random.randint(0, 9)
            data.append([j, k, value * 2 + 4])
    return data


@C.funcs
def bar3d_base() -> Bar3D:
    data = [(i, j, random.randint(0, 12)) for i in range(6) for j in range(24)]
    c = (
        Bar3D()
        .add(
            "",
            [[d[1], d[0], d[2]] for d in data],
            xaxis3d_opts=opts.Axis3DOpts(Faker.clock, type_="category"),
            yaxis3d_opts=opts.Axis3DOpts(Faker.week_en, type_="category"),
            zaxis3d_opts=opts.Axis3DOpts(type_="value"),
        )
        .set_global_opts(
            visualmap_opts=opts.VisualMapOpts(max_=20),
            title_opts=opts.TitleOpts(title="Bar3D-基本示例"),
        )
    )
    return c


@C.funcs
def bar3d_stack() -> Bar3D:
    x_data = y_data = list(range(10))
    bar3d = Bar3D()
    for _ in range(10):
        bar3d.add(
            "",
            generate_data(),
            shading="lambert",
            xaxis3d_opts=opts.Axis3DOpts(data=x_data, type_="value"),
            yaxis3d_opts=opts.Axis3DOpts(data=y_data, type_="value"),
            zaxis3d_opts=opts.Axis3DOpts(type_="value"),
        )
    bar3d.set_global_opts(title_opts=opts.TitleOpts("Bar3D-堆叠柱状图示例"))
    bar3d.set_series_opts(**{"stack": "stack"})
    return bar3d


Page().add(*[fn() for fn, _ in C.charts]).render()
