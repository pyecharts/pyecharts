import random
from unittest.mock import patch

from nose.tools import assert_equal, assert_in

from pyecharts import options as opts
from pyecharts.charts import Bar3D
from pyecharts.faker import Faker


@patch("pyecharts.render.engine.write_utf8_html_file")
def test_bar3d_base(fake_writer):
    data = [(i, j, random.randint(0, 12)) for i in range(6) for j in range(24)]
    c = (
        Bar3D()
        .add(
            "",
            [[d[1], d[0], d[2]] for d in data],
            xaxis3d_opts=opts.Axis3DOpts(Faker.clock, type_="category"),
            yaxis3d_opts=opts.Axis3DOpts(Faker.week_en, type_="category"),
            zaxis3d_opts=opts.Axis3DOpts(type_="value"),
        )
        .set_global_opts(visualmap_opts=opts.VisualMapOpts(max_=20))
    )
    c.render()
    _, content = fake_writer.call_args[0]
    assert_equal(c.theme, "white")
    assert_equal(c.renderer, "canvas")


@patch("pyecharts.render.engine.write_utf8_html_file")
def test_bar3d_stack(fake_writer):
    data1 = [(i, j, random.randint(0, 12)) for i in range(6) for j in range(24)]
    data2 = [(i, j, random.randint(13, 20)) for i in range(6) for j in range(24)]
    c = (
        Bar3D()
        .add(
            "1",
            [[d[1], d[0], d[2]] for d in data1],
            xaxis3d_opts=opts.Axis3DOpts(Faker.clock, type_="category"),
            yaxis3d_opts=opts.Axis3DOpts(Faker.week_en, type_="category"),
            zaxis3d_opts=opts.Axis3DOpts(type_="value"),
        )
        .add(
            "2",
            [[d[1], d[0], d[2]] for d in data2],
            xaxis3d_opts=opts.Axis3DOpts(Faker.clock, type_="category"),
            yaxis3d_opts=opts.Axis3DOpts(Faker.week_en, type_="category"),
            zaxis3d_opts=opts.Axis3DOpts(type_="value"),
        )
        .set_global_opts(visualmap_opts=opts.VisualMapOpts(max_=20))
        .set_series_opts(**{"stack": "stack"})
    )
    c.render()
    _, content = fake_writer.call_args[0]
    assert_in("stack", content)
