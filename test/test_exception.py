from nose.tools import assert_equal

from pyecharts import options as opts
from pyecharts.charts import Geo, BMap
from pyecharts.exceptions import NonexistentCoordinatesException

BAIDU_MAP_API_PREFIX = "https://api.map.baidu.com/api?v=2.0"
FAKE_API_KEY = "fake_application_key"


def test_geo_catch_nonexistent_coord_exception():
    try:
        (
            Geo()
            .add_schema(maptype="china")
            .add("geo", [["NonexistentLocation", 123]])
            .set_series_opts(label_opts=opts.LabelOpts(is_show=False))
            .set_global_opts(visualmap_opts=opts.VisualMapOpts())
        )
    except NonexistentCoordinatesException as err:
        assert_equal(type(err), NonexistentCoordinatesException)
        assert err.__str__() != ""


def test_geo_ignore_nonexistent_coord_exception():
    (
        Geo(is_ignore_nonexistent_coord=True)
        .add_schema(maptype="china")
        .add("geo", [["NonexistentLocation", 123]])
        .set_series_opts(label_opts=opts.LabelOpts(is_show=False))
        .set_global_opts(visualmap_opts=opts.VisualMapOpts())
    )


def test_bmap_catch_nonexistent_coord_exception():
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
        assert_equal(type(err), NonexistentCoordinatesException)


def test_bmap_ignore_nonexistent_coord_exception():
    (
        BMap(is_ignore_nonexistent_coord=True)
        .add_schema(baidu_ak=FAKE_API_KEY, center=[-0.118092, 51.509865])
        .add(
            "bmap",
            [["NonexistentLocation", 123]],
            label_opts=opts.LabelOpts(formatter="{b}"),
        )
    )
