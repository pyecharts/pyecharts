import uuid

from jinja2 import Environment

from ..charts.mixins import ChartMixin
from ..commons.utils import OrderedSet
from ..globals import CurrentConfig
from ..options import ComponentTitleOpts
from ..render import engine
from ..types import Optional, Union


class Image(ChartMixin):
    def __init__(self, page_title: str = CurrentConfig.PAGE_TITLE, js_host: str = ""):
        self.page_title = page_title
        self.js_host = js_host or CurrentConfig.ONLINE_HOST
        self.js_dependencies: OrderedSet = OrderedSet()
        self.title_opts: ComponentTitleOpts = ComponentTitleOpts()
        self.html_content: str = ""
        self._component_type: str = "image"
        self.chart_id: str = uuid.uuid4().hex

    def add(self, src: str, style_opts: Optional[dict] = None):
        html_tag_args = ""
        html_tag_args += 'src="{}" '.format(src)
        if style_opts:
            for k, v in style_opts.items():
                html_tag_args += '{}="{}" '.format(k, v)
        self.html_content = html_tag_args
        return self

    def set_global_opts(self, title_opts: Union[ComponentTitleOpts, dict, None] = None):
        self.title_opts = title_opts
        return self

    def render(
        self,
        path: str = "render.html",
        template_name: str = "components.html",
        env: Optional[Environment] = None,
        **kwargs,
    ) -> str:
        return engine.render(self, path, template_name, env, **kwargs)

    def render_embed(
        self,
        template_name: str = "components.html",
        env: Optional[Environment] = None,
        **kwargs,
    ) -> str:
        return engine.render_embed(self, template_name, env, **kwargs)

    def render_notebook(self):
        # only notebook env need to re-generate chart_id
        self.chart_id = uuid.uuid4().hex
        return engine.render_notebook(self, "nb_components.html", "nb_components.html")
