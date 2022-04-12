from unittest.mock import patch

from nose.tools import assert_equal
from pyecharts.charts import Line


@patch("pyecharts.render.engine.write_utf8_html_file")
def test_chart_append_color(fake_writer):
    x_data = ["周一", "周二", "周三", "周四", "周五", "周六", "周日"]
    y_data1 = [140, 232, 101, 264, 90, 340, 250]
    y_data2 = [120, 282, 111, 234, 220, 340, 310]

    c = (
        Line()
            .add_xaxis(xaxis_data=x_data)
            .add_yaxis(
            series_name="品类 1",
            y_axis=y_data1,
            color='#80FFA5')
            .add_yaxis(
            series_name="品类 2",
            y_axis=y_data2,
            color='#00DDFF')
    )
    c.render()
    _, content = fake_writer.call_args[0]
    default_colors = (
        "#c23531 #2f4554 #61a0a8 #d48265 #749f83 #ca8622 #bda29a #6e7074 "
        "#546570 #c4ccd3 #f05b72 #ef5b9c #f47920 #905a3d #fab27b #2a5caa "
        "#444693 #726930 #b2d235 #6d8346 #ac6767 #1d953f #6950a1 #918597"
    ).split()
    expected_result = ['#80FFA5', '#00DDFF', *default_colors]
    assert_equal(c.colors, expected_result)