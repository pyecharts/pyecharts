from unittest.mock import patch

from nose.tools import assert_equal, assert_in

from pyecharts import options as opts
from pyecharts.charts import TreeMap

example_data = [
    {"value": 40, "name": "我是A"},
    {
        "value": 180,
        "name": "我是B",
        "children": [
            {
                "value": 76,
                "name": "我是B.children",
                "children": [
                    {"value": 12, "name": "我是B.children.a"},
                    {"value": 28, "name": "我是B.children.b"},
                    {"value": 20, "name": "我是B.children.c"},
                    {"value": 16, "name": "我是B.children.d"},
                ],
            }
        ],
    },
]


@patch("pyecharts.render.engine.write_utf8_html_file")
def test_treemap_base(fake_writer):
    c = TreeMap().add("演示数据", example_data)
    c.render()
    _, content = fake_writer.call_args[0]
    assert_equal(c.theme, "white")
    assert_equal(c.renderer, "canvas")


@patch("pyecharts.render.engine.write_utf8_html_file")
def test_treemap_options(fake_writer):
    c = TreeMap().add("演示数据", example_data, width="90%", height="100%", roam=False)
    c.render()
    _, content = fake_writer.call_args[0]
    assert_in("width", content)
    assert_in("height", content)
    assert_in("roam", content)


@patch("pyecharts.render.engine.write_utf8_html_file")
def test_treemap_levels_options(fake_writer):
    c = TreeMap().add(
        "演示数据",
        example_data,
        width="90%",
        height="100%",
        roam=False,
        levels=opts.TreeMapLevelsOpts(),
    )
    c.render()
    _, content = fake_writer.call_args[0]
    assert_in("levels", content)
