from unittest.mock import patch

from nose.tools import eq_

from pyecharts.charts import Gauge


@patch("pyecharts.render.engine.write_utf8_html_file")
def test_gauge_base(fake_writer):
    c = Gauge().add("", [("完成率", 66.6)])
    c.render()
    _, content = fake_writer.call_args[0]
    eq_(c.theme, "white")
    eq_(c.renderer, "canvas")
