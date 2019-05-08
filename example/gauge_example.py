from example.commons import Collector
from pyecharts import options as opts
from pyecharts.charts import Gauge, Page

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


Page().add(*[fn() for fn, _ in C.charts]).render()
