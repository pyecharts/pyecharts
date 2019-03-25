# coding=utf-8
import pyecharts.options as opts
from example.commons import Collector, Faker
from pyecharts.charts import Line, Page

C = Collector()


@C.funcs
def line_base() -> Line:
    c = (
        Line()
        .add_xaxis(Faker.choose())
        .add_yaxis("商家A", Faker.values())
        .add_yaxis("商家B", Faker.values())
        .set_global_opts(title_opts=opts.TitleOpts(title="Line-基本示例"))
    )
    return c


@C.funcs
def line_smooth() -> Line:
    c = (
        Line()
        .add_xaxis(Faker.choose())
        .add_yaxis("商家A", Faker.values(), is_smooth=True)
        .add_yaxis("商家B", Faker.values(), is_smooth=True)
        .set_global_opts(title_opts=opts.TitleOpts(title="Line-smooth"))
    )
    return c


@C.funcs
def line_markpoint() -> Line:
    c = (
        Line()
        .add_xaxis(Faker.choose())
        .add_yaxis(
            "商家A",
            Faker.values(),
            markpoint_opts=opts.MarkPointOpts(data=[opts.MarkPointItem(type_="min")]),
        )
        .add_yaxis(
            "商家B",
            Faker.values(),
            markpoint_opts=opts.MarkPointOpts(data=[opts.MarkPointItem(type_="max")]),
        )
        .set_global_opts(title_opts=opts.TitleOpts(title="Line-MarkPoint"))
    )
    return c


@C.funcs
def line_markline() -> Line:
    c = (
        Line()
        .add_xaxis(Faker.choose())
        .add_yaxis(
            "商家A",
            Faker.values(),
            markline_opts=opts.MarkLineOpts(data=[opts.MarkLineItem(type_="average")]),
        )
        .add_yaxis(
            "商家B",
            Faker.values(),
            markline_opts=opts.MarkLineOpts(data=[opts.MarkLineItem(type_="average")]),
        )
        .set_global_opts(title_opts=opts.TitleOpts(title="Line-MarkLine"))
    )
    return c


@C.funcs
def line_step() -> Line:
    c = (
        Line()
        .add_xaxis(Faker.choose())
        .add_yaxis("商家A", Faker.values(), is_step=True)
        .set_global_opts(title_opts=opts.TitleOpts(title="Line-阶梯图"))
    )
    return c


Page().add(*[fn() for fn, _ in C.charts]).render()
