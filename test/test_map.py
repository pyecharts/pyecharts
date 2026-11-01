import unittest
from unittest.mock import patch

import simplejson as json

from pyecharts import options as opts
from pyecharts.charts import Map
from pyecharts.faker import Faker


class TestMapChart(unittest.TestCase):
    @patch("pyecharts.render.engine.write_utf8_html_file")
    def test_map_base(self, fake_writer):
        c = Map().add(
            "商家A", [list(z) for z in zip(Faker.provinces, Faker.values())], "china"
        )
        c.render()
        _, content = fake_writer.call_args[0]
        self.assertEqual(c.theme, "white")
        self.assertEqual(c.renderer, "canvas")

    @patch("pyecharts.render.engine.write_utf8_html_file")
    def test_map_item_base(self, fake_writer):
        location_name = ["广东"]
        location_data = [[100, 200, 300, 400]]
        mock_data = [
            opts.MapItem(name=d[0], value=d[1])
            for d in list(zip(location_name, location_data))
        ]

        c = Map().add("商家A", mock_data, "china")
        c.render()
        _, content = fake_writer.call_args[0]
        self.assertEqual(c.theme, "white")
        self.assertEqual(c.renderer, "canvas")

    def test_map_emphasis(self):
        c = Map().add(
            "商家A",
            [list(z) for z in zip(Faker.provinces, Faker.values())],
            "china",
            emphasis_label_opts=opts.LabelOpts(is_show=False),
            emphasis_itemstyle_opts=opts.ItemStyleOpts(
                border_color="white", area_color="red"
            ),
        )
        options = json.loads(c.dump_options())
        expected = {
            "label": {
                "show": False,
                "richInheritPlainLabel": True,
                "margin": 8,
                "valueAnimation": False,
            },
            "itemStyle": {
                "borderColor": "white",
                "areaColor": "red",
            },
        }
        self.assertEqual(expected, options["series"][0]["emphasis"])

    def test_map_add_geo_json(self):
        # Arrange: dado sintético mínimo
        dummy_geo_json = {"type": "FeatureCollection", "features": []}

        # Act
        c = Map()
        c.add_geo_json(geo_json=dummy_geo_json)

        # Assert
        self.assertEqual(c._geo_json, dummy_geo_json)

