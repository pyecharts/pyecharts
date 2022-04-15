import random
from unittest.mock import patch

from nose.tools import assert_equal

from pyecharts import options as opts
from pyecharts.charts import Polar


@patch("pyecharts.render.engine.write_utf8_html_file")
def test_polar_scatter(fake_writer):
    data = [(i, random.randint(1, 100)) for i in range(101)]
    c = Polar().add("", data, type_="scatter", label_opts=opts.LabelOpts(is_show=False))
    c.render()
    _, content = fake_writer.call_args[0]
    assert_equal(c.theme, "white")
    assert_equal(c.renderer, "canvas")


@patch("pyecharts.render.engine.write_utf8_html_file")
def test_polar_effect_scatter(fake_writer):
    data = [(i, random.randint(1, 100)) for i in range(101)]
    c = (
        Polar()
        .add(
            "",
            data,
            type_="effectScatter",
            effect_opts=opts.EffectOpts(scale=10, period=5),
            label_opts=opts.LabelOpts(is_show=False),
        )
        .set_global_opts(title_opts=opts.TitleOpts(title="Polar-EffectScatter"))
    )
    c.render()
    _, content = fake_writer.call_args[0]
    assert_equal(c.theme, "white")
    assert_equal(c.renderer, "canvas")


@patch("pyecharts.render.engine.write_utf8_html_file")
def test_polar_base_1(fake_writer):
    data = [(i, random.randint(1, 100)) for i in range(101)]
    c = (
        Polar()
        .add(
            "",
            data,
            type_="effectScatter",
            effect_opts=opts.EffectOpts(scale=10, period=5),
            label_opts=opts.LabelOpts(is_show=True),
        )
        .set_global_opts(title_opts=opts.TitleOpts(title="Polar-Base-1"))
    )
    c.render()
    _, content = fake_writer.call_args[0]
    assert_equal(c.theme, "white")
    assert_equal(c.renderer, "canvas")
