from unittest.mock import patch

from nose.tools import assert_in

from pyecharts import options as opts
from pyecharts.charts import BMap
from pyecharts.globals import BMapType, ChartType

BAIDU_MAP_API_PREFIX = "https://api.map.baidu.com/api?v=2.0"
FAKE_API_KEY = "fake_application_key"

TEST_LOCATION = ["London"]
TEST_VALUE = [1]


@patch("pyecharts.render.engine.write_utf8_html_file")
def test_bmap(fake_writer):
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
    assert_in(f'src="{BAIDU_MAP_API_PREFIX}&ak={FAKE_API_KEY}"', content)
    assert_in('"coordinateSystem": "bmap"', content, "non bmap found")


def test_bmap_heatmap():
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
        assert_in("name", item)
        assert_in("value", item)


@patch("pyecharts.render.engine.write_utf8_html_file")
def test_bmap_effect_trail_length(fake_writer):
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
    assert_in('"trailLength": 0.5', content, "trainLength parameter is error")


@patch("pyecharts.render.engine.write_utf8_html_file")
def test_bmap_polyline_and_large(fake_writer):
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
    assert_in('"polyline": true', content, "polyline parameter is error")
    assert_in('"large": true', content, "large parameter is error")


@patch("pyecharts.render.engine.write_utf8_html_file")
def test_bmap_map_control_panel(fake_writer):
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
    assert_in("new BMap.CopyrightControl", content)
    assert_in("new BMap.MapTypeControl", content)
    assert_in("new BMap.ScaleControl", content)
    assert_in("new BMap.OverviewMapControl", content)
    assert_in("new BMap.NavigationControl", content)
    assert_in("new BMap.GeolocationControl", content)


@patch("pyecharts.render.engine.write_utf8_html_file")
def test_bmap_progressive_options(fake_writer):
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
    assert_in("progressive", content)
    assert_in("progressiveThreshold", content)
