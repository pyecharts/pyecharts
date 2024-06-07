import unittest
from unittest.mock import patch

from pyecharts import options as opts
from pyecharts.charts import Funnel
from pyecharts.faker import Faker


class TestFunnelChart(unittest.TestCase):

    @patch("pyecharts.render.engine.write_utf8_html_file")
    def test_funnel_base(self, fake_writer):
        c = Funnel().add("商品", [list(z) for z in zip(Faker.choose(), Faker.values())])
        c.render()
        _, content = fake_writer.call_args[0]
        self.assertEqual(c.theme, "white")
        self.assertEqual(c.renderer, "canvas")

    @patch("pyecharts.render.engine.write_utf8_html_file")
    def test_funnel_item_base(self, fake_writer):
        funnel_item = [
            opts.FunnelItem(name=d[0], value=d[1])
            for d in list(zip(Faker.choose(), Faker.values()))
        ]
        c = (
            Funnel()
            .add("商品", funnel_item)
            .set_global_opts(title_opts=opts.TitleOpts(title="Funnel-基本示例"))
        )
        c.render()
        _, content = fake_writer.call_args[0]
        self.assertEqual(c.theme, "white")
        self.assertEqual(c.renderer, "canvas")
