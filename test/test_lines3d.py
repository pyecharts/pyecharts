import requests
from unittest.mock import patch

from nose.tools import assert_in, assert_equal

from pyecharts import options as opts
from pyecharts.charts import Lines3D


@patch("pyecharts.render.engine.write_utf8_html_file")
def test_lines3d_base(fake_writer):
    test_main_url: str = (
        "https://cdn.jsdelivr.net/gh/apache/echarts-website@asf-site/examples"
    )
    data_json_url = test_main_url + "/data-gl/asset/data/flights.json"
    base_texture = test_main_url + "/data-gl/asset/world.topo.bathy.200401.jpg"
    height_texture = test_main_url + "/data-gl/asset/bathymetry_bw_composite_4k.jpg"

    resp = requests.get(data_json_url).json()
    json_routes = resp.get("routes")
    json_airports = resp.get("airports")

    routes_data = []
    for d in json_routes:

        def _inner_func(idx):
            return [json_airports[idx][3], json_airports[idx][4]]

        routes_data.append([_inner_func(d[1]), _inner_func(d[2])])

    c = (
        Lines3D(init_opts=opts.InitOpts(bg_color="#000"))
        .add_globe(
            base_texture=base_texture,
            height_texture=height_texture,
            shading="lambert",
            light_opts=opts.Map3DLightOpts(ambient_intensity=0.4, main_intensity=0.4),
        )
        .add(
            series_name="1",
            coordinate_system="globe",
            blend_mode="lighter",
            linestyle_opts=opts.LineStyleOpts(
                width=1, color="rgb(50, 50, 150)", opacity=0.1
            ),
            data_pair=routes_data,
        )
    )
    c.render()
    _, content = fake_writer.call_args[0]
    assert_equal(c.theme, "white")
    assert_equal(c.renderer, "canvas")
    assert_in("baseTexture", content)
    assert_in("heightTexture", content)
