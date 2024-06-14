import unittest
from unittest.mock import patch

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


class TestTreeMapChart(unittest.TestCase):
    @patch("pyecharts.render.engine.write_utf8_html_file")
    def test_treemap_base(self, fake_writer):
        c = TreeMap().add("演示数据", example_data)
        c.render()
        _, content = fake_writer.call_args[0]
        self.assertEqual(c.theme, "white")
        self.assertEqual(c.renderer, "canvas")

    @patch("pyecharts.render.engine.write_utf8_html_file")
    def test_treemap_options(self, fake_writer):
        c = TreeMap().add(
            "演示数据", example_data, width="90%", height="100%", roam=False
        )
        c.render()
        _, content = fake_writer.call_args[0]
        self.assertIn("width", content)
        self.assertIn("height", content)
        self.assertIn("roam", content)

    @patch("pyecharts.render.engine.write_utf8_html_file")
    def test_treemap_levels_options(self, fake_writer):
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
        self.assertIn("levels", content)
