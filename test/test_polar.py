import random

from pyecharts import options as opts
from pyecharts.charts import Polar


def test_polar_scatter():
    data = [(i, random.randint(1, 100)) for i in range(101)]
    c = Polar().add("", data, type_="scatter", label_opts=opts.LabelOpts(is_show=False))
    assert c.theme == "white"
    assert c.renderer == "canvas"
    c.render("render.html")
