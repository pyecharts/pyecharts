from nose.tools import eq_

from pyecharts.charts import Tree


def test_tree_base():
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
    c = Tree().add("", data)
    eq_(c.theme, "white")
    eq_(c.renderer, "canvas")
    c.render()
