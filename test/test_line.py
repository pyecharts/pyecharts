from unittest.mock import patch

from nose.tools import assert_equal, assert_in

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
    assert_equal(c.theme, "white")
    assert_equal(c.renderer, "canvas")


@patch("pyecharts.render.engine.write_utf8_html_file")
def test_set_global_opts(fake_writer):
    test_type, test_range = "test_type", [-10001, 10001]
    c = (
        Line()
        .set_global_opts(
            xaxis_opts=opts.AxisOpts(is_inverse=True),
            datazoom_opts=opts.DataZoomOpts(type_=test_type),
            visualmap_opts=opts.VisualMapOpts(type_="size", range_size=test_range),
        )
        .add_xaxis(["A", "B", "C"])
        .add_yaxis("series0", [1, 2, 4])
        .add_yaxis("series1", [2, 3, 6])
    )
    c.render()
    _, content = fake_writer.call_args[0]
    assert_in('"inverse": true', content)
    assert_in("test_type", content)
    assert_in("-10001", content)


@patch("pyecharts.render.engine.write_utf8_html_file")
def test_data_label_none_animation_opts(fake_writer):
    c = (
        Line()
        .add_xaxis(["A", "B", "C"])
        .add_yaxis("series0", [1, 2, 4], is_hover_animation=False)
        .add_yaxis("series1", [2, 3, 6], is_hover_animation=False)
    )
    c.render()
    _, content = fake_writer.call_args[0]
    assert_in("hoverAnimation", content)
