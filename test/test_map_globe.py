import unittest
from unittest.mock import patch

from pyecharts.charts import MapGlobe
from pyecharts.faker import Faker
from pyecharts.globals import CurrentConfig, NotebookType


class TestMapGlobeChart(unittest.TestCase):
    @patch("pyecharts.render.engine.write_utf8_html_file")
    def test_map_base(self, fake_writer):
        c = MapGlobe().add(
            "商家A", [list(z) for z in zip(Faker.provinces, Faker.values())], "china"
        )
        c.render()
        _, content = fake_writer.call_args[0]
        self.assertIn("document.createElement('canvas')", content)
        self.assertEqual(c.theme, "white")
        self.assertEqual(c.renderer, "canvas")
        self.assertIn("baseTexture", content)

    @patch("pyecharts.render.engine.write_utf8_html_file")
    def test_map_base_v2(self, fake_writer):
        c = (
            MapGlobe()
            .add(
                "商家A",
                [list(z) for z in zip(Faker.provinces, Faker.values())],
                "china",
            )
            .add_schema(maptype="china")
        )
        c.render()
        _, content = fake_writer.call_args[0]
        self.assertIn("document.createElement('canvas')", content)
        self.assertEqual(c.theme, "white")
        self.assertEqual(c.renderer, "canvas")
        self.assertIn("baseTexture", content)

    def test_map_globe_in_jupyter(self):
        CurrentConfig.NOTEBOOK_TYPE = NotebookType.JUPYTER_NOTEBOOK

        c = MapGlobe().add(
            "商家A", [list(z) for z in zip(Faker.provinces, Faker.values())], "china"
        )
        content = c.render_notebook()._repr_html_()
        self.assertIn("document.createElement('canvas')", content)
        self.assertIn("baseTexture", content)
