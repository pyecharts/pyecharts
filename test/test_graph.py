from nose.tools import eq_

from pyecharts.charts import Graph


def test_graph_base():
    nodes = [
        {"name": "结点1", "symbolSize": 10},
        {"name": "结点2", "symbolSize": 20},
        {"name": "结点3", "symbolSize": 30},
        {"name": "结点4", "symbolSize": 40},
    ]
    links = []
    for i in nodes:
        for j in nodes:
            links.append({"source": i.get("name"), "target": j.get("name")})
    c = Graph().add("", nodes, links, repulsion=8000)
    eq_(c.theme, "white")
    eq_(c.renderer, "canvas")
    c.render()
