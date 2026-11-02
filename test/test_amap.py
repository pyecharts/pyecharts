import unittest
from unittest.mock import patch

from pyecharts import options as opts
from pyecharts.charts import AMap
from pyecharts.globals import ChartType


class TestAMapChart(unittest.TestCase):
    def setUp(self):
        self.fake_api_key = "fake_application_key"
        self.amap_api_prefix = "https://webapi.amap.com/maps?v=2.0"
        self.test_location = ["London"]
        self.test_value = [1]

    @patch("pyecharts.render.engine.write_utf8_html_file")
    def test_amap(self, fake_writer):
        amap = (
            AMap()
            .add_schema(amap_ak=self.fake_api_key, center=[-0.118092, 51.509865])
            .add_coordinate("London", -0.118092, 51.509865)
            .add(
                "amap",
                [list(z) for z in zip(self.test_location, self.test_value)],
                label_opts=opts.LabelOpts(formatter="{b}"),
            )
        )
        amap.render()
        content = fake_writer.call_args[0][1]
        self.assertIn(f'src="{self.amap_api_prefix}&key={self.fake_api_key}', content)
        self.assertIn('"coordinateSystem": "amap"', content, "non amap found")

    @patch("pyecharts.render.engine.write_utf8_html_file")
    def test_amap_map_control_panel(self, fake_writer):
        amap = (
            AMap()
            .add_schema(amap_ak=self.fake_api_key, center=[-0.118092, 51.509865])
            .add_coordinate("London", -0.118092, 51.509865)
            .add(
                "amap",
                [list(z) for z in zip(self.test_location, self.test_value)],
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
            .add_schema(amap_ak=self.fake_api_key, center=[-0.118092, 51.509865])
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
        amap.render()
        content = fake_writer.call_args[0][1]
        self.assertIn('"polyline": true', content, "polyline parameter is error")
        self.assertIn('"large": true', content, "large parameter is error")

    def test_amap_heatmap(self):
        amap = (
            AMap()
            .add_schema(amap_ak=self.fake_api_key, center=[-0.118092, 51.509865])
            .add_coordinate("London", -0.118092, 51.509865)
            .add(
                "amap",
                [list(z) for z in zip(self.test_location, self.test_value)],
                label_opts=opts.LabelOpts(formatter="{b}"),
            )
        )
        data = amap.options.get("series")[0]["data"]
        self.assertEqual(len(self.test_location), len(data),)
        self.assertIn("name", data[0])
        self.assertIn("value", data[0])
