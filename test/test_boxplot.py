from unittest.mock import patch

from nose.tools import assert_equal, assert_in

from pyecharts import options as opts
from pyecharts.charts import Boxplot


@patch("pyecharts.render.engine.write_utf8_html_file")
def test_boxplot_base(fake_writer):
    v1 = [
        [850, 740, 900, 1070, 930, 850, 950, 980, 980, 880, 1000, 980],
        [960, 940, 960, 940, 880, 800, 850, 880, 900, 840, 830, 790],
    ]
    v2 = [
        [890, 810, 810, 820, 800, 770, 760, 740, 750, 760, 910, 920],
        [890, 840, 780, 810, 760, 810, 790, 810, 820, 850, 870, 870],
    ]
    c = Boxplot()
    c.add_xaxis(["expr1", "expr2"]).add_yaxis(
        "A", c.prepare_data(v1), box_width=40
    ).add_yaxis("B", c.prepare_data(v2))
    c.render()
    _, content = fake_writer.call_args[0]
    assert_equal(c.theme, "white")
    assert_equal(c.renderer, "canvas")
    assert_in("boxWidth", content)


@patch("pyecharts.render.engine.write_utf8_html_file")
def test_boxplot_base_v1(fake_writer):
    v1 = [
        [1000, 1000, 1000],
        [200, 200, 200],
    ]
    v2 = [
        [1000, 1000, 1000],
        [200, 200, 200],
    ]
    c = Boxplot()
    c.add_xaxis(["expr1", "expr2"]).add_yaxis(
        "A", c.prepare_data(v1), box_width=40
    ).add_yaxis("B", c.prepare_data(v2))
    c.render()
    _, content = fake_writer.call_args[0]
    assert_equal(c.theme, "white")
    assert_equal(c.renderer, "canvas")
    assert_in("boxWidth", content)


@patch("pyecharts.render.engine.write_utf8_html_file")
def test_boxplot_base_v2(fake_writer):
    v1 = [
        None,
        [200, 200, 200],
    ]
    v2 = [
        [1000, None, 1000],
        [200, 200, 200],
    ]
    c = Boxplot()
    c.add_xaxis(["expr1", "expr2"]).add_yaxis(
        "A", c.prepare_data(v1), box_width=40
    ).add_yaxis("B", c.prepare_data(v2))
    c.render()
    _, content = fake_writer.call_args[0]
    assert_equal(c.theme, "white")
    assert_equal(c.renderer, "canvas")
    assert_in("boxWidth", content)


@patch("pyecharts.render.engine.write_utf8_html_file")
def test_boxplot_item_base(fake_writer):
    x_axis = ["expr1", "expr2"]
    v1 = [
        [850, 740, 900, 1070, 930, 850, 950, 980, 980, 880, 1000, 980],
        [960, 940, 960, 940, 880, 800, 850, 880, 900, 840, 830, 790],
    ]
    v2 = [
        [890, 810, 810, 820, 800, 770, 760, 740, 750, 760, 910, 920],
        [890, 840, 780, 810, 760, 810, 790, 810, 820, 850, 870, 870],
    ]
    c = Boxplot()

    series_a = [opts.BoxplotItem(name=x_axis[0], value=d) for d in c.prepare_data(v1)]
    series_b = [opts.BoxplotItem(name=x_axis[1], value=d) for d in c.prepare_data(v2)]

    c.add_xaxis(xaxis_data=x_axis).add_yaxis("A", series_a).add_yaxis("B", series_b)
    c.render()
    _, content = fake_writer.call_args[0]
    assert_equal(c.theme, "white")
    assert_equal(c.renderer, "canvas")
