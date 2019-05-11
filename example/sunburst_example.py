import json
import os

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
                opts.SunburstItem(
                    name="Uncle Leo",
                    value=15,
                    children=[
                        opts.SunburstItem(name="Cousin Jack", value=2),
                        opts.SunburstItem(
                            name="Cousin Mary",
                            value=5,
                            children=[opts.SunburstItem(name="Jackson", value=2)],
                        ),
                        opts.SunburstItem(name="Cousin Ben", value=4),
                    ],
                ),
                opts.SunburstItem(
                    name="Father",
                    value=10,
                    children=[
                        opts.SunburstItem(name="Me", value=5),
                        opts.SunburstItem(name="Brother Peter", value=1),
                    ],
                ),
            ],
        ),
        opts.SunburstItem(
            name="Nancy",
            children=[
                opts.SunburstItem(
                    name="Uncle Nike",
                    children=[
                        opts.SunburstItem(name="Cousin Betty", value=1),
                        opts.SunburstItem(name="Cousin Jenny", value=2),
                    ],
                )
            ],
        ),
    ]

    c = (
        Sunburst(init_opts=opts.InitOpts(width="1000px", height="600px"))
        .add(series_name="", data_pair=data, radius=[0, "90%"])
        .set_global_opts(title_opts=opts.TitleOpts(title="Sunburst-基本示例"))
        .set_series_opts(label_opts=opts.LabelOpts(formatter="{b}"))
    )
    return c


@C.funcs
def sunburst_official() -> Sunburst:
    with open(os.path.join("fixtures", "drink.json"), "r", encoding="utf-8") as f:
        j = json.load(f)

    c = (
        Sunburst(init_opts=opts.InitOpts(width="1000px", height="600px"))
        .add(
            "",
            data_pair=j,
            highlight_policy="ancestor",
            radius=[0, "95%"],
            sort_="null",
            levels=[
                {},
                {
                    "r0": "15%",
                    "r": "35%",
                    "itemStyle": {"borderWidth": 2},
                    "label": {"rotate": "tangential"},
                },
                {"r0": "35%", "r": "70%", "label": {"align": "right"}},
                {
                    "r0": "70%",
                    "r": "72%",
                    "label": {"position": "outside", "padding": 3, "silent": False},
                    "itemStyle": {"borderWidth": 3},
                },
            ],
        )
        .set_global_opts(title_opts=opts.TitleOpts(title="Sunburst-官方示例"))
        .set_series_opts(label_opts=opts.LabelOpts(formatter="{b}"))
    )
    return c


Page().add(*[fn() for fn, _ in C.charts]).render()
