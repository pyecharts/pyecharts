import unittest
from unittest.mock import patch

from pyecharts import options as opts
from pyecharts.charts import Sunburst


class TestSunburstChart(unittest.TestCase):
    @patch("pyecharts.render.engine.write_utf8_html_file")
    def test_sunburst_base(self, fake_writer):
        data = [
            {
                "name": "Grandpa",
                "children": [
                    {
                        "name": "Uncle Leo",
                        "value": 15,
                        "children": [
                            {"name": "Cousin Jack", "value": 2},
                            {
                                "name": "Cousin Mary",
                                "value": 5,
                                "children": [{"name": "Jackson", "value": 2}],
                            },
                            {"name": "Cousin Ben", "value": 4},
                        ],
                    },
                    {
                        "name": "Father",
                        "value": 10,
                        "children": [
                            {"name": "Me", "value": 5},
                            {"name": "Brother Peter", "value": 1},
                        ],
                    },
                ],
            },
            {
                "name": "Nancy",
                "children": [
                    {
                        "name": "Uncle Nike",
                        "children": [
                            {"name": "Cousin Betty", "value": 1},
                            {"name": "Cousin Jenny", "value": 2},
                        ],
                    }
                ],
            },
        ]

        c = Sunburst().add("Sunburst 演示数据", data)
        c.render()
        _, content = fake_writer.call_args[0]
        self.assertEqual(c.theme, "white")
        self.assertEqual(c.renderer, "canvas")

    def test_sunburst_dataitem(self):
        item_name = "test_data_item"
        item = opts.SunburstItem(name=item_name)
        self.assertEqual(item.opts.get("name"), item_name)
