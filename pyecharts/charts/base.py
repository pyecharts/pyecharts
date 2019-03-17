# coding=utf-8

import uuid
import json

from pyecharts.commons import engine, consts, utils
from pyecharts.commons.engine import RenderEngine
from pyecharts.commons.structures import OrderedSet
from pyecharts.commons.consts import ONLINE_HOST
from pyecharts.commons.types import *
from pyecharts.options import InitOpts
from pyecharts.datasets import FILENAMES


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
        self.js_dependencies: OrderedSet = OrderedSet("echarts")

    def get_options(self) -> dict:
        return utils.remove_key_with_none_value(self.options)

    def dump_options(self) -> str:
        return json.dumps(self.get_options(), indent=4)

    def render(self, path="render.html", template_name="simple_chart.html"):
        self.options = self.dump_options()
        RenderEngine().render_chart_to_file(
            chart=self, path=path, template_name=template_name
        )

    # TODO: finally validate
    def __use_theme(self, theme_name: str):
        if theme_name not in consts.BUILTIN_THEMES:
            self.js_dependencies.add(theme_name)
        return self

    def __produce_require_dict(self) -> dict:
        confs, libraries = [], []
        for name in self.js_dependencies.items:
            confs.append("'{}':'{}/{}'".format(name, self.js_host, FILENAMES[name]))
            libraries = ["'{}'".format(name)]
        return dict(config_items=confs, libraries=libraries)

    def _repr_html_(self):
        require_config = self.__produce_require_dict()
        self.options = self.dump_options()
        return engine.RenderEngine().render_chart_to_notebook(
            template_name="notebook.html",
            charts=(self,),
            config_items=require_config["config_items"],
            libraries=require_config["libraries"],
        )

        # elif CURRENT_CONFIG.jupyter_presentation == consts.NTERACT:
        #     env = engine.create_default_environment(consts.DEFAULT_HTML)
        #     return env.render_chart_to_notebook(
        #         chart=self, template_name="nteract.html"
        #     )

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
