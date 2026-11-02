import unittest
from unittest.mock import patch

from pyecharts import options as opts
from pyecharts.charts import Geo
from pyecharts.faker import Faker
from pyecharts.globals import ChartType, SymbolType


class TestGeoChart(unittest.TestCase):
    @patch("pyecharts.render.engine.write_utf8_html_file")
    def test_geo_base(self, fake_writer):
        c = (
            Geo()
            .add_schema(maptype="china")
            .add("geo", [list(z) for z in zip(Faker.provinces, Faker.values())])
            .set_series_opts(label_opts=opts.LabelOpts(is_show=False))
            .set_global_opts(visualmap_opts=opts.VisualMapOpts())
        )
        self.assertEqual(c.theme, "white")
        c.render()
        _, content = fake_writer.call_args[0]
        self.assertIn("canvas", content)

    def test_geo_add_coord_json(self):
        c = (
            Geo()
            .add_schema(maptype="china")
            .add_coordinate_json(json_file="test/fixtures/city_coordinates.json")
            .add("geo", [list(z) for z in zip(Faker.provinces, Faker.values())])
            .set_series_opts(label_opts=opts.LabelOpts(is_show=False))
            .set_global_opts(visualmap_opts=opts.VisualMapOpts())
        )
        self.assertEqual(c.theme, "white")

    @patch("pyecharts.render.engine.write_utf8_html_file")
    def test_geo_custom(self, fake_writer):
        c = (
            Geo()
            .add_schema(maptype="china")
            .add(
                "geo",
                [list(z) for z in zip(Faker.provinces, Faker.values())],
                type_=ChartType.CUSTOM,
            )
            .set_series_opts(label_opts=opts.LabelOpts(is_show=False))
            .set_global_opts(title_opts=opts.TitleOpts(title="Geo-EffectScatter"))
        )
        self.assertEqual(c.theme, "white")
        c.render()
        _, content = fake_writer.call_args[0]
        self.assertIn("canvas", content)

    @patch("pyecharts.render.engine.write_utf8_html_file")
    def test_geo_effectscatter(self, fake_writer):
        c = (
            Geo()
            .add_schema(maptype="china")
            .add(
                "geo",
                [list(z) for z in zip(Faker.provinces, Faker.values())],
                type_=ChartType.EFFECT_SCATTER,
            )
            .set_series_opts(label_opts=opts.LabelOpts(is_show=False))
            .set_global_opts(title_opts=opts.TitleOpts(title="Geo-EffectScatter"))
        )
        self.assertEqual(c.theme, "white")
        c.render()
        _, content = fake_writer.call_args[0]
        self.assertIn("canvas", content)

    @patch("pyecharts.render.engine.write_utf8_html_file")
    def test_geo_heatmap(self, fake_writer):
        c = (
            Geo()
            .add_schema(maptype="china")
            .add(
                "geo",
                [list(z) for z in zip(Faker.provinces, Faker.values())],
                type_=ChartType.HEATMAP,
            )
            .set_series_opts(label_opts=opts.LabelOpts(is_show=False))
            .set_global_opts(
                visualmap_opts=opts.VisualMapOpts(),
                title_opts=opts.TitleOpts(title="Geo-HeatMap"),
            )
        )
        self.assertEqual(c.theme, "white")
        c.render()
        _, content = fake_writer.call_args[0]
        self.assertIn("canvas", content)

    @patch("pyecharts.render.engine.write_utf8_html_file")
    def test_geo_lines(self, fake_writer):
        c = (
            Geo()
            .add_schema(maptype="china")
            .add(
                "",
                [("广州", 55), ("北京", 66), ("杭州", 77), ("重庆", 88)],
                type_=ChartType.EFFECT_SCATTER,
                color="white",
            )
            .add(
                "geo",
                [
                    ("广州", "上海"),
                    ("广州", "北京"),
                    ("广州", "杭州"),
                    ("广州", "重庆"),
                ],
                type_=ChartType.LINES,
                effect_opts=opts.EffectOpts(
                    symbol=SymbolType.ARROW, symbol_size=6, color="blue"
                ),
                linestyle_opts=opts.LineStyleOpts(curve=0.2),
            )
            .set_series_opts(label_opts=opts.LabelOpts(is_show=False))
            .set_global_opts(title_opts=opts.TitleOpts(title="Geo-Lines"))
        )
        self.assertEqual(c.theme, "white")
        c.render()
        _, content = fake_writer.call_args[0]
        self.assertIn("canvas", content)

    @patch("pyecharts.render.engine.write_utf8_html_file")
    def test_extra_geo_parameters(self, fake_writer):
        c = (
            Geo()
            .add_schema(maptype="china", center=[39, 117.7], zoom=9)
            .add("geo", [list(z) for z in zip(Faker.provinces, Faker.values())])
            .set_series_opts(label_opts=opts.LabelOpts(is_show=False))
            .set_global_opts(visualmap_opts=opts.VisualMapOpts())
        )
        self.assertEqual(c.theme, "white")
        self.assertEqual(c.renderer, "canvas")
        c.render()
        _, content = fake_writer.call_args[0]
        center_string = "center"
        self.assertIn(center_string, content)
        self.assertIn('"zoom": 9', content)

    @staticmethod
    def _geo_chart() -> Geo:
        return (
            Geo()
            .add_schema(maptype="china", center=[39, 117.7], zoom=9)
            .add("geo", [list(z) for z in zip(Faker.provinces, Faker.values())])
            .set_global_opts(visualmap_opts=opts.VisualMapOpts())
        )

    def test_geo_dump_options(self):
        c = self._geo_chart()
        formatter = """"formatter": function (params) {        return params.name + ' : ' + params.value[2];    }"""  # noqa
        self.assertIn(formatter, c.dump_options())

    def test_geo_dump_options_with_quotes(self):
        c = self._geo_chart()
        formatter = """"formatter": "function (params) {        return params.name + ' : ' + params.value[2];    }"""  # noqa
        self.assertIn(formatter, c.dump_options_with_quotes())

    def test_geo_add_geo_json(self):
        dummy_geo_json = {"type": "FeatureCollection", "features": []}
        c = Geo()
        c.add_geo_json(geo_json=dummy_geo_json)
        self.assertEqual(c._geo_json, dummy_geo_json)

    @patch("pyecharts.render.engine.write_utf8_html_file")
    def test_geo_scatter_gl(self, fake_writer):
        c = (
            Geo()
            .add_schema(maptype="china")
            .add(
                "geo",
                [list(z) for z in zip(Faker.provinces, Faker.values())],
                type_=ChartType.SCATTERGL,
            )
            .set_series_opts(label_opts=opts.LabelOpts(is_show=False))
            .set_global_opts(visualmap_opts=opts.VisualMapOpts())
        )
        self.assertEqual(c.theme, "white")
        c.render()
        _, content = fake_writer.call_args[0]
        self.assertIn("canvas", content)

    @patch("pyecharts.render.engine.write_utf8_html_file")
    def test_geo_lines_gl(self, fake_writer):
        c = (
            Geo()
            .add_schema(maptype="china")
            .add(
                "geo",
                [list(z) for z in zip(Faker.provinces, Faker.values())],
                type_=ChartType.LINESGL,
            )
            .set_series_opts(label_opts=opts.LabelOpts(is_show=False))
            .set_global_opts(visualmap_opts=opts.VisualMapOpts())
        )
        self.assertEqual(c.theme, "white")
        c.render()
        _, content = fake_writer.call_args[0]
        self.assertIn("canvas", content)

    @patch("pyecharts.render.engine.write_utf8_html_file")
    def test_geo_flow_gl(self, fake_writer):
        c = (
            Geo()
            .add_schema(maptype="china")
            .add(
                "geo",
                [list(z) for z in zip(Faker.provinces, Faker.values())],
                type_=ChartType.FLOWGL,
            )
            .set_series_opts(label_opts=opts.LabelOpts(is_show=False))
            .set_global_opts(visualmap_opts=opts.VisualMapOpts())
        )
        self.assertEqual(c.theme, "white")
        c.render()
        _, content = fake_writer.call_args[0]
        self.assertIn("canvas", content)

    @patch("pyecharts.render.engine.write_utf8_html_file")
    def test_geo_pie(self, fake_writer):
        c = (
            Geo()
            .add_schema(maptype="china")
            .add(
                series_name="广东省",
                data_pair=[("A", 10), ("B", 20), ("C", 30), ("D", 50)],
                type_=ChartType.PIE,
            )
            .set_global_opts(title_opts=opts.TitleOpts(title="Geo-Pie"), legend_opts={})
        )
        self.assertEqual(c.theme, "white")
        c.render()
        _, content = fake_writer.call_args[0]
        self.assertIn("canvas", content)

    @patch("pyecharts.render.engine.write_utf8_html_file")
    def test_geo_item_base(self, fake_writer):
        data_pair = [
            opts.GeoItem(longitude=121.97, latitude=30.88, name="公园", value=12),
        ]
        c = (
            Geo()
            .add_schema(maptype="china")
            .add(series_name="测试数据", data_pair=data_pair)
            .set_global_opts(
                visualmap_opts=opts.VisualMapOpts(),
                title_opts=opts.TitleOpts(title="Geo-基本示例"),
            )
        )
        c.render()
        _, content = fake_writer.call_args[0]
        self.assertEqual(c.theme, "white")
        self.assertEqual(c.renderer, "canvas")
