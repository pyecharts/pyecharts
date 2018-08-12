# coding=utf-8
from __future__ import unicode_literals

import os
import json
import codecs

from pyecharts import Tree


def test_tree_default():
    data = [
        {
            "children": [
                {"children": [], "name": "B"},
                {
                    "children": [
                        {
                            "children": [{"children": [], "name": "I"}],
                            "name": "E",
                        },
                        {"children": [], "name": "F"},
                    ],
                    "name": "C",
                },
                {
                    "children": [
                        {
                            "children": [
                                {"children": [], "name": "J"},
                                {"children": [], "name": "K"},
                            ],
                            "name": "G",
                        },
                        {"children": [], "name": "H"},
                    ],
                    "name": "D",
                },
            ],
            "name": "A",
        }
    ]
    tree = Tree("树图示例")
    tree.add("", data)
    tree.render()


def test_tree_official_data():
    with codecs.open(
        os.path.join("fixtures", "flare.json"), "r", encoding="utf-8"
    ) as f:
        j = json.load(f)

    tree = Tree(width=1200, height=800)
    data = tree.collapse_interval([j], interval=2)
    tree.add("", data, tree_orient="RL")
    tree.render()


test_tree_default()
