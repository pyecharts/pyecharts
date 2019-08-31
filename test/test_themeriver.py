from unittest.mock import patch

from nose.tools import assert_equal

from pyecharts import options as opts
from pyecharts.charts import ThemeRiver


@patch("pyecharts.render.engine.write_utf8_html_file")
def test_themeriver_basefake_writer(fake_writer):
    data = [
        ["2015/11/08", 10, "DQ"],
        ["2015/11/20", 30, "TY"],
        ["2015/11/08", 21, "SS"],
        ["2015/11/14", 7, "QG"],
        ["2015/11/22", 4, "SY"],
        ["2015/11/20", 26, "DD"],
    ]
    c = ThemeRiver().add(
        ["DQ", "TY", "SS", "QG", "SY", "DD"],
        data,
        singleaxis_opts=opts.SingleAxisOpts(type_="time", pos_bottom="10%"),
    )
    c.render()
    _, content = fake_writer.call_args[0]
    assert_equal(c.theme, "white")
    assert_equal(c.renderer, "canvas")
