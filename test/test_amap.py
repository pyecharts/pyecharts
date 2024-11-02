import unittest
from unittest.mock import patch

from pyecharts import options as opts
from pyecharts.charts import AMap
from pyecharts.globals import ChartType

FAKE_API_KEY = "fake_application_key"
AMAP_API_PREFIX = "https://webapi.amap.com/maps?v=2.0"

TEST_LOCATION = ["London"]
TEST_VALUE = [1]


class TestAMapChart(unittest.TestCase):

    @patch("pyecharts.render.engine.write_utf8_html_file")
    def test_amap(self, fake_writer):
        amap = (
            AMap()
            .add_schema(amap_ak=FAKE_API_KEY, center=[-0.118092, 51.509865])
            .add_coordinate("London", -0.118092, 51.509865)
            .add(
                "amap",
                [list(z) for z in zip(TEST_LOCATION, TEST_VALUE)],
                label_opts=opts.LabelOpts(formatter="{b}"),
            )
        )
        amap.render()
        content = fake_writer.call_args[0][1]
        self.assertIn(f'src="{AMAP_API_PREFIX}&key={FAKE_API_KEY}', content)
        self.assertIn('"coordinateSystem": "amap"', content, "non amap found")

    @patch("pyecharts.render.engine.write_utf8_html_file")
    def test_amap_map_control_panel(self, fake_writer):
        amap = (
            AMap()
            .add_schema(amap_ak=FAKE_API_KEY, center=[-0.118092, 51.509865])
            .add_coordinate("London", -0.118092, 51.509865)
            .add(
                "amap",
                [list(z) for z in zip(TEST_LOCATION, TEST_VALUE)],
                label_opts=opts.LabelOpts(formatter="{b}"),
            )
            .add_control_panel(
                is_add_satellite_layer=True,
                is_add_road_net_layer=True,
            )
        )
        amap.render()
        content = fake_writer.call_args[0][1]
        self.assertIn("new AMap.TileLayer.Satellite", content)
        self.assertIn("new AMap.TileLayer.RoadNet", content)

    @patch("pyecharts.render.engine.write_utf8_html_file")
    def test_amap_polyline_and_large(self, fake_writer):
        amap = (
            AMap()
            .add_schema(amap_ak=FAKE_API_KEY, center=[-0.118092, 51.509865])
            .add_coordinate("London", -0.118092, 51.509865)
            .add(
                "amap",
                [list(z) for z in zip(TEST_LOCATION, TEST_VALUE)],
                is_polyline=True,
                is_large=True,
                type_=ChartType.LINES,
                label_opts=opts.LabelOpts(formatter="{b}"),
            )
        )
        amap.render()
        content = fake_writer.call_args[0][1]
        self.assertIn('"polyline": true', content, "polyline parameter is error")
        self.assertIn('"large": true', content, "large parameter is error")

    def test_amap_heatmap(self):
        amap = (
            AMap()
            .add_schema(amap_ak=FAKE_API_KEY, center=[-0.118092, 51.509865])
            .add_coordinate("London", -0.118092, 51.509865)
            .add(
                "amap",
                [list(z) for z in zip(TEST_LOCATION, TEST_VALUE)],
                label_opts=opts.LabelOpts(formatter="{b}"),
            )
        )
        data = amap.options.get("series")[0]["data"]
        for item in data:
            self.assertIn("name", item)
            self.assertIn("value", item)
