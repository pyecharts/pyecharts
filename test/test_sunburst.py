import unittest
from unittest.mock import patch

from pyecharts import options as opts
from pyecharts.charts import Sunburst


class TestSunburstChart(unittest.TestCase):
    @patch("pyecharts.render.engine.write_utf8_html_file")
    def test_sunburst_base(self, fake_writer):
        # Arrange
        data = [{"name": "A", "children": [{"name": "B", "value": 1}]}]

        # Act
        c = Sunburst().add("Sunburst", data)
        c.render()

        # Assert
        fake_writer.assert_called_once()
        self.assertEqual(c.theme, "white")
        self.assertEqual(c.renderer, "canvas")

    def test_sunburst_dataitem(self):
        item_name = "test_data_item"
        item = opts.SunburstItem(name=item_name)
        self.assertEqual(item.opts.get("name"), item_name)