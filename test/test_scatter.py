from unittest.mock import patch

from nose.tools import assert_equal

from pyecharts.charts import Scatter


@patch("pyecharts.render.engine.write_utf8_html_file")
def test_bar_base(fake_writer):
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
