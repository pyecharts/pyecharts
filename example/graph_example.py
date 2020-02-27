import json
import os

from pyecharts.commons.utils import JsCode

from pyecharts import options as opts
from pyecharts.charts import Graph, Page
from pyecharts.faker import Collector

C = Collector()


@C.funcs
def graph_base() -> Graph:
    nodes = [
        {"name": "结点1", "symbolSize": 10},
        {"name": "结点2", "symbolSize": 20},
        {"name": "结点3", "symbolSize": 30},
        {"name": "结点4", "symbolSize": 40},
        {"name": "结点5", "symbolSize": 50},
        {"name": "结点6", "symbolSize": 40},
        {"name": "结点7", "symbolSize": 30},
        {"name": "结点8", "symbolSize": 20},
    ]
    links = []
    for i in nodes:
        for j in nodes:
            links.append({"source": i.get("name"), "target": j.get("name")})
    c = (
        Graph()
        .add("", nodes, links, repulsion=8000)
        .set_global_opts(title_opts=opts.TitleOpts(title="Graph-基本示例"))
    )
    return c


@C.funcs
def graph_with_opts() -> Graph:
    nodes = [
        opts.GraphNode(name="结点1", symbol_size=10),
        opts.GraphNode(name="结点2", symbol_size=20),
        opts.GraphNode(name="结点3", symbol_size=30),
        opts.GraphNode(name="结点4", symbol_size=40),
        opts.GraphNode(name="结点5", symbol_size=50),
    ]
    links = [
        opts.GraphLink(source="结点1", target="结点2"),
        opts.GraphLink(source="结点2", target="结点3"),
        opts.GraphLink(source="结点3", target="结点4"),
        opts.GraphLink(source="结点4", target="结点5"),
        opts.GraphLink(source="结点5", target="结点1"),
    ]
    c = (
        Graph()
        .add("", nodes, links, repulsion=4000)
        .set_global_opts(title_opts=opts.TitleOpts(title="Graph-GraphNode-GraphLink"))
    )
    return c


@C.funcs
def graph_with_edge_opts() -> Graph:
    nodes_data = [
        opts.GraphNode(name="结点1", symbol_size=10),
        opts.GraphNode(name="结点2", symbol_size=20),
        opts.GraphNode(name="结点3", symbol_size=30),
        opts.GraphNode(name="结点4", symbol_size=40),
        opts.GraphNode(name="结点5", symbol_size=50),
        opts.GraphNode(name="结点6", symbol_size=60),
    ]
    links_data = [
        opts.GraphLink(source="结点1", target="结点2", value=2),
        opts.GraphLink(source="结点2", target="结点3", value=3),
        opts.GraphLink(source="结点3", target="结点4", value=4),
        opts.GraphLink(source="结点4", target="结点5", value=5),
        opts.GraphLink(source="结点5", target="结点6", value=6),
        opts.GraphLink(source="结点6", target="结点1", value=7),
    ]
    c = (
        Graph()
        .add(
            "",
            nodes_data,
            links_data,
            repulsion=4000,
            edge_label=opts.LabelOpts(
                is_show=True, position="middle", formatter="{b} 的数据 {c}"
            ),
        )
        .set_global_opts(
            title_opts=opts.TitleOpts(title="Graph-GraphNode-GraphLink-WithEdgeLabel")
        )
    )
    return c


@C.funcs
def graph_weibo() -> Graph:
    with open(os.path.join("fixtures", "weibo.json"), "r", encoding="utf-8") as f:
        j = json.load(f)
        nodes, links, categories, cont, mid, userl = j
    c = (
        Graph()
        .add(
            "",
            nodes,
            links,
            categories,
            repulsion=50,
            linestyle_opts=opts.LineStyleOpts(curve=0.2),
            label_opts=opts.LabelOpts(is_show=False),
        )
        .set_global_opts(
            legend_opts=opts.LegendOpts(is_show=False),
            title_opts=opts.TitleOpts(title="Graph-微博转发关系图"),
        )
    )
    return c


@C.funcs
def graph_les_miserables():
    with open(
        os.path.join("fixtures", "les-miserables.json"), "r", encoding="utf-8"
    ) as f:
        j = json.load(f)
        nodes = j["nodes"]
        links = j["links"]
        categories = j["categories"]

    c = (
        Graph(init_opts=opts.InitOpts(width="1000px", height="600px"))
        .add(
            "",
            nodes=nodes,
            links=links,
            categories=categories,
            layout="circular",
            is_rotate_label=True,
            linestyle_opts=opts.LineStyleOpts(color="source", curve=0.3),
            label_opts=opts.LabelOpts(position="right"),
        )
        .set_global_opts(
            title_opts=opts.TitleOpts(title="Graph-Les Miserables"),
            legend_opts=opts.LegendOpts(
                orient="vertical", pos_left="2%", pos_top="20%"
            ),
        )
    )
    return c


@C.funcs
def graph_npm_dependencies() -> Graph:
    with open(os.path.join("fixtures", "npmdepgraph.json"), "r", encoding="utf-8") as f:
        j = json.load(f)
    nodes = [
        {
            "x": node["x"],
            "y": node["y"],
            "id": node["id"],
            "name": node["label"],
            "symbolSize": node["size"],
            "itemStyle": {"normal": {"color": node["color"]}},
        }
        for node in j["nodes"]
    ]

    edges = [
        {"source": edge["sourceID"], "target": edge["targetID"]} for edge in j["edges"]
    ]

    c = (
        Graph(init_opts=opts.InitOpts(width="1000px", height="600px"))
        .add(
            "",
            nodes=nodes,
            links=edges,
            layout="none",
            label_opts=opts.LabelOpts(is_show=False),
            linestyle_opts=opts.LineStyleOpts(width=0.5, curve=0.3, opacity=0.7),
        )
        .set_global_opts(title_opts=opts.TitleOpts(title="Graph-NPM Dependencies"))
    )
    return c


Page().add(*[fn() for fn, _ in C.charts]).render()
