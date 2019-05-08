from unittest.mock import patch

from nose.tools import assert_in, assert_not_in, eq_

from pyecharts import options as opts
from pyecharts.charts import Bar


def test_bar_base():
    c = (
        Bar()
        .add_xaxis(["A", "B", "C"])
        .add_yaxis("series0", [1, 2, 4])
        .add_yaxis("series1", [2, 3, 6])
    )
    eq_(c.theme, "white")
    eq_(c.renderer, "canvas")
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
    eq_("render.html", file_name)
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
    eq_("my_chart.html", file_name)
    assert_not_in("null", content)


@patch("pyecharts.render.engine.write_utf8_html_file")
def test_bar_default_remote_host(fake_writer):
    c = Bar().add_xaxis(["A", "B", "C"]).add_yaxis("series0", [1, 2, 4])
    c.render()
    eq_(c.js_host, "https://assets.pyecharts.org/assets/")
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
    eq_(c.js_host, "http://localhost:8000/assets/")
    _, content = fake_writer.call_args[0]
    assert_in("http://localhost:8000/assets/echarts.min.js", content)
