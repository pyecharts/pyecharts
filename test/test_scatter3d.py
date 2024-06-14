import random
import unittest
from unittest.mock import patch

from pyecharts import options as opts
from pyecharts.charts import Scatter3D
from pyecharts.faker import Faker


class TestScatter3D(unittest.TestCase):
    @patch("pyecharts.render.engine.write_utf8_html_file")
    def test_scatter3d_base(self, fake_writer):
        data = [
            [random.randint(0, 100), random.randint(0, 100), random.randint(0, 100)]
            for _ in range(80)
        ]
        c = (
            Scatter3D()
            .add("", data)
            .set_global_opts(
                visualmap_opts=opts.VisualMapOpts(range_color=Faker.visual_color)
            )
        )
        c.render()
        _, content = fake_writer.call_args[0]
        self.assertEqual(c.theme, "white")
        self.assertEqual(c.renderer, "canvas")
