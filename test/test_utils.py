import unittest

from pyecharts.commons import utils
from pyecharts.datasets import EXTRA


class TestUtils(unittest.TestCase):
    def test_utils_produce_require_dict(self):
        cfg = utils.produce_require_dict(
            utils.OrderedSet("echarts"), "https://example.com"
        )
        self.assertEqual(
            cfg["config_items"], ["'echarts':'https://example.comecharts.min'"]
        )
        self.assertEqual(cfg["libraries"], ["'echarts'"])

        cfg_1 = utils.produce_require_dict(
            utils.OrderedSet("https://api.map.baidu.com"),
            "https://example.com",
        )
        self.assertEqual(
            cfg_1["config_items"],
            ["'baidu_map_api25':'https://api.map.baidu.com'"],
        )
        self.assertEqual(cfg_1["libraries"], ["'baidu_map_api25'"])

        cfg_2 = utils.produce_require_dict(
            utils.OrderedSet("https://webapi.amap.com"),
            "https://example.com",
        )
        self.assertEqual(
            cfg_2["config_items"],
            ["'amap_map_api23':'https://webapi.amap.com'"],
        )
        self.assertEqual(cfg_2["libraries"], ["'amap_map_api23'"])

    def test_utils_produce_require_dict_with_extra(self):
        global EXTRA
        EXTRA["https://api.baidu.com"] = {
            "https://api.baidu.com/test.min": ["https://api.baidu.com/test.min", "css"]
        }
        cfg_0 = utils.produce_require_dict(
            utils.OrderedSet("https://api.baidu.com/test.min"),
            "https://example.com",
        )
        self.assertEqual(cfg_0["libraries"], ["'https://api.baidu.com/test.min'"])

    def test_js_code(self):
        fn = "function() { console.log('test_js_code') }"
        js_code = utils.JsCode(fn)
        self.assertEqual(js_code.js_code, "--x_x--0_0--{}--x_x--0_0--".format(fn))

    def test_ordered_set(self):
        s = utils.OrderedSet()
        s.add("a", "b", "c")
        self.assertEqual(s.items, ["a", "b", "c"])

    def test_utils_remove_key_with_none_value(self):
        mock_data = [1, 2, 3]
        list_res = utils.remove_key_with_none_value(mock_data)
        assert list_res == mock_data

        mock_data_none = None
        none_res = utils.remove_key_with_none_value(mock_data_none)
        assert none_res == mock_data_none

    def test_utils_remove_key_with_none_value_raise_value_error(self):
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
