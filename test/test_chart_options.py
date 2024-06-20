import unittest

from pyecharts.commons.utils import remove_key_with_none_value
from pyecharts.options.charts_options import (
    BarBackgroundStyleOpts,
    GlobeLayersOpts,
    GraphCategory,
    SunburstLevelOpts,
    SunburstLabelLineOpts,
    SunburstLabelLayoutOpts,
    ThemeRiverItem,
    TimelineCheckPointerStyle,
    TimelineControlStyle,
    TreeItem,
    TreeMapItemStyleOpts,
    GraphicImageStyleOpts,
    GraphicTextStyleOpts,
    GeoRegionsOpts,
)


class TestChartOptions(unittest.TestCase):

    def test_bar_background_style_options_remove_none(self):
        option = BarBackgroundStyleOpts()
        expected = {
            "color": "rgba(180, 180, 180, 0.2)",
            "borderColor": "#000",
            "borderWidth": 0,
            "borderType": "solid",
            "borderRadius": 0,
            "shadowOffsetX": 0,
            "shadowOffsetY": 0,
        }
        self.assertEqual(expected, remove_key_with_none_value(option.opts))

    def test_globe_layers_options_remove_none(self):
        option = GlobeLayersOpts()
        expected = {
            "show": True,
            "type": "overlay",
            "blendTo": "albedo",
            "intensity": 1,
            "shading": "lambert",
        }
        self.assertEqual(expected, remove_key_with_none_value(option.opts))

    def test_theme_river_item_remove_none(self):
        item = ThemeRiverItem()
        expected = {}
        self.assertEqual(expected, remove_key_with_none_value(item.opts))

    def test_tree_river_item_remove_none(self):
        item = TreeItem()
        expected = {}
        self.assertEqual(expected, remove_key_with_none_value(item.opts))

    def test_timeline_check_pointer_style_options_remove_none(self):
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
        self.assertEqual(expected, remove_key_with_none_value(option.opts))

    def test_timeline_control_style_options_remove_none(self):
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
        self.assertEqual(expected, remove_key_with_none_value(option.opts))

    def test_graph_category_item_remove_none(self):
        item = GraphCategory()
        expected = {}
        self.assertEqual(expected, remove_key_with_none_value(item.opts))

    def test_tree_map_item_style_options_remove_none(self):
        option = TreeMapItemStyleOpts()
        expected = {
            "gapWidth": 0,
            "borderWidth": 0,
        }
        self.assertEqual(expected, remove_key_with_none_value(option.opts))

    def test_graphic_image_style_opts_remove_none(self):
        option = GraphicImageStyleOpts(graphic_basicstyle_opts={"fill": "#000"})
        expected = {
            "x": 0,
            "y": 0,
            "width": 0,
            "height": 0,
            "opacity": 1,
            "fill": "#000",
        }
        self.assertEqual(expected, remove_key_with_none_value(option.opts))

    def test_graphic_text_style_opts_remove_none(self):
        option = GraphicTextStyleOpts(graphic_basicstyle_opts={"fill": "#000"})
        expected = {
            "x": 0,
            "y": 0,
            "fontSize": 0,
            "textAlign": "left",
            "fill": "#000",
        }
        self.assertEqual(expected, remove_key_with_none_value(option.opts))

    def test_geo_region_opts_remove_none(self):
        option = GeoRegionsOpts()
        expected = {
            "blur": {},
            "emphasis": {},
            "select": {},
            "selected": False,
            "silent": False,
        }
        self.assertEqual(expected, remove_key_with_none_value(option.opts))

    def test_sunburst_label_line_opts_remove_none(self):
        option = SunburstLabelLineOpts()
        expected = {"smooth": False}
        self.assertEqual(expected, remove_key_with_none_value(option.opts))

    def test_sunburst_label_layout_opts_remove_none(self):
        option = SunburstLabelLayoutOpts()
        expected = {}
        self.assertEqual(expected, remove_key_with_none_value(option.opts))

    def test_sunburst_level_opts_remove_none(self):
        option = SunburstLevelOpts()
        expected = {}
        self.assertEqual(expected, remove_key_with_none_value(option.opts))
