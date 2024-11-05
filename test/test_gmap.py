import unittest
from unittest.mock import patch

from pyecharts import options as opts
from pyecharts.charts import GMap
from pyecharts.globals import ChartType

FAKE_API_KEY = "fake_application_key"
GMAP_API_PREFIX = "https://maps.googleapis.com/maps/api/js"

TEST_LOCATION = ["London"]
TEST_VALUE = [1]


class TestGMapChart(unittest.TestCase):

    @patch("pyecharts.render.engine.write_utf8_html_file")
    def test_gmap(self, fake_writer):
        gmap = (
            GMap()
            .add_schema(gmap_ak=FAKE_API_KEY, center=[-0.118092, 51.509865])
            .add_coordinate("London", -0.118092, 51.509865)
            .add(
                "gmap",
                [list(z) for z in zip(TEST_LOCATION, TEST_VALUE)],
                label_opts=opts.LabelOpts(formatter="{b}"),
            )
        )
        gmap.render()
        content = fake_writer.call_args[0][1]
        self.assertIn(f'src="{GMAP_API_PREFIX}?key={FAKE_API_KEY}', content)
        self.assertIn('"coordinateSystem": "gmap"', content, "non gmap found")

    @patch("pyecharts.render.engine.write_utf8_html_file")
    def test_gmap_map_control_panel(self, fake_writer):
        gmap = (
            GMap()
            .add_schema(gmap_ak=FAKE_API_KEY, center=[-0.118092, 51.509865])
            .add_coordinate("London", -0.118092, 51.509865)
            .add(
                "amap",
                [list(z) for z in zip(TEST_LOCATION, TEST_VALUE)],
                label_opts=opts.LabelOpts(formatter="{b}"),
            )
            .add_control_panel(is_add_traffic_layer=True)
        )
        gmap.render()
        content = fake_writer.call_args[0][1]
        self.assertIn("new google.maps.TrafficLayer", content)

    @patch("pyecharts.render.engine.write_utf8_html_file")
    def test_gmap_polyline_and_large(self, fake_writer):
        gmap = (
            GMap()
            .add_schema(gmap_ak=FAKE_API_KEY, center=[-0.118092, 51.509865])
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
        gmap.render()
        content = fake_writer.call_args[0][1]
        self.assertIn('"polyline": true', content, "polyline parameter is error")
        self.assertIn('"large": true', content, "large parameter is error")

    def test_gmap_heatmap(self):
        gmap = (
            GMap()
            .add_schema(gmap_ak=FAKE_API_KEY, center=[-0.118092, 51.509865])
            .add_coordinate("London", -0.118092, 51.509865)
            .add(
                "amap",
                [list(z) for z in zip(TEST_LOCATION, TEST_VALUE)],
                label_opts=opts.LabelOpts(formatter="{b}"),
            )
        )
        data = gmap.options.get("series")[0]["data"]
        for item in data:
            self.assertIn("name", item)
            self.assertIn("value", item)
