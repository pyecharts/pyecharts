from nose.tools import assert_equal

from pyecharts.commons import utils


def test_utils_produce_require_dict():
    cfg = utils.produce_require_dict(utils.OrderedSet("echarts"), "https://example.com")
    assert_equal(cfg["config_items"], ["'echarts':'https://example.comecharts.min'"])
    assert_equal(cfg["libraries"], ["'echarts'"])

    cfg_1 = utils.produce_require_dict(utils.OrderedSet("https://api.map.baidu.com"), "https://example.com")
    print(cfg_1)
    assert_equal(cfg_1["config_items"], ["'baidu_map_api25':'https://api.map.baidu.com'"])
    assert_equal(cfg_1["libraries"], ["'baidu_map_api25'"])


def test_js_code():
    fn = "function() { console.log('test_js_code') }"
    js_code = utils.JsCode(fn)
    assert_equal(js_code.js_code, "--x_x--0_0--{}--x_x--0_0--".format(fn))


def test_ordered_set():
    s = utils.OrderedSet()
    s.add("a", "b", "c")
    assert_equal(s.items, ["a", "b", "c"])


def test_utils_remove_key_with_none_value():
    mock_data = [1, 2, 3]
    list_res = utils.remove_key_with_none_value(mock_data)
    assert list_res == mock_data

    mock_data_none = None
    none_res = utils.remove_key_with_none_value(mock_data_none)
    assert none_res == mock_data_none
