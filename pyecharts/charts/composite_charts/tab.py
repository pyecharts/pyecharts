import os
import uuid

from jinja2 import Environment

from ... import types
from ...commons import utils
from ...globals import CurrentConfig, NotebookType, ThemeType
from ...render.display import HTML
from ...render.engine import RenderEngine


class Tab:
    def __init__(
        self,
        page_title: str = CurrentConfig.PAGE_TITLE,
        js_host: str = "",
    ):
        self.page_title = page_title
        self.js_dependencies = utils.OrderedSet()
        self.js_functions: utils.OrderedSet = utils.OrderedSet()
        self.js_host = js_host or CurrentConfig.ONLINE_HOST
        self.download_button: bool = False
        self._charts = []

    def add(self, chart, tab_name):
        chart.tab_name = tab_name
        self._charts.append(chart)
        for d in chart.js_dependencies.items:
            self.js_dependencies.add(d)
        return self

    # List-Like Feature
    def __iter__(self):
        for chart in self._charts:
            yield chart

    def __len__(self):
        return len(self._charts)

    def _prepare_render(self):
        for c in self:
            c.json_contents = c.dump_options()
            if c.theme not in ThemeType.BUILTIN_THEMES:
                self.js_dependencies.add(c.theme)

    # TODO:
    def add_js_funcs(self, *fns):
        for fn in fns:
            self.js_functions.add(fn)
        return self

    def render(
        self,
        path: str = "render.html",
        template_name: str = "simple_tab.html",
        env: types.Optional[Environment] = None,
        **kwargs,
    ) -> str:
        self._prepare_render()
        RenderEngine(env).render_chart_to_file(
            template_name=template_name, chart=self, path=path, **kwargs
        )
        return os.path.abspath(path)

    def render_embed(
        self,
        template_name: str = "simple_tab.html",
        env: types.Optional[Environment] = None,
        **kwargs,
    ) -> str:
        self._prepare_render()
        return RenderEngine(env).render_chart_to_template(
            template_name=template_name, chart=self, **kwargs
        )

    # TODO:
    def render_notebook(self):
        for c in self:
            c.json_contents = c.dump_options()
            c.chart_id = uuid.uuid4().hex
            if c.theme not in ThemeType.BUILTIN_THEMES:
                self.js_dependencies.add(c.theme)

        if CurrentConfig.NOTEBOOK_TYPE == NotebookType.JUPYTER_NOTEBOOK:
            require_config = utils.produce_require_dict(
                self.js_dependencies, self.js_host
            )
            return HTML(
                RenderEngine().render_chart_to_notebook(
                    template_name="jupyter_notebook_tab.html",
                    charts=self,
                    config_items=require_config["config_items"],
                    libraries=require_config["libraries"],
                )
            )
