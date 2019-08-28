from unittest.mock import patch

from nose.tools import assert_equal, assert_in

from pyecharts import options as opts
from pyecharts.charts import Grid, Liquid
from pyecharts.commons.utils import JsCode


@patch("pyecharts.render.engine.write_utf8_html_file")
def test_liquid_base(fake_writer):
    c = Liquid().add("lq", [0.6, 0.7])
    c.render()
    _, content = fake_writer.call_args[0]
    assert_equal(c.theme, "white")
    assert_equal(c.renderer, "canvas")


@patch("pyecharts.render.engine.write_utf8_html_file")
def test_liquid_grid(fake_writer):
    l1 = (
        Liquid()
        .add("lq", [0.6, 0.7], center=["60%", "50%"])
        .set_global_opts(title_opts=opts.TitleOpts(title="多个 Liquid 显示"))
    )

    l2 = Liquid().add(
        "lq",
        [0.3254],
        center=["25%", "50%"],
        label_opts=opts.LabelOpts(
            font_size=50,
            formatter=JsCode(
                """function (param) {
                        return (Math.floor(param.value * 10000) / 100) + '%';
                    }"""
            ),
            position="inside",
        ),
    )

    c = Grid().add(l1, grid_opts=opts.GridOpts()).add(l2, grid_opts=opts.GridOpts())
    c.render()
    _, content = fake_writer.call_args[0]
    assert_in("center", content)
