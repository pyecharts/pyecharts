import os

from jinja2 import Environment
from prettytable import PrettyTable

from pyecharts.types import Optional, Sequence, Union

from ..commons.utils import OrderedSet
from ..globals import CurrentConfig
from ..options import ComponentTitleOpts
from ..render.display import HTML
from ..render.engine import RenderEngine


class Table:
    def __init__(self, page_title: str = CurrentConfig.PAGE_TITLE, js_host: str = ""):
        self.page_title = page_title
        self.js_host = js_host or CurrentConfig.ONLINE_HOST
        self.js_dependencies: OrderedSet = OrderedSet()
        self._tables = []
        self.title_opts = ComponentTitleOpts()

    def add(self, headers: Sequence, rows: Sequence, attributes: Optional[dict] = None):
        attributes = attributes or {"class": "fl-table"}
        table = PrettyTable(headers, attributes=attributes)
        for r in rows:
            table.add_row(r)
        self._tables.append(table.get_html_string())
        return self

    def set_global_opts(self, title_opts: Union[ComponentTitleOpts, dict, None] = None):
        self.title_opts = title_opts
        return self

    # List-Like Feature
    def __iter__(self):
        for chart in self._tables:
            yield chart

    def __len__(self):
        return len(self._tables)

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
