import os

from jinja2 import Environment

from ..commons.utils import OrderedSet
from ..globals import CurrentConfig
from ..options import ComponentTitleOpts
from ..render.display import HTML
from ..render.engine import RenderEngine
from ..types import Optional, Union


class Image:
    def __init__(self, page_title: str = CurrentConfig.PAGE_TITLE, js_host: str = ""):
        self.page_title = page_title
        self.js_host = js_host or CurrentConfig.ONLINE_HOST
        self.js_dependencies: OrderedSet = OrderedSet()
        self.title_opts = ComponentTitleOpts()

    def add(self, src: str, style_opts: Optional[dict] = None):
        html_tag_args = ""
        html_tag_args += 'src="{}" '.format(src)
        if style_opts:
            for k, v in style_opts.items():
                html_tag_args += '{}="{}" '.format(k, v)
        return self

    def set_global_opts(self, title_opts: Union[ComponentTitleOpts, dict, None] = None):
        self.title_opts = title_opts
        return self

    def render(
        self,
        path: str = "render.html",
        template_name: str = "component_image.html",
        env: Optional[Environment] = None,
        **kwargs,
    ) -> str:
        RenderEngine(env).render_chart_to_file(
            chart=self, path=path, template_name=template_name, **kwargs
        )
        return os.path.abspath(path)

    def render_notebook(self):
        return HTML(
            RenderEngine().render_chart_to_notebook("component_image.html", chart=self)
        )
