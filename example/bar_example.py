# coding=utf-8
from example.commons import Collector, Faker
from pyecharts import options as opts
from pyecharts.charts import Bar, Page

C = Collector()


@C.funcs
def bar_base() -> Bar:
    c = (
        Bar()
        .add_xaxis(Faker.choose())
        .add_yaxis("商家A", Faker.values())
        .add_yaxis("商家B", Faker.values(), is_selected=False)
        .set_global_opts(title_opts=opts.TitleOpts(title="Bar-基本示例", subtitle="我是副标题"))
    )
    return c


@C.funcs
def bar_reversal_axis() -> Bar:
    c = (
        Bar()
        .add_xaxis(Faker.choose())
        .add_yaxis("商家A", Faker.values())
        .add_yaxis("商家B", Faker.values())
        .reversal_axis()
        .set_series_opts(label_opts=opts.LabelOpts(position="right"))
        .set_global_opts(title_opts=opts.TitleOpts(title="Bar-翻转 XY 轴"))
    )
    return c


@C.funcs
def bar_stack0() -> Bar:
    c = (
        Bar()
        .add_xaxis(Faker.choose())
        .add_yaxis("商家A", Faker.values(), stack="stack1")
        .add_yaxis("商家B", Faker.values(), stack="stack1")
        .set_series_opts(label_opts=opts.LabelOpts(is_show=False))
        .set_global_opts(title_opts=opts.TitleOpts(title="Bar-堆叠数据（全部）"))
    )
    return c


@C.funcs
def bar_stack1() -> Bar:
    c = (
        Bar()
        .add_xaxis(Faker.choose())
        .add_yaxis("商家A", Faker.values(), stack="stack1")
        .add_yaxis("商家B", Faker.values(), stack="stack1")
        .add_yaxis("商家C", Faker.values())
        .set_series_opts(label_opts=opts.LabelOpts(is_show=False))
        .set_global_opts(title_opts=opts.TitleOpts(title="Bar-堆叠数据（部分）"))
    )
    return c


@C.funcs
def bar_markpoint_type() -> Bar:
    c = (
        Bar()
        .add_xaxis(Faker.choose())
        .add_yaxis("商家A", Faker.values())
        .add_yaxis("商家B", Faker.values())
        .set_global_opts(title_opts=opts.TitleOpts(title="Bar-MarkPoint（指定类型）"))
        .set_series_opts(
            label_opts=opts.LabelOpts(is_show=False),
            markpoint_opts=opts.MarkPointOpts(
                data=[
                    opts.MarkPointItem(type_="max", name="最大值"),
                    opts.MarkPointItem(type_="min", name="最小值"),
                    opts.MarkPointItem(type_="average", name="平均值"),
                ]
            ),
        )
    )
    return c


@C.funcs
def bar_markpoint_custom() -> Bar:
    x, y = Faker.choose(), Faker.values()
    c = (
        Bar()
        .add_xaxis(x)
        .add_yaxis(
            "商家A",
            y,
            markpoint_opts=opts.MarkPointOpts(
                data=[opts.MarkPointItem(name="自定义标记点", coord=[x[2], y[2]], value=y[2])]
            ),
        )
        .add_yaxis("商家B", Faker.values())
        .set_global_opts(title_opts=opts.TitleOpts(title="Bar-MarkPoint（自定义）"))
        .set_series_opts(label_opts=opts.LabelOpts(is_show=False))
    )
    return c


@C.funcs
def bar_markline_type() -> Bar:
    c = (
        Bar()
        .add_xaxis(Faker.choose())
        .add_yaxis("商家A", Faker.values())
        .add_yaxis("商家B", Faker.values())
        .set_global_opts(title_opts=opts.TitleOpts(title="Bar-MarkLine（指定类型）"))
        .set_series_opts(
            label_opts=opts.LabelOpts(is_show=False),
            markline_opts=opts.MarkLineOpts(
                data=[
                    opts.MarkLineItem(type_="min", name="最小值"),
                    opts.MarkLineItem(type_="max", name="最大值"),
                    opts.MarkLineItem(type_="average", name="平均值"),
                ]
            ),
        )
    )
    return c


@C.funcs
def bar_markline_custom() -> Bar:
    c = (
        Bar()
        .add_xaxis(Faker.choose())
        .add_yaxis("商家A", Faker.values())
        .add_yaxis("商家B", Faker.values())
        .set_global_opts(title_opts=opts.TitleOpts(title="Bar-MarkLine（自定义）"))
        .set_series_opts(
            label_opts=opts.LabelOpts(is_show=False),
            markline_opts=opts.MarkLineOpts(
                data=[opts.MarkLineItem(y=50, name="yAxis=50")]
            ),
        )
    )
    return c


@C.funcs
def bar_datazoom_slider() -> Bar:
    c = (
        Bar()
        .add_xaxis(Faker.days_attrs)
        .add_yaxis("商家A", Faker.days_values)
        .set_global_opts(
            title_opts=opts.TitleOpts(title="Bar-DataZoom（slider-水平）"),
            datazoom_opts=[opts.DataZoomOpts()],
        )
    )
    return c


@C.funcs
def bar_datazoom_slider_vertical() -> Bar:
    c = (
        Bar()
        .add_xaxis(Faker.days_attrs)
        .add_yaxis("商家A", Faker.days_values, color=Faker.rand_color())
        .set_global_opts(
            title_opts=opts.TitleOpts(title="Bar-DataZoom（slider-垂直）"),
            datazoom_opts=[opts.DataZoomOpts(orient="vertical")],
        )
    )
    return c


@C.funcs
def bar_datazoom_inside() -> Bar:
    c = (
        Bar()
        .add_xaxis(Faker.days_attrs)
        .add_yaxis("商家A", Faker.days_values, color=Faker.rand_color())
        .set_global_opts(
            title_opts=opts.TitleOpts(title="Bar-DataZoom（inside）"),
            datazoom_opts=[opts.DataZoomOpts(type_="inside")],
        )
    )
    return c


@C.funcs
def bar_datazoom_both() -> Bar:
    c = (
        Bar()
        .add_xaxis(Faker.days_attrs)
        .add_yaxis("商家A", Faker.days_values, color=Faker.rand_color())
        .set_global_opts(
            title_opts=opts.TitleOpts(title="Bar-DataZoom（slider+inside）"),
            datazoom_opts=[opts.DataZoomOpts(), opts.DataZoomOpts(type_="inside")],
        )
    )
    return c


@C.funcs
def bar_histogram() -> Bar:
    c = (
        Bar()
        .add_xaxis(Faker.choose())
        .add_yaxis("商家A", Faker.values(), category_gap=0, color=Faker.rand_color())
        .set_global_opts(title_opts=opts.TitleOpts(title="Bar-直方图"))
    )
    return c


Page().add(*[fn() for fn, _ in C.charts]).render()
