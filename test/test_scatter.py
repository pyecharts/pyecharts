import json
from unittest.mock import patch

from nose.tools import assert_equal, assert_in

from pyecharts import options as opts
from pyecharts.charts import Scatter, Grid
from pyecharts.commons.utils import JsCode
from pyecharts.faker import Faker


@patch("pyecharts.render.engine.write_utf8_html_file")
def test_scatter_base(fake_writer):
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


@patch("pyecharts.render.engine.write_utf8_html_file")
def test_scatter_base_no_xaxis(fake_writer):
    c = (
        Scatter()
        .add_xaxis([])
        .add_yaxis("series0", [1, 2, 4])
        .add_yaxis("series1", [2, 3, 6])
    )
    c.render()
    _, content = fake_writer.call_args[0]
    assert_equal(c.theme, "white")
    assert_equal(c.renderer, "canvas")


@patch("pyecharts.render.engine.write_utf8_html_file")
def test_scatter_item_base(fake_writer):
    x_axis = ["A", "B", "C"]
    y_axis = [1, 2, 4]
    chart_item = [
        opts.ScatterItem(name=d[0], value=d[1]) for d in list(zip(x_axis, y_axis))
    ]

    c = (
        Scatter()
        .add_xaxis(x_axis)
        .add_yaxis("series0", chart_item)
        .set_global_opts(title_opts=opts.TitleOpts(title="Scatter-基本示例"))
    )
    c.render()
    _, content = fake_writer.call_args[0]
    assert_equal(c.theme, "white")
    assert_equal(c.renderer, "canvas")


@patch("pyecharts.render.engine.write_utf8_html_file")
def test_scatter_dataset(fake_writer):
    with open("test/fixtures/life-expectancy-table.json", "r", encoding="utf-8") as f:
        j = json.load(f)

    l1_1 = (
        Scatter()
        .add_dataset(
            dimensions=[
                "Income",
                "Life Expectancy",
                "Population",
                "Country",
                {"name": "Year", "type": "ordinal"},
            ],
            source=j,
        )
        .add_yaxis(
            series_name="",
            y_axis=[],
            symbol_size=2.5,
            xaxis_index=0,
            yaxis_index=0,
            encode={"x": "Income", "y": "Life Expectancy", "tooltip": [0, 1, 2, 3, 4]},
            label_opts=opts.LabelOpts(is_show=False),
        )
        .set_global_opts(
            xaxis_opts=opts.AxisOpts(
                type_="value",
                grid_index=0,
                name="Income",
                axislabel_opts=opts.LabelOpts(rotate=50, interval=0),
            ),
            yaxis_opts=opts.AxisOpts(
                type_="value", grid_index=0, name="Life Expectancy"
            ),
            title_opts=opts.TitleOpts(title="Encode and Matrix"),
        )
    )

    l1_2 = (
        Scatter()
        .add_dataset()
        .add_yaxis(
            series_name="",
            y_axis=[],
            symbol_size=2.5,
            xaxis_index=1,
            yaxis_index=1,
            encode={"x": "Country", "y": "Income", "tooltip": [0, 1, 2, 3, 4]},
            label_opts=opts.LabelOpts(is_show=False),
        )
        .set_global_opts(
            xaxis_opts=opts.AxisOpts(
                type_="category",
                grid_index=1,
                name="Country",
                boundary_gap=False,
                axislabel_opts=opts.LabelOpts(rotate=50, interval=0),
            ),
            yaxis_opts=opts.AxisOpts(type_="value", grid_index=1, name="Income"),
        )
    )

    l2_1 = (
        Scatter()
        .add_dataset()
        .add_yaxis(
            series_name="",
            y_axis=[],
            symbol_size=2.5,
            xaxis_index=2,
            yaxis_index=2,
            encode={"x": "Income", "y": "Population", "tooltip": [0, 1, 2, 3, 4]},
            label_opts=opts.LabelOpts(is_show=False),
        )
        .set_global_opts(
            xaxis_opts=opts.AxisOpts(
                type_="value",
                grid_index=2,
                name="Income",
                axislabel_opts=opts.LabelOpts(rotate=50, interval=0),
            ),
            yaxis_opts=opts.AxisOpts(type_="value", grid_index=2, name="Population"),
        )
    )

    l2_2 = (
        Scatter()
        .add_dataset()
        .add_yaxis(
            series_name="",
            y_axis=[],
            symbol_size=2.5,
            xaxis_index=3,
            yaxis_index=3,
            encode={
                "x": "Life Expectancy",
                "y": "Population",
                "tooltip": [0, 1, 2, 3, 4],
            },
            label_opts=opts.LabelOpts(is_show=False),
        )
        .set_global_opts(
            xaxis_opts=opts.AxisOpts(
                type_="value",
                grid_index=3,
                name="Life Expectancy",
                axislabel_opts=opts.LabelOpts(rotate=50, interval=0),
            ),
            yaxis_opts=opts.AxisOpts(type_="value", grid_index=3, name="Population"),
        )
    )

    grid = (
        Grid(init_opts=opts.InitOpts(width="1280px", height="960px"))
        .add(
            chart=l1_1,
            grid_opts=opts.GridOpts(pos_right="57%", pos_bottom="57%"),
            grid_index=0,
        )
        .add(
            chart=l1_2,
            grid_opts=opts.GridOpts(pos_left="57%", pos_bottom="57%"),
            grid_index=1,
        )
        .add(
            chart=l2_1,
            grid_opts=opts.GridOpts(pos_right="57%", pos_top="57%"),
            grid_index=2,
        )
        .add(
            chart=l2_2,
            grid_opts=opts.GridOpts(pos_left="57%", pos_top="57%"),
            grid_index=3,
        )
    )
    grid.render()
    _, content = fake_writer.call_args[0]
    assert_in("grid", content)


@patch("pyecharts.render.engine.write_utf8_html_file")
def test_scatter_multi_dimension_data(fake_writer):
    c = (
        Scatter()
        .add_xaxis(Faker.choose())
        .add_yaxis(
            "商家A",
            [list(z) for z in zip(Faker.values(), Faker.choose())],
            label_opts=opts.LabelOpts(
                formatter=JsCode(
                    "function(params){return params.value[1] +' : '+ params.value[2];}"
                )
            ),
        )
        .set_global_opts(
            title_opts=opts.TitleOpts(title="Scatter-多维度数据"),
            tooltip_opts=opts.TooltipOpts(
                formatter=JsCode(
                    "function (params) {return params.name + ' : ' + params.value[2];}"
                )
            ),
            visualmap_opts=opts.VisualMapOpts(
                type_="color", max_=150, min_=20, dimension=1
            ),
        )
    )
    c.render()
    _, content = fake_writer.call_args[0]
    assert_equal(c.theme, "white")
    assert_equal(c.renderer, "canvas")
