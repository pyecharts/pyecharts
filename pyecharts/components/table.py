# coding=utf-8
from prettytable import PrettyTable

from ..commons.types import List
from ..globals import CurrentConfig
from ..render.engine import RenderEngine
from ..commons import utils


class Table:
    def __init__(
        self,
        page_title: str = "Awesome-pyecharts",
        js_host: str = CurrentConfig.ONLINE_HOST,
    ):
        self.page_title = page_title
        self.js_host = js_host
        self.js_dependencies = utils.OrderedSet("bulma")
        self._charts = []

    def add(self, headers: List, rows: List):
        table = PrettyTable(headers)
        for r in rows:
            table.add_row(r)
        self._charts.append(
            table.get_html_string(
                attributes={
                    "class": "table is-bordered is-striped is-narrow is-hoverable is-fullwidth"
                }
            )
        )
        return self

    # List-Like Feature
    def __iter__(self):
        for chart in self._charts:
            yield chart

    def __len__(self):
        return len(self._charts)

    def _repr_html_(self):
        return RenderEngine().render_chart_to_notebook("table.html", chart=self)
