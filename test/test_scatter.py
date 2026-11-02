import json
import unittest
from unittest.mock import patch

from pyecharts import options as opts
from pyecharts.charts import Scatter, Grid
from pyecharts.commons.utils import JsCode
from pyecharts.faker import Faker


class TestScatterChart(unittest.TestCase):
    @patch("pyecharts.render.engine.write_utf8_html_file")
    def test_scatter_base(self, fake_writer):
        c = (
            Scatter()
            .add_xaxis(["A", "B", "C"])
            .add_yaxis("series0", [1, 2, 4])
            .add_yaxis("series1", [2, 3, 6])
        )
        c.render()
        _, content = fake_writer.call_args[0]
        self.assertEqual(c.theme, "white")
        self.assertEqual(c.renderer, "canvas")

    @patch("pyecharts.render.engine.write_utf8_html_file")
    def test_scatter_base_no_xaxis(self, fake_writer):
        c = (
            Scatter()
            .add_xaxis([])
            .add_yaxis("series0", [1, 2, 4])
            .add_yaxis("series1", [2, 3, 6])
        )
        c.render()
        _, content = fake_writer.call_args[0]
        self.assertEqual(c.theme, "white")
        self.assertEqual(c.renderer, "canvas")

    @patch("pyecharts.render.engine.write_utf8_html_file")
    def test_scatter_item_base(self, fake_writer):
        x_axis = ["A", "B", "C"]
        y_axis = [1, 2, 4]
        chart_item = [
            opts.ScatterItem(name=d[0], value=d[1]) for d in list(zip(x_axis, y_axis))
        ]

        c = (
            Scatter()
            .add_xaxis(x_axis)
            .add_yaxis("series0", chart_item)
            .set_global_opts(title_opts=opts.TitleOpts(title="Scatter-基本示例"))
        )
        c.render()
        _, content = fake_writer.call_args[0]
        self.assertEqual(c.theme, "white")
        self.assertEqual(c.renderer, "canvas")

    @patch("pyecharts.render.engine.write_utf8_html_file")
    def test_scatter_dataset(self, fake_writer):
        source = [["Income", "Life"], [1000, 70]]
        scatter = (
            Scatter()
            .add_dataset(source=source)
            .add_yaxis(
                series_name="",
                y_axis=[],
                encode={"x": "Income", "y": "Life"},
            )
        )
        grid = Grid().add(chart=scatter, grid_opts=opts.GridOpts())
        grid.render()
        _, content = fake_writer.call_args[0]
        self.assertIn("grid", content)



    @patch("pyecharts.render.engine.write_utf8_html_file")
    def test_scatter_multi_dimension_data(self, fake_writer):
        js_code_for_label_opts = JsCode(
            "function(params){return params.value[1] +' : '+ params.value[2];}"
        )
        js_code_for_tooltip = JsCode(
            "function (params) {return params.name + ' : ' + params.value[2];}"
        )
        c = (
            Scatter()
            .add_xaxis(Faker.choose())
            .add_yaxis(
                "商家A",
                [list(z) for z in zip(Faker.values(), Faker.choose())],
                label_opts=opts.LabelOpts(formatter=js_code_for_label_opts),
            )
            .set_global_opts(
                title_opts=opts.TitleOpts(title="Scatter-多维度数据"),
                tooltip_opts=opts.TooltipOpts(formatter=js_code_for_tooltip),
                visualmap_opts=opts.VisualMapOpts(
                    type_="color", max_=150, min_=20, dimension=1
                ),
            )
        )
        c.render()
        _, content = fake_writer.call_args[0]
        self.assertEqual(c.theme, "white")
        self.assertEqual(c.renderer, "canvas")
