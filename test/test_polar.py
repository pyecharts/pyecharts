import random

from nose.tools import eq_

from pyecharts import options as opts
from pyecharts.charts import Polar


def test_polar_scatter():
    data = [(i, random.randint(1, 100)) for i in range(101)]
    c = Polar().add("", data, type_="scatter", label_opts=opts.LabelOpts(is_show=False))
    eq_(c.theme, "white")
    eq_(c.renderer, "canvas")
    c.render()
