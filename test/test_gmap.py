import unittest
from unittest.mock import patch

from pyecharts import options as opts
from pyecharts.charts import GMap
from pyecharts.globals import ChartType


class TestGMapChart(unittest.TestCase):
    def setUp(self):
        self.fake_api_key = "fake_application_key"
        self.gmap_api_prefix = "https://maps.googleapis.com/maps/api/js"
        self.test_location = ["London"]
        self.test_value = [1]

    @patch("pyecharts.render.engine.write_utf8_html_file")
    def test_gmap(self, fake_writer):
        gmap = (
            GMap()
            .add_schema(gmap_ak=self.fake_api_key, center=[-0.118092, 51.509865])
            .add_coordinate("London", -0.118092, 51.509865)
            .add(
                "gmap",
                [list(z) for z in zip(self.test_location, self.test_value)],
                label_opts=opts.LabelOpts(formatter="{b}"),
            )
        )
        gmap.render()
        content = fake_writer.call_args[0][1]
        self.assertIn(f'src="{self.gmap_api_prefix}?key={self.fake_api_key}', content)
        self.assertIn('"coordinateSystem": "gmap"', content, "non gmap found")

    @patch("pyecharts.render.engine.write_utf8_html_file")
    def test_gmap_map_control_panel(self, fake_writer):
        gmap = (
            GMap()
            .add_schema(gmap_ak=self.fake_api_key, center=[-0.118092, 51.509865])
            .add_coordinate("London", -0.118092, 51.509865)
            .add(
                "amap",
                [list(z) for z in zip(self.test_location, self.test_value)],
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
            .add_schema(gmap_ak=self.fake_api_key, center=[-0.118092, 51.509865])
            .add_coordinate("London", -0.118092, 51.509865)
            .add(
                "amap",
                [list(z) for z in zip(self.test_location, self.test_value)],
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
            .add_schema(gmap_ak=self.fake_api_key, center=[-0.118092, 51.509865])
            .add_coordinate("London", -0.118092, 51.509865)
            .add(
                "amap",
                [list(z) for z in zip(self.test_location, self.test_value)],
                label_opts=opts.LabelOpts(formatter="{b}"),
            )
        )
        data = gmap.options.get("series")[0]["data"]
        for item in data:
            self.assertIn("name", item)
            self.assertIn("value", item)
