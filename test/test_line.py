from unittest.mock import patch

from nose.tools import assert_equal, assert_in

from pyecharts import options as opts
from pyecharts.charts import Line


@patch("pyecharts.render.engine.write_utf8_html_file")
def test_line_base(fake_writer):
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
def test_line_with_emphasis(fake_writer):
    c = (
        Line()
        .add_xaxis(["A", "B", "C"])
        .add_yaxis("series0", [1, 2, 4], emphasis_opts=opts.EmphasisOpts())
        .add_yaxis("series1", [2, 3, 6], emphasis_opts=opts.EmphasisOpts())
    )
    c.render()
    _, content = fake_writer.call_args[0]
    assert_equal(c.theme, "white")
    assert_equal(c.renderer, "canvas")
    assert_in("emphasis", content)


@patch("pyecharts.render.engine.write_utf8_html_file")
def test_line_item_base(fake_writer):
    x_axis = ["A", "B", "C"]
    y_axis_0 = [1, 2, 4]
    line_item_0 = [
        opts.LineItem(name=d[0], value=d[1]) for d in list(zip(x_axis, y_axis_0))
    ]
    y_axis_1 = [2, 3, 6]
    line_item_1 = [
        opts.LineItem(name=d[0], value=d[1]) for d in list(zip(x_axis, y_axis_1))
    ]

    c = (
        Line()
        .add_xaxis(x_axis)
        .add_yaxis("series0", line_item_0)
        .add_yaxis("series1", line_item_1)
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


@patch("pyecharts.render.engine.write_utf8_html_file")
def test_line_opts_with_zlevel_z(fake_writer):
    c = (
        Line()
        .add_xaxis(["A", "B", "C"])
        .add_yaxis("series0", [1, 2, 4])
        .add_yaxis("series1", [2, 3, 6], z_level=2, z=1)
    )
    c.render()
    _, content = fake_writer.call_args[0]
    assert_in("zlevel", content)
    assert_in("z", content)


def test_line_dataset():
    c = (
        Line()
        .add_dataset(
            source=[
                ["product", "2012", "2013", "2014", "2015", "2016", "2017"],
                ["Milk Tea", 56.5, 82.1, 88.7, 70.1, 53.4, 85.1],
                ["Matcha Latte", 51.1, 51.4, 55.1, 53.3, 73.8, 68.7],
                ["Cheese Cocoa", 40.1, 62.2, 69.5, 36.4, 45.2, 32.5],
                ["Walnut Brownie", 25.2, 37.1, 41.2, 18, 33.9, 49.1],
            ]
        )
        .add_yaxis(
            series_name="Milk Tea",
            y_axis=[],
            is_smooth=True,
            series_layout_by="row",
        )
        .add_yaxis(
            series_name="Matcha Latte",
            y_axis=[],
            is_smooth=True,
            series_layout_by="row",
        )
        .add_yaxis(
            series_name="Cheese Cocoa",
            y_axis=[],
            is_smooth=True,
            series_layout_by="row",
        )
        .add_yaxis(
            series_name="Walnut Brownie",
            y_axis=[],
            is_smooth=True,
            series_layout_by="row",
        )
        .set_global_opts(
            title_opts=opts.TitleOpts(title="Dataset Line Example"),
            xaxis_opts=opts.AxisOpts(type_="category"),
        )
    )
    assert_equal(c.options.get("series")[0].get("data"), None)
