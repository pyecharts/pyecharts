# coding=utf-8

from ...commons import consts, utils
from ...commons.structures import OrderedSet
from ...render.engine import RenderEngine


class Page:
    """
    <<< 同一网页按顺序展示多图 >>>

    A container object to present multiple charts vertically in a single page
    """

    def __init__(self, page_title="EChart", js_host=consts.ONLINE_HOST):
        self.page_title = page_title
        self._charts = []
        self.js_dependencies = OrderedSet()
        self.js_host = js_host

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

    def render(self, path="render.html", template_name="simple_page.html"):
        for c in self:
            c.options = c.dump_options()
        RenderEngine().render_chart_to_file(
            template_name=template_name, chart=self, path=path
        )

    def _repr_html_(self):
        require_config = utils.produce_require_dict(self.js_dependencies, self.js_host)
        for c in self:
            c.options = c.dump_options()
        return RenderEngine().render_chart_to_notebook(
            template_name="notebook.html",
            charts=self,
            config_items=require_config["config_items"],
            libraries=require_config["libraries"],
        )
