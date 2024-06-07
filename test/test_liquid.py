import unittest
from unittest.mock import patch

from pyecharts import options as opts
from pyecharts.charts import Grid, Liquid
from pyecharts.commons.utils import JsCode


class TestLiquidChart(unittest.TestCase):
    @patch("pyecharts.render.engine.write_utf8_html_file")
    def test_liquid_base(self, fake_writer):
        c = Liquid().add("lq", [0.6, 0.7], is_animation=False)
        c.render()
        _, content = fake_writer.call_args[0]
        self.assertEqual(c.theme, "white")
        self.assertEqual(c.renderer, "canvas")
        self.assertIn("animationDuration", content)
        self.assertIn("animationDurationUpdate", content)

    @patch("pyecharts.render.engine.write_utf8_html_file")
    def test_liquid_grid(self, fake_writer):
        l1 = (
            Liquid()
            .add("lq", [0.6, 0.7], center=["60%", "50%"])
            .set_global_opts(title_opts=opts.TitleOpts(title="多个 Liquid 显示"))
        )

        l2 = Liquid().add(
            "lq",
            [0.3254],
            center=["25%", "50%"],
            label_opts=opts.LabelOpts(
                font_size=50,
                formatter=JsCode(
                    """function (param) {
                            return (Math.floor(param.value * 10000) / 100) + '%';
                        }"""
                ),
                position="inside",
            ),
        )

        c = Grid().add(l1, grid_opts=opts.GridOpts()).add(l2, grid_opts=opts.GridOpts())
        c.render()
        _, content = fake_writer.call_args[0]
        self.assertIn("center", content)
