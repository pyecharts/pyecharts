import re
import sys
import unittest
from io import StringIO
from test import stdout_redirect
from unittest.mock import patch

from pyecharts import options as opts
from pyecharts.charts import Bar
from pyecharts.commons.utils import JsCode
from pyecharts.globals import CurrentConfig, NotebookType, ThemeType
from pyecharts.render.display import HTML


class TestBarChart(unittest.TestCase):

    @patch("pyecharts.render.engine.write_utf8_html_file")
    def test_bar_base(self, fake_writer):
        c = (
            Bar()
            .add_xaxis(["A", "B", "C"])
            .add_yaxis("series0", [1, 2, 4])
            .add_yaxis("series1", [2, 3, 6])
        )
        c.render()
        _, content = fake_writer.call_args[0]
        self.assertGreater(len(content), 2000)
        self.assertEqual(c.theme, "white")
        self.assertEqual(c.renderer, "canvas")

    @patch("pyecharts.render.engine.write_utf8_html_file")
    def test_bar_item_base(self, fake_writer):
        x_axis = ["A", "B", "C"]
        bar_item_1 = [
            opts.BarItem(name=d[0], value=d[1]) for d in list(zip(x_axis, [1, 2, 3]))
        ]
        bar_item_2 = [
            opts.BarItem(name=d[0], value=d[1]) for d in list(zip(x_axis, [4, 5, 6]))
        ]

        c = (
            Bar()
            .add_xaxis(x_axis)
            .add_yaxis("series0", bar_item_1)
            .add_yaxis("series1", bar_item_2)
        )
        c.render()
        _, content = fake_writer.call_args[0]
        self.assertGreater(len(content), 2000)
        self.assertEqual(c.theme, "white")
        self.assertEqual(c.renderer, "canvas")

    @patch("pyecharts.render.engine.write_utf8_html_file")
    def test_bar_item_show_label_line(self, fake_writer):
        x_axis = ["A", "B", "C"]
        bar_item_1 = [
            opts.BarItem(name=d[0], value=d[1], is_show_label_line=True)
            for d in list(zip(x_axis, [1, 2, 3]))
        ]
        bar_item_2 = [
            opts.BarItem(name=d[0], value=d[1], is_show_label_line=True)
            for d in list(zip(x_axis, [4, 5, 6]))
        ]

        c = (
            Bar()
            .add_xaxis(x_axis)
            .add_yaxis("series0", bar_item_1)
            .add_yaxis("series1", bar_item_2)
        )
        c.render()
        _, content = fake_writer.call_args[0]
        self.assertGreater(len(content), 2000)
        self.assertEqual(c.theme, "white")
        self.assertEqual(c.renderer, "canvas")

    @patch("pyecharts.render.engine.write_utf8_html_file")
    def test_bar_base_with_animation(self, fake_writer):
        c = (
            Bar(
                init_opts=opts.InitOpts(
                    animation_opts=opts.AnimationOpts(animation_delay=1000)
                )
            )
            .add_xaxis(["A", "B", "C"])
            .add_yaxis("series0", [1, 2, 4])
            .add_yaxis("series1", [2, 3, 6])
        )
        c.render()
        _, content = fake_writer.call_args[0]
        self.assertIn("animationDelay", content)

    @patch("pyecharts.render.engine.write_utf8_html_file")
    def test_bar_base_with_custom_background_image(self, fake_writer):
        c = (
            Bar(
                init_opts=opts.InitOpts(
                    bg_color={
                        "type": "pattern",
                        "image": JsCode("img"),
                        "repeat": "no-repeat",
                    }
                )
            )
            .add_xaxis(["A", "B", "C"])
            .add_yaxis("series0", [1, 2, 4])
            .add_yaxis("series1", [2, 3, 6])
            .set_global_opts(
                title_opts=opts.TitleOpts(
                    title="Bar-背景图基本示例",
                    subtitle="我是副标题",
                    title_textstyle_opts=opts.TextStyleOpts(color="white"),
                )
            )
        )
        c.add_js_funcs(
            """
            var img = new Image(); img.src = 'https://s2.ax1x.com/2019/07/08/ZsS0fK.jpg';
            """
        )
        c.render()
        _, content = fake_writer.call_args[0]
        self.assertIn("image", content)

    @patch("pyecharts.render.engine.write_utf8_html_file")
    def test_bar_base_dict_config(self, fake_writer):
        c = (
            Bar({"theme": ThemeType.MACARONS})
            .add_xaxis(["A", "B", "C"])
            .add_yaxis("series0", [1, 2, 4])
            .add_yaxis("series1", [2, 3, 6])
            .set_global_opts(
                title_opts={
                    "text": "Bar-dict-setting",
                    "subtext": "subtext also set by dict",
                }
            )
        )
        c.render()
        _, content = fake_writer.call_args[0]
        self.assertEqual(c.theme, "macarons")
        self.assertEqual(c.renderer, "canvas")
        self.assertIn("Bar-dict-setting", content)
        self.assertIn("subtext also set by dict", content)

    @patch("pyecharts.render.engine.write_utf8_html_file")
    def test_bar_colors(self, fake_writer):
        c = Bar().add_xaxis(["A", "B", "C"]).add_yaxis("series0", [1, 2, 4])
        c.set_colors(["#AABBCC", "#BBCCDD", "#CCDDEE"] + c.colors)
        c.render()
        _, content = fake_writer.call_args[0]
        self.assertIn("#AABBCC", content)
        self.assertIn("#BBCCDD", content)
        self.assertIn("#CCDDEE", content)

    @patch("pyecharts.render.engine.write_utf8_html_file")
    def test_bar_series_stack(self, fake_writer):
        c = (
            Bar()
            .add_xaxis(["A", "B", "C"])
            .add_yaxis("series0", [1, 2, 4])
            .add_yaxis("series1", [2, 3, 6])
            .add_yaxis("series2", [5, 8, 7])
            .set_series_opts(stack="MY_STACK_NAME")
        )
        c.render()
        _, content = fake_writer.call_args[0]
        stack_cnt = re.findall("MY_STACK_NAME", content)
        self.assertEqual(3, len(stack_cnt))

    @patch("pyecharts.render.engine.write_utf8_html_file")
    def test_bar_title_options(self, fake_writer):
        c = (
            Bar()
            .add_xaxis(["A", "B", "C"])
            .add_yaxis("series0", [1, 2, 4])
            .set_global_opts(
                title_opts=opts.TitleOpts(
                    title="This is title.", subtitle="This is subtitle."
                )
            )
        )
        c.render()
        file_name, content = fake_writer.call_args[0]
        self.assertEqual("render.html", file_name)
        self.assertIn("This is title.", content)
        self.assertIn("This is subtitle.", content)
        self.assertNotIn("null", content)

    @patch("pyecharts.render.engine.write_utf8_html_file")
    def test_bar_default_set_function(self, fake_writer):
        c = (
            Bar()
            .add_xaxis(["A", "B", "C"])
            .add_yaxis("series0", [1, 2, 4])
            .set_global_opts()
            .set_series_opts()
        )

        c.render("my_chart.html")
        file_name, content = fake_writer.call_args[0]
        self.assertEqual("my_chart.html", file_name)
        self.assertNotIn("null", content)

    @patch("pyecharts.render.engine.write_utf8_html_file")
    def test_bar_default_remote_host(self, fake_writer):
        c = Bar().add_xaxis(["A", "B", "C"]).add_yaxis("series0", [1, 2, 4])
        c.render()
        self.assertEqual(c.js_host, "https://assets.pyecharts.org/assets/v5/")
        _, content = fake_writer.call_args[0]
        self.assertIn("https://assets.pyecharts.org/assets/v5/echarts.min.js", content)

    @patch("pyecharts.render.engine.write_utf8_html_file")
    def test_bar_custom_remote_host(self, fake_writer):
        c = (
            Bar(init_opts=opts.InitOpts(js_host="http://localhost:8000/assets/"))
            .add_xaxis(["A", "B", "C"])
            .add_yaxis("series0", [1, 2, 4])
        )
        c.render()
        self.assertEqual(c.js_host, "http://localhost:8000/assets/")
        _, content = fake_writer.call_args[0]
        self.assertIn("http://localhost:8000/assets/echarts.min.js", content)

    @patch("pyecharts.render.engine.write_utf8_html_file")
    def test_bar_graphic(self, fake_writer):
        c = (
            Bar()
            .add_xaxis(["A", "B", "C"])
            .add_yaxis("series0", [1, 2, 4])
            .set_global_opts(
                graphic_opts=[
                    opts.GraphicImage(
                        graphic_item=opts.GraphicItem(
                            id_="logo",
                            right=20,
                            top=20,
                            z=-10,
                            bounding="raw",
                            origin=[75, 75],
                        ),
                        graphic_imagestyle_opts=opts.GraphicImageStyleOpts(
                            image="http://echarts.baidu.com/images/favicon.png",
                            width=150,
                            height=150,
                            opacity=0.4,
                            graphic_basicstyle_opts=opts.GraphicBasicStyleOpts(),
                        ),
                    )
                ]
            )
        )
        c.render()
        file_name, content = fake_writer.call_args[0]
        self.assertEqual("render.html", file_name)
        self.assertIn("graphic", content)

    @patch("pyecharts.render.engine.write_utf8_html_file")
    def test_bar_graphic_v1(self, fake_writer):
        c = (
            Bar()
            .add_xaxis(["A", "B", "C"])
            .add_yaxis("series0", [1, 2, 4])
            .set_global_opts(
                graphic_opts=[
                    opts.GraphicImage(
                        graphic_item=opts.GraphicItem(
                            id_="logo",
                            right=20,
                            top=20,
                            z=-10,
                            bounding="raw",
                            origin=[75, 75],
                        ),
                        graphic_imagestyle_opts=opts.GraphicImageStyleOpts(
                            image="http://echarts.baidu.com/images/favicon.png",
                            width=150,
                            height=150,
                            opacity=0.4,
                        ),
                    )
                ]
            )
        )
        c.render()
        file_name, content = fake_writer.call_args[0]
        self.assertEqual("render.html", file_name)
        self.assertIn("graphic", content)

    def test_bar_render_nteract(self):
        CurrentConfig.NOTEBOOK_TYPE = NotebookType.NTERACT
        c = (
            Bar()
            .add_xaxis(["A", "B", "C"])
            .add_yaxis("series0", [1, 2, 4])
            .add_yaxis("series1", [2, 3, 6])
        )
        nteract_code = c.render_notebook()
        self.assertEqual(isinstance(nteract_code, HTML), True)

    def test_bar_render_zeppelin(self):
        CurrentConfig.NOTEBOOK_TYPE = NotebookType.ZEPPELIN
        c = (
            Bar()
            .add_xaxis(["A", "B", "C"])
            .add_yaxis("series0", [1, 2, 4])
            .add_yaxis("series1", [2, 3, 6])
        )
        # Block Console stdout
        stdout_redirect.fp = StringIO()
        temp_stdout, sys.stdout = sys.stdout, stdout_redirect

        # render
        c.render_notebook()
        sys.stdout = temp_stdout

        # Block Result
        self.assertIn("%html", stdout_redirect.fp.getvalue())

    @patch("pyecharts.render.engine.write_utf8_html_file")
    def test_bar_with_brush(self, fake_writer):
        c = (
            Bar()
            .add_xaxis(["A", "B", "C"])
            .add_yaxis("series0", [1, 2, 4])
            .add_yaxis("series1", [2, 3, 6])
            .set_global_opts(
                title_opts=opts.TitleOpts(title="Bar-Brush示例", subtitle="我是副标题"),
                brush_opts=opts.BrushOpts(),
            )
        )
        c.render()
        _, content = fake_writer.call_args[0]
        self.assertIn("brush", content)

    @patch("pyecharts.render.engine.write_utf8_html_file")
    def test_bar_add_dataset(self, fake_writer):
        c = (
            Bar()
            .add_dataset(
                source=[
                    ["product", "2015", "2016", "2017"],
                    ["Matcha Latte", 43.3, 85.8, 93.7],
                    ["Milk Tea", 83.1, 73.4, 55.1],
                    ["Cheese Cocoa", 86.4, 65.2, 82.5],
                    ["Walnut Brownie", 72.4, 53.9, 39.1],
                ]
            )
            .add_yaxis(series_name="2015", y_axis=[])
            .add_yaxis(series_name="2016", y_axis=[])
            .add_yaxis(series_name="2017", y_axis=[])
            .set_global_opts(
                title_opts=opts.TitleOpts(title="Dataset simple bar example"),
                xaxis_opts=opts.AxisOpts(type_="category"),
            )
        )
        c.render()
        _, content = fake_writer.call_args[0]
        self.assertIn("dataset", content)
