from unittest.mock import patch

from nose.tools import assert_in, eq_

from pyecharts import options as opts
from pyecharts.charts import Line


@patch("pyecharts.render.engine.write_utf8_html_file")
def test_bar_base(fake_writer):
    c = (
        Line()
        .add_xaxis(["A", "B", "C"])
        .add_yaxis("series0", [1, 2, 4])
        .add_yaxis("series1", [2, 3, 6])
    )
    c.render()
    _, content = fake_writer.call_args[0]
    eq_(c.theme, "white")
    eq_(c.renderer, "canvas")


@patch("pyecharts.render.engine.write_utf8_html_file")
def test_set_global_opts(fake_writer):
    c = (
        Line()
        .set_global_opts(xaxis_opts=opts.AxisOpts(is_inverse=True))
        .add_xaxis(["A", "B", "C"])
        .add_yaxis("series0", [1, 2, 4])
        .add_yaxis("series1", [2, 3, 6])
    )
    c.render()
    _, content = fake_writer.call_args[0]
    assert_in('"inverse": true', content)
