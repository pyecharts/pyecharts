import os
import json
from unittest.mock import patch

from nose.tools import assert_equal, assert_in

from pyecharts.commons.utils import remove_key_with_none_value
from pyecharts import options as opts


def test_graphic_group():
    group = opts.GraphicGroup(
        graphic_item={"item": 1},
        is_diff_children_by_name=False,
    )
    expected = {
        "type": "group",
        "diffChildrenByName": False,
        "item": 1,
    }
    assert_equal(expected, remove_key_with_none_value(group.opts))


def test_graphic_image():
    image = opts.GraphicImage(
        graphic_item={"item": 1}, graphic_imagestyle_opts={"opts": 1}
    )
    expected = {
        "type": "image",
        "item": 1,
        "style": {
            "opts": 1,
        },
    }
    assert_equal(expected, remove_key_with_none_value(image.opts))


def test_graphic_text():
    text = opts.GraphicText(
        graphic_item={"item": 1}, graphic_textstyle_opts={"opts": 1}
    )
    expected = {
        "type": "text",
        "item": 1,
        "style": {
            "opts": 1,
        },
    }
    assert_equal(expected, remove_key_with_none_value(text.opts))


def test_graphic_rect():
    rect = opts.GraphicRect(
        graphic_item={"item": 1},
        graphic_shape_opts={"shape": 1},
        graphic_basicstyle_opts={"opts": 1},
    )
    expected = {
        "type": "rect",
        "item": 1,
        "shape": 1,
        "style": {
            "opts": 1,
        },
    }
    assert_equal(expected, remove_key_with_none_value(rect.opts))
