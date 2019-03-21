# coding=utf-8
from ...commons import utils
from ...consts import BUILTIN_THEMES, ONLINE_HOST
from ...render.engine import RenderEngine


class Page:
    """
    <<< 同一网页按顺序展示多图 >>>

    A container object to present multiple charts vertically in a single page
    """

    def __init__(
        self, page_title: str = "Awesome-pyecharts", js_host: str = ONLINE_HOST
    ):
        self.page_title = page_title
        self.js_dependencies = utils.OrderedSet()
        self.js_host = js_host
        self._charts = []

    def add(self, *charts):
        for c in charts:
            self._charts.append(c)
            for d in c.js_dependencies.items:
                self.js_dependencies.add(d)
        return self

    # List-Like Feature
    def __iter__(self):
        for chart in self._charts:
            yield chart

    def __len__(self):
        return len(self._charts)

    def render(
        self, path: str = "render.html", template_name: str = "simple_page.html"
    ):
        for c in self:
            c.options = c.dump_options()
            if c.theme not in BUILTIN_THEMES:
                self.js_dependencies.add(c.theme)
        RenderEngine().render_chart_to_file(
            template_name=template_name, chart=self, path=path
        )

    def _repr_html_(self):
        require_config = utils.produce_require_dict(self.js_dependencies, self.js_host)
        for c in self:
            c.options = c.dump_options()
            if c.theme not in BUILTIN_THEMES:
                self.js_dependencies.add(c.theme)
        return RenderEngine().render_chart_to_notebook(
            template_name="notebook.html",
            charts=self,
            config_items=require_config["config_items"],
            libraries=require_config["libraries"],
        )
