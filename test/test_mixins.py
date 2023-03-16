from unittest.mock import patch

from nose.tools import assert_equal

from pyecharts import options as opts
from pyecharts.charts import Bar, Line
from pyecharts.charts.mixins import CompositeMixin


class CustomCompositeChart(CompositeMixin):
    def __init__(self):
        self._charts: list = []

    def add(self, chart, tab_name):
        chart.tab_name = tab_name
        self._charts.append(chart)
        return self


def test_composite_mixin_len():
    b_1 = Bar()
    b_2 = Line()
    c = CustomCompositeChart()
    c.add(b_1, "bar")
    c.add(b_2, "line")
    assert len(c) == 2
