# coding=utf8

from __future__ import unicode_literals

import os

from pyecharts import Bar, Polar
from test.utils import get_default_rendering_file_content


# ------ Test Cases for Chart Rendering -----


def generic_formatter_t_est(**keywords):
    attr = ["Jan", "Feb"]
    v1 = [2.0, 4.9]
    bar = Bar("Bar chart", "precipitation and evaporation one year")
    bar.add(
        "precipitation",
        attr,
        v1,
        mark_line=["average"],
        mark_point=["max", "min"],
        **keywords
    )
    bar.render()


def label_formatter(params):
    return params.name + "abc"


def test_label_formatter_with_function():
    generic_formatter_t_est(label_formatter=label_formatter)
    content = get_default_rendering_file_content()

    assert "function label_formatter(params)" in content
    assert 'params.name + "abc"' in content
    assert '"formatter": label_formatter' in content
    os.unlink("render.html")


def tooltip_formatter(params):
    return params.name + "abc"


def test_xaxis_formatter_with_function():
    generic_formatter_t_est(tooltip_formatter=tooltip_formatter)
    content = get_default_rendering_file_content()

    assert "function tooltip_formatter(params)" in content
    assert 'params.name + "abc"' in content
    assert '"formatter": tooltip_formatter' in content
    os.unlink("render.html")


def custom_polar_render_item(params, api):
    return "test"


def render_polar():
    data = []
    polar = Polar("polar test")
    polar.add(
        "",
        data,
        symbol_size=0,
        symbol="circle",
        area_color="#f3c5b3",
        type="custom",
        render_item=custom_polar_render_item,
        area_opacity=0.5,
        is_angleaxis_show=False,
    )
    polar.render()


def test_polar_draw_snail():
    render_polar()
    content = get_default_rendering_file_content()

    assert "function custom_polar_render_item(params, api)" in content
    assert 'return "test"' in content
    assert '"renderItem": custom_polar_render_item' in content
    os.unlink("render.html")
