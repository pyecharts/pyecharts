import os
import sys

from nose.tools import assert_raises

from pyecharts import Bar
from pyecharts.constants import PY35_ABOVE
import pyecharts.exceptions as exceptions
import pyecharts.javascript as javascript

from test.utils import get_default_rendering_file_content


WINDOWS = sys.platform == 'win32'


def label_formatter(params):
    return params.name + 'abc'


def generic_formatter_t_est(**keywords):
    attr = ["Jan", "Feb"]
    v1 = [2.0, 4.9]
    bar = Bar("Bar chart", "precipitation and evaporation one year")
    if PY35_ABOVE:
        if WINDOWS:
            with assert_raises(exceptions.ExtensionMissing):
                bar.add("precipitation", attr, v1, mark_line=["average"],
                        mark_point=["max", "min"],
                        **keywords)
        else:
            bar.add("precipitation", attr, v1, mark_line=["average"],
                    mark_point=["max", "min"], **keywords)
            bar.render()
    else:
        with assert_raises(exceptions.JavascriptNotSupported):
            bar.add("precipitation", attr, v1, mark_line=["average"],
                    mark_point=["max", "min"], **keywords)

    javascript.clear()


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
