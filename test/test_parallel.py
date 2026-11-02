import unittest
from unittest.mock import patch

from pyecharts import options as opts
from pyecharts.charts import Parallel


class TestParallelChart(unittest.TestCase):
    @patch("pyecharts.render.engine.write_utf8_html_file")
    def test_parallel_base(self, fake_writer):
        data = [
            [1, 91, 45, 125, 0.82, 34],
            [2, 65, 27, 78, 0.86, 45],
            [3, 83, 60, 84, 1.09, 73],
            [4, 109, 81, 121, 1.28, 68],
            [5, 106, 77, 114, 1.07, 55],
            [6, 109, 81, 121, 1.28, 68],
        ]
        c = (
            Parallel()
            .add_schema(
                [
                    {"dim": 0, "name": "data"},
                    {"dim": 1, "name": "AQI"},
                    {"dim": 2, "name": "PM2.5"},
                    {"dim": 3, "name": "PM10"},
                    {"dim": 4, "name": "CO"},
                    {"dim": 5, "name": "NO2"},
                ]
            )
            .add("parallel", data)
        )
        c.render()
        _, content = fake_writer.call_args[0]
        self.assertEqual(c.theme, "white")
        self.assertEqual(c.renderer, "canvas")

    @patch("pyecharts.render.engine.write_utf8_html_file")
    def test_parallel_item_base(self, fake_writer):
        item_data = [
            opts.ParallelItem(value=[1, 91, 45, 125, 0.82, 34]),
            opts.ParallelItem(value=[2, 65, 27, 78, 0.86, 45]),
            opts.ParallelItem(value=[3, 83, 60, 84, 1.09, 73]),
            opts.ParallelItem(value=[4, 109, 81, 121, 1.28, 68]),
            opts.ParallelItem(value=[5, 106, 77, 114, 1.07, 55]),
            opts.ParallelItem(value=[6, 109, 81, 121, 1.28, 68]),
        ]

        c = (
            Parallel()
            .add_schema(
                [
                    {"dim": 0, "name": "data"},
                    {"dim": 1, "name": "AQI"},
                    {"dim": 2, "name": "PM2.5"},
                    {"dim": 3, "name": "PM10"},
                    {"dim": 4, "name": "CO"},
                    {"dim": 5, "name": "NO2"},
                ]
            )
            .add("parallel", item_data)
        )
        c.render()
        _, content = fake_writer.call_args[0]
        self.assertEqual(c.theme, "white")
        self.assertEqual(c.renderer, "canvas")

    @patch("pyecharts.render.engine.write_utf8_html_file")
    def test_parallel_base_v1(self, fake_writer):
        # Arrange: 1 dado de exemplo com 2 eixos (numérico e categórico)
        data = [[1, "A"]]
        schema = [
            opts.ParallelAxisOpts(dim=0, name="dim1"),
            opts.ParallelAxisOpts(dim=1, name="dim2", type_="category", data=["A", "B"]),
        ]

        # Act
        c = Parallel().add_schema(schema=schema).add("parallel", data)
        c.render()

        # Assert
        fake_writer.assert_called_once()
        self.assertEqual(len(c.options.get("parallelAxis")), 2)
        self.assertEqual(c.theme, "white")
        self.assertEqual(c.renderer, "canvas")

