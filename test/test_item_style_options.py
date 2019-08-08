from nose.tools import eq_

from pyecharts import options as opts


def test_area_color_in_item_styles():
    op = opts.ItemStyleOpts(area_color="red")
    eq_(op.opts["areaColor"], "red")
