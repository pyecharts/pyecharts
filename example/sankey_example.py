import json
import os

from pyecharts import options as opts
from pyecharts.charts import Page, Sankey
from pyecharts.faker import Collector

C = Collector()


@C.funcs
def sankey_base() -> Sankey:
    nodes = [
        {"name": "category1"},
        {"name": "category2"},
        {"name": "category3"},
        {"name": "category4"},
        {"name": "category5"},
        {"name": "category6"},
    ]

    links = [
        {"source": "category1", "target": "category2", "value": 10},
        {"source": "category2", "target": "category3", "value": 15},
        {"source": "category3", "target": "category4", "value": 20},
        {"source": "category5", "target": "category6", "value": 25},
    ]
    c = (
        Sankey()
        .add(
            "sankey",
            nodes,
            links,
            linestyle_opt=opts.LineStyleOpts(opacity=0.2, curve=0.5, color="source"),
            label_opts=opts.LabelOpts(position="right"),
        )
        .set_global_opts(title_opts=opts.TitleOpts(title="Sankey-基本示例"))
    )
    return c


@C.funcs
def sankey_offical() -> Sankey:
    with open(os.path.join("fixtures", "energy.json"), "r", encoding="utf-8") as f:
        j = json.load(f)
    c = (
        Sankey()
        .add(
            "sankey",
            nodes=j["nodes"],
            links=j["links"],
            linestyle_opt=opts.LineStyleOpts(opacity=0.2, curve=0.5, color="source"),
            label_opts=opts.LabelOpts(position="right"),
        )
        .set_global_opts(title_opts=opts.TitleOpts(title="Sankey-官方示例"))
    )
    return c


@C.funcs
def sankey_vertical() -> Sankey:
    colors = [
        "#67001f",
        "#b2182b",
        "#d6604d",
        "#f4a582",
        "#fddbc7",
        "#d1e5f0",
        "#92c5de",
        "#4393c3",
        "#2166ac",
        "#053061",
    ]
    nodes = [
        {"name": "a"},
        {"name": "b"},
        {"name": "a1"},
        {"name": "b1"},
        {"name": "c"},
        {"name": "e"},
    ]
    links = [
        {"source": "a", "target": "a1", "value": 5},
        {"source": "e", "target": "b", "value": 3},
        {"source": "a", "target": "b1", "value": 3},
        {"source": "b1", "target": "a1", "value": 1},
        {"source": "b1", "target": "c", "value": 2},
        {"source": "b", "target": "c", "value": 1},
    ]
    c = (
        Sankey()
        .set_colors(colors)
        .add(
            "sankey",
            nodes=nodes,
            links=links,
            pos_bottom="10%",
            focus_node_adjacency="allEdges",
            orient="vertical",
            linestyle_opt=opts.LineStyleOpts(opacity=0.2, curve=0.5, color="source"),
            label_opts=opts.LabelOpts(position="top"),
        )
        .set_global_opts(
            title_opts=opts.TitleOpts(title="Sankey-Vertical"),
            tooltip_opts=opts.TooltipOpts(trigger="item", trigger_on="mousemove"),
        )
    )
    return c


@C.funcs
def sankey_with_level_setting() -> Sankey:
    with open(os.path.join("fixtures", "product.json"), "r", encoding="utf-8") as f:
        j = json.load(f)
    c = (
        Sankey()
        .add(
            "sankey",
            nodes=j["nodes"],
            links=j["links"],
            pos_top="10%",
            focus_node_adjacency=True,
            levels=[
                opts.SankeyLevelsOpts(
                    depth=0,
                    itemstyle_opts=opts.ItemStyleOpts(color="#fbb4ae"),
                    linestyle_opts=opts.LineStyleOpts(color="source", opacity=0.6),
                ),
                opts.SankeyLevelsOpts(
                    depth=1,
                    itemstyle_opts=opts.ItemStyleOpts(color="#b3cde3"),
                    linestyle_opts=opts.LineStyleOpts(color="source", opacity=0.6),
                ),
                opts.SankeyLevelsOpts(
                    depth=2,
                    itemstyle_opts=opts.ItemStyleOpts(color="#ccebc5"),
                    linestyle_opts=opts.LineStyleOpts(color="source", opacity=0.6),
                ),
                opts.SankeyLevelsOpts(
                    depth=3,
                    itemstyle_opts=opts.ItemStyleOpts(color="#decbe4"),
                    linestyle_opts=opts.LineStyleOpts(color="source", opacity=0.6),
                ),
            ],
            linestyle_opt=opts.LineStyleOpts(curve=0.5),
        )
        .set_global_opts(
            title_opts=opts.TitleOpts(title="Sankey-Level Settings"),
            tooltip_opts=opts.TooltipOpts(trigger="item", trigger_on="mousemove"),
        )
    )
    return c


Page().add(*[fn() for fn, _ in C.charts]).render()
