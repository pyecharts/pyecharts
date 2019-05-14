from unittest.mock import patch

from nose.tools import assert_in

from pyecharts.components import Table


@patch("pyecharts.render.engine.write_utf8_html_file")
def test_table_base(fake_writer):
    table = Table()

    headers = ["City name", "Area", "Population", "Annual Rainfall"]
    rows = [["Brisbane", 5905, 1857594, 1146.4], ["Perth", 5386, 1554769, 869.4]]
    table.add(headers, rows).render()
    _, content = fake_writer.call_args[0]
    assert_in("fl-table", content)
