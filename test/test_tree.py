from unittest.mock import patch

from nose.tools import assert_equal

from pyecharts.charts import Tree


@patch("pyecharts.render.engine.write_utf8_html_file")
def test_tree_base(fake_writer):
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
    c.render()
    _, content = fake_writer.call_args[0]
    assert_equal(c.theme, "white")
    assert_equal(c.renderer, "canvas")
