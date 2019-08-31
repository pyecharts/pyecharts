from nose.tools import assert_equal

from pyecharts.commons import utils


def test_utils_produce_require_dict():
    cfg = utils.produce_require_dict(utils.OrderedSet("echarts"), "https://example.com")
    assert_equal(cfg["config_items"], ["'echarts':'https://example.comecharts.min'"])
    assert_equal(cfg["libraries"], ["'echarts'"])


def test_js_code():
    fn = "function() { console.log('test_js_code') }"
    js_code = utils.JsCode(fn)
    assert_equal(js_code.js_code, "--x_x--0_0--{}--x_x--0_0--".format(fn))


def test_ordered_set():
    s = utils.OrderedSet()
    s.add("a", "b", "c")
    assert_equal(s.items, ["a", "b", "c"])
