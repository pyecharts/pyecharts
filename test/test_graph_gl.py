import unittest
from unittest.mock import patch

from pyecharts import options as opts
from pyecharts.charts import GraphGL


class TestGraphGLChart(unittest.TestCase):
    @patch("pyecharts.render.engine.write_utf8_html_file")
    def test_graph_gl_base(self, fake_writer):
        # Arrange: estrutura mínima representativa (2 nós e 1 aresta)
        nodes = [
            opts.GraphGLNode(x=1, y=1, value=1),
            opts.GraphGLNode(x=2, y=2, value=1),
        ]
        links = [opts.GraphGLLink(source=0, target=1, value=1)]

        # Act
        c = (
            GraphGL()
            .add(series_name="", nodes=nodes, links=links)
            .set_dark_mode()
        )
        c.render()

        # Assert
        fake_writer.assert_called_once()
        self.assertEqual(c.theme, "dark")
        self.assertEqual(c.renderer, "canvas")

