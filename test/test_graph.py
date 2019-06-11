from unittest.mock import patch

from nose.tools import eq_

from pyecharts import options as opts
from pyecharts.charts import Graph


@patch("pyecharts.render.engine.write_utf8_html_file")
def test_graph_base(fake_writer):
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
    c.render()
    _, content = fake_writer.call_args[0]
    eq_(c.theme, "white")
    eq_(c.renderer, "canvas")


def test_graph_item():
    node_name, link_source = "test_node_name", "test_link_source"
    node = opts.GraphNode(name=node_name)
    link = opts.GraphLink(source=link_source)
    eq_(node_name, node.opts.get("name"))
    eq_(link_source, link.opts.get("source"))
