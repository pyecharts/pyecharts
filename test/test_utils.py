from nose.tools import assert_equal

from pyecharts.commons import utils
from pyecharts.datasets import EXTRA


def test_utils_produce_require_dict():
    cfg = utils.produce_require_dict(utils.OrderedSet("echarts"), "https://example.com")
    assert_equal(cfg["config_items"], ["'echarts':'https://example.comecharts.min'"])
    assert_equal(cfg["libraries"], ["'echarts'"])

    cfg_1 = utils.produce_require_dict(
        utils.OrderedSet("https://api.map.baidu.com"),
        "https://example.com",
    )
    assert_equal(
        cfg_1["config_items"],
        ["'baidu_map_api25':'https://api.map.baidu.com'"],
    )
    assert_equal(cfg_1["libraries"], ["'baidu_map_api25'"])


def test_utils_produce_require_dict_with_extra():
    global EXTRA
    EXTRA["https://api.baidu.com"] = {
        "https://api.baidu.com/test.min": ["https://api.baidu.com/test.min", "css"]
    }
    cfg_0 = utils.produce_require_dict(
        utils.OrderedSet("https://api.baidu.com/test.min"),
        "https://example.com",
    )
    assert_equal(cfg_0["libraries"], ["'https://api.baidu.com/test.min'"])


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


def test_utils_remove_key_with_none_value_raise_value_error():
    import numpy as np
    import pandas as pd

    mock_data = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11]
    mock_numpy_data = np.array(mock_data)
    tmp_df = pd.DataFrame({"x": mock_data})
    mock_series_data = tmp_df["x"]
    try:
        utils.remove_key_with_none_value({"data": mock_numpy_data})
    except ValueError:
        pass

    try:
        utils.remove_key_with_none_value({"data": mock_series_data})
    except ValueError:
        pass
