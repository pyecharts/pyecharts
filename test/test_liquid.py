from nose.tools import eq_

from pyecharts.charts import Liquid


def test_liquid_base():
    c = Liquid().add("lq", [0.6, 0.7])
    eq_(c.theme, "white")
    eq_(c.renderer, "canvas")
    c.render()
