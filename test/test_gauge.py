from nose.tools import eq_

from pyecharts.charts import Gauge


def test_gauge_base():
    c = Gauge().add("", [("完成率", 66.6)])
    eq_(c.theme, "white")
    eq_(c.renderer, "canvas")
    c.render()
