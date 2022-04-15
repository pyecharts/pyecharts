from unittest.mock import patch

from nose.tools import assert_in

from pyecharts import options as opts
from pyecharts.components import Table
from pyecharts.globals import CurrentConfig, NotebookType


def _gen_table() -> Table:
    table = Table()

    headers = ["City name", "Area", "Population", "Annual Rainfall"]
    rows = [["Brisbane", 5905, 1857594, 1146.4], ["Perth", 5386, 1554769, 869.4]]
    table.add(headers, rows)
    return table


@patch("pyecharts.render.engine.write_utf8_html_file")
def test_table_base(fake_writer):
    table = _gen_table()
    table.render()
    _, content = fake_writer.call_args[0]
    assert_in("fl-table", content)


@patch("pyecharts.render.engine.write_utf8_html_file")
def test_table_base_v1(fake_writer):
    table = _gen_table()
    table.set_global_opts(title_opts=opts.ComponentTitleOpts(title="Table Test"))
    table.render()
    _, content = fake_writer.call_args[0]
    assert_in("fl-table", content)


def test_table_render_notebook():
    CurrentConfig.NOTEBOOK_TYPE = NotebookType.JUPYTER_NOTEBOOK
    table = _gen_table()
    html = table.render_notebook().__html__()
    assert_in("City name", html)
    assert_in("Brisbane", html)


def test_table_render_jupyter_lab():
    CurrentConfig.NOTEBOOK_TYPE = NotebookType.JUPYTER_LAB
    table = _gen_table()
    html = table.render_notebook().__html__()
    assert_in("City name", html)
    assert_in("Brisbane", html)


def test_table_render_embed():
    table = _gen_table()
    s = table.render_embed()
    assert s is not None
