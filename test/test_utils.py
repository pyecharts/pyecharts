from nose.tools import eq_

from pyecharts.commons import utils


def test_utils_produce_require_dict():
    cfg = utils.produce_require_dict(utils.OrderedSet("echarts"), "https://example.com")
    eq_(cfg["config_items"], ["'echarts':'https://example.comecharts.min'"])
    eq_(cfg["libraries"], ["'echarts'"])
