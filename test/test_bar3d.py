import random
import unittest
from unittest.mock import patch

from pyecharts import options as opts
from pyecharts.charts import Bar3D
from pyecharts.faker import Faker


class TestBar3DChart(unittest.TestCase):

    @patch("pyecharts.render.engine.write_utf8_html_file")
    def test_bar3d_base(self, fake_writer):
        data = [(i, j, random.randint(0, 12)) for i in range(6) for j in range(24)]
        c = (
            Bar3D()
            .add(
                "",
                [[d[1], d[0], d[2]] for d in data],
                xaxis3d_opts=opts.Axis3DOpts(Faker.clock, type_="category"),
                yaxis3d_opts=opts.Axis3DOpts(Faker.week_en, type_="category"),
                zaxis3d_opts=opts.Axis3DOpts(type_="value"),
            )
            .set_global_opts(visualmap_opts=opts.VisualMapOpts(max_=20))
        )
        c.render()
        _, content = fake_writer.call_args[0]
        self.assertEqual(c.theme, "white")
        self.assertEqual(c.renderer, "canvas")

    @patch("pyecharts.render.engine.write_utf8_html_file")
    def test_bar3d_stack(self, fake_writer):
        data1 = [(i, j, random.randint(0, 12)) for i in range(6) for j in range(24)]
        data2 = [(i, j, random.randint(13, 20)) for i in range(6) for j in range(24)]
        c = (
            Bar3D()
            .add(
                "1",
                [[d[1], d[0], d[2]] for d in data1],
                xaxis3d_opts=opts.Axis3DOpts(Faker.clock, type_="category"),
                yaxis3d_opts=opts.Axis3DOpts(Faker.week_en, type_="category"),
                zaxis3d_opts=opts.Axis3DOpts(type_="value"),
            )
            .add(
                "2",
                [[d[1], d[0], d[2]] for d in data2],
                xaxis3d_opts=opts.Axis3DOpts(Faker.clock, type_="category"),
                yaxis3d_opts=opts.Axis3DOpts(Faker.week_en, type_="category"),
                zaxis3d_opts=opts.Axis3DOpts(type_="value"),
            )
            .set_global_opts(visualmap_opts=opts.VisualMapOpts(max_=20))
            .set_series_opts(**{"stack": "stack"})
        )
        c.render()
        _, content = fake_writer.call_args[0]
        self.assertIn("stack", content)

    @patch("pyecharts.render.engine.write_utf8_html_file")
    def test_bar3d_with_globe(self, fake_writer):
        c = (
            Bar3D(init_opts=opts.InitOpts(bg_color="#000"))
            .add(
                series_name="Population",
                coordinate_system="globe",
                data=[[120, 30, 1.11112222]],
                itemstyle_opts=opts.ItemStyleOpts(color="orange"),
                xaxis3d_opts=None,
                yaxis3d_opts=None,
                zaxis3d_opts=None,
                grid3d_opts=None,
            )
            .add_globe(
                base_texture="world.topo.bathy.200401.jpg",
                height_texture="world.topo.bathy.200401.jpg",
                shading="lambert",
                environment="starfield.jpg",
                light_opts=opts.Map3DLightOpts(main_intensity=2),
                view_control_opts={"autoRotate": False},
            )
        )
        c.render()
        _, content = fake_writer.call_args[0]
        self.assertIn("globe", content)
