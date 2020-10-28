from unittest.mock import patch

from nose.tools import assert_equal

from pyecharts import options as opts
from pyecharts.charts import Pie
from pyecharts.faker import Faker


@patch("pyecharts.render.engine.write_utf8_html_file")
def test_pie_base(fake_writer):
    c = (
        Pie()
        .add("", [list(z) for z in zip(Faker.choose(), Faker.values())])
        .set_series_opts(label_opts=opts.LabelOpts(formatter="{b}: {c}"))
    )
    c.render()
    _, content = fake_writer.call_args[0]
    assert_equal(c.theme, "white")
    assert_equal(c.renderer, "canvas")


@patch("pyecharts.render.engine.write_utf8_html_file")
def test_pie_item_base(fake_writer):
    d = [
        opts.PieItem(name="河马", value=131),
        opts.PieItem(name="蟒蛇", value=89),
        opts.PieItem(name="老虎", value=149),
        opts.PieItem(name="大象", value=178),
    ]
    c = (
        Pie()
        .add("", d)
        .set_series_opts(label_opts=opts.LabelOpts(formatter="{b}: {c}"))
    )
    c.render()
    _, content = fake_writer.call_args[0]
    assert_equal(c.theme, "white")
    assert_equal(c.renderer, "canvas")
