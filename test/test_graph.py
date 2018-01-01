#!/usr/bin/env python
# coding=utf-8
from __future__ import unicode_literals

import os
import json
import codecs
from pyecharts import Graph


nodes = [
    {"name": "结点1", "symbolSize": 10},
    {"name": "结点2", "symbolSize": 20},
    {"name": "结点3", "symbolSize": 30},
    {"name": "结点4", "symbolSize": 40},
    {"name": "结点5", "symbolSize": 50},
    {"name": "结点6", "symbolSize": 40},
    {"name": "结点7", "symbolSize": 30},
    {"name": "结点8", "symbolSize": 20}]


def test_graph_force_layout():
    links = []
    for i in nodes:
        for j in nodes:
            links.append({"source": i.get('name'), "target": j.get('name')})
    graph = Graph("关系图-力引导布局示例")
    graph.add("", nodes, links, repulsion=8000, line_color='#aaa')
    graph.render()


def test_graph_circular_layout():
    links = []
    for i in nodes:
        for j in nodes:
            links.append({"source": i.get('name'), "target": j.get('name')})
    graph = Graph("关系图-环形布局示例")
    graph.add("", nodes, links, is_label_show=True, graph_repulsion=8000,
              graph_layout='circular', label_text_color=None)
    graph.render()


def test_graph_official_data():
    with codecs.open(os.path.join("fixtures", "weibo.json"), "r",
                     encoding='utf-8') as f:
        j = json.load(f)
    nodes, links, categories, cont, mid, _ = j
    graph = Graph("微博转发关系图", width=1200, height=600)
    graph.add("", nodes, links, categories, label_pos="right",
              graph_repulsion=50, is_legend_show=False,
              line_curve=0.2, label_text_color=None)
    graph.render()
