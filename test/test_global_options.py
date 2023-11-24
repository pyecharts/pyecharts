from nose.tools import assert_equal

from pyecharts.commons.utils import remove_key_with_none_value
from pyecharts.options.global_options import (
    AnimationOpts,
    AngleAxisItem,
    AngleAxisOpts,
    AriaLabelOpts,
    AriaDecalOpts,
    AxisTickOpts,
    CalendarYearLabelOpts,
    DatasetTransformOpts,
    InitOpts,
    ParallelAxisOpts,
    RadiusAxisItem,
    RadiusAxisOpts,
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


def test_aria_label_options_remove_none():
    option = AriaLabelOpts()
    expected = {
        "enabled": True,
        "general": {
            "withTitle": "这是一个关于“{title}”的图表。",
            "withoutTitle": "这是一个图表，",
        },
        "series": {
            "maxCount": 10,
            "single": {
                "withName": "图表类型是{seriesType}，表示{seriesName}。",
                "withoutName": "图表类型是{seriesType}。",
            },
            "multiple": {
                "prefix": "它由{seriesCount}个图表系列组成。",
                "withName": "图表类型是{seriesType}，表示{seriesName}。",
                "withoutName": "图表类型是{seriesType}。",
                "separator": {
                    "middle": "；",
                    "end": "。",
                },
            },
        },
        "data": {
            "maxCount": 10,
            "allData": "其数据是——",
            "partialData": "其中，前{displayCnt}项是——",
            "withName": "{name}的数据是{value}",
            "withoutName": "{value}",
            "separator": {
                "middle": "，",
            },
        },
    }
    assert_equal(expected, remove_key_with_none_value(option.opts))


def test_aria_decal_options_remove_none():
    option = AriaDecalOpts()
    expected = {
        "show": False,
        "decals": {
            "symbol": "rect",
            "symbolSize": 1,
            "symbolKeepAspect": True,
            "color": "rgba(0, 0, 0, 0.2)",
            "dashArrayX": 5,
            "dashArrayY": 5,
            "rotation": 0,
            "maxTileWidth": 512,
            "maxTileHeight": 512,
        },
    }
    assert_equal(expected, remove_key_with_none_value(option.opts))


def test_init_options_remove_none():
    option = InitOpts(animation_opts={}, aria_opts={})
    expected = {
        "animationOpts": {},
        "height": "500px",
        "page_title": "Awesome-pyecharts",
        "renderer": "canvas",
        "theme": "white",
        "width": "900px",
        "ariaOpts": {},
        "fill_bg": False,
        "is_horizontal_center": False,
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
        "z": 10000,
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
        "showDetail": True,
        "showDataShadow": True,
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
        "backgroundColor": "transparent",
        "borderColor": "#ccc",
        "borderRadius": 0,
        "pageButtonItemGap": 5,
        "pageButtonPosition": "end",
        "pageFormatter": "{current}/{total}",
        "pageIconColor": "#2f4554",
        "pageIconInactiveColor": "#aaa",
        "pageIconSize": 15,
        "animationDurationUpdate": 800,
        "selector": False,
        "selectorPosition": "auto",
        "selectorItemGap": 7,
        "selectorButtonGap": 10,
    }
    assert_equal(expected, remove_key_with_none_value(option.opts))


def test_visual_map_options_remove_none():
    option = VisualMapOpts(range_opacity=0.1)
    expected = {
        "calculable": True,
        "inRange": {"color": ["#50a3ba", "#eac763", "#d94e5d"], "opacity": 0.1},
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
        "hoverLink": True,
        "padding": 5,
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
        "enterable": False,
        "confine": False,
        "appendToBody": False,
        "transitionDuration": 0.4,
        "order": "seriesAsc",
        "triggerOn": "mousemove|click",
    }
    assert_equal(expected, remove_key_with_none_value(option.opts))


def test_axis_tick_options_remove_none():
    option = AxisTickOpts()
    expected = {
        "show": True,
        "alignWithLabel": False,
        "inside": False,
    }
    assert_equal(expected, remove_key_with_none_value(option.opts))


def test_parallel_axis_options_remove_none():
    option = ParallelAxisOpts(dim=1)
    expected = {
        "dim": 1,
        "parallelIndex": 0,
        "realtime": True,
        "name_location": "end",
        "name_gap": 15,
        "inverse": False,
        "scale": False,
        "logBase": 10,
        "silent": False,
        "triggerEvent": False,
    }
    assert_equal(expected, remove_key_with_none_value(option.opts))


def test_calendar_year_label_options_remove_none():
    option = CalendarYearLabelOpts()
    expected = {
        "show": True,
        "color": "#000",
        "fontStyle": "normal",
        "fontWeight": "normal",
        "fontFamily": "sans-serif",
        "fontSize": 12,
    }
    assert_equal(expected, remove_key_with_none_value(option.opts))


def test_angle_axis_item_remove_none():
    item = AngleAxisItem(textstyle_opts=None)
    expected = {}
    assert_equal(expected, remove_key_with_none_value(item.opts))


def test_angle_axis_options_remove_none():
    mock_data = [AngleAxisItem(value="1"), AngleAxisItem(value="2")]
    option = AngleAxisOpts(data=mock_data)
    expected = {
        "data": mock_data,
        "startAngle": 90,
        "clockwise": False,
        "scale": False,
        "splitNumber": 5,
    }
    assert_equal(expected, remove_key_with_none_value(option.opts))


def test_radius_axis_item_remove_none():
    item = RadiusAxisItem()
    expected = {}
    assert_equal(expected, remove_key_with_none_value(item.opts))


def test_radius_axis_options_remove_none():
    mock_data = [RadiusAxisItem(value="1"), RadiusAxisItem(value="2")]
    option = RadiusAxisOpts(data=mock_data)
    expected = {
        "data": mock_data,
        "nameGap": 15,
        "inverse": False,
        "scale": False,
        "splitNumber": 5,
        "minInterval": 0,
    }
    assert_equal(expected, remove_key_with_none_value(option.opts))


def test_dataset_transform_options_remove_none():
    option = DatasetTransformOpts()
    expected = {"type": "filter", "print": False}
    assert_equal(expected, remove_key_with_none_value(option.opts))
