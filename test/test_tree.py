from unittest.mock import patch

from nose.tools import assert_equal, assert_in

from pyecharts import options as opts
from pyecharts.charts import Tree

TEST_DATA = [
    {
        "children": [
            {"name": "B"},
            {
                "children": [{"children": [{"name": "I"}], "name": "E"}, {"name": "F"}],
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


@patch("pyecharts.render.engine.write_utf8_html_file")
def test_tree_base(fake_writer):
    c = Tree().add("", TEST_DATA)
    c.render()
    _, content = fake_writer.call_args[0]
    assert_equal(c.theme, "white")
    assert_equal(c.renderer, "canvas")


@patch("pyecharts.render.engine.write_utf8_html_file")
def test_tree_collapse_interval(fake_writer):
    c = Tree().add("", TEST_DATA, collapse_interval=1)
    c.render()
    _, content = fake_writer.call_args[0]
    assert_equal(c.theme, "white")
    assert_equal(c.renderer, "canvas")


@patch("pyecharts.render.engine.write_utf8_html_file")
def test_tree_options(fake_writer):
    c = Tree().add(
        series_name="tree",
        data=TEST_DATA,
        orient="BT",
        initial_tree_depth=1,
        label_opts=opts.LabelOpts(),
        leaves_label_opts=opts.LabelOpts(),
    )
    c.render()
    _, content = fake_writer.call_args[0]
    assert_in("orient", content)
    assert_in("initialTreeDepth", content)
    assert_in("label", content)
    assert_in("leaves", content)
