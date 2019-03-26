# coding=utf-8
import json
import os

from example.commons import Collector
from pyecharts import options as opts
from pyecharts.charts import Page, Tree

C = Collector()


@C.funcs
def tree_base() -> Tree:
    data = [
        {
            "children": [
                {"name": "B"},
                {
                    "children": [
                        {"children": [{"name": "I"}], "name": "E"},
                        {"name": "F"},
                    ],
                    "name": "C",
                },
                {
                    "children": [
                        {"children": [{"name": "J"}, {"name": "K"}], "name": "G"},
                        {"name": "H"},
                    ],
                    "name": "D",
                },
            ],
            "name": "A",
        }
    ]
    c = (
        Tree()
        .add("", data)
        .set_global_opts(title_opts=opts.TitleOpts(title="Tree-基本示例"))
    )
    return c


@C.funcs
def tree_official() -> Tree:
    with open(os.path.join("fixtures", "flare.json"), "r", encoding="utf-8") as f:
        j = json.load(f)
    c = (
        Tree()
        .add("", [j], collapse_interval=2)
        .set_global_opts(title_opts=opts.TitleOpts(title="Tree-官方示例"))
    )
    return c


Page().add(*[fn() for fn, _ in C.charts]).render()
