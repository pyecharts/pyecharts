from nose.tools import eq_

from pyecharts.commons import utils


def test_utils_produce_require_dict():
    cfg = utils.produce_require_dict(utils.OrderedSet("echarts"), "https://example.com")
    eq_(cfg["config_items"], ["'echarts':'https://example.comecharts.min'"])
    eq_(cfg["libraries"], ["'echarts'"])


def test_js_code():
    fn = "function() { console.log('test_js_code') }"
    js_code = utils.JsCode(fn)
    eq_(js_code.js_code, "--x_x--0_0--{}--x_x--0_0--".format(fn))


def test_ordered_set():
    s = utils.OrderedSet()
    s.add("a", "b", "c")
    eq_(s.items, ["a", "b", "c"])
