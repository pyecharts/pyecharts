import unittest
from unittest.mock import patch

from pyecharts import options as opts
from pyecharts.components import Table
from pyecharts.globals import CurrentConfig, NotebookType


def _gen_table() -> Table:
    table = Table()

    headers = ["City name", "Area", "Population", "Annual Rainfall"]
    rows = [["Brisbane", 5905, 1857594, 1146.4], ["Perth", 5386, 1554769, 869.4]]
    table.add(headers, rows)
    return table


class TestTableComponent(unittest.TestCase):
    @patch("pyecharts.render.engine.write_utf8_html_file")
    def test_table_base(self, fake_writer):
        table = _gen_table()
        table.render()
        _, content = fake_writer.call_args[0]
        self.assertIn("fl-table", content)

    @patch("pyecharts.render.engine.write_utf8_html_file")
    def test_table_base_v1(self, fake_writer):
        table = _gen_table()
        table.set_global_opts(title_opts=opts.ComponentTitleOpts(title="Table Test"))
        table.render()
        _, content = fake_writer.call_args[0]
        self.assertIn("fl-table", content)

    def test_table_render_notebook(self):
        CurrentConfig.NOTEBOOK_TYPE = NotebookType.JUPYTER_NOTEBOOK
        table = _gen_table()
        html = table.render_notebook().__html__()
        self.assertIn("City name", html)
        self.assertIn("Brisbane", html)

    def test_table_render_jupyter_lab(self):
        CurrentConfig.NOTEBOOK_TYPE = NotebookType.JUPYTER_LAB
        table = _gen_table()
        html = table.render_notebook().__html__()
        self.assertIn("City name", html)
        self.assertIn("Brisbane", html)

    def test_table_render_embed(self):
        table = _gen_table()
        s = table.render_embed()
        assert s is not None
