import unittest
from unittest.mock import patch

from pyecharts import options as opts
from pyecharts.charts import EffectScatter
from pyecharts.faker import Faker


class TestEffectScatterChart(unittest.TestCase):
    @patch("pyecharts.render.engine.write_utf8_html_file")
    def test_effectscatter_base(self, fake_writer):
        c = EffectScatter().add_xaxis(Faker.choose()).add_yaxis("", Faker.values())
        c.render()
        _, content = fake_writer.call_args[0]
        self.assertEqual(c.theme, "white")
        self.assertEqual(c.renderer, "canvas")

    @patch("pyecharts.render.engine.write_utf8_html_file")
    def test_effectscatter_item_base(self, fake_writer):
        x_axis = Faker.choose()
        chart_item = [
            opts.EffectScatterItem(name=d[0], value=d[1])
            for d in list(zip(x_axis, Faker.values()))
        ]

        c = EffectScatter().add_xaxis(x_axis).add_yaxis("", chart_item)
        c.render()
        _, content = fake_writer.call_args[0]
        self.assertEqual(c.theme, "white")
        self.assertEqual(c.renderer, "canvas")
