from unittest.mock import patch

from nose.tools import assert_equal

from pyecharts import options as opts
from pyecharts.charts import Scatter


@patch("pyecharts.render.engine.write_utf8_html_file")
def test_scatter_base(fake_writer):
    c = (
        Scatter()
        .add_xaxis(["A", "B", "C"])
        .add_yaxis("series0", [1, 2, 4])
        .add_yaxis("series1", [2, 3, 6])
    )
    c.render()
    _, content = fake_writer.call_args[0]
    assert_equal(c.theme, "white")
    assert_equal(c.renderer, "canvas")


@patch("pyecharts.render.engine.write_utf8_html_file")
def test_scatter_item_base(fake_writer):
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
    assert_equal(c.theme, "white")
    assert_equal(c.renderer, "canvas")
