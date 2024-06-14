import random
import unittest
from unittest.mock import patch

from pyecharts import options as opts
from pyecharts.charts import Polar


class TestPolarChart(unittest.TestCase):
    @patch("pyecharts.render.engine.write_utf8_html_file")
    def test_polar_scatter(self, fake_writer):
        data = [(i, random.randint(1, 100)) for i in range(101)]
        c = Polar().add(
            "", data, type_="scatter", label_opts=opts.LabelOpts(is_show=False)
        )
        c.render()
        _, content = fake_writer.call_args[0]
        self.assertEqual(c.theme, "white")
        self.assertEqual(c.renderer, "canvas")

    @patch("pyecharts.render.engine.write_utf8_html_file")
    def test_polar_effect_scatter(self, fake_writer):
        data = [(i, random.randint(1, 100)) for i in range(101)]
        c = (
            Polar()
            .add(
                "",
                data,
                type_="effectScatter",
                effect_opts=opts.EffectOpts(scale=10, period=5),
                label_opts=opts.LabelOpts(is_show=False),
            )
            .set_global_opts(title_opts=opts.TitleOpts(title="Polar-EffectScatter"))
        )
        c.render()
        _, content = fake_writer.call_args[0]
        self.assertEqual(c.theme, "white")
        self.assertEqual(c.renderer, "canvas")

    @patch("pyecharts.render.engine.write_utf8_html_file")
    def test_polar_base_1(self, fake_writer):
        data = [(i, random.randint(1, 100)) for i in range(101)]
        c = (
            Polar()
            .add(
                "",
                data,
                type_="effectScatter",
                effect_opts=opts.EffectOpts(scale=10, period=5),
                label_opts=opts.LabelOpts(is_show=True),
            )
            .set_global_opts(title_opts=opts.TitleOpts(title="Polar-Base-1"))
        )
        c.render()
        _, content = fake_writer.call_args[0]
        self.assertEqual(c.theme, "white")
        self.assertEqual(c.renderer, "canvas")
