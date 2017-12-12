# coding=utf-8

import uuid

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
                 page_title=constants.PAGE_TITLE,
                 jshost=None):
        """

        :param width:
            画布宽度，默认为 800（px）
        :param height:
            画布高度，默认为 400（px）
        :param page_title:
            指定生成的 html 文件中 <title> 标签的值。默认为'Echarts'
        :param jshost:
            自定义每个实例的 JavaScript host
        """
        self._option = {}
        self._js_dependencies = set()
        self._chart_id = uuid.uuid4().hex
        self.width, self.height = width, height
        self._page_title = page_title
        self._jshost = jshost if jshost else CURRENT_CONFIG.jshost
        self._js_dependencies = {'echarts'}

    @property
    def chart_id(self):
        return self._chart_id

    @property
    def options(self):
        return self._option

    @property
    def js_dependencies(self):
        return self._js_dependencies

    @property
    def page_title(self):
        return self._page_title

    def show_config(self):
        """ 打印输出图形所有配置项
        """
        print(utils.json_dumps(self._option, indent=4))

    def render_embed(self):
        """ 渲染图表的所有配置项，为 web pages 服务，不过需先提供
        所需要的js 依赖文件
        """
        my_option = utils.json_dumps(self._option, indent=4)
        html = engine.render('chart_component.html',
                             my_option=my_option,
                             chart_id=self._chart_id,
                             my_width=self.width,
                             my_height=self.height)
        return html

    def get_js_dependencies(self):
        """ 声明所有的 js 文件路径
        """
        return CURRENT_CONFIG.produce_html_script_list(self._js_dependencies)

    def render(self,
               path='render.html',
               template_name='simple_chart.html',
               object_name='chart',
               extra_context=None):
        context = {object_name: self}
        context.update(extra_context or {})
        html = engine.render(template_name, **context)
        utils.write_utf8_html_file(path, html)

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
        """
        dom = self._render_notebook_dom_()
        component = self._render_notebook_component_()
        require_config = CURRENT_CONFIG.produce_require_configuration(
            self._js_dependencies,
            CURRENT_CONFIG.get_current_jshost_for_jupyter(jshost=self._jshost)
        )
        return engine.render('notebook.html',
                             single_chart=component,
                             dom=dom,
                             **require_config)

    def _render_notebook_dom_(self):
        """ 为 notebook 渲染 dom 模板
        """
        return engine.render("notebook_dom.html",
                             chart_id=self._chart_id,
                             chart_width=self.width,
                             chart_height=self.height)

    def _render_notebook_component_(self):
        """ 为 notebook 渲染组件模板
        """
        my_option = utils.json_dumps(self._option, indent=4)
        return engine.render("notebook_chart_component.html",
                             my_option=my_option,
                             chart_id=self._chart_id)

    def _add_chinese_map(self, map_name_in_chinese):
        name_in_pinyin = CURRENT_CONFIG.chinese_to_pinyin(map_name_in_chinese)
        self._js_dependencies.add(name_in_pinyin)
