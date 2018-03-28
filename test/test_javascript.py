import os

from nose.tools import assert_raises

from pyecharts import Bar
from pyecharts.constants import PY35_ABOVE
import pyecharts.exceptions as exceptions

from test.utils import get_default_rendering_file_content


def label_formatter(params):
    return params.name + 'abc'


def test_label_formatter():
    attr = ["Jan", "Feb"]
    v1 = [2.0, 4.9]
    bar = Bar("Bar chart", "precipitation and evaporation one year")
    bar.add("precipitation", attr, v1, mark_line=["average"],
            mark_point=["max", "min"], label_formatter=label_formatter)
    if PY35_ABOVE:
        bar.render()
        content = get_default_rendering_file_content()
        assert 'function label_formatter(params)' in content
        assert 'params.name + \"abc\"' in content
        assert '"formatter": label_formatter' in content
        os.unlink('render.html')
    else:
        with assert_raises(exceptions.JavascriptNotSupported):
            bar.render()


def yaxis_formatter(value, index):
    return value + index


def test_yaxis_formatter():
    attr = ["Jan", "Feb"]
    v1 = [2.0, 4.9]
    bar = Bar("Bar chart", "precipitation and evaporation one year")
    bar.add("precipitation", attr, v1, mark_line=["average"],
            mark_point=["max", "min"], yaxis_formatter=yaxis_formatter)
    if PY35_ABOVE:
        bar.render()
        content = get_default_rendering_file_content()
        assert 'function yaxis_formatter(value, index)' in content
        assert 'value + index' in content
        assert '"formatter": yaxis_formatter' in content
        os.unlink('render.html')
    else:
        with assert_raises(exceptions.JavascriptNotSupported):
            bar.render()


def xaxis_formatter(value, index):
    return value + index


def test_xaxis_formatter():
    attr = ["Jan", "Feb"]
    v1 = [2.0, 4.9]
    bar = Bar("Bar chart", "precipitation and evaporation one year")
    bar.add("precipitation", attr, v1, mark_line=["average"],
            mark_point=["max", "min"], xaxis_formatter=xaxis_formatter)
    if PY35_ABOVE:
        bar.render()
        content = get_default_rendering_file_content()
        assert 'function xaxis_formatter(value, index)' in content
        assert 'value + index' in content
        assert '"formatter": xaxis_formatter' in content
        os.unlink('render.html')
    else:
        with assert_raises(exceptions.JavascriptNotSupported):
            bar.render()


def tooltip_formatter(params):
    return params.name + 'abc'


def test_tooltip_formatter():
    attr = ["Jan", "Feb"]
    v1 = [2.0, 4.9]
    bar = Bar("Bar chart", "precipitation and evaporation one year")
    bar.add("precipitation", attr, v1, mark_line=["average"],
            mark_point=["max", "min"], tooltip_formatter=tooltip_formatter)
    if PY35_ABOVE:
        bar.render()
        content = get_default_rendering_file_content()
        assert 'function tooltip_formatter(params)' in content
        assert 'params.name + \"abc\"' in content
        assert '"formatter": tooltip_formatter' in content
        os.unlink('render.html')
    else:
        with assert_raises(exceptions.JavascriptNotSupported):
            bar.render()
