# coding=utf-8

import uuid
import warnings

from jinja2 import Markup

import pyecharts.constants as constants
import pyecharts.engine as engine
import pyecharts.utils as utils
from pyecharts.conf import CURRENT_CONFIG


class Base(object):
    """
    `Base`类是所有图形类的基类，提供部分初始化参数和基本的方法
    """

    def __init__(self,
                 width=800,
                 height=400,
                 renderer=constants.CANVAS_RENDERER,
                 page_title=constants.PAGE_TITLE):
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
        self._option = {}
        self._js_dependencies = set()
        self._chart_id = uuid.uuid4().hex
        self.width, self.height = width, height
        self.renderer = renderer
        self._page_title = page_title
        self._js_dependencies = {'echarts'}

    @property
    def chart_id(self):
        return self._chart_id

    @chart_id.setter
    def chart_id(self, chart_id):
        self._chart_id = chart_id

    @property
    def options(self):
        return self._option

    @property
    def js_dependencies(self):
        return utils.merge_js_dependencies(self._js_dependencies)

    @property
    def page_title(self):
        return self._page_title

    def print_echarts_options(self):
        """ 打印输出图形所有配置项
        """
        print(utils.json_dumps(self._option, indent=4))

    def show_config(self):
        """ 打印输出图形所有配置项
        """
        deprecated_tpl = 'The {} is deprecated, please use {} instead!'
        warnings.warn(
            deprecated_tpl.format('show_config', 'print_echarts_options'),
            DeprecationWarning
        )
        self.print_echarts_options()

    def render_embed(self):
        """ 渲染图表的所有配置项，为 web pages 服务，不过需先提供
        所需要的js 依赖文件
        """
        env = engine.create_default_environment()
        html = env.render_container_and_echarts_code(self)
        return Markup(html)

    def get_js_dependencies(self):
        """ 声明所有的 js 文件路径
        """
        return CURRENT_CONFIG.produce_html_script_list(self._js_dependencies)

    def render(self,
               path='render.html',
               template_name='simple_chart.html',
               object_name='chart',
               extra_context=None):
        env = engine.create_default_environment()
        env.render_chart_to_file(
            chart=self,
            object_name=object_name,
            path=path,
            template_name=template_name,
            extra_context=extra_context
        )

    @staticmethod
    def cast(seq):
        """ 转换数据序列，将带字典和元组类型的序列转换为 k_lst,v_lst 两个列表

        元组列表
            [(A1, B1), (A2, B2), ...] -->
                k_lst[ A[i1, i2...] ], v_lst[ B[i1, i2...] ]
        字典列表
            [{A1: B1}, {A2: B2}, ...] -->
                k_lst[ A[i1, i2...] ], v_lst[ B[i1, i2...] ]
        字典
            {A1: B1, A2: B2, ...} -- >
                k_lst[ A[i1, i2...] ], v_lst[ B[i1, i2...] ]

        :param seq:
            待转换的序列
        :return:
        """
        k_lst, v_lst = [], []
        if isinstance(seq, list):
            for s in seq:
                if isinstance(s, tuple):
                    _attr, _value = s
                    k_lst.append(_attr)
                    v_lst.append(_value)
                elif isinstance(s, dict):
                    for k, v in s.items():
                        k_lst.append(k)
                        v_lst.append(v)
        elif isinstance(seq, dict):
            for key in sorted(list(seq.keys())):
                k_lst.append(key)
                v_lst.append(seq[key])
        return k_lst, v_lst

    def _repr_html_(self):
        """ 渲染配置项并将图形显示在 notebook 中
        chart/page => charts
        chart.js_dependencies => require_config => config_items, libraries
        :return A unicode string.
        """
        require_config = CURRENT_CONFIG.produce_require_configuration(
            self.js_dependencies
        )
        config_items = require_config['config_items']
        libraries = require_config['libraries']
        env = engine.create_default_environment()
        return env.render_chart_to_notebook(
            charts=(self,),
            config_items=config_items,
            libraries=libraries
        )

    def _add_chinese_map(self, map_name_in_chinese):
        name_in_pinyin = CURRENT_CONFIG.chinese_to_pinyin(map_name_in_chinese)
        self._js_dependencies.add(name_in_pinyin)
