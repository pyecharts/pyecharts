import unittest
from unittest.mock import patch

from pyecharts import options as opts
from pyecharts.charts import LMap
from pyecharts.globals import ChartType

TEST_LOCATION = ["London"]
TEST_VALUE = [1]


class TestLMapChart(unittest.TestCase):

    @patch("pyecharts.render.engine.write_utf8_html_file")
    def test_amap(self, fake_writer):
        lmap = (
            LMap()
            .add_schema(center=[-0.118092, 51.509865])
            .add_coordinate("London", -0.118092, 51.509865)
            .add(
                "lmap",
                [list(z) for z in zip(TEST_LOCATION, TEST_VALUE)],
                label_opts=opts.LabelOpts(formatter="{b}"),
            )
        )
        lmap.render()
        content = fake_writer.call_args[0][1]
        self.assertIn('"coordinateSystem": "lmap"', content, "non lmap found")

    @patch("pyecharts.render.engine.write_utf8_html_file")
    def test_amap_polyline_and_large(self, fake_writer):
        lmap = (
            LMap()
            .add_schema(center=[-0.118092, 51.509865])
            .add_coordinate("London", -0.118092, 51.509865)
            .add(
                "lmap",
                [list(z) for z in zip(TEST_LOCATION, TEST_VALUE)],
                is_polyline=True,
                is_large=True,
                type_=ChartType.LINES,
                label_opts=opts.LabelOpts(formatter="{b}"),
            )
        )
        lmap.render()
        content = fake_writer.call_args[0][1]
        self.assertIn('"polyline": true', content, "polyline parameter is error")
        self.assertIn('"large": true', content, "large parameter is error")

    def test_amap_heatmap(self):
        lmap = (
            LMap()
            .add_schema(center=[-0.118092, 51.509865])
            .add_coordinate("London", -0.118092, 51.509865)
            .add(
                "lmap",
                [list(z) for z in zip(TEST_LOCATION, TEST_VALUE)],
                label_opts=opts.LabelOpts(formatter="{b}"),
            )
        )
        data = lmap.options.get("series")[0]["data"]
        for item in data:
            self.assertIn("name", item)
            self.assertIn("value", item)
