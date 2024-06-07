import unittest
from typing import Iterable
from unittest.mock import patch

from pyecharts import options as opts
from pyecharts.charts import Bar, Line, Tab
from pyecharts.commons.utils import OrderedSet
from pyecharts.components import Table
from pyecharts.faker import Faker
from pyecharts.globals import ThemeType


def _create_bar() -> Bar:
    return (
        Bar(init_opts=opts.InitOpts(theme=ThemeType.ESSOS))
        .add_xaxis(Faker.week)
        .add_yaxis("商家A", [1, 2, 3, 4, 5, 6, 7])
    )


def _create_line() -> Line:
    return Line().add_xaxis(Faker.week).add_yaxis("商家A", [7, 6, 5, 4, 3, 2, 1])


def _create_table() -> Table:
    table = Table()
    headers = ["City name", "Area", "Population", "Annual Rainfall"]
    rows = [
        ["Brisbane", 5905, 1857594, 1146.4],
        ["Adelaide", 1295, 1158259, 600.5],
        ["Darwin", 112, 120900, 1714.7],
    ]
    table.add(headers, rows)
    return table


class TestTabComponent(unittest.TestCase):
    @patch("pyecharts.render.engine.write_utf8_html_file")
    def test_tab_base(self, fake_writer):
        bar = _create_bar()
        line = _create_line()
        tab = Tab().add(bar, "bar-example").add(line, "line-example")
        tab.render()
        _, content = fake_writer.call_args[0]
        self.assertIn("bar-example", content)
        self.assertIn("line-example", content)

    def test_tab_render_embed(self):
        bar = _create_bar()
        line = _create_line()
        content = Tab().add(bar, "bar").add(line, "line").render_embed()
        self.assertTrue(len(content) > 8000)

    def test_tab_render_notebook(self):
        from pyecharts.globals import CurrentConfig, NotebookType

        CurrentConfig.NOTEBOOK_TYPE = NotebookType.JUPYTER_NOTEBOOK

        tab = Tab()
        tab.add(_create_line(), "line-example")
        tab.add(_create_bar(), "bar-example")
        tab.add(_create_table(), "table-example")
        html = tab.render_notebook().__html__()
        self.assertIn("City name", html)

    def test_page_jshost_default(self):
        bar = _create_bar()
        tab = Tab().add(bar, "bar")
        self.assertEqual(tab.js_host, "https://assets.pyecharts.org/assets/v5/")

    def test_tab_jshost_custom(self):
        from pyecharts.globals import CurrentConfig

        default_host = CurrentConfig.ONLINE_HOST
        custom_host = "http://localhost:8888/assets/"
        CurrentConfig.ONLINE_HOST = custom_host
        bar = _create_bar()
        line = _create_line()
        tab = Tab().add(bar, "bar").add(line, "line")
        self.assertEqual(tab.js_host, custom_host)
        CurrentConfig.ONLINE_HOST = default_host

    def test_tab_iterable(self):
        tab = Tab()
        self.assertTrue(isinstance(tab, Iterable))

    def test_tab_attr(self):
        tab = Tab()
        self.assertTrue(isinstance(tab.js_functions, OrderedSet))
        self.assertTrue(isinstance(tab._charts, list))

    def test_tab_with_chart_container(self):
        tab = Tab(
            tab_css_opts=opts.TabChartGlobalOpts(
                is_enable=False, tab_base_css={"overflow": "hidden"}
            )
        )
        self.assertTrue(isinstance(tab._charts, list))
