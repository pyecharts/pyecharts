import uuid

from jinja2 import Environment

from ... import types
from ...commons import utils
from ...datasets import FILENAMES
from ...globals import CurrentConfig, NotebookType, ThemeType
from ...options import PageLayoutOpts
from ...render.display import HTML, Javascript
from ...render.engine import RenderEngine


class Page:
    """
    `Page` A container object to present multiple charts vertically in a single page
    """

    SimplePageLayout = PageLayoutOpts(
        justify_content="center", display="flex", flex_wrap="wrap"
    )

    def __init__(
        self,
        page_title: str = CurrentConfig.PAGE_TITLE,
        js_host: str = "",
        interval: int = 1,
        layout: types.Union[PageLayoutOpts, dict] = PageLayoutOpts(),
    ):
        self.page_title = page_title
        self.page_interval = interval
        self.js_dependencies = utils.OrderedSet()
        self.js_host = js_host or CurrentConfig.ONLINE_HOST
        self.layout = self._assembly_layout(layout)
        self._charts = []

    def add(self, *charts):
        for c in charts:
            self._charts.append(c)
            for d in c.js_dependencies.items:
                self.js_dependencies.add(d)
        return self

    def _assembly_layout(self, layout: types.Union[PageLayoutOpts, dict]) -> str:
        result = ""
        if isinstance(layout, PageLayoutOpts):
            layout = layout.opts
        layout = utils.remove_key_with_none_value(layout)
        for k, v in layout.items():
            result += "{}:{}; ".format(k, v)
        return result

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

    def render(
        self,
        path: str = "render.html",
        template_name: str = "simple_page.html",
        env: types.Optional[Environment] = None,
    ):
        self._prepare_render()
        RenderEngine(env).render_chart_to_file(
            template_name=template_name, chart=self, path=path
        )

    def render_embed(
        self,
        template_name: str = "simple_page.html",
        env: types.Optional[Environment] = None,
    ):
        self._prepare_render()
        return RenderEngine(env).render_chart_to_template(
            template_name=template_name, chart=self
        )

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
                    template_name="jupyter_notebook.html",
                    charts=self,
                    config_items=require_config["config_items"],
                    libraries=require_config["libraries"],
                )
            )

        if CurrentConfig.NOTEBOOK_TYPE == NotebookType.JUPYTER_LAB:
            return HTML(
                RenderEngine().render_chart_to_notebook(
                    template_name="jupyter_lab.html", charts=self
                )
            )

        if CurrentConfig.NOTEBOOK_TYPE == NotebookType.NTERACT:
            pass

    def load_javascript(self):
        scripts = []
        for dep in self.js_dependencies.items:
            f, ext = FILENAMES[dep]
            scripts.append("{}{}.{}".format(CurrentConfig.ONLINE_HOST, f, ext))
        return Javascript(lib=scripts)
