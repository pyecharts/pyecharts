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
def tree_lr() -> Tree:
    with open(os.path.join("fixtures", "flare.json"), "r", encoding="utf-8") as f:
        j = json.load(f)
    c = (
        Tree()
        .add("", [j], collapse_interval=2)
        .set_global_opts(title_opts=opts.TitleOpts(title="Tree-左右方向"))
    )
    return c


@C.funcs
def tree_rl() -> Tree:
    with open(os.path.join("fixtures", "flare.json"), "r", encoding="utf-8") as f:
        j = json.load(f)
    c = (
        Tree()
        .add("", [j], collapse_interval=2, orient="RL")
        .set_global_opts(title_opts=opts.TitleOpts(title="Tree-右左方向"))
    )
    return c


@C.funcs
def tree_tb() -> Tree:
    with open(os.path.join("fixtures", "flare.json"), "r", encoding="utf-8") as f:
        j = json.load(f)
    c = (
        Tree()
        .add(
            "",
            [j],
            collapse_interval=2,
            orient="TB",
            label_opts=opts.LabelOpts(
                position="top",
                horizontal_align="right",
                vertical_align="middle",
                rotate=-90,
            ),
        )
        .set_global_opts(title_opts=opts.TitleOpts(title="Tree-上下方向"))
    )
    return c


@C.funcs
def tree_bt() -> Tree:
    with open(os.path.join("fixtures", "flare.json"), "r", encoding="utf-8") as f:
        j = json.load(f)
    c = (
        Tree()
        .add(
            "",
            [j],
            collapse_interval=2,
            orient="BT",
            label_opts=opts.LabelOpts(
                position="top",
                horizontal_align="right",
                vertical_align="middle",
                rotate=-90,
            ),
        )
        .set_global_opts(title_opts=opts.TitleOpts(title="Tree-下上方向"))
    )
    return c


@C.funcs
def tree_layout() -> Tree:
    with open(os.path.join("fixtures", "flare.json"), "r", encoding="utf-8") as f:
        j = json.load(f)
    c = (
        Tree()
        .add("", [j], collapse_interval=2, layout="radial")
        .set_global_opts(title_opts=opts.TitleOpts(title="Tree-Layout"))
    )
    return c


Page().add(*[fn() for fn, _ in C.charts]).render()
