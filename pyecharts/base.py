# coding=utf-8
import copy
import os
import uuid
import warnings
from tempfile import mkstemp

from jinja2 import Markup

import pyecharts.constants as constants
import pyecharts.engine as engine
import pyecharts.exceptions as exceptions
import pyecharts.utils as utils
from pyecharts.app import get_default_config
from pyecharts.echarts.option import get_other_options
from pyecharts.interfaces import IPythonRichDisplayMixin
from pyecharts.shortcuts import cast, dumps_json


class Base(IPythonRichDisplayMixin):
    """
    `Base`类是所有图形类的基类，提供部分初始化参数和基本的方法
    """

    def __init__(
        self,
        width='800px',
        height='400px',
        renderer=constants.CANVAS_RENDERER,
        page_title=constants.PAGE_TITLE,
        extra_html_text_label=None,
        is_animation=True,
    ):
        """

        :param width:
            画布宽度，默认为 '800px'
        :param height:
            画布高度，默认为 '400px'
        :param renderer:
            指定使用渲染方式，有 'svg' 和 'canvas' 可选，默认为 'canvas'。
            3D 图仅能使用 'canvas'。
        :param page_title:
            指定生成的 html 文件中 <title> 标签的值。默认为 'Echarts'
        :param extra_html_text_label:
            额外的 HTML 文本标签，(<p> 标签)。类型为 list，list[0] 为文本内容，
            list[1] 为字体风格样式（选填）。如 ["this is a p label", "color:red"]
        :param is_animation:
            是否开启动画，默认为 True。V0.5.9+
        """
        self._chart_id = uuid.uuid4().hex
        self._width = utils.to_css_length(width)
        self._height = utils.to_css_length(height)
        self._page_title = page_title
        self.extra_html_text_label = extra_html_text_label

        self._option = {}
        self._js_dependencies = set()
        self.renderer = renderer
        self._js_dependencies = {"echarts"}
        self.event_handlers = {}
        self.theme = None
        self.use_theme(get_default_config().theme)
        self.is_animation = is_animation

    # ----- Properties for html element -----

    @property
    def chart_id(self):
        return self._chart_id

    @chart_id.setter
    def chart_id(self, chart_id):
        self._chart_id = chart_id

    @property
    def width(self):
        return self._width

    @width.setter
    def width(self, width):
        self._width = utils.to_css_length(width)

    @property
    def height(self):
        return self._height

    @height.setter
    def height(self, height):
        self._height = utils.to_css_length(height)

    @property
    def page_title(self):
        return self._page_title

    @property
    def options(self):
        return self.get_options()

    @property
    def js_dependencies(self):
        return utils.merge_js_dependencies(self._js_dependencies)

    def _get_all_options(self, **kwargs):
        return get_other_options(**kwargs)

    def get_options(self, remove_none=True):
        if remove_none:
            return utils.remove_key_with_none_value(self._option)
        else:
            return copy.deepcopy(self._option)

    def use_theme(self, theme_name):
        self.theme = theme_name
        if theme_name not in constants.BUILTIN_THEMES:
            self._js_dependencies.add(self.theme)
        return self

    def _add_chinese_map(self, map_name_in_chinese):
        # TODO Lazy Resolve ?
        current_config = get_default_config()
        name_in_pinyin = current_config.chinese_to_pinyin(map_name_in_chinese)
        self._js_dependencies.add(name_in_pinyin)

    def on(self, event_name, handler):
        self.event_handlers[event_name] = handler
        return self

    def print_echarts_options(self):
        """
        打印输出图形所有配置项
        """
        print(dumps_json(self.options))

    def render_embed(self):
        """
        渲染图表的所有配置项，为 web pages 服务，不过需先提供所需要的js 依赖文件
        """
        env = engine.create_default_environment(constants.DEFAULT_HTML)
        html = env.render_container_and_echarts_code(self)
        return Markup(html)

    def get_js_dependencies(self):
        """
        声明所有的 js 文件路径
        """
        current_config = get_default_config()
        return current_config.produce_html_script_list(self._js_dependencies)

    # ----- Render API -----

    def render(
        self,
        path="render.html",
        template_name="simple_chart.html",
        object_name="chart",
        **kwargs
    ):
        _, ext = os.path.splitext(path)
        _file_type = ext[1:]
        env = engine.create_default_environment(_file_type)
        env.render_chart_to_file(
            chart=self,
            object_name=object_name,
            path=path,
            template_name=template_name,
            **kwargs
        )

    def _repr_html_(self):
        """
        渲染配置项并将图形显示在 notebook 中

        chart/page => charts
        chart.js_dependencies => require_config => config_items, libraries
        :return A unicode string.
        """
        env = engine.create_default_environment(constants.DEFAULT_HTML)
        current_config = env.pyecharts_config
        if current_config.is_run_on_nteract:
            return env.render_chart_to_notebook(
                chart=self, template_name="nteract.html"
            )
        elif current_config.jupyter_presentation == constants.DEFAULT_HTML:
            require_config = current_config.produce_require_configuration(
                self.js_dependencies
            )
            config_items = require_config["config_items"]
            libraries = require_config["libraries"]
            return env.render_chart_to_notebook(
                charts=(self,), config_items=config_items, libraries=libraries
            )
        else:
            return None

    def _repr_svg_(self):
        content = self._render_as_image(constants.SVG)
        if content:
            # fix alignment problem in notebook
            content = content.replace("position: absolute;", "")
        return content

    def _repr_png_(self):
        return self._render_as_image(constants.PNG)

    def _repr_jpeg_(self):
        return self._render_as_image(constants.JPEG)

    def _render_as_image(self, file_type):
        """
        This is an internal function to serve _repr_jpeg_,
        _repr_png_ and _repr_svg_.

        :param file_type: the parameter is mostly image file types.
        """
        env = engine.create_default_environment(file_type)
        current_config = env.pyecharts_config
        if current_config.jupyter_presentation != file_type:
            return None

        if self.renderer == constants.SVG_RENDERER:
            if file_type != constants.SVG:
                raise exceptions.InvalidConfiguration(
                    "svg renderer produces only svg image."
                )

        elif file_type not in [constants.JPEG, constants.PNG]:
            # CANVAS_RENDERER here
            raise exceptions.InvalidConfiguration(
                "svg output requires svg renderer."
            )
        tmp_file_handle, tmp_file_path = mkstemp(suffix="." + file_type)
        # SnapshotEnvironment.render_chart_to_file returns file binary data.
        content = env.render_chart_to_file(
            chart=self, path=tmp_file_path, verbose=False
        )
        os.close(tmp_file_handle)
        return content

    # ----- Deprecated API -----

    def show_config(self):
        """
        打印输出图形所有配置项
        """
        deprecated_tpl = "The {} is deprecated, please use {} instead!"
        warnings.warn(
            deprecated_tpl.format("show_config", "print_echarts_options"),
            DeprecationWarning,
        )
        self.print_echarts_options()

    def render_notebook(self):
        warnings.warn(
            "Implementation has been removed. "
            + "Please pass the chart instance directly to Jupyter."
            + "If you need more help, please read documentation"
        )

    @staticmethod
    def cast(seq):
        warnings.warn(
            "This method is deprecated. Use shortcuts.cast instead.",
            DeprecationWarning,
        )
        return cast(seq)
