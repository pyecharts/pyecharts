from unittest.mock import patch

from nose.tools import assert_equal, assert_in

from pyecharts import options as opts
from pyecharts.charts import Line, Bar


@patch("pyecharts.render.engine.write_utf8_html_file")
def test_chart_dark_mode(fake_writer):
    x_data = ["周一", "周二", "周三", "周四", "周五", "周六", "周日"]
    y_data1 = [140, 232, 101, 264, 90, 340, 250]
    y_data2 = [120, 282, 111, 234, 220, 340, 310]
    c = (
        Line()
        .add_xaxis(xaxis_data=x_data)
        .add_yaxis(series_name="品类 1", y_axis=y_data1, color="#80FFA5")
        .add_yaxis(series_name="品类 2", y_axis=y_data2, color="#00DDFF")
        .set_dark_mode()
    )
    c.render()
    _, content = fake_writer.call_args[0]
    assert_in("darkMode", content)


@patch("pyecharts.render.engine.write_utf8_html_file")
def test_chart_line_style_opts(fake_writer):
    x_data = ["周一", "周二", "周三", "周四", "周五", "周六", "周日"]
    y_data1 = [140, 232, 101, 264, 90, 340, 250]
    y_data2 = [120, 282, 111, 234, 220, 340, 310]
    c = (
        Line()
        .add_xaxis(xaxis_data=x_data)
        .add_yaxis(series_name="品类 1", y_axis=y_data1, color="#80FFA5")
        .add_yaxis(series_name="品类 2", y_axis=y_data2, color="#00DDFF")
        .set_series_opts(linestyle_opts=opts.LineStyleOpts())
    )
    c.render()
    _, content = fake_writer.call_args[0]
    assert_in("lineStyle", content)


@patch("pyecharts.render.engine.write_utf8_html_file")
def test_chart_split_line_style_opts(fake_writer):
    x_data = ["周一", "周二", "周三", "周四", "周五", "周六", "周日"]
    y_data1 = [140, 232, 101, 264, 90, 340, 250]
    y_data2 = [120, 282, 111, 234, 220, 340, 310]
    c = (
        Line()
        .add_xaxis(xaxis_data=x_data)
        .add_yaxis(series_name="品类 1", y_axis=y_data1, color="#80FFA5")
        .add_yaxis(series_name="品类 2", y_axis=y_data2, color="#00DDFF")
        .set_series_opts(splitline_opts=opts.SplitLineOpts())
    )
    c.render()
    _, content = fake_writer.call_args[0]
    assert_in("splitLine", content)


@patch("pyecharts.render.engine.write_utf8_html_file")
def test_chart_area_style_opts(fake_writer):
    x_data = ["周一", "周二", "周三", "周四", "周五", "周六", "周日"]
    y_data1 = [140, 232, 101, 264, 90, 340, 250]
    y_data2 = [120, 282, 111, 234, 220, 340, 310]
    c = (
        Line()
        .add_xaxis(xaxis_data=x_data)
        .add_yaxis(series_name="品类 1", y_axis=y_data1, color="#80FFA5")
        .add_yaxis(series_name="品类 2", y_axis=y_data2, color="#00DDFF")
        .set_series_opts(areastyle_opts=opts.AreaStyleOpts())
    )
    c.render()
    _, content = fake_writer.call_args[0]
    assert_in("areaStyle", content)


@patch("pyecharts.render.engine.write_utf8_html_file")
def test_chart_axis_line_opts(fake_writer):
    x_data = ["周一", "周二", "周三", "周四", "周五", "周六", "周日"]
    y_data1 = [140, 232, 101, 264, 90, 340, 250]
    y_data2 = [120, 282, 111, 234, 220, 340, 310]
    c = (
        Line()
        .add_xaxis(xaxis_data=x_data)
        .add_yaxis(series_name="品类 1", y_axis=y_data1, color="#80FFA5")
        .add_yaxis(series_name="品类 2", y_axis=y_data2, color="#00DDFF")
        .set_series_opts(axisline_opts=opts.AxisLineOpts())
    )
    c.render()
    _, content = fake_writer.call_args[0]
    assert_in("axisLine", content)


@patch("pyecharts.render.engine.write_utf8_html_file")
def test_chart_mark_point_opts(fake_writer):
    x_data = ["周一", "周二", "周三", "周四", "周五", "周六", "周日"]
    y_data1 = [140, 232, 101, 264, 90, 340, 250]
    y_data2 = [120, 282, 111, 234, 220, 340, 310]
    c = (
        Line()
        .add_xaxis(xaxis_data=x_data)
        .add_yaxis(series_name="品类 1", y_axis=y_data1, color="#80FFA5")
        .add_yaxis(series_name="品类 2", y_axis=y_data2, color="#00DDFF")
        .set_series_opts(markpoint_opts=opts.MarkPointOpts())
    )
    c.render()
    _, content = fake_writer.call_args[0]
    assert_in("markPoint", content)


@patch("pyecharts.render.engine.write_utf8_html_file")
def test_chart_mark_line_opts(fake_writer):
    x_data = ["周一", "周二", "周三", "周四", "周五", "周六", "周日"]
    y_data1 = [140, 232, 101, 264, 90, 340, 250]
    y_data2 = [120, 282, 111, 234, 220, 340, 310]
    c = (
        Line()
        .add_xaxis(xaxis_data=x_data)
        .add_yaxis(series_name="品类 1", y_axis=y_data1, color="#80FFA5")
        .add_yaxis(series_name="品类 2", y_axis=y_data2, color="#00DDFF")
        .set_series_opts(markline_opts=opts.MarkLineOpts())
    )
    c.render()
    _, content = fake_writer.call_args[0]
    assert_in("markLine", content)


@patch("pyecharts.render.engine.write_utf8_html_file")
def test_chart_mark_area_opts(fake_writer):
    x_data = ["周一", "周二", "周三", "周四", "周五", "周六", "周日"]
    y_data1 = [140, 232, 101, 264, 90, 340, 250]
    y_data2 = [120, 282, 111, 234, 220, 340, 310]
    c = (
        Line()
        .add_xaxis(xaxis_data=x_data)
        .add_yaxis(series_name="品类 1", y_axis=y_data1, color="#80FFA5")
        .add_yaxis(series_name="品类 2", y_axis=y_data2, color="#00DDFF")
        .set_series_opts(markarea_opts=opts.MarkAreaOpts())
    )
    c.render()
    _, content = fake_writer.call_args[0]
    assert_in("markArea", content)


@patch("pyecharts.render.engine.write_utf8_html_file")
def test_chart_tooltip_opts(fake_writer):
    x_data = ["周一", "周二", "周三", "周四", "周五", "周六", "周日"]
    y_data1 = [140, 232, 101, 264, 90, 340, 250]
    y_data2 = [120, 282, 111, 234, 220, 340, 310]
    c = (
        Line()
        .add_xaxis(xaxis_data=x_data)
        .add_yaxis(series_name="品类 1", y_axis=y_data1, color="#80FFA5")
        .add_yaxis(series_name="品类 2", y_axis=y_data2, color="#00DDFF")
        .set_series_opts(tooltip_opts=opts.TooltipOpts())
    )
    c.render()
    _, content = fake_writer.call_args[0]
    assert_in("tooltip", content)


@patch("pyecharts.render.engine.write_utf8_html_file")
def test_chart_item_style_opts(fake_writer):
    x_data = ["周一", "周二", "周三", "周四", "周五", "周六", "周日"]
    y_data1 = [140, 232, 101, 264, 90, 340, 250]
    y_data2 = [120, 282, 111, 234, 220, 340, 310]
    c = (
        Line()
        .add_xaxis(xaxis_data=x_data)
        .add_yaxis(series_name="品类 1", y_axis=y_data1, color="#80FFA5")
        .add_yaxis(series_name="品类 2", y_axis=y_data2, color="#00DDFF")
        .set_series_opts(itemstyle_opts=opts.ItemStyleOpts())
    )
    c.render()
    _, content = fake_writer.call_args[0]
    assert_in("itemStyle", content)


@patch("pyecharts.render.engine.write_utf8_html_file")
def test_chart_append_color(fake_writer):
    x_data = ["周一", "周二", "周三", "周四", "周五", "周六", "周日"]
    y_data1 = [140, 232, 101, 264, 90, 340, 250]
    y_data2 = [120, 282, 111, 234, 220, 340, 310]

    c = (
        Line()
        .add_xaxis(xaxis_data=x_data)
        .add_yaxis(series_name="品类 1", y_axis=y_data1, color="#80FFA5")
        .add_yaxis(series_name="品类 2", y_axis=y_data2, color="#00DDFF")
    )
    c.render()
    _, content = fake_writer.call_args[0]
    # Old Version (Before 2.0)
    # default_colors = (
    #     "#c23531 #2f4554 #61a0a8 #d48265 #749f83 #ca8622 #bda29a #6e7074 "
    #     "#546570 #c4ccd3 #f05b72 #ef5b9c #f47920 #905a3d #fab27b #2a5caa "
    #     "#444693 #726930 #b2d235 #6d8346 #ac6767 #1d953f #6950a1 #918597"
    # ).split()

    # New Version
    default_colors = (
        "#5470c6 #91cc75 #fac858 #ee6666 #73c0de #3ba272 #fc8452 #9a60b4 " "#ea7ccc"
    ).split()
    expected_result = ["#80FFA5", "#00DDFF", *default_colors]
    assert_equal(c.colors, expected_result)


@patch("pyecharts.render.engine.write_utf8_html_file")
def test_chart_add_dataset(fake_writer):
    c = (
        Bar()
        .add_dataset(
            source=[
                ["product", "2015", "2016", "2017"],
                ["Matcha Latte", 43.3, 85.8, 93.7],
                ["Milk Tea", 83.1, 73.4, 55.1],
                ["Cheese Cocoa", 86.4, 65.2, 82.5],
                ["Walnut Brownie", 72.4, 53.9, 39.1],
            ]
        )
        .add_dataset(from_dataset_index=1, from_transform_result=1)
        .add_yaxis(series_name="2015", y_axis=[])
        .add_yaxis(series_name="2016", y_axis=[])
        .add_yaxis(series_name="2017", y_axis=[])
        .set_global_opts(
            title_opts=opts.TitleOpts(title="Dataset simple bar example"),
            xaxis_opts=opts.AxisOpts(type_="category"),
        )
    )
    c.render()
    _, content = fake_writer.call_args[0]
    assert_in("dataset", content)


@patch("pyecharts.render.engine.write_utf8_html_file")
def test_chart_extend_axis(fake_writer):
    v1 = [2.0, 4.9, 7.0, 23.2, 25.6, 76.7, 135.6, 162.2, 32.6, 20.0, 6.4, 3.3]
    v2 = [2.6, 5.9, 9.0, 26.4, 28.7, 70.7, 175.6, 182.2, 48.7, 18.8, 6.0, 2.3]
    v3 = [2.0, 2.2, 3.3, 4.5, 6.3, 10.2, 20.3, 23.4, 23.0, 16.5, 12.0, 6.2]

    bar = (
        Bar()
        .add_xaxis([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12])
        .add_yaxis("蒸发量", v1)
        .add_yaxis("降水量", v2)
        .extend_axis(
            xaxis=opts.AxisOpts(),
            yaxis=opts.AxisOpts(
                axislabel_opts=opts.LabelOpts(formatter="{value} °C"), interval=5
            ),
        )
        .set_series_opts(label_opts=opts.LabelOpts(is_show=False))
        .set_global_opts(
            title_opts=opts.TitleOpts(title="Overlap-bar+line"),
            yaxis_opts=opts.AxisOpts(
                axislabel_opts=opts.LabelOpts(formatter="{value} ml")
            ),
        )
    )

    line = (
        Line()
        .add_xaxis([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12])
        .add_yaxis("平均温度", v3, yaxis_index=0, z_level=999)
        .set_global_opts(xaxis_opts=opts.AxisOpts(type_="value"))
    )
    bar.overlap(line)
    bar.render()
    _, content = fake_writer.call_args[0]
    assert_in("xAxis", content)
