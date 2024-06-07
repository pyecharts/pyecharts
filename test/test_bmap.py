import unittest
from unittest.mock import patch

from pyecharts import options as opts
from pyecharts.charts import BMap
from pyecharts.globals import BMapType, ChartType

BAIDU_MAP_API_PREFIX = "https://api.map.baidu.com/api?v=2.0"
FAKE_API_KEY = "fake_application_key"

TEST_LOCATION = ["London"]
TEST_VALUE = [1]


class TestBMapChart(unittest.TestCase):

    @patch("pyecharts.render.engine.write_utf8_html_file")
    def test_bmap(self, fake_writer):
        bmap = (
            BMap()
            .add_schema(baidu_ak=FAKE_API_KEY, center=[-0.118092, 51.509865])
            .add_coordinate("London", -0.118092, 51.509865)
            .add(
                "bmap",
                [list(z) for z in zip(TEST_LOCATION, TEST_VALUE)],
                label_opts=opts.LabelOpts(formatter="{b}"),
            )
        )
        bmap.render()
        content = fake_writer.call_args[0][1]
        self.assertIn(f'src="{BAIDU_MAP_API_PREFIX}&ak={FAKE_API_KEY}"', content)
        self.assertIn('"coordinateSystem": "bmap"', content, "non bmap found")

    def test_bmap_heatmap(self):
        bmap = (
            BMap()
            .add_schema(baidu_ak=FAKE_API_KEY, center=[-0.118092, 51.509865])
            .add_coordinate("London", -0.118092, 51.509865)
            .add(
                "bmap",
                [list(z) for z in zip(TEST_LOCATION, TEST_VALUE)],
                label_opts=opts.LabelOpts(formatter="{b}"),
            )
        )
        data = bmap.options.get("series")[0]["data"]
        for item in data:
            self.assertIn("name", item)
            self.assertIn("value", item)

    @patch("pyecharts.render.engine.write_utf8_html_file")
    def test_bmap_effect_trail_length(self, fake_writer):
        bmap = (
            BMap()
            .add_schema(baidu_ak=FAKE_API_KEY, center=[-0.118092, 51.509865])
            .add_coordinate("London", -0.118092, 51.509865)
            .add(
                "bmap",
                [list(z) for z in zip(TEST_LOCATION, TEST_VALUE)],
                type_=ChartType.LINES,
                effect_opts=opts.EffectOpts(trail_length=0.5),
                label_opts=opts.LabelOpts(formatter="{b}"),
            )
        )
        bmap.render("render.html")
        content = fake_writer.call_args[0][1]
        self.assertIn('"trailLength": 0.5', content, "trainLength parameter is error")

    @patch("pyecharts.render.engine.write_utf8_html_file")
    def test_bmap_polyline_and_large(self, fake_writer):
        bmap = (
            BMap()
            .add_schema(baidu_ak=FAKE_API_KEY, center=[-0.118092, 51.509865])
            .add_coordinate("London", -0.118092, 51.509865)
            .add(
                "bmap",
                [list(z) for z in zip(TEST_LOCATION, TEST_VALUE)],
                is_polyline=True,
                is_large=True,
                type_=ChartType.LINES,
                label_opts=opts.LabelOpts(formatter="{b}"),
            )
        )
        bmap.render()
        content = fake_writer.call_args[0][1]
        self.assertIn('"polyline": true', content, "polyline parameter is error")
        self.assertIn('"large": true', content, "large parameter is error")

    @patch("pyecharts.render.engine.write_utf8_html_file")
    def test_bmap_map_control_panel(self, fake_writer):
        bmap = (
            BMap()
            .add_schema(baidu_ak=FAKE_API_KEY, center=[-0.118092, 51.509865])
            .add_coordinate("London", -0.118092, 51.509865)
            .add(
                "bmap",
                [list(z) for z in zip(TEST_LOCATION, TEST_VALUE)],
                type_=ChartType.LINES,
                label_opts=opts.LabelOpts(formatter="{b}"),
            )
            .add_control_panel(
                copyright_control_opts=opts.BMapCopyrightTypeOpts(position=3),
                maptype_control_opts=opts.BMapTypeControlOpts(
                    type_=BMapType.MAPTYPE_CONTROL_DROPDOWN
                ),
                scale_control_opts=opts.BMapScaleControlOpts(),
                overview_map_opts=opts.BMapOverviewMapControlOpts(is_open=True),
                navigation_control_opts=opts.BMapNavigationControlOpts(),
                geo_location_control_opts=opts.BMapGeoLocationControlOpts(),
            )
        )
        bmap.render()
        content = fake_writer.call_args[0][1]
        self.assertIn("new BMap.CopyrightControl", content)
        self.assertIn("new BMap.MapTypeControl", content)
        self.assertIn("new BMap.ScaleControl", content)
        self.assertIn("new BMap.OverviewMapControl", content)
        self.assertIn("new BMap.NavigationControl", content)
        self.assertIn("new BMap.GeolocationControl", content)

    @patch("pyecharts.render.engine.write_utf8_html_file")
    def test_bmap_progressive_options(self, fake_writer):
        bmap = (
            BMap()
            .add_schema(baidu_ak=FAKE_API_KEY, center=[-0.118092, 51.509865])
            .add_coordinate("London", -0.118092, 51.509865)
            .add(
                "bmap",
                type_="lines",
                data_pair=[list(z) for z in zip(TEST_LOCATION, TEST_VALUE)],
                label_opts=opts.LabelOpts(formatter="{b}"),
                progressive=200,
                progressive_threshold=500,
            )
        )
        bmap.render()
        content = fake_writer.call_args[0][1]
        self.assertIn("progressive", content)
        self.assertIn("progressiveThreshold", content)
