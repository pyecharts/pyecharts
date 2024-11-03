import unittest

from pyecharts.commons.utils import remove_key_with_none_value
from pyecharts.options.series_options import (
    AnimationOpts,
    LabelOpts,
    ItemStyleOpts,
    MarkPointItem,
    MarkLineItem,
    MarkLineOpts,
    MarkAreaItem,
    MarkAreaOpts,
    MarkPointOpts,
    MinorTickOpts,
    MinorSplitLineOpts,
    TreeMapBreadcrumbOpts,
)


class TestSeriesOptions(unittest.TestCase):
    def test_label_options_defaults(self):
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
            "textBorderColor": None,
            "textBorderWidth": None,
            "textShadowColor": None,
            "textShadowBlur": None,
            "textShadowOffsetX": None,
            "textShadowOffsetY": None,
            "overflow": None,
            "rich": None,
            "valueAnimation": False,
        }
        self.assertEqual(expected, option.opts)

    def test_label_options_custom(self):
        option = LabelOpts(
            background_color="red",
            border_color="green",
            border_width=1,
            border_radius=2,
            text_border_color="black",
            text_border_width=3,
            text_shadow_color="whitesmoke",
            text_shadow_blur=.1,
            text_shadow_offset_x=.2,
            text_shadow_offset_y=.3,
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
            "textBorderColor": "black",
            "textBorderWidth": 3,
            "textShadowColor": "whitesmoke",
            "textShadowBlur": .1,
            "textShadowOffsetX": .2,
            "textShadowOffsetY": .3,
            "overflow": None,
            "rich": None,
            "valueAnimation": False,
        }
        self.assertEqual(expected, option.opts)

    def test_mark_point_item_remove_none(self):
        item = MarkPointItem()
        expected = {}
        self.assertEqual(expected, remove_key_with_none_value(item.opts))

    def test_mark_line_item_remove_none(self):
        item = MarkLineItem()
        expected = {}
        self.assertEqual(expected, remove_key_with_none_value(item.opts))

    def test_mark_area_item_remove_none(self):
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
        self.assertEqual(expected, remove_key_with_none_value(item.opts))

    def test_mark_area_options_remove_none(self):
        label_opts = LabelOpts()
        option = MarkAreaOpts(label_opts=label_opts)
        expected = {
            "silent": False,
            "label": label_opts,
        }
        self.assertEqual(expected, remove_key_with_none_value(option.opts))

    def test_tree_map_breadcrumb_options_remove_none(self):
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
        self.assertEqual(expected, remove_key_with_none_value(option.opts))

    def test_minor_tick_options_remove_none(self):
        option = MinorTickOpts()
        expected = {
            "show": False,
            "splitNumber": 5,
            "length": 3,
        }
        self.assertEqual(expected, remove_key_with_none_value(option.opts))

    def test_minor_split_line_options_remove_none(self):
        option = MinorSplitLineOpts()
        expected = {
            "show": False,
            "width": 1,
            "type": "solid",
        }
        self.assertEqual(expected, remove_key_with_none_value(option.opts))

    def test_area_color_in_item_styles(self):
        op = ItemStyleOpts(area_color="red")
        self.assertEqual(op.opts["areaColor"], "red")

    def test_mark_point_opts_with_animation(self):
        op = MarkPointOpts(animation_opts=AnimationOpts(animation=True))
        self.assertEqual(op.opts["animation"], True)

    def test_mark_line_opts_with_animation(self):
        op = MarkLineOpts(animation_opts=AnimationOpts(animation=True))
        self.assertEqual(op.opts["animation"], True)

    def test_mark_area_opts_with_animation(self):
        op = MarkAreaOpts(animation_opts=AnimationOpts(animation=True))
        self.assertEqual(op.opts["animation"], True)
