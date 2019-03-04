# coding=utf-8

import os
import uuid
from tempfile import mkstemp
from typing import Union

from pyecharts import engine, exceptions, utils, consts
from pyecharts.javascripthon.api import EChartsTranslator

from .structures import OrderedSet


class Base:
    """
    `Base`类是所有图形类的基类，提供部分初始化参数和基本的方法
    """

    def __init__(
        self,
        width: str = "800px",
        height: str = "400px",
        renderer: str = consts.RENDER_TYPE.CANVAS,
        page_title: str = consts.PAGE_TITLE,
        theme="white",
    ):
        """
        :param width:
            画布宽度，默认为 800（px）
        :param height:
            画布高度，默认为 400（px）
        :param renderer:
            指定使用渲染方式，有 'svg' 和 'canvas' 可选，默认为 'canvas'。
            3D 图仅能使用 'canvas'。
        :param page_title:
            指定生成的 html 文件中 <title> 标签的值。默认为 'Echarts'
        """
        self.width = width
        self.height = height

        self.chart_id = uuid.uuid4().hex
        self.renderer = renderer
        self.page_title = page_title
        self.theme = theme

        self.options: dict = {}
        self.jshost: str = ""
        self.js_dependencies: OrderedSet = OrderedSet("echarts.min.js")

    def get_options(self) -> dict:
        return utils.remove_key_with_none_value(self.options)

    def dump_options(self) -> str:
        return EChartsTranslator.dumps(self.options)

    # TODO: finally validate
    def use_theme(self, theme_name: str):
        if theme_name not in consts.BUILTIN_THEMES:
            self.js_dependencies.add(theme_name)
        return self

    # def get_js_dependencies(self):
    #     return CURRENT_CONFIG.produce_html_script_list(self.js_dependencies)

    def render(self, path="render.html", template_name="simple_chart.html"):
        eg = engine.RenderEngine()
        self.options = self.dump_options()
        eg.render_chart_to_file(chart=self, path=path, template_name=template_name)

    # def _repr_html_(self):

    # """
    # 渲染配置项并将图形显示在 notebook 中
    #
    # chart/page => charts
    # chart.js_dependencies => require_config => config_items, libraries
    # :return A unicode string.
    # """
    # if True:
    # if CURRENT_CONFIG.jupyter_presentation == consts.DEFAULT_HTML:
    #     require_config = CURRENT_CONFIG.produce_require_configuration(
    #         self.js_dependencies
    #     )
    #     config_items = require_config["config_items"]
    #     libraries = require_config["libraries"]
    #     env = engine.create_default_environment(consts.DEFAULT_HTML)
    #     return env.render_chart_to_notebook(
    #         charts=(self,), config_items=config_items, libraries=libraries
    #     )

    # elif CURRENT_CONFIG.jupyter_presentation == consts.NTERACT:
    #     env = engine.create_default_environment(consts.DEFAULT_HTML)
    #     return env.render_chart_to_notebook(
    #         chart=self, template_name="nteract.html"
    #     )

    # else:
    #     return None

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
