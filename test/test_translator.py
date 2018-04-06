# coding=utf8

from __future__ import unicode_literals

import os
import unittest

from nose.tools import assert_raises

from pyecharts import Bar, Polar
from pyecharts.translator.api import TRANSLATOR
from pyecharts.translator.compat import (
    TranslatorCompatAPI,
    FunctionTranslatorDisabled
)
from test.utils import get_default_rendering_file_content

SHOULD_TEST_JS_TRANSLATE = TranslatorCompatAPI.check_enabled()
SKIP_MESSAGE = 'Javascript-translate is not supported on current environment'


# ----- Test cases for Translator API -----

@unittest.skipUnless(SHOULD_TEST_JS_TRANSLATE, SKIP_MESSAGE)
def test_basic_usage():
    def my_fmt(x):
        return x + 5

    def my_fmt2(x, z, y):
        return '{x},{y},{z}'.format(x=x, y=y, z=z)

    source = {'a': '23', 'b': my_fmt, 'c': my_fmt2, 'd': '-=>test<=-'}
    snippet = TRANSLATOR.translate(source)
    assert 'function my_fmt' in snippet.function_snippet
    assert 'function my_fmt2' in snippet.function_snippet
    assert 'function test' not in snippet.function_snippet
    assert '"my_fmt"' not in snippet.option_snippet
    assert '"my_fmt2"' not in snippet.option_snippet
    assert '"-=>test<=-"' in snippet.option_snippet

    source2 = {'e': my_fmt}
    snippet = TRANSLATOR.translate(source2)
    assert 'function my_fmt' in snippet.function_snippet
    assert '"my_fmt"' not in snippet.option_snippet


@unittest.skipIf(SHOULD_TEST_JS_TRANSLATE, SKIP_MESSAGE)
def test_usage_on_unsupported():
    with assert_raises(FunctionTranslatorDisabled):
        def my_fmt(x):
            return x + 5

        def my_fmt2(x, z, y):
            return '{x},{y},{z}'.format(x=x, y=y, z=z)

        source = {'a': '23', 'b': my_fmt, 'c': my_fmt2, 'd': '-=>test<=-'}
        TRANSLATOR.translate(source)


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
    return params.name + 'abc'


@unittest.skipUnless(SHOULD_TEST_JS_TRANSLATE, SKIP_MESSAGE)
def test_label_formatter_with_function():
    generic_formatter_t_est(label_formatter=label_formatter)
    content = get_default_rendering_file_content()

    assert 'function label_formatter(params)' in content
    assert 'params.name + \"abc\"' in content
    assert '"formatter": label_formatter' in content
    os.unlink('render.html')


@unittest.skipIf(SHOULD_TEST_JS_TRANSLATE, SKIP_MESSAGE)
def test_label_formatter_on_unsupported():
    with assert_raises(FunctionTranslatorDisabled):
        generic_formatter_t_est(label_formatter=label_formatter)


def tooltip_formatter(params):
    return params.name + 'abc'


@unittest.skipUnless(SHOULD_TEST_JS_TRANSLATE, SKIP_MESSAGE)
def test_xaxis_formatter_with_function():
    generic_formatter_t_est(tooltip_formatter=tooltip_formatter)
    content = get_default_rendering_file_content()

    assert 'function tooltip_formatter(params)' in content
    assert 'params.name + \"abc\"' in content
    assert '"formatter": tooltip_formatter' in content
    os.unlink('render.html')


@unittest.skipIf(SHOULD_TEST_JS_TRANSLATE, SKIP_MESSAGE)
def test_xaxis_formatter_on_unsupported():
    with assert_raises(FunctionTranslatorDisabled):
        generic_formatter_t_est(tooltip_formatter=tooltip_formatter)


def custom_polar_render_item(params, api):
    return 'test'


def render_polar():
    data = []
    polar = Polar("polar test")
    polar.add(
        "",
        data,
        symbol_size=0,
        symbol='circle',
        area_color="#f3c5b3",
        type='custom',
        render_item=custom_polar_render_item,
        area_opacity=0.5,
        is_angleaxis_show=False,
    )
    polar.render()


@unittest.skipUnless(SHOULD_TEST_JS_TRANSLATE, SKIP_MESSAGE)
def test_polar_draw_snail():
    render_polar()
    content = get_default_rendering_file_content()

    assert 'function custom_polar_render_item(params, api)' in content
    assert 'return "test"' in content
    assert '"renderItem": custom_polar_render_item' in content
    os.unlink('render.html')


@unittest.skipIf(SHOULD_TEST_JS_TRANSLATE, SKIP_MESSAGE)
def test_polar_draw_snail_on_unsupported():
    with assert_raises(FunctionTranslatorDisabled):
        render_polar()
