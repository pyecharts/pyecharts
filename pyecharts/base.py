# coding=utf-8

import uuid
import json
import datetime

import pyecharts.utils as utils
import pyecharts.template as template
import pyecharts.constants as constants
from pyecharts.engine import DEFAULT_CONFIG


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
        self._jshost = jshost if jshost else constants.CONFIGURATION['HOST']
        self._js_dependencies = {'echarts'}

    @property
    def chart_id(self):
        """ 设置 chart_id 属性为可读
        """
        return self._chart_id

    @property
    def options(self):
        """ 设置 options 属性为可读
        """
        return self._option

    @property
    def js_dependencies(self):
        """ 依赖的 js 文件列表
        """
        return self._js_dependencies

    def show_config(self):
        """ 打印输出图形所有配置项
        """
        print(utils.json_dumps(self._option, indent=4))

    def render_embed(self):
        """ 渲染图表的所有配置项，为 web pages 服务，不过需先提供
        所需要的js 依赖文件
        """
        embed = 'chart_component.html'
        tmp = template.JINJA2_ENV.get_template(embed)
        my_option = utils.json_dumps(self._option, indent=4)
        html = tmp.render(my_option=my_option,
                          chart_id=self._chart_id,
                          my_width=self.width,
                          my_height=self.height)
        return html

    def get_js_dependencies(self):
        """ 声明所有的 js 文件路径
        """
        return template.produce_html_script_list(self._js_dependencies)

    def render(self,
               path='render.html',
               new_version=False,
               template_name='simple_chart.html',
               object_name='chart',
               extra_context=None
               ):
        if new_version:
            tpl = template.JINJA2_ENV.get_template(template_name, parent=DEFAULT_CONFIG.echarts_template_dir)
            context = {
                object_name: self
            }
            extra_context = extra_context or {}
            context.update(extra_context)
            html = tpl.render(**context)
            utils.write_utf8_html_file(path, html)
        else:
            self._render(path=path)

    def _render(self, path="render.html"):
        """ 渲染配置项并生成 html 文件

        :param path:
            文件保存路径
        """
        _tmp = "local.html"
        my_option = utils.json_dumps(self._option, indent=4)
        tmp = template.JINJA2_ENV.get_template(_tmp)
        script_list = template.produce_html_script_list(self._js_dependencies)
        html = tmp.render(
            my_option=my_option,
            chart_id=self._chart_id,
            script_list=script_list,
            page_title=self._page_title,
            my_width=self.width,
            my_height=self.height)
        html = utils.freeze_js(html)
        utils.write_utf8_html_file(path, html)

    @staticmethod
    def cast(seq):
        """ 转换数据序列，将带字典和元组类型的序列转换为 k_lst,v_lst 两个列表

        元组列表
            [(A1, B1), (A2, B2), ...] --> k_lst[ A[i1, i2...] ], v_lst[ B[i1, i2...] ]
        字典列表
            [{A1: B1}, {A2: B2}, ...] --> k_lst[ A[i1, i2...] ], v_lst[ B[i1, i2...] ]
        字典
            {A1: B1, A2: B2, ...} -- > k_lst[ A[i1, i2...] ], v_lst[ B[i1, i2...] ]

        :param seq:
            待转换的序列
        :return:
        """
        k_lst, v_lst = [], []
        if isinstance(seq, list):
            for s in seq:
                try:
                    if isinstance(s, tuple):
                        _attr, _value = s
                        k_lst.append(_attr)
                        v_lst.append(_value)
                    elif isinstance(s, dict):
                        for k, v in s.items():
                            k_lst.append(k)
                            v_lst.append(v)
                except:
                    raise
        elif isinstance(seq, dict):
            for k, v in seq.items():
                k_lst.append(k)
                v_lst.append(v)
        return k_lst, v_lst

    def _repr_html_(self):
        """ 渲染配置项并将图形显示在 notebook 中
        """
        _tmp = 'notebook.html'
        dom = self._render_notebook_dom_()
        component = self._render_notebook_component_()
        tmp = template.JINJA2_ENV.get_template(_tmp)
        require_config = template.produce_require_configuration(
            self._js_dependencies, self._jshost)
        html = tmp.render(
            single_chart=component, dom=dom, **require_config)
        return html

    def _render_notebook_dom_(self):
        """ 为 notebook 渲染 dom 模板
        """
        _tmp = "notebook_dom.html"
        tmp = template.JINJA2_ENV.get_template(_tmp)
        component = tmp.render(
            chart_id=self._chart_id,
            chart_width=self.width,
            chart_height=self.height)
        return component

    def _render_notebook_component_(self):
        """ 为 notebook 渲染组件模板
        """
        _tmp = "notebook_chart_component.html"
        my_option = utils.json_dumps(self._option, indent=4)
        tmp = template.JINJA2_ENV.get_template(_tmp)
        component = tmp.render(
            my_option=my_option, chart_id=self._chart_id)
        return component
