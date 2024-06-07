import requests
import unittest
from unittest.mock import patch

from pyecharts import options as opts
from pyecharts.charts import Lines3D, Map3D
from pyecharts.globals import ChartType


class TestLines3DChart(unittest.TestCase):
    @patch("pyecharts.render.engine.write_utf8_html_file")
    def test_lines3d_base(self, fake_writer):
        test_main_url: str = "https://echarts.apache.org/examples"
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
                light_opts=opts.Map3DLightOpts(
                    ambient_intensity=0.4, main_intensity=0.4
                ),
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
        self.assertEqual(c.theme, "white")
        self.assertEqual(c.renderer, "canvas")
        self.assertIn("baseTexture", content)
        self.assertIn("heightTexture", content)

    @patch("pyecharts.render.engine.write_utf8_html_file")
    def test_lines3d_with_map3d_base(self, fake_writer):
        example_data = [
            [[119.107078, 36.70925, 1000], [116.587245, 35.415393, 1000]],
            [[117.000923, 36.675807], [120.355173, 36.082982]],
            [[118.047648, 36.814939], [118.66471, 37.434564]],
            [[121.391382, 37.539297], [119.107078, 36.70925]],
            [[116.587245, 35.415393], [122.116394, 37.509691]],
            [[119.461208, 35.428588], [118.326443, 35.065282]],
            [[116.307428, 37.453968], [115.469381, 35.246531]],
        ]
        c = (
            Map3D()
            .add_schema(
                maptype="山东",
                itemstyle_opts=opts.ItemStyleOpts(
                    color="rgb(5,101,123)",
                    opacity=1,
                    border_width=0.8,
                    border_color="rgb(62,215,213)",
                ),
                light_opts=opts.Map3DLightOpts(
                    main_color="#fff",
                    main_intensity=1.2,
                    is_main_shadow=False,
                    main_alpha=55,
                    main_beta=10,
                    ambient_intensity=0.3,
                ),
                view_control_opts=opts.Map3DViewControlOpts(center=[-10, 0, 10]),
                post_effect_opts=opts.Map3DPostEffectOpts(is_enable=False),
            )
            .add(
                series_name="",
                data_pair=example_data,
                type_=ChartType.LINES3D,
                effect=opts.Lines3DEffectOpts(
                    is_show=True,
                    period=4,
                    trail_width=3,
                    trail_length=0.5,
                    trail_color="#f00",
                    trail_opacity=1,
                ),
                linestyle_opts=opts.LineStyleOpts(
                    is_show=False, color="#fff", opacity=0
                ),
            )
            .set_global_opts(title_opts=opts.TitleOpts(title="Map3D-Lines3D"))
        )
        c.render()
        _, content = fake_writer.call_args[0]
        self.assertEqual(c.theme, "white")
        self.assertEqual(c.renderer, "canvas")
