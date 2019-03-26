# coding=utf-8
import random

from example.commons import Collector, Faker
from pyecharts import options as opts
from pyecharts.charts import Page, Polar

C = Collector()


@C.funcs
def polar_scatter0() -> Polar:
    data = [(i, random.randint(1, 100)) for i in range(101)]
    c = (
        Polar()
        .add("", data, type_="scatter", label_opts=opts.LabelOpts(is_show=False))
        .set_global_opts(title_opts=opts.TitleOpts(title="Polar-Scatter0"))
    )
    return c


@C.funcs
def polar_scatter1() -> Polar:
    c = (
        Polar()
        .add("", [(10, random.randint(1, 100)) for i in range(300)], type_="scatter")
        .add("", [(11, random.randint(1, 100)) for i in range(300)], type_="scatter")
        .set_series_opts(label_opts=opts.LabelOpts(is_show=False))
        .set_global_opts(title_opts=opts.TitleOpts(title="Polar-Scatter1"))
    )

    return c


@C.funcs
def polar_effectscatter() -> Polar:
    data = [(i, random.randint(1, 100)) for i in range(10)]
    c = (
        Polar()
        .add(
            "",
            data,
            type_="effectScatter",
            effect_opts=opts.EffectOpts(scale=10, period=5),
            label_opts=opts.LabelOpts(is_show=False),
        )
        .set_global_opts(title_opts=opts.TitleOpts(title="Polar-EffectScatter"))
    )
    return c


@C.funcs
def polar_radiusaxis():
    c = (
        Polar()
        .add_schema(
            radiusaxis_opts=opts.RadiusAxisOpts(data=Faker.week, type_="category")
        )
        .add("A", [1, 2, 3, 4, 3, 5, 1], type_="bar", stack="stack0")
        .add("B", [2, 4, 6, 1, 2, 3, 1], type_="bar", stack="stack0")
        .add("C", [1, 2, 3, 4, 1, 2, 5], type_="bar", stack="stack0")
        .set_global_opts(title_opts=opts.TitleOpts(title="Polar-RadiusAxis"))
    )
    return c


@C.funcs
def polar_angleaxis():
    c = (
        Polar()
        .add_schema(
            angleaxis_opts=opts.AngleAxisOpts(data=Faker.week, type_="category")
        )
        .add("A", [1, 2, 3, 4, 3, 5, 1], type_="bar", stack="stack0")
        .add("B", [2, 4, 6, 1, 2, 3, 1], type_="bar", stack="stack0")
        .add("C", [1, 2, 3, 4, 1, 2, 5], type_="bar", stack="stack0")
        .set_global_opts(title_opts=opts.TitleOpts(title="Polar-AngleAxis"))
    )
    return c


Page().add(*[fn() for fn, _ in C.charts]).render()
