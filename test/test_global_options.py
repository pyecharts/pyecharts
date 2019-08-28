from nose.tools import assert_equal

from pyecharts.commons.utils import remove_key_with_none_value
from pyecharts.options.global_options import ToolboxOpts


def test_toolbox_options_remove_none():
    option = ToolboxOpts(feature={})
    expected = {
        "show": True,
        "orient": "horizontal",
        "itemSize": 15,
        "itemGap": 10,
        "left": "80%",
        "feature": {},
    }
    assert_equal(expected, remove_key_with_none_value(option.opts))
