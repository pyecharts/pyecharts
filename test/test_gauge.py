import unittest
from unittest.mock import patch

from pyecharts.charts import Gauge
from pyecharts import options as opts


class TestGaugeChart(unittest.TestCase):

    @patch("pyecharts.render.engine.write_utf8_html_file")
    def test_gauge_base(self, fake_writer):
        c = Gauge().add("", [("完成率", 66.6)])
        c.render()
        _, content = fake_writer.call_args[0]
        self.assertEqual(c.theme, "white")
        self.assertEqual(c.renderer, "canvas")

    @patch("pyecharts.render.engine.write_utf8_html_file")
    def test_gauage_label_setting(self, fake_writer):
        c = Gauge().add(
            "",
            [("完成率", 66.6)],
            detail_label_opts=opts.GaugeDetailOpts(formatter="{value}"),
            title_label_opts=opts.GaugeTitleOpts(
                font_size=40, color="blue", font_family="Microsoft YaHei"
            ),
        )
        c.render()
        _, content = fake_writer.call_args[0]
        self.assertIn("title", content)
        self.assertIn("detail", content)

    @patch("pyecharts.render.engine.write_utf8_html_file")
    def test_gauage_radius_setting(self, fake_writer):
        c = Gauge().add("", [("完成率", 66.6)], radius="50%")
        c.render()
        _, content = fake_writer.call_args[0]
        self.assertIn("radius", content)
