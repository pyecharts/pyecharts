# coding=utf-8
from __future__ import unicode_literals

import sys

from pyecharts import TreeMap

PY2 = sys.version_info[0] == 2

data = [
    {
        "value": 40,
        "name": "我是A",
    },
    {
        "value": 180,
        "name": "我是B",
        "children": [
            {
                "value": 76,
                "name": "我是B.children",
                "children": [
                    {
                        "value": 12,
                        "name": "我是B.children.a",
                    },
                    {
                        "value": 28,
                        "name": "我是B.children.b",
                    },
                    {
                        "value": 20,
                        "name": "我是B.children.c",
                    },
                    {
                        "value": 16,
                        "name": "我是B.children.d",
                    }]
            }]}
]


def test_treemap_default():
    treemap = TreeMap("树图-默认示例", width=1200, height=600)
    treemap.add("演示数据", data, is_label_show=True, label_pos='inside')
    treemap.render()


def test_treemap_drilldown():
    treemap = TreeMap("树图-下钻示例", width=1200, height=600)
    treemap.add("演示数据", data, is_label_show=True, label_pos='inside',
                treemap_left_depth=1)
    treemap.render()


def test_treemap_offcical_data():
    treemap = TreeMap("树图-官方数据", width=1200, height=600)
    import os
    import json
    import codecs
    test_fixture = os.path.join("fixtures", "treemap.json")
    with codecs.open(test_fixture, "r", encoding='utf-8') as f:
        data = json.load(f)
    treemap.add("演示数据", data, is_label_show=True, label_pos='inside')
    treemap.render()
