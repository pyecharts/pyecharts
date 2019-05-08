from nose.tools import eq_

from pyecharts.charts import Scatter


def test_bar_base():
    c = (
        Scatter()
        .add_xaxis(["A", "B", "C"])
        .add_yaxis("series0", [1, 2, 4])
        .add_yaxis("series1", [2, 3, 6])
    )
    eq_(c.theme, "white")
    eq_(c.renderer, "canvas")
    c.render()
