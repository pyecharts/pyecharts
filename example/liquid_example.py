# coding=utf-8
from pyecharts import options as opts
from pyecharts.charts import Page, Liquid
from pyecharts.consts import SymbolType


charts = []


def collect_charts(fn):
    charts.append((fn, fn.__name__))
    return fn


@collect_charts
def liquid_base() -> Liquid:
    c = (
        Liquid()
        .add("lq", [0.6, 0.7])
        .set_global_opts(title_opts=opts.TitleOpts(title="Liquid-基本示例"))
    )
    return c


@collect_charts
def liquid_without_outline() -> Liquid:
    c = (
        Liquid()
        .add("lq", [0.6, 0.7, 0.8], is_outline_show=False)
        .set_global_opts(title_opts=opts.TitleOpts(title="Liquid-无边框"))
    )
    return c


@collect_charts
def liquid_shape_diamond() -> Liquid:
    c = (
        Liquid()
        .add("lq", [0.4, 0.7], is_outline_show=False, shape=SymbolType.DIAMOND)
        .set_global_opts(title_opts=opts.TitleOpts(title="Liquid-Shape-diamond"))
    )
    return c


@collect_charts
def liquid_shape_diamond() -> Liquid:
    c = (
        Liquid()
        .add("lq", [0.3, 0.7], is_outline_show=False, shape=SymbolType.ARROW)
        .set_global_opts(title_opts=opts.TitleOpts(title="Liquid-Shape-arrow"))
    )
    return c


@collect_charts
def liquid_shape_diamond() -> Liquid:
    c = (
        Liquid()
        .add("lq", [0.3, 0.7], is_outline_show=False, shape=SymbolType.RECT)
        .set_global_opts(title_opts=opts.TitleOpts(title="Liquid-Shape-rect"))
    )
    return c


Page().add(*[fn() for fn, _ in charts]).render()
