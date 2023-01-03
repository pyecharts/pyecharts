from nose.tools import assert_equal

from pyecharts.commons.utils import remove_key_with_none_value
from pyecharts.options.charts_options import (
    BarBackgroundStyleOpts,
    GlobeLayersOpts,
    GraphCategory,
    ThemeRiverItem,
    TimelineCheckPointerStyle,
    TimelineControlStyle,
    TreeItem,
    TreeMapItemStyleOpts,
)


def test_bar_background_style_options_remove_none():
    option = BarBackgroundStyleOpts()
    expected = {
        "color": "rgba(180, 180, 180, 0.2)",
        "borderColor": "#000",
        "borderWidth": 0,
        "borderType": "solid",
        "barBorderRadius": 0,
        "shadowOffsetX": 0,
        "shadowOffsetY": 0,
    }
    assert_equal(expected, remove_key_with_none_value(option.opts))


def test_globe_layers_options_remove_none():
    option = GlobeLayersOpts()
    expected = {
        "show": True,
        "type": "overlay",
        "blendTo": "albedo",
        "intensity": 1,
        "shading": "lambert",
    }
    assert_equal(expected, remove_key_with_none_value(option.opts))


def test_theme_river_item_remove_none():
    item = ThemeRiverItem()
    expected = {}
    assert_equal(expected, remove_key_with_none_value(item.opts))


def test_tree_river_item_remove_none():
    item = TreeItem()
    expected = {}
    assert_equal(expected, remove_key_with_none_value(item.opts))


def test_timeline_check_pointer_style_options_remove_none():
    option = TimelineCheckPointerStyle(symbol_offset=None)
    expected = {
        "symbol": "circle",
        "symbolSize": 13,
        "symbolKeepAspect": False,
        "symbolOffset": [0, 0],
        "color": "#c23531",
        "borderWidth": 5,
        "borderColor": "rgba(194,53,49,0.5)",
        "animation": True,
        "animationDuration": 300,
        "animationEasing": "quinticInOut",
    }
    assert_equal(expected, remove_key_with_none_value(option.opts))


def test_timeline_control_style_options_remove_none():
    option = TimelineControlStyle()
    expected = {
        "show": True,
        "showPlayBtn": True,
        "showPrevBtn": True,
        "showNextBtn": True,
        "itemSize": 22,
        "itemGap": 12,
        "position": "left",
        "color": "#304654",
        "borderColor": "#304654",
        "borderWidth": 1,
    }
    assert_equal(expected, remove_key_with_none_value(option.opts))


def test_graph_category_item_remove_none():
    item = GraphCategory()
    expected = {}
    assert_equal(expected, remove_key_with_none_value(item.opts))


def test_tree_map_item_style_options_remove_none():
    option = TreeMapItemStyleOpts()
    expected = {
        "gapWidth": 0,
        "borderWidth": 0,
    }
    assert_equal(expected, remove_key_with_none_value(option.opts))

