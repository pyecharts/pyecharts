from unittest.mock import patch

from pyecharts import options as opts
from pyecharts.charts import Bar


def test_bar_base():
    c = (
        Bar()
        .add_xaxis(["A", "B", "C"])
        .add_yaxis("series0", [1, 2, 4])
        .add_yaxis("series1", [2, 3, 6])
    )
    assert c.theme == "white"
    assert c.renderer == "canvas"
    c.render("render.html")


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
    c.render("render.html")
    file_name, content = fake_writer.call_args[0]
    assert "render.html" == file_name
    assert "This is title." in content
    assert "This is subtitle." in content
    assert "null" not in content


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
    assert "my_chart.html" == file_name
    assert "null" not in content


@patch("pyecharts.render.engine.write_utf8_html_file")
def test_bar_default_remote_host(fake_writer):
    c = Bar().add_xaxis(["A", "B", "C"]).add_yaxis("series0", [1, 2, 4])
    c.render()
    assert c.js_host == "https://assets.pyecharts.org/assets/"
    _, content = fake_writer.call_args[0]
    assert "https://assets.pyecharts.org/assets/echarts.min.js" in content


@patch("pyecharts.render.engine.write_utf8_html_file")
def test_bar_custom_remote_host(fake_writer):
    c = (
        Bar(init_opts=opts.InitOpts(js_host="http://localhost:8000/assets/"))
        .add_xaxis(["A", "B", "C"])
        .add_yaxis("series0", [1, 2, 4])
    )
    c.render()
    assert c.js_host == "http://localhost:8000/assets/"
    _, content = fake_writer.call_args[0]
    assert "http://localhost:8000/assets/echarts.min.js" in content
