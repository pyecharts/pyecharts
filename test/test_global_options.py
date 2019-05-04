from nose.tools import eq_

from pyecharts.options.global_options import ToolboxOpts
from pyecharts.commons.utils import remove_key_with_none_value


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
    eq_(expected, remove_key_with_none_value(option.opts))
