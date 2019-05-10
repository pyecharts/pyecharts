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
def line_yaxis_log() -> Line:
    c = (
        Line()
        .add_xaxis(xaxis_data=["一", "二", "三", "四", "五", "六", "七", "八", "九"])
        .add_yaxis(
            "2 的指数",
            y_axis=[1, 2, 4, 8, 16, 32, 64, 128, 256],
            linestyle_opts=opts.LineStyleOpts(width=2),
        )
        .add_yaxis(
            "3 的指数",
            y_axis=[1, 3, 9, 27, 81, 247, 741, 2223, 6669],
            linestyle_opts=opts.LineStyleOpts(width=2),
        )
        .set_global_opts(
            title_opts=opts.TitleOpts(title="Line-对数轴示例"),
            xaxis_opts=opts.AxisOpts(name="x"),
            yaxis_opts=opts.AxisOpts(
                type_="log",
                name="y",
                splitline_opts=opts.SplitLineOpts(is_show=True),
                is_scale=True,
            ),
        )
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


@C.funcs
def line_itemstyle() -> Line:
    c = (
        Line()
        .add_xaxis(xaxis_data=Faker.choose())
        .add_yaxis(
            "商家A",
            Faker.values(),
            symbol="triangle",
            symbol_size=20,
            linestyle_opts=opts.LineStyleOpts(color="green", width=4, type_="dashed"),
            itemstyle_opts=opts.ItemStyleOpts(
                border_width=3, border_color="yellow", color="blue"
            ),
        )
        .set_global_opts(title_opts=opts.TitleOpts(title="Line-ItemStyle"))
    )
    return c


Page().add(*[fn() for fn, _ in C.charts]).render()
