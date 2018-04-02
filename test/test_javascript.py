import os
import re
import sys
import json
from datetime import date
import numpy as np

from nose.tools import assert_raises, eq_

from pyecharts import Bar, Polar
from pyecharts.constants import PY35_ABOVE
import pyecharts.exceptions as exceptions
from pyecharts.javascript import GLOBAL_CALLBACKS

from test.utils import get_default_rendering_file_content


WINDOWS = sys.platform == 'win32'


def label_formatter(params):
    return params.name + 'abc'


def generic_formatter_t_est(**keywords):
    attr = ["Jan", "Feb"]
    v1 = [2.0, 4.9]
    bar = Bar("Bar chart", "precipitation and evaporation one year")
    if PY35_ABOVE:
        bar.add(
            "precipitation",
            attr,
            v1,
            mark_line=["average"],
            mark_point=["max", "min"],
            **keywords
        )
        if WINDOWS:
            with assert_raises(exceptions.ExtensionMissing):
                bar.render()
        else:
            bar.render()
    else:
        with assert_raises(exceptions.JavascriptNotSupported):
            bar.add(
                "precipitation",
                attr,
                v1,
                mark_line=["average"],
                mark_point=["max", "min"],
                **keywords
            )


def test_label_formatter():
    generic_formatter_t_est(label_formatter=label_formatter)
    if PY35_ABOVE and not WINDOWS:
        content = get_default_rendering_file_content()
        assert 'function label_formatter(params)' in content
        assert 'params.name + \"abc\"' in content
        assert '"formatter": label_formatter' in content
        os.unlink('render.html')


def yaxis_formatter(value, index):
    return value + index


def test_yaxis_formatter():
    generic_formatter_t_est(yaxis_formatter=yaxis_formatter)
    if PY35_ABOVE and not WINDOWS:
        content = get_default_rendering_file_content()
        assert 'function yaxis_formatter(value, index)' in content
        assert 'value + index' in content
        assert '"formatter": yaxis_formatter' in content
        os.unlink('render.html')


def xaxis_formatter(value, index):
    return value + index


def test_xaxis_formatter():
    generic_formatter_t_est(xaxis_formatter=xaxis_formatter)
    if PY35_ABOVE and not WINDOWS:
        content = get_default_rendering_file_content()
        assert 'function xaxis_formatter(value, index)' in content
        assert 'value + index' in content
        assert '"formatter": xaxis_formatter' in content
        os.unlink('render.html')


def tooltip_formatter(params):
    return params.name + 'abc'


def test_tooltip_formatter():
    generic_formatter_t_est(tooltip_formatter=tooltip_formatter)
    if PY35_ABOVE and not WINDOWS:
        content = get_default_rendering_file_content()
        assert 'function tooltip_formatter(params)' in content
        assert 'params.name + \"abc\"' in content
        assert '"formatter": tooltip_formatter' in content
        os.unlink('render.html')


def custom_polar_render_item(params, api):
    return 'test'


def test_polar_draw_snail():
    data = []
    polar = Polar("polar test")
    if PY35_ABOVE:
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
        if WINDOWS:
            with assert_raises(exceptions.ExtensionMissing):
                polar.render()
        else:
            polar.render()
            content = get_default_rendering_file_content()
            assert 'function custom_polar_render_item(params, api)' in content
            assert 'return "test"' in content
            assert '"renderItem": custom_polar_render_item' in content
            os.unlink('render.html')
    else:
        with assert_raises(exceptions.JavascriptNotSupported):
            polar.add(
                "",
                data,
                symbol_size=0,
                symbol='circle',
                start_angle=-25,
                area_color="#f3c5b3",
                type='custom',
                render_item=custom_polar_render_item,
                area_opacity=0.5,
                is_angleaxis_show=False,
            )


def global_formatter(params):
    return params.name + 'abc'


def global_formatter_t_est(**keywords):
    attr = ["Jan", "Feb"]
    v1 = [2.0, 4.9]
    bar = Bar("Bar chart", "precipitation and evaporation one year")
    if PY35_ABOVE:
        bar.add(
            "precipitation",
            attr,
            v1,
            mark_line=["average"],
            mark_point=["max", "min"],
            **keywords
        )
        if WINDOWS:
            with assert_raises(exceptions.ExtensionMissing):
                bar.render()
        else:
            bar.render()
    else:
        with assert_raises(exceptions.JavascriptNotSupported):
            bar.add(
                "precipitation",
                attr,
                v1,
                mark_line=["average"],
                mark_point=["max", "min"],
                **keywords
            )


def test_global_formatter():
    GLOBAL_CALLBACKS.add_a_python_function(global_formatter)
    generic_formatter_t_est(
        label_formatter=global_formatter,
        tooltip_formatter=global_formatter)
    if PY35_ABOVE and not WINDOWS:
        content = get_default_rendering_file_content()
        occurences = [
            m.start() for m in
            re.finditer('function global_formatter\(params\)', content)]
        eq_(len(occurences), 1)
        assert 'params.name + \"abc\"' in content
        occurences = [
            m.start() for m in
            re.finditer('"formatter": global_formatter', content)]
        eq_(len(occurences), 2)
        os.unlink('render.html')
    GLOBAL_CALLBACKS.clear()


def test_json_encoder():
    """
    Test json encoder.
    :return:
    """
    data = date(2017, 1, 1)
    bar = Bar()
    bar._option = {'date': data, 'a': '1'}
    eq_(
        json.dumps({'date': '2017-01-01', 'a': '1'}, indent=4),
        bar.translate_options()
    )

    bar._option = {'np_list': np.array(['a', 'b', 'c'])}
    data2_e = {'np_list': ['a', 'b', 'c']}
    eq_(json.dumps(data2_e, indent=4), bar.translate_options())
