import unittest

from pyecharts import options as opts
from pyecharts.charts import Geo, AMap, BMap, LMap, GMap
from pyecharts.exceptions import NonexistentCoordinatesException

BAIDU_MAP_API_PREFIX = "https://api.map.baidu.com/api?v=2.0"
FAKE_API_KEY = "fake_application_key"


class TestException(unittest.TestCase):

    def test_geo_catch_nonexistent_coord_exception(self):
        try:
            (
                Geo()
                .add_schema(maptype="china")
                .add("geo", [["NonexistentLocation", 123]])
                .set_series_opts(label_opts=opts.LabelOpts(is_show=False))
                .set_global_opts(visualmap_opts=opts.VisualMapOpts())
            )
        except NonexistentCoordinatesException as err:
            self.assertEqual(type(err), NonexistentCoordinatesException)
            assert err.__str__() != ""

    def test_geo_ignore_nonexistent_coord_exception(self):
        (
            Geo(is_ignore_nonexistent_coord=True)
            .add_schema(maptype="china")
            .add("geo", [["NonexistentLocation", 123]])
            .set_series_opts(label_opts=opts.LabelOpts(is_show=False))
            .set_global_opts(visualmap_opts=opts.VisualMapOpts())
        )

    def test_bmap_catch_nonexistent_coord_exception(self):
        try:
            (
                BMap()
                .add_schema(baidu_ak=FAKE_API_KEY, center=[-0.118092, 51.509865])
                .add(
                    "bmap",
                    [["NonexistentLocation", 123]],
                    label_opts=opts.LabelOpts(formatter="{b}"),
                )
            )
        except NonexistentCoordinatesException as err:
            self.assertEqual(type(err), NonexistentCoordinatesException)

    def test_amap_catch_nonexistent_coord_exception(self):
        try:
            (
                AMap()
                .add_schema(amap_ak=FAKE_API_KEY, center=[-0.118092, 51.509865])
                .add(
                    "amap",
                    [["NonexistentLocation", 123]],
                    label_opts=opts.LabelOpts(formatter="{b}"),
                )
            )
        except NonexistentCoordinatesException as err:
            self.assertEqual(type(err), NonexistentCoordinatesException)

    def test_lmap_catch_nonexistent_coord_exception(self):
        try:
            (
                LMap()
                .add_schema(center=[-0.118092, 51.509865])
                .add(
                    "lmap",
                    [["NonexistentLocation", 123]],
                    label_opts=opts.LabelOpts(formatter="{b}"),
                )
            )
        except NonexistentCoordinatesException as err:
            self.assertEqual(type(err), NonexistentCoordinatesException)

    def test_gmap_catch_nonexistent_coord_exception(self):
        try:
            (
                GMap()
                .add_schema(gmap_ak=FAKE_API_KEY, center=[-0.118092, 51.509865])
                .add(
                    "gmap",
                    [["NonexistentLocation", 123]],
                    label_opts=opts.LabelOpts(formatter="{b}"),
                )
            )
        except NonexistentCoordinatesException as err:
            self.assertEqual(type(err), NonexistentCoordinatesException)

    def test_bmap_ignore_nonexistent_coord_exception(self):
        (
            BMap(is_ignore_nonexistent_coord=True)
            .add_schema(baidu_ak=FAKE_API_KEY, center=[-0.118092, 51.509865])
            .add(
                "bmap",
                [["NonexistentLocation", 123]],
                label_opts=opts.LabelOpts(formatter="{b}"),
            )
        )
