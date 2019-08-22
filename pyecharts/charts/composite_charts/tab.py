from jinja2 import Environment

from ... import types
from ...charts.composite_charts.page import IterChart
from ...globals import CurrentConfig


class Tab(IterChart):
    def __init__(self, page_title: str = CurrentConfig.PAGE_TITLE, js_host: str = ""):
        super().__init__(js_host=js_host or CurrentConfig.ONLINE_HOST)
        self.page_title = page_title
        self.download_button: bool = False

    def add(self, chart, tab_name):
        chart.tab_name = tab_name
        self._charts.append(chart)
        for d in chart.js_dependencies.items:
            self.js_dependencies.add(d)
        return self

    def render(
        self,
        path: str = "render.html",
        template_name: str = "simple_tab.html",
        env: types.Optional[Environment] = None,
        **kwargs,
    ) -> str:
        return super()._render(path, template_name, env, **kwargs)

    def render_embed(
        self,
        template_name: str = "simple_tab.html",
        env: types.Optional[Environment] = None,
        **kwargs,
    ) -> str:
        return super()._render_embed(template_name, env, **kwargs)

    def render_notebook(self):
        return super()._render_notebook("jupyter_notebook_tab.html", "jupyter_lab.html")
