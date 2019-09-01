import re
import sys
from io import StringIO
from test import stdout_redirect
from unittest.mock import patch

from nose.tools import assert_equal, assert_greater, assert_in, assert_not_in

from pyecharts import options as opts
from pyecharts.charts import Bar
from pyecharts.commons.utils import JsCode
from pyecharts.globals import CurrentConfig, NotebookType, ThemeType
from pyecharts.render.display import HTML


@patch("pyecharts.render.engine.write_utf8_html_file")
def test_bar_base(fake_writer):
    c = (
        Bar()
        .add_xaxis(["A", "B", "C"])
        .add_yaxis("series0", [1, 2, 4])
        .add_yaxis("series1", [2, 3, 6])
    )
    c.render()
    _, content = fake_writer.call_args[0]
    assert_greater(len(content), 2000)
    assert_equal(c.theme, "white")
    assert_equal(c.renderer, "canvas")


@patch("pyecharts.render.engine.write_utf8_html_file")
def test_bar_base_with_animation(fake_writer):
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
    assert_in("animationDelay", content)


@patch("pyecharts.render.engine.write_utf8_html_file")
def test_bar_base_with_custom_background_image(fake_writer):
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
    assert_in("image", content)


@patch("pyecharts.render.engine.write_utf8_html_file")
def test_bar_base_dict_config(fake_writer):
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
    assert_equal(c.theme, "macarons")
    assert_equal(c.renderer, "canvas")
    assert_in("Bar-dict-setting", content)
    assert_in("subtext also set by dict", content)


@patch("pyecharts.render.engine.write_utf8_html_file")
def test_bar_colors(fake_writer):
    c = Bar().add_xaxis(["A", "B", "C"]).add_yaxis("series0", [1, 2, 4])
    c.set_colors(["#AABBCC", "#BBCCDD", "#CCDDEE"] + c.colors)
    c.render()
    _, content = fake_writer.call_args[0]
    assert_in("#AABBCC", content)
    assert_in("#BBCCDD", content)
    assert_in("#CCDDEE", content)


@patch("pyecharts.render.engine.write_utf8_html_file")
def test_bar_series_stack(fake_writer):
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
    assert_equal(3, len(stack_cnt))


@patch("pyecharts.render.engine.write_utf8_html_file")
def test_bar_title_options(fake_writer):
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
    assert_equal("render.html", file_name)
    assert_in("This is title.", content)
    assert_in("This is subtitle.", content)
    assert_not_in("null", content)


@patch("pyecharts.render.engine.write_utf8_html_file")
def test_bar_default_set_function(fake_writer):
    c = (
        Bar()
        .add_xaxis(["A", "B", "C"])
        .add_yaxis("series0", [1, 2, 4])
        .set_global_opts()
        .set_series_opts()
    )

    c.render("my_chart.html")
    file_name, content = fake_writer.call_args[0]
    assert_equal("my_chart.html", file_name)
    assert_not_in("null", content)


@patch("pyecharts.render.engine.write_utf8_html_file")
def test_bar_default_remote_host(fake_writer):
    c = Bar().add_xaxis(["A", "B", "C"]).add_yaxis("series0", [1, 2, 4])
    c.render()
    assert_equal(c.js_host, "https://assets.pyecharts.org/assets/")
    _, content = fake_writer.call_args[0]
    assert_in("https://assets.pyecharts.org/assets/echarts.min.js", content)


@patch("pyecharts.render.engine.write_utf8_html_file")
def test_bar_custom_remote_host(fake_writer):
    c = (
        Bar(init_opts=opts.InitOpts(js_host="http://localhost:8000/assets/"))
        .add_xaxis(["A", "B", "C"])
        .add_yaxis("series0", [1, 2, 4])
    )
    c.render()
    assert_equal(c.js_host, "http://localhost:8000/assets/")
    _, content = fake_writer.call_args[0]
    assert_in("http://localhost:8000/assets/echarts.min.js", content)


@patch("pyecharts.render.engine.write_utf8_html_file")
def test_bar_graphic(fake_writer):
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
    assert_equal("render.html", file_name)
    assert_in("graphic", content)


def test_bar_render_nteract():
    CurrentConfig.NOTEBOOK_TYPE = NotebookType.NTERACT
    c = (
        Bar()
        .add_xaxis(["A", "B", "C"])
        .add_yaxis("series0", [1, 2, 4])
        .add_yaxis("series1", [2, 3, 6])
    )
    nteract_code = c.render_notebook()
    assert_equal(isinstance(nteract_code, HTML), True)


def test_bar_render_zeppelin():
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
    assert_in("%html", stdout_redirect.fp.getvalue())


@patch("pyecharts.render.engine.write_utf8_html_file")
def test_bar_with_brush(fake_writer):
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
    assert_in("brush", content)
