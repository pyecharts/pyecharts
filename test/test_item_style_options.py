from nose.tools import assert_equal

from pyecharts import options as opts


def test_area_color_in_item_styles():
    op = opts.ItemStyleOpts(area_color="red")
    assert_equal(op.opts["areaColor"], "red")
