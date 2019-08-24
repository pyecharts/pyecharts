import uuid

from jinja2 import Environment

from ... import types
from ...commons import utils
from ...globals import CurrentConfig, ThemeType
from ...render.engine import Render


class Tab(Render):
    def __init__(self, page_title: str = CurrentConfig.PAGE_TITLE, js_host: str = ""):
        self.js_host: str = js_host or CurrentConfig.ONLINE_HOST
        self.page_title: str = page_title
        self.download_button: bool = False
        self.js_functions: utils.OrderedSet = utils.OrderedSet()
        self.js_dependencies = utils.OrderedSet()
        self._charts: list = []

    def add(self, chart, tab_name):
        chart.tab_name = tab_name
        self._charts.append(chart)
        for d in chart.js_dependencies.items:
            self.js_dependencies.add(d)
        return self

    def __iter__(self):
        for chart in self._charts:
            yield chart

    def __len__(self):
        return len(self._charts)

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

    def _prepare_render(self):
        for c in self:
            c.json_contents = c.dump_options()
            if c.theme not in ThemeType.BUILTIN_THEMES:
                self.js_dependencies.add(c.theme)

    def render_notebook(self):
        for c in self:
            c.json_contents = c.dump_options()
            c.chart_id = uuid.uuid4().hex
            if c.theme not in ThemeType.BUILTIN_THEMES:
                self.js_dependencies.add(c.theme)
        return super()._render_notebook("jupyter_notebook_tab.html", "jupyter_lab.html")
