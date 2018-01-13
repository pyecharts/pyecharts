#!/usr/bin/env python
# coding=utf-8
from __future__ import unicode_literals
import sys
import os
import codecs
import json
from pyecharts import Sankey

PY2 = sys.version_info[0] == 2


def test_sankey_default():
    nodes = [
        {'name': 'category1'}, {'name': 'category2'}, {'name': 'category3'},
        {'name': 'category4'}, {'name': 'category5'}, {'name': 'category6'},
    ]

    links = [
        {'source': 'category1', 'target': 'category2', 'value': 10},
        {'source': 'category2', 'target': 'category3', 'value': 15},
        {'source': 'category3', 'target': 'category4', 'value': 20},
        {'source': 'category5', 'target': 'category6', 'value': 25}
    ]
    sankey = Sankey("桑基图示例", width=1200, height=600)
    sankey.add("sankey", nodes, links, line_opacity=0.2,
               line_curve=0.5, line_color='source', is_label_show=True,
               label_pos='right')
    sankey.render()

    with codecs.open(os.path.join("fixtures", "energy.json"), "r",
                     encoding='utf-8') as f:
        j = json.load(f)
    sankey = Sankey("桑基图示例", width=1200, height=600)
    sankey.add("sankey", nodes=j['nodes'], links=j['links'], line_opacity=0.2,
               line_curve=0.5, line_color='source',
               is_label_show=True, label_pos='right')
    sankey.render()
