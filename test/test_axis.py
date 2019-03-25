# coding=utf-8
from __future__ import unicode_literals

import types

from pyecharts.options import YAxisLabel


def test_yaxis_wo_formatter():
    label = YAxisLabel(
        interval="auto", rotate=0, margin=8, text_size=12, text_color="#000"
    )
    assert label.__json__() == {
        "interval": "auto",
        "rotate": 0,
        "margin": 8,
        "textStyle": {"fontSize": 12, "color": "#000"},
    }


def test_yaxis_none_formatter():
    label = YAxisLabel(
        interval="auto",
        rotate=0,
        margin=8,
        text_size=12,
        text_color="#000",
        formatter=None,
    )
    assert label.__json__() == {
        "interval": "auto",
        "rotate": 0,
        "margin": 8,
        "textStyle": {"fontSize": 12, "color": "#000"},
    }


def test_yaxis_str_formatter():
    label = YAxisLabel(
        interval="auto",
        rotate=0,
        margin=8,
        text_size=12,
        text_color="#000",
        formatter="",
    )
    assert label.__json__() == {
        "interval": "auto",
        "rotate": 0,
        "margin": 8,
        "textStyle": {"fontSize": 12, "color": "#000"},
        "formatter": "{value} ",
    }


def test_yaxis_func_formatter():
    def formatter(params):
        return "test"

    label = YAxisLabel(
        interval="auto",
        rotate=0,
        margin=8,
        text_size=12,
        text_color="#000",
        formatter=formatter,
    )
    json_obj = label.__json__()
    assert isinstance(json_obj["formatter"], types.FunctionType)
    del json_obj["formatter"]
    assert json_obj == {
        "interval": "auto",
        "rotate": 0,
        "margin": 8,
        "textStyle": {"fontSize": 12, "color": "#000"},
    }
