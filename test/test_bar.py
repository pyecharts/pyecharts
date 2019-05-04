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
                title="This is title.", subtitle="This is subtitle"
            )
        )
    )
    c.render("render.html")
    file_name, content = fake_writer.call_args[0]
    assert "render.html" == file_name
    assert "This is title." in content
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
