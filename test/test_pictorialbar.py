from unittest.mock import patch

from nose.tools import assert_equal

from pyecharts.charts import PictorialBar


@patch("pyecharts.render.engine.write_utf8_html_file")
def test_pictorialbar_base(fake_writer):
    c = (
        PictorialBar()
        .add_xaxis(["山西", "四川", "西藏", "北京", "上海", "内蒙古"])
        .add_yaxis(
            "",
            [13, 42, 67, 81, 86, 94, 166],
            symbol_size=18,
            symbol_repeat="fixed",
            symbol_offset=[0, 0],
            is_symbol_clip=True,
        )
        .reversal_axis()
    )
    c.render()
    _, content = fake_writer.call_args[0]
    assert_equal(c.theme, "white")
    assert_equal(c.renderer, "canvas")
