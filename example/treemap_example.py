import json
import os

from pyecharts import options as opts
from pyecharts.charts import Page, TreeMap
from pyecharts.faker import Collector

C = Collector()


@C.funcs
def treemap_base() -> TreeMap:
    data = [
        {"value": 40, "name": "我是A"},
        {
            "value": 180,
            "name": "我是B",
            "children": [
                {
                    "value": 76,
                    "name": "我是B.children",
                    "children": [
                        {"value": 12, "name": "我是B.children.a"},
                        {"value": 28, "name": "我是B.children.b"},
                        {"value": 20, "name": "我是B.children.c"},
                        {"value": 16, "name": "我是B.children.d"},
                    ],
                }
            ],
        },
    ]

    c = (
        TreeMap()
        .add("演示数据", data)
        .set_global_opts(title_opts=opts.TitleOpts(title="TreeMap-基本示例"))
    )
    return c


@C.funcs
def treemap_official():
    with open(os.path.join("fixtures", "treemap.json"), "r", encoding="utf-8") as f:
        data = json.load(f)
    c = (
        TreeMap()
        .add("演示数据", data)
        .set_global_opts(title_opts=opts.TitleOpts(title="TreeMap-官方示例"))
    )
    return c


@C.funcs
def treemap_levels_example():
    with open(os.path.join("fixtures", "treemap.json"), "r", encoding="utf-8") as f:
        data = json.load(f)
    c = (
        TreeMap()
        .add(
            series_name="演示数据",
            data=data,
            levels=[
                opts.TreeMapLevelsOpts(
                    treemap_itemstyle_opts=opts.TreeMapItemStyleOpts(
                        border_color="#555",
                        border_width=4,
                        gap_width=4,
                    )
                ),
                opts.TreeMapLevelsOpts(
                    color_saturation=[0.3, 0.6],
                    treemap_itemstyle_opts=opts.TreeMapItemStyleOpts(
                        border_color_saturation=0.7,
                        gap_width=2,
                        border_width=2,
                    ),
                ),
                opts.TreeMapLevelsOpts(
                    color_saturation=[0.3, 0.5],
                    treemap_itemstyle_opts=opts.TreeMapItemStyleOpts(
                        border_color_saturation=0.6,
                        gap_width=1,
                    ),
                ),
                opts.TreeMapLevelsOpts(
                    color_saturation=[0.3, 0.5],
                ),
            ]
        )
        .set_global_opts(title_opts=opts.TitleOpts(title="TreeMap-Levels-配置"))
    )
    return c


Page().add(*[fn() for fn, _ in C.charts]).render()
