from unittest.mock import patch

from nose.tools import assert_equal

from pyecharts.charts import Gauge


@patch("pyecharts.render.engine.write_utf8_html_file")
def test_gauge_base(fake_writer):
    c = Gauge().add("", [("完成率", 66.6)])
    c.render()
    _, content = fake_writer.call_args[0]
    assert_equal(c.theme, "white")
    assert_equal(c.renderer, "canvas")
