from nose.tools import assert_equal

from pyecharts.commons.utils import remove_key_with_none_value
from pyecharts.options.global_options import (
    AnimationOpts,
    InitOpts,
    ToolBoxFeatureBrushOpts,
    ToolBoxFeatureDataViewOpts,
    ToolBoxFeatureDataZoomOpts,
    ToolBoxFeatureMagicTypeOpts,
    ToolBoxFeatureOpts,
    ToolBoxFeatureRestoreOpts,
    ToolBoxFeatureSaveAsImageOpts,
    ToolboxOpts,
    BrushOpts,
    DataZoomOpts,
    LegendOpts,
    VisualMapOpts,
    TooltipOpts,
)


def test_animation_options_remove_none():
    option = AnimationOpts()
    expected = {
        "animation": True,
        "animationDelay": 0,
        "animationDelayUpdate": 0,
        "animationDuration": 1000,
        "animationDurationUpdate": 300,
        "animationEasing": "cubicOut",
        "animationEasingUpdate": "cubicOut",
        "animationThreshold": 2000,
    }
    assert_equal(expected, remove_key_with_none_value(option.opts))


def test_init_options_remove_none():
    option = InitOpts(animation_opts={})
    expected = {
        "animationOpts": {},
        "height": "500px",
        "page_title": "Awesome-pyecharts",
        "renderer": "canvas",
        "theme": "white",
        "width": "900px",
    }
    assert_equal(expected, remove_key_with_none_value(option.opts))


def test_toolbox_feature_options_remove_none():
    save_as_image = ToolBoxFeatureSaveAsImageOpts()
    restore = ToolBoxFeatureRestoreOpts()
    data_view = ToolBoxFeatureDataViewOpts()
    data_zoom = ToolBoxFeatureDataZoomOpts()
    magic_type = ToolBoxFeatureMagicTypeOpts()
    brush = ToolBoxFeatureBrushOpts()

    option = ToolBoxFeatureOpts(
        save_as_image=save_as_image,
        restore=restore,
        data_view=data_view,
        data_zoom=data_zoom,
        magic_type=magic_type,
        brush=brush,
    )
    expected = {
        "saveAsImage": save_as_image,
        "restore": restore,
        "dataView": data_view,
        "dataZoom": data_zoom,
        "magicType": magic_type,
        "brush": brush,
    }
    assert_equal(expected, remove_key_with_none_value(option.opts))


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


def test_brush_options_remove_none():
    option = BrushOpts()
    expected = {
        "brushMode": "single",
        "brushStyle": {
            "borderColor": "rgba(120,140,180,0.8)",
            "borderWidth": 1,
            "color": "rgba(120,140,180,0.3)",
        },
        "brushType": "rect",
        "removeOnClick": True,
        "throttleDelay": 0,
        "throttleType": "fixRate",
        "toolbox": ["rect", "polygon", "keep", "clear"],
        "transformable": True,
    }
    assert_equal(expected, remove_key_with_none_value(option.opts))


def test_data_zoom_options_remove_none():
    option = DataZoomOpts()
    expected = {
        "end": 80,
        "filterMode": "filter",
        "orient": "horizontal",
        "realtime": True,
        "show": True,
        "start": 20,
        "type": "slider",
        "zoomLock": False,
    }
    assert_equal(expected, remove_key_with_none_value(option.opts))


def test_legend_options_remove_none():
    option = LegendOpts()
    expected = {
        "show": True,
        "padding": 5,
        "itemGap": 10,
        "itemWidth": 25,
        "itemHeight": 14,
    }
    assert_equal(expected, remove_key_with_none_value(option.opts))


def test_visual_map_options_remove_none():
    option = VisualMapOpts()
    expected = {
        "calculable": True,
        "inRange": {"color": ["#50a3ba", "#eac763", "#d94e5d"]},
        "itemHeight": 140,
        "itemWidth": 20,
        "max": 100,
        "min": 0,
        "orient": "vertical",
        "show": True,
        "showLabel": True,
        "inverse": False,
        "splitNumber": 5,
        "type": "continuous",
        "borderWidth": 0,
    }
    assert_equal(expected, remove_key_with_none_value(option.opts))


def test_tool_tip_options_remove_none():
    option = TooltipOpts(textstyle_opts=None)
    expected = {
        "alwaysShowContent": False,
        "axisPointer": {"type": "line"},
        "borderWidth": 0,
        "hideDelay": 100,
        "padding": 5,
        "show": True,
        "showContent": True,
        "showDelay": 0,
        "trigger": "item",
        "triggerOn": "mousemove|click",
    }
    assert_equal(expected, remove_key_with_none_value(option.opts))
