from unittest.mock import patch

from pyecharts import options as opts
from pyecharts.charts import BMap
from pyecharts.globals import BMapType, ChartType

BAIDU_MAP_API_PREFIX = "http://api.map.baidu.com/api?v=2.0"


@patch("pyecharts.render.engine.write_utf8_html_file")
def test_bmap(fake_writer):
    fake_api_key = "fake_application_key"
    provinces = ["London"]
    values = [1]
    bmap = (
        BMap()
        .add_schema(baidu_ak=fake_api_key, center=[-0.118092, 51.509865])
        .add_coordinate("London", -0.118092, 51.509865)
        .add(
            "bmap",
            [list(z) for z in zip(provinces, values)],
            label_opts=opts.LabelOpts(formatter="{b}"),
        )
        .set_global_opts(title_opts=opts.TitleOpts(title="BMap-基本示例"))
    )
    bmap.render("render.html")
    content = fake_writer.call_args[0][1]
    expected_baidu_key = f'src="{BAIDU_MAP_API_PREFIX}&ak={fake_api_key}"'
    expected_map_type = '"coordinateSystem": "bmap"'
    assert expected_baidu_key in content, "missing baidu api key"
    assert expected_map_type in content, "non bmap found"


@patch("pyecharts.render.engine.write_utf8_html_file")
def test_bmap_effect_trail_length(fake_writer):
    fake_api_key = "fake_application_key"
    provinces = ["London"]
    values = [1]
    bmap = (
        BMap()
        .add_schema(baidu_ak=fake_api_key, center=[-0.118092, 51.509865])
        .add_coordinate("London", -0.118092, 51.509865)
        .add(
            "bmap",
            [list(z) for z in zip(provinces, values)],
            type_=ChartType.LINES,
            trail_length=0.5,
            effect_opts=opts.EffectOpts(),
            label_opts=opts.LabelOpts(formatter="{b}"),
        )
        .set_global_opts(title_opts=opts.TitleOpts(title="BMap-polyline-large"))
    )
    bmap.render("render.html")
    content = fake_writer.call_args[0][1]
    expected_trail_length = '"trailLength": 0.5'
    assert expected_trail_length in content, "trainLength parameter is error"


@patch("pyecharts.render.engine.write_utf8_html_file")
def test_bmap_polyline_and_large(fake_writer):
    fake_api_key = "fake_application_key"
    provinces = ["London"]
    values = [1]
    bmap = (
        BMap()
        .add_schema(baidu_ak=fake_api_key, center=[-0.118092, 51.509865])
        .add_coordinate("London", -0.118092, 51.509865)
        .add(
            "bmap",
            [list(z) for z in zip(provinces, values)],
            is_polyline=True,
            is_large=True,
            type_=ChartType.LINES,
            label_opts=opts.LabelOpts(formatter="{b}"),
        )
        .set_global_opts(title_opts=opts.TitleOpts(title="BMap-polyline-large"))
    )
    bmap.render("render.html")
    content = fake_writer.call_args[0][1]
    expected_poly_line = '"polyline": true'
    expected_large = '"large": true'
    assert expected_poly_line in content, "polyline parameter is error"
    assert expected_large in content, "large parameter is error"


@patch("pyecharts.render.engine.write_utf8_html_file")
def test_bmap_map_control_panel(fake_writer):
    fake_api_key = "fake_application_key"
    provinces = ["London"]
    values = [1]
    bmap = (
        BMap()
        .add_schema(baidu_ak=fake_api_key, center=[-0.118092, 51.509865])
        .add_coordinate("London", -0.118092, 51.509865)
        .add(
            "bmap",
            [list(z) for z in zip(provinces, values)],
            type_=ChartType.LINES,
            label_opts=opts.LabelOpts(formatter="{b}"),
        )
        .add_control_panel(
            copyright_control_opts=opts.BMapCopyrightType(position=3),
            maptype_control_opts=opts.BMapTypeControl(
                type_=BMapType.BMAP_MAPTYPE_CONTROL_DROPDOWN
            ),
            scale_control_opts=opts.BMapScaleControlOpts(),
            overview_map_opts=opts.BMapOverviewMapControlOpts(is_open=True),
            navigation_control_opts=opts.BMapNavigationControlOpts(),
            geo_location_control_opts=opts.BMapGeoLocationControlOpts(),
        )
        .set_global_opts(title_opts=opts.TitleOpts(title="BMap-控制面板示例"))
    )
    bmap.render("render.html")
    content = fake_writer.call_args[0][1]
    expected_copyright_control = "new BMap.CopyrightControl"
    expected_map_type_control = "new BMap.MapTypeControl"
    expected_scale_control = "new BMap.ScaleControl"
    expected_overview_map_control = "new BMap.OverviewMapControl"
    expected_navigation_control = "new BMap.NavigationControl"
    expected_geo_location_control = "new BMap.GeolocationControl"
    assert expected_copyright_control in content, "copyright function isn`t initialize"
    assert expected_map_type_control in content, "maptype function isn`t initialize"
    assert expected_scale_control in content, "scale function isn`t initialize"
    assert (
        expected_overview_map_control in content
    ), "overview function isn`t initialize"
    assert (
        expected_navigation_control in content
    ), "navigation function isn`t initialize"
    assert (
        expected_geo_location_control in content
    ), "geo_location function isn`t initialize"
