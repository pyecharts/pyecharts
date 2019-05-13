import os

from jinja2 import Environment
from prettytable import PrettyTable

from ..commons.types import Optional, Sequence
from ..commons.utils import OrderedSet
from ..globals import CurrentConfig
from ..render.display import HTML
from ..render.engine import RenderEngine


class Table:
    def __init__(
        self,
        page_title: str = "Awesome-pyecharts",
        js_host: str = CurrentConfig.ONLINE_HOST,
    ):
        self.page_title = page_title
        self.js_host = js_host
        self.js_dependencies: OrderedSet = OrderedSet()
        self._charts = []

    def add(self, headers: Sequence, rows: Sequence, attributes: Optional[dict] = None):
        attributes = attributes or {"class": "fl-table"}
        table = PrettyTable(headers, attributes=attributes)
        for r in rows:
            table.add_row(r)
        self._charts.append(table.get_html_string())
        return self

    # List-Like Feature
    def __iter__(self):
        for chart in self._charts:
            yield chart

    def __len__(self):
        return len(self._charts)

    def render(
        self,
        path: str = "render.html",
        template_name: str = "table.html",
        env: Optional[Environment] = None,
    ) -> str:
        RenderEngine(env).render_chart_to_file(
            chart=self, path=path, template_name=template_name
        )
        return os.path.abspath(path)

    def render_notebook(self):
        return HTML(RenderEngine().render_chart_to_notebook("table.html", chart=self))
