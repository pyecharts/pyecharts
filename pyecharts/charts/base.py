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
        self._chart_type = ""

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

    # TODO: necessary?
    # def _repr_svg_(self):
    #     content = self._render_as_image(consts.SVG)
    #     if content:
    #         # fix alignment problem in notebook
    #         content = content.replace("position: absolute;", "")
    #     return content
    #
    # def _repr_png_(self):
    #     return self._render_as_image(consts.PNG)
    #
    # def _repr_jpeg_(self):
    #     return self._render_as_image(consts.JPEG)

    # def _render_as_image(self, file_type):
    #     """
    #     This is an internal function to serve _repr_jpeg_, _repr_png_ and _repr_svg_.
    #
    #     :param file_type: the parameter is mostly image file types.
    #     """
    #     if CURRENT_CONFIG.jupyter_presentation != file_type:
    #         return None
    #
    #     if self.renderer == consts.SVG_RENDERER:
    #         if file_type != consts.SVG:
    #             raise exceptions.InvalidConfiguration(
    #                 "svg renderer produces only svg image."
    #             )
    #
    #     elif file_type not in [consts.JPEG, consts.PNG]:
    #         # CANVAS_RENDERER here
    #         raise exceptions.InvalidConfiguration("svg output requires svg renderer.")
    #
    #     env = engine.create_default_environment(file_type)
    #     tmp_file_handle, tmp_file_path = mkstemp(suffix="." + file_type)
    #     content = env.render_chart_to_file(
    #         chart=self, path=tmp_file_path, verbose=False
    #     )
    #     os.close(tmp_file_handle)
    #     return content
