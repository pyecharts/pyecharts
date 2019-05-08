from nose.tools import eq_

from pyecharts import options as opts
from pyecharts.charts import Sankey


def test_sankey_base():
    nodes = [{"name": "category1"}, {"name": "category2"}, {"name": "category3"}]

    links = [
        {"source": "category1", "target": "category2", "value": 10},
        {"source": "category2", "target": "category3", "value": 15},
    ]
    c = Sankey().add(
        "sankey",
        nodes,
        links,
        linestyle_opt=opts.LineStyleOpts(opacity=0.2, curve=0.5, color="source"),
        label_opts=opts.LabelOpts(position="right"),
    )
    eq_(c.theme, "white")
    eq_(c.renderer, "canvas")
    c.render()
