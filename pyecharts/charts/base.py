import datetime
import uuid

import simplejson as json
from jinja2 import Environment

from ..commons import utils
from ..globals import CurrentConfig, RenderType, ThemeType
from ..options import InitOpts, RenderOpts
from ..options.series_options import BasicOpts, AnimationOpts
from ..render import engine
from ..types import Optional, Sequence, Union
from .mixins import ChartMixin


class Base(ChartMixin):
    """
    `Base` is the root class for all graphical class, it provides
    part of the initialization parameters and common methods
    """

    def __init__(
        self,
        init_opts: Union[InitOpts, dict] = InitOpts(),
        render_opts: Union[RenderOpts, dict] = RenderOpts(),
    ):
        _opts = init_opts
        if isinstance(init_opts, InitOpts):
            _opts = init_opts.opts

        _render_opts = render_opts
        if isinstance(render_opts, RenderOpts):
            _render_opts = render_opts.opts

        self.width = _opts.get("width", "900px")
        self.height = _opts.get("height", "500px")
        self.horizontal_center = (
            "text-align:center; margin: auto"
            if _opts.get("is_horizontal_center", False)
            else ""
        )
        self.renderer = _opts.get("renderer", RenderType.CANVAS)
        self.page_title = _opts.get("page_title", CurrentConfig.PAGE_TITLE)
        self.theme = _opts.get("theme", ThemeType.WHITE)
        self.chart_id = _opts.get("chart_id") or uuid.uuid4().hex
        self.fill_bg = _opts.get("fill_bg", False)
        self.bg_color = _opts.get("bg_color")

        self.options: dict = {}
        self.render_options: dict = {}
        self.js_host: str = _opts.get("js_host") or CurrentConfig.ONLINE_HOST
        self.js_functions: utils.OrderedSet = utils.OrderedSet()
        self.js_dependencies: utils.OrderedSet = utils.OrderedSet("echarts")
        self.js_events: utils.OrderedSet = utils.OrderedSet()
        self.options.update(backgroundColor=self.bg_color)
        if isinstance(_opts.get("animationOpts", AnimationOpts()), dict):
            self.options.update(_opts.get("animationOpts", AnimationOpts().opts))
        else:
            self.options.update(_opts.get("animationOpts", AnimationOpts()).opts)
        self.options.update(aria=_opts.get("ariaOpts"))

        self._is_geo_chart: bool = False
        self._geo_json_name: Optional[str] = None
        self._geo_json: Optional[dict] = None

        self.render_options.update(embed_js=bool(_render_opts.get("embed_js")))
        self._render_cache: dict = dict()

    def get_chart_id(self) -> str:
        return self.chart_id

    def get_options(self) -> dict:
        return utils.remove_key_with_none_value(self.options)

    def dump_options(self) -> str:
        return utils.replace_placeholder(
            json.dumps(self.get_options(), indent=4, default=default, ignore_nan=True)
        )

    def dump_options_with_quotes(self) -> str:
        return utils.replace_placeholder_with_quotes(
            json.dumps(self.get_options(), indent=4, default=default, ignore_nan=True)
        )

    def render(
        self,
        path: str = "render.html",
        template_name: str = "simple_chart.html",
        env: Optional[Environment] = None,
        **kwargs,
    ) -> str:
        self._prepare_render()
        return engine.render(self, path, template_name, env, **kwargs)

    def render_embed(
        self,
        template_name: str = "simple_chart.html",
        env: Optional[Environment] = None,
        **kwargs,
    ) -> str:
        self._prepare_render()
        return engine.render_embed(self, template_name, env, **kwargs)

    def render_notebook(self):
        self.chart_id = uuid.uuid4().hex
        self._prepare_render()
        return engine.render_notebook(
            self, "nb_jupyter_notebook.html", "nb_jupyter_lab.html"
        )

    def _use_theme(self):
        if self.theme not in ThemeType.BUILTIN_THEMES:
            self.js_dependencies.add(self.theme)

    def _prepare_render(self):
        self.json_contents = self.dump_options()
        self._use_theme()

        self._render_cache.clear()
        if self.render_options.get("embed_js"):
            self._render_cache[
                "javascript"
            ] = self.load_javascript().load_javascript_contents()


def default(o):
    if isinstance(o, (datetime.date, datetime.datetime)):
        return o.isoformat()
    if isinstance(o, utils.JsCode):
        return (
            o.replace("\\n|\\t", "").replace(r"\\n", "\n").replace(r"\\t", "\t").js_code
        )
    if isinstance(o, BasicOpts):
        if isinstance(o.opts, Sequence):
            return [utils.remove_key_with_none_value(item) for item in o.opts]
        else:
            return utils.remove_key_with_none_value(o.opts)
