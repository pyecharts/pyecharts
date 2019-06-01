from example.commons import Collector, Faker
from pyecharts import options as opts
from pyecharts.charts import Page, Scatter
from pyecharts.commons.utils import JsCode

C = Collector()


@C.funcs
def scatter_base() -> Scatter:
    c = (
        Scatter()
        .add_xaxis(Faker.choose())
        .add_yaxis("商家A", Faker.values())
        .set_global_opts(title_opts=opts.TitleOpts(title="Scatter-基本示例"))
    )
    return c


@C.funcs
def scatter_spliteline() -> Scatter:
    c = (
        Scatter()
        .add_xaxis(Faker.choose())
        .add_yaxis("商家A", Faker.values())
        .set_global_opts(
            title_opts=opts.TitleOpts(title="Scatter-显示分割线"),
            xaxis_opts=opts.AxisOpts(splitline_opts=opts.SplitLineOpts(is_show=True)),
            yaxis_opts=opts.AxisOpts(splitline_opts=opts.SplitLineOpts(is_show=True)),
        )
    )
    return c


@C.funcs
def scatter_visualmap_color() -> Scatter:
    c = (
        Scatter()
        .add_xaxis(Faker.choose())
        .add_yaxis("商家A", Faker.values())
        .set_global_opts(
            title_opts=opts.TitleOpts(title="Scatter-VisualMap(Color)"),
            visualmap_opts=opts.VisualMapOpts(max_=150),
        )
    )
    return c


@C.funcs
def scatter_visualmap_size() -> Scatter:
    c = (
        Scatter()
        .add_xaxis(Faker.choose())
        .add_yaxis("商家A", Faker.values())
        .add_yaxis("商家B", Faker.values())
        .set_global_opts(
            title_opts=opts.TitleOpts(title="Scatter-VisualMap(Size)"),
            visualmap_opts=opts.VisualMapOpts(type_="size", max_=150, min_=20),
        )
    )
    return c


@C.funcs
def scatter_muti_dimension_data() -> Scatter:
    c = (
        Scatter()
        .add_xaxis(Faker.choose())
        .add_yaxis(
            "商家A",
            [list(z) for z in zip(Faker.values(), Faker.choose())],
            label_opts=opts.LabelOpts(
                formatter=JsCode(
                    "function(params){return params.value[1] +' : '+ params.value[2];}"
                )
            ),
        )
        .set_global_opts(
            title_opts=opts.TitleOpts(title="Scatter-多维度数据"),
            tooltip_opts=opts.TooltipOpts(
                formatter=JsCode(
                    "function (params) {return params.name + ' : ' + params.value[2];}"
                )
            ),
            visualmap_opts=opts.VisualMapOpts(
                type_="color", max_=150, min_=20, dimension=1
            ),
        )
    )
    return c


Page().add(*[fn() for fn, _ in C.charts]).render()
