from example.commons import Collector
from pyecharts import options as opts
from pyecharts.charts import Page, Sunburst

C = Collector()


@C.funcs
def sunburst_base() -> Sunburst:
    data = [
        opts.SunburstItem(
            name="Grandpa",
            children=[
                opts.SunburstItem(name="Uncle Leo", value=15, children=[
                    opts.SunburstItem(name="Cousin Jack", value=2),
                    opts.SunburstItem(name="Cousin Mary", value=5, children=[
                        opts.SunburstItem(name="Jackson", value=2),
                    ]),
                    opts.SunburstItem(name="Cousin Ben", value=4),
                ]),
                opts.SunburstItem(name="Father", value=10, children=[
                    opts.SunburstItem(name="Me", value=5),
                    opts.SunburstItem(name="Brother Peter", value=1),
                ]),
            ]),
        opts.SunburstItem(
            name="Nancy",
            children=[
                opts.SunburstItem(name="Uncle Nike", children=[
                    opts.SunburstItem(name="Cousin Betty", value=1),
                    opts.SunburstItem(name="Cousin Jenny", value=2),
                ]),
            ]),
    ]

    c = (
        Sunburst()
        .add(
            series_name="",
            data_pair=data,
            radius=[0, "90%"],
        )
        .set_global_opts(title_opts=opts.TitleOpts(title="Sunburst-基本示例"))
        .set_series_opts(label_opts=opts.LabelOpts(formatter="{b}"))
    )
    return c


Page().add(*[fn() for fn, _ in C.charts]).render()
