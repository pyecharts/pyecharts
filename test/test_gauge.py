from unittest.mock import patch

from nose.tools import assert_equal, assert_in

from pyecharts.charts import Gauge
from pyecharts import options as opts


@patch("pyecharts.render.engine.write_utf8_html_file")
def test_gauge_base(fake_writer):
    c = Gauge().add("", [("完成率", 66.6)])
    c.render()
    _, content = fake_writer.call_args[0]
    assert_equal(c.theme, "white")
    assert_equal(c.renderer, "canvas")


@patch("pyecharts.render.engine.write_utf8_html_file")
def test_gauage_label_setting(fake_writer):
    c = Gauge().add(
        "",
        [("完成率", 66.6)],
        detail_label_opts=opts.GaugeDetailOpts(formatter="{value}"),
        title_label_opts=opts.GaugeTitleOpts(
            font_size=40, color="blue", font_family="Microsoft YaHei"
        ),
    )
    c.render()
    _, content = fake_writer.call_args[0]
    assert_in("title", content)
    assert_in("detail", content)


@patch("pyecharts.render.engine.write_utf8_html_file")
def test_gauage_radius_setting(fake_writer):
    c = Gauge().add("", [("完成率", 66.6)], radius="50%")
    c.render()
    _, content = fake_writer.call_args[0]
    assert_in("radius", content)
