from unittest.mock import patch

from nose.tools import assert_equal, assert_in

from pyecharts import options as opts
from pyecharts.charts import Bar, Grid, Line, Geo
from pyecharts.globals import ThemeType
from pyecharts.faker import Faker
from pyecharts.commons.utils import JsCode


def _chart_for_grid() -> Bar:
    x_data = ["{}月".format(i) for i in range(1, 13)]
    bar = (
        Bar()
        .add_xaxis(x_data)
        .add_yaxis(
            "蒸发量",
            [2.0, 4.9, 7.0, 23.2, 25.6, 76.7, 135.6, 162.2, 32.6, 20.0, 6.4, 3.3],
            yaxis_index=0,
        )
        .add_yaxis(
            "降水量",
            [2.6, 5.9, 9.0, 26.4, 28.7, 70.7, 175.6, 182.2, 48.7, 18.8, 6.0, 2.3],
            yaxis_index=1,
        )
        .extend_axis(yaxis=opts.AxisOpts(name="蒸发量", type_="value", position="right"))
        .extend_axis(yaxis=opts.AxisOpts(type_="value", name="温度", position="left"))
        .set_global_opts(
            yaxis_opts=opts.AxisOpts(name="降水量", position="right", offset=80)
        )
    )

    line = (
        Line()
        .add_xaxis(x_data)
        .add_yaxis(
            "平均温度",
            [2.0, 2.2, 3.3, 4.5, 6.3, 10.2, 20.3, 23.4, 23.0, 16.5, 12.0, 6.2],
            yaxis_index=2,
            color="#675bba",
            label_opts=opts.LabelOpts(is_show=False),
        )
    )

    bar.overlap(line)
    return bar


def test_grid_control_axis_index():
    bar = _chart_for_grid()
    gc = Grid().add(
        bar, opts.GridOpts(pos_left="5%", pos_right="20%"), is_control_axis_index=True
    )
    expected_idx = (0, 1, 2)
    for idx, series in enumerate(gc.options.get("series")):
        assert_equal(series.get("yAxisIndex"), expected_idx[idx])


def test_grid_do_not_control_axis_index():
    bar = _chart_for_grid()
    gc = Grid().add(bar, opts.GridOpts(pos_left="5%", pos_right="20%"))
    expected_idx = (0, 0, 0)
    for idx, series in enumerate(gc.options.get("series")):
        assert_equal(series.get("yAxisIndex"), expected_idx[idx])


@patch("pyecharts.render.engine.write_utf8_html_file")
def test_grid_options(fake_writer):
    bar = _chart_for_grid()
    gc = Grid(init_opts=opts.InitOpts(theme=ThemeType.ESSOS)).add(
        bar, opts.GridOpts(pos_left="5%", pos_right="20%", is_contain_label=True)
    )
    gc.render()
    _, content = fake_writer.call_args[0]
    assert_in("containLabel", content)
    assert_in("color", content)


def _chart_for_grid_v2():
    x_data = ["{}月".format(i) for i in range(1, 13)]
    bar = (
        Bar()
        .add_xaxis(x_data)
        .add_yaxis(
            "蒸发量",
            [2.0, 4.9, 7.0, 23.2, 25.6, 76.7, 135.6, 162.2, 32.6, 20.0, 6.4, 3.3],
            yaxis_index=0,
            color="red",
        )
        .add_yaxis(
            "降水量",
            [2.6, 5.9, 9.0, 26.4, 28.7, 70.7, 175.6, 182.2, 48.7, 18.8, 6.0, 2.3],
            yaxis_index=1,
            color="green",
        )
        .extend_axis(yaxis=opts.AxisOpts(name="蒸发量", type_="value", position="right"))
        .extend_axis(yaxis=opts.AxisOpts(type_="value", name="温度", position="left"))
        .set_global_opts(
            yaxis_opts=opts.AxisOpts(name="降水量", position="right", offset=80)
        )
    )

    line = (
        Line()
        .add_xaxis(x_data)
        .add_yaxis(
            "平均温度",
            [2.0, 2.2, 3.3, 4.5, 6.3, 10.2, 20.3, 23.4, 23.0, 16.5, 12.0, 6.2],
            yaxis_index=2,
            color="blue",
            label_opts=opts.LabelOpts(is_show=False),
        )
    )

    bar.overlap(line)
    assert_equal(bar.colors[:3], ["red", "green", "blue"])
    return bar


@patch("pyecharts.render.engine.write_utf8_html_file")
def test_grid_example_1(fake_writer):
    bar = _chart_for_grid_v2()
    gc = Grid().add(
        bar, opts.GridOpts(pos_left="5%", pos_right="20%"), is_control_axis_index=True
    )
    expected_idx = (0, 1, 2)
    for idx, series in enumerate(gc.options.get("series")):
        assert_equal(series.get("yAxisIndex"), expected_idx[idx])
    gc.render()
    _, content = fake_writer.call_args[0]
    assert_in("yAxisIndex", content)


@patch("pyecharts.render.engine.write_utf8_html_file")
def test_grid_geo_bar(fake_writer):
    bar = (
        Bar()
        .add_xaxis(Faker.choose())
        .add_yaxis("商家A", Faker.values())
        .add_yaxis("商家B", Faker.values())
        .set_global_opts(legend_opts=opts.LegendOpts(pos_left="20%"))
    )
    geo = (
        Geo()
        .add_schema(maptype="china")
        .add("geo", [list(z) for z in zip(Faker.provinces, Faker.values())])
        .set_series_opts(label_opts=opts.LabelOpts(is_show=False))
        .set_global_opts(
            visualmap_opts=opts.VisualMapOpts(),
            title_opts=opts.TitleOpts(title="Grid-Geo-Bar"),
        )
    )

    grid = (
        Grid()
        .add(bar, grid_opts=opts.GridOpts(pos_top="50%", pos_right="75%"))
        .add(geo, grid_opts=opts.GridOpts(pos_left="60%"))
    )
    grid.render()
    _, content = fake_writer.call_args[0]
    assert_in("geo", content)


@patch("pyecharts.render.engine.write_utf8_html_file")
def test_grid_mutil_yaxis(fake_writer):
    bar = (
        Bar()
        .add_xaxis(["{}月".format(i) for i in range(1, 13)])
        .add_yaxis(
            "蒸发量",
            [2.0, 4.9, 7.0, 23.2, 25.6, 76.7, 135.6, 162.2, 32.6, 20.0, 6.4, 3.3],
            yaxis_index=0,
            color="#d14a61",
        )
        .add_yaxis(
            "降水量",
            [2.6, 5.9, 9.0, 26.4, 28.7, 70.7, 175.6, 182.2, 48.7, 18.8, 6.0, 2.3],
            yaxis_index=1,
            color="#5793f3",
        )
        .extend_axis(
            yaxis=opts.AxisOpts(
                name="蒸发量",
                type_="value",
                min_=0,
                max_=250,
                position="right",
                axisline_opts=opts.AxisLineOpts(
                    linestyle_opts=opts.LineStyleOpts(color="#d14a61")
                ),
                axislabel_opts=opts.LabelOpts(formatter="{value} ml"),
            )
        )
        .extend_axis(
            yaxis=opts.AxisOpts(
                type_="value",
                name="温度",
                min_=0,
                max_=25,
                position="left",
                axisline_opts=opts.AxisLineOpts(
                    linestyle_opts=opts.LineStyleOpts(color="#675bba")
                ),
                axislabel_opts=opts.LabelOpts(formatter="{value} °C"),
                splitline_opts=opts.SplitLineOpts(
                    is_show=True, linestyle_opts=opts.LineStyleOpts(opacity=1)
                ),
            )
        )
        .set_global_opts(
            yaxis_opts=opts.AxisOpts(
                name="降水量",
                min_=0,
                max_=250,
                position="right",
                offset=80,
                axisline_opts=opts.AxisLineOpts(
                    linestyle_opts=opts.LineStyleOpts(color="#5793f3")
                ),
                axislabel_opts=opts.LabelOpts(formatter="{value} ml"),
            ),
            title_opts=opts.TitleOpts(title="Grid-Overlap-多 X/Y 轴示例"),
            tooltip_opts=opts.TooltipOpts(trigger="axis", axis_pointer_type="cross"),
            legend_opts=opts.LegendOpts(pos_left="25%"),
        )
    )

    line = (
        Line()
        .add_xaxis(["{}月".format(i) for i in range(1, 13)])
        .add_yaxis(
            "平均温度",
            [2.0, 2.2, 3.3, 4.5, 6.3, 10.2, 20.3, 23.4, 23.0, 16.5, 12.0, 6.2],
            yaxis_index=2,
            color="#675bba",
            label_opts=opts.LabelOpts(is_show=False),
        )
    )

    bar1 = (
        Bar()
        .add_xaxis(["{}月".format(i) for i in range(1, 13)])
        .add_yaxis(
            "蒸发量 1",
            [2.0, 4.9, 7.0, 23.2, 25.6, 76.7, 135.6, 162.2, 32.6, 20.0, 6.4, 3.3],
            color="#d14a61",
            xaxis_index=1,
            yaxis_index=3,
        )
        .add_yaxis(
            "降水量 2",
            [2.6, 5.9, 9.0, 26.4, 28.7, 70.7, 175.6, 182.2, 48.7, 18.8, 6.0, 2.3],
            color="#5793f3",
            xaxis_index=1,
            yaxis_index=3,
        )
        .extend_axis(
            yaxis=opts.AxisOpts(
                name="蒸发量",
                type_="value",
                min_=0,
                max_=250,
                position="right",
                axisline_opts=opts.AxisLineOpts(
                    linestyle_opts=opts.LineStyleOpts(color="#d14a61")
                ),
                axislabel_opts=opts.LabelOpts(formatter="{value} ml"),
            )
        )
        .extend_axis(
            yaxis=opts.AxisOpts(
                type_="value",
                name="温度",
                min_=0,
                max_=25,
                position="left",
                axisline_opts=opts.AxisLineOpts(
                    linestyle_opts=opts.LineStyleOpts(color="#675bba")
                ),
                axislabel_opts=opts.LabelOpts(formatter="{value} °C"),
                splitline_opts=opts.SplitLineOpts(
                    is_show=True, linestyle_opts=opts.LineStyleOpts(opacity=1)
                ),
            )
        )
        .set_global_opts(
            xaxis_opts=opts.AxisOpts(grid_index=1),
            yaxis_opts=opts.AxisOpts(
                name="降水量",
                min_=0,
                max_=250,
                position="right",
                offset=80,
                grid_index=1,
                axisline_opts=opts.AxisLineOpts(
                    linestyle_opts=opts.LineStyleOpts(color="#5793f3")
                ),
                axislabel_opts=opts.LabelOpts(formatter="{value} ml"),
            ),
            tooltip_opts=opts.TooltipOpts(trigger="axis", axis_pointer_type="cross"),
            legend_opts=opts.LegendOpts(pos_left="65%"),
        )
    )

    line1 = (
        Line()
        .add_xaxis(["{}月".format(i) for i in range(1, 13)])
        .add_yaxis(
            "平均温度 1",
            [2.0, 2.2, 3.3, 4.5, 6.3, 10.2, 20.3, 23.4, 23.0, 16.5, 12.0, 6.2],
            color="#675bba",
            label_opts=opts.LabelOpts(is_show=False),
            xaxis_index=1,
            yaxis_index=5,
        )
    )

    overlap_1 = bar.overlap(line)
    overlap_2 = bar1.overlap(line1)

    grid = (
        Grid(init_opts=opts.InitOpts(width="1200px", height="800px"))
        .add(
            overlap_1,
            grid_opts=opts.GridOpts(pos_right="58%"),
            is_control_axis_index=True,
        )
        .add(
            overlap_2,
            grid_opts=opts.GridOpts(pos_left="58%"),
            is_control_axis_index=True,
        )
    )
    grid.render()
    _, content = fake_writer.call_args[0]
    assert_in("xAxis", content)
    assert_in("yAxis", content)
