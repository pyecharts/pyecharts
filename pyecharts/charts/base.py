# coding=utf-8
import json
import os
import uuid

from ..commons import utils
from ..consts import BUILTIN_THEMES, ONLINE_HOST
from ..options import InitOpts
from ..render.engine import RenderEngine


class Base:
    """
    `Base`类是所有图形类的基类，提供部分初始化参数和基本的方法
    """

    def __init__(self, init_opts: InitOpts = InitOpts()):

        self.width = init_opts.width
        self.height = init_opts.height
        self.renderer = init_opts.renderer
        self.page_title = init_opts.page_title
        self.theme = init_opts.theme

        self.chart_id = uuid.uuid4().hex
        self.options: dict = {}
        self.js_host: str = ONLINE_HOST
        self.js_functions: utils.OrderedSet = utils.OrderedSet()
        self.js_dependencies: utils.OrderedSet = utils.OrderedSet("echarts")

    @staticmethod
    def produce_js_func(fn: str) -> str:
        return utils.filter_js_func(fn)

    def add_js_funcs(self, *fns):
        for fn in fns:
            self.js_functions.add(fn)

    def get_options(self) -> dict:
        return utils.remove_key_with_none_value(self.options)

    def dump_options(self) -> str:
        return json.dumps(self.get_options(), indent=4)

    def render(self, path="render.html", template_name="simple_chart.html") -> str:
        self.options = self.dump_options()
        self._use_theme()
        RenderEngine().render_chart_to_file(
            chart=self, path=path, template_name=template_name
        )
        return os.path.abspath(path)

    def _use_theme(self):
        if self.theme not in BUILTIN_THEMES:
            self.js_dependencies.add(self.theme)

    def _repr_html_(self):
        require_config = utils.produce_require_dict(self.js_dependencies, self.js_host)
        self.options = self.dump_options()
        self._use_theme()
        return RenderEngine().render_chart_to_notebook(
            template_name="notebook.html",
            charts=(self,),
            config_items=require_config["config_items"],
            libraries=require_config["libraries"],
        )
