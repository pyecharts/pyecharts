import os
import json
import unittest
from unittest.mock import patch

from pyecharts import options as opts
from pyecharts.charts import Graph


class TestGraphChart(unittest.TestCase):
    @patch("pyecharts.render.engine.write_utf8_html_file")
    def test_graph_base(self, fake_writer):
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
        self.assertEqual(c.theme, "white")
        self.assertEqual(c.renderer, "canvas")

    @patch("pyecharts.render.engine.write_utf8_html_file")
    def test_graph_base_v1(self, fake_writer):
        nodes = [
            opts.GraphNode(name="结点1", symbol_size=10),
            opts.GraphNode(name="结点2", symbol_size=20),
            opts.GraphNode(name="结点3", symbol_size=30),
            opts.GraphNode(name="结点4", symbol_size=40),
            opts.GraphNode(name="结点5", symbol_size=50),
        ]
        links = [
            opts.GraphLink(source="结点1", target="结点2"),
            opts.GraphLink(source="结点2", target="结点3"),
            opts.GraphLink(source="结点3", target="结点4"),
            opts.GraphLink(source="结点4", target="结点5"),
            opts.GraphLink(source="结点5", target="结点1"),
        ]
        c = (
            Graph()
            .add("", nodes, links, repulsion=4000)
            .set_global_opts(
                title_opts=opts.TitleOpts(title="Graph-GraphNode-GraphLink")
            )
        )
        c.render()
        _, content = fake_writer.call_args[0]
        self.assertEqual(c.theme, "white")
        self.assertEqual(c.renderer, "canvas")

    @patch("pyecharts.render.engine.write_utf8_html_file")
    def test_graph_base_v2(self, fake_writer):
        with open(
            os.path.join("test/fixtures", "les-miserables.json"), "r", encoding="utf-8"
        ) as f:
            j = json.load(f)
            nodes = j["nodes"]
            links = j["links"]
            categories = j["categories"]

        categories = [opts.GraphCategory(name=d.get("name")) for d in categories]

        c = (
            Graph(init_opts=opts.InitOpts(width="1000px", height="600px"))
            .add(
                "",
                nodes=nodes,
                links=links,
                categories=categories,
                layout="circular",
                is_rotate_label=True,
                linestyle_opts=opts.LineStyleOpts(color="source", curve=0.3),
                label_opts=opts.LabelOpts(position="right"),
            )
            .set_global_opts(
                title_opts=opts.TitleOpts(title="Graph-Les Miserables"),
                legend_opts=opts.LegendOpts(
                    orient="vertical", pos_left="2%", pos_top="20%"
                ),
            )
        )
        c.render()
        _, content = fake_writer.call_args[0]
        self.assertEqual(c.theme, "white")
        self.assertEqual(c.renderer, "canvas")

    @patch("pyecharts.render.engine.write_utf8_html_file")
    def test_graph_draggable_and_symbol_size(self, fake_writer):
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
        c = Graph().add(
            "", nodes, links, repulsion=8000, is_draggable=True, symbol_size=50
        )
        c.render()
        _, content = fake_writer.call_args[0]
        self.assertIn("draggable", content)
        self.assertIn("symbolSize", content)

    @patch("pyecharts.render.engine.write_utf8_html_file")
    def test_graph_edge_label_opts(self, fake_writer):
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
        c = Graph().add(
            "", nodes, links, repulsion=4000, edge_label=opts.LabelOpts(is_show=True)
        )
        c.render()
        _, content = fake_writer.call_args[0]
        self.assertIn("edgeLabel", content)

    def test_graph_item(self):
        node_name, link_source = "test_node_name", "test_link_source"
        node = opts.GraphNode(name=node_name)
        link = opts.GraphLink(source=link_source)
        self.assertEqual(node_name, node.opts.get("name"))
        self.assertEqual(link_source, link.opts.get("source"))
