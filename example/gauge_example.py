from pyecharts import options as opts
from pyecharts.charts import Gauge, Page
from pyecharts.faker import Collector

C = Collector()


@C.funcs
def gauge_base() -> Gauge:
    c = (
        Gauge()
        .add("", [("完成率", 66.6)])
        .set_global_opts(title_opts=opts.TitleOpts(title="Gauge-基本示例"))
    )
    return c


@C.funcs
def gauge_color() -> Gauge:
    c = (
        Gauge()
        .add(
            "业务指标",
            [("完成率", 55.5)],
            axisline_opts=opts.AxisLineOpts(
                linestyle_opts=opts.LineStyleOpts(
                    color=[(0.3, "#67e0e3"), (0.7, "#37a2da"), (1, "#fd666d")], width=30
                )
            ),
        )
        .set_global_opts(
            title_opts=opts.TitleOpts(title="Gauge-不同颜色"),
            legend_opts=opts.LegendOpts(is_show=False),
        )
    )
    return c


@C.funcs
def gauge_splitnum_label() -> Gauge:
    c = (
        Gauge()
        .add(
            "业务指标",
            [("完成率", 55.5)],
            split_number=5,
            axisline_opts=opts.AxisLineOpts(
                linestyle_opts=opts.LineStyleOpts(
                    color=[(0.3, "#67e0e3"), (0.7, "#37a2da"), (1, "#fd666d")], width=30
                )
            ),
            detail_label_opts=opts.LabelOpts(formatter="{value}"),
        )
        .set_global_opts(
            title_opts=opts.TitleOpts(title="Gauge-分割段数-Label"),
            legend_opts=opts.LegendOpts(is_show=False),
        )
    )
    return c


@C.funcs
def gauge_label_title_setting() -> Gauge:
    c = (
        Gauge()
        .add(
            "",
            [("完成率", 66.6)],
            title_label_opts=opts.LabelOpts(
                font_size=40, color="blue", font_family="Microsoft YaHei"
            ),
        )
        .set_global_opts(title_opts=opts.TitleOpts(title="Gauge-改变轮盘内的字体"))
    )
    return c


@C.funcs
def gauge_change_radius() -> Gauge:
    c = (
        Gauge()
        .add("", [("完成率", 66.6)], radius="50%")
        .set_global_opts(title_opts=opts.TitleOpts(title="Gauge-修改 Radius 为 50%"))
    )
    return c


Page().add(*[fn() for fn, _ in C.charts]).render()
