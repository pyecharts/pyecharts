from nose.tools import assert_equal

from pyecharts.commons.utils import remove_key_with_none_value
from pyecharts.options.series_options import (
    LabelOpts,
    ItemStyleOpts,
    MarkPointItem,
    MarkLineItem,
    MarkAreaItem,
    MarkAreaOpts,
    MinorTickOpts,
    MinorSplitLineOpts,
    TreeMapBreadcrumbOpts,
)


def test_label_options_defaults():
    option = LabelOpts()
    expected = {
        "show": True,
        "position": None,
        "color": None,
        "distance": None,
        "rotate": None,
        "margin": 8,
        "interval": None,
        "fontSize": None,
        "fontStyle": None,
        "fontWeight": None,
        "fontFamily": None,
        "align": None,
        "verticalAlign": None,
        "formatter": None,
        "backgroundColor": None,
        "borderColor": None,
        "borderWidth": None,
        "borderRadius": None,
        "padding": None,
        "width": None,
        "height": None,
        "overflow": None,
        "rich": None,
    }
    assert_equal(expected, option.opts)


def test_label_options_custom():
    option = LabelOpts(
        background_color="red", border_color="green", border_width=1, border_radius=2
    )
    expected = {
        "show": True,
        "position": None,
        "color": None,
        "distance": None,
        "rotate": None,
        "margin": 8,
        "interval": None,
        "fontSize": None,
        "fontStyle": None,
        "fontWeight": None,
        "fontFamily": None,
        "align": None,
        "verticalAlign": None,
        "formatter": None,
        "backgroundColor": "red",
        "borderColor": "green",
        "borderWidth": 1,
        "borderRadius": 2,
        "padding": None,
        "width": None,
        "height": None,
        "overflow": None,
        "rich": None,
    }
    assert_equal(expected, option.opts)


def test_mark_point_item_remove_none():
    item = MarkPointItem()
    expected = {}
    assert_equal(expected, remove_key_with_none_value(item.opts))


def test_mark_line_item_remove_none():
    item = MarkLineItem()
    expected = {}
    assert_equal(expected, remove_key_with_none_value(item.opts))


def test_mark_area_item_remove_none():
    item = MarkAreaItem()
    expected = [
        {
            "itemStyle": None,
            "label": None,
            "name": None,
            "type": None,
            "valueDim": None,
            "valueIndex": None,
            "xAxis": None,
            "yAxis": None,
        },
        {
            "type": None,
            "valueDim": None,
            "valueIndex": None,
            "xAxis": None,
            "yAxis": None,
        },
    ]
    assert_equal(expected, remove_key_with_none_value(item.opts))


def test_mark_area_options_remove_none():
    label_opts = LabelOpts()
    option = MarkAreaOpts(label_opts=label_opts)
    expected = {
        "silent": False,
        "label": label_opts,
    }
    assert_equal(expected, remove_key_with_none_value(option.opts))


def test_tree_map_breadcrumb_options_remove_none():
    item_opts = ItemStyleOpts()
    option = TreeMapBreadcrumbOpts(item_opts=item_opts)
    expected = {
        "show": True,
        "left": "center",
        "right": "auto",
        "top": "auto",
        "bottom": 0,
        "height": 22,
        "emptyItemWidth": 25,
        "itemStyle": item_opts,
    }
    assert_equal(expected, remove_key_with_none_value(option.opts))


def test_minor_tick_options_remove_none():
    option = MinorTickOpts()
    expected = {
        "show": False,
        "splitNumber": 5,
        "length": 3,
    }
    assert_equal(expected, remove_key_with_none_value(option.opts))


def test_minor_split_line_options_remove_none():
    option = MinorSplitLineOpts()
    expected = {
        "show": False,
        "width": 1,
        "type": "solid",
    }
    assert_equal(expected, remove_key_with_none_value(option.opts))
