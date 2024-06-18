import unittest
from unittest.mock import patch

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


class TestTreeChart(unittest.TestCase):
    @patch("pyecharts.render.engine.write_utf8_html_file")
    def test_tree_base(self, fake_writer):
        c = Tree().add("", TEST_DATA)
        c.render()
        _, content = fake_writer.call_args[0]
        self.assertEqual(c.theme, "white")
        self.assertEqual(c.renderer, "canvas")

    @patch("pyecharts.render.engine.write_utf8_html_file")
    def test_tree_collapse_interval(self, fake_writer):
        c = Tree().add("", TEST_DATA, collapse_interval=1)
        c.render()
        _, content = fake_writer.call_args[0]
        self.assertEqual(c.theme, "white")
        self.assertEqual(c.renderer, "canvas")

    @patch("pyecharts.render.engine.write_utf8_html_file")
    def test_tree_options(self, fake_writer):
        c = Tree().add(
            series_name="tree",
            data=TEST_DATA,
            orient="BT",
            initial_tree_depth=1,
            label_opts=opts.LabelOpts(),
            leaves_opts=opts.TreeLeavesOpts(),
        )
        c.render()
        _, content = fake_writer.call_args[0]
        self.assertIn("orient", content)
        self.assertIn("initialTreeDepth", content)
        self.assertIn("label", content)
        self.assertIn("leaves", content)
