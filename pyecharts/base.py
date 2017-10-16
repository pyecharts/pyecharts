# coding=utf-8

import uuid
import json
import datetime

import pyecharts.constants as constants
from pyecharts import template
from pyecharts import utils


class Base(object):
    def __init__(self,
                 width=800,
                 height=400,
                 title_pos="auto",
                 title_top="auto",
                 title_color="#000",
                 subtitle_color="#aaa",
                 title_text_size=18,
                 subtitle_text_size=12,
                 background_color="#fff",
                 page_title=constants.PAGE_TITLE,
                 jshost=None):
        self._option = {}
        self._js_dependencies = set()
        self._chart_id = uuid.uuid4().hex
        self._width, self._height = width, height
        self._page_title = page_title
        self._jshost = jshost if jshost else constants.CONFIGURATION['HOST']
        self._js_dependencies = {'echarts'}

    @property
    def options(self):
        """

        :return:
        """
        return self._option

    def show_config(self):
        """ Print all options of charts"""
        print(json_dumps(self._option, indent=4))

    def render_embed(self):
        """
        Render the chart component and its options

        You can include it into your web pages. And you will
        provide all dependent echarts javascript libraries.
        """
        embed = 'chart_component.html'
        tmp = template.JINJA2_ENV.get_template(embed)
        my_option = json_dumps(self._option, indent=4)
        html = tmp.render(myOption=my_option,
                          chart_id=self._chart_id,
                          myWidth=self._width, myHeight=self._height)
        return html

    def get_js_dependencies(self):
        """
        Declare its javascript dependencies for embedding purpose
        """
        return template.produce_html_script_list(self._js_dependencies)

    def render(self, path="render.html"):
        """ Render the options dict, generate the html file

        :param path:
            path of render html file
        """
        _tmp = "local.html"
        my_option = json_dumps(self._option, indent=4)
        tmp = template.JINJA2_ENV.get_template(_tmp)
        script_list = template.produce_html_script_list(self._js_dependencies)
        html = tmp.render(
            myOption=my_option,
            chart_id=self._chart_id,
            script_list=script_list,
            page_title=self._page_title,
            myWidth=self._width, myHeight=self._height)
        html = utils.freeze_js(html)
        utils.write_utf8_html_file(path, html)

    @staticmethod
    def cast(seq):
        """ Convert the sequence with the dictionary and tuple type into k_lst, v_lst.
        1.[(A1, B1),(A2, B2),(A3, B3),(A4, B4)] --> k_lst[A[i1,i2...]], v_lst[B[i1,i2...]]
        2.[{A1: B1},{A2: B2},{A3: B3},{A4: B4}] --> k_lst[A[i1,i2...]], v_lst[B[i1,i2...]]
        3.{A1: B1, A2: B2, A3: B3, A4: B4} -- > k_lst[A[i1,i2...]], v_lst[B[i1,i2...]]

        :param seq:
            data sequence
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
        """ Render the options dict, displayed in the jupyter notebook

        :return:
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
        """

        :return:
        """
        _tmp = "notebook_dom.html"
        tmp = template.JINJA2_ENV.get_template(_tmp)
        component = tmp.render(
            chart_id=self._chart_id,
            chart_width=self._width,
            chart_height=self._height)
        return component

    def _render_notebook_component_(self):
        """

        :return:
        """
        _tmp = "notebook_chart_component.html"
        my_option = json_dumps(self._option, indent=4)
        tmp = template.JINJA2_ENV.get_template(_tmp)
        component = tmp.render(
            my_option=my_option, chart_id=self._chart_id)
        return component


class UnknownTypeEncoder(json.JSONEncoder):
    def default(self, obj):
        if isinstance(obj, (datetime.datetime, datetime.date)):
            return obj.isoformat()
        else:
            # Pandas and Numpy lists
            try:
                return obj.astype(float).tolist()
            except:
                try:
                    return obj.astype(str).tolist()
                except:
                    return json.JSONEncoder.default(self, obj)


def json_dumps(data, indent=0):
    """

    :param data:
    :param indent:
    :return:
    """
    return json.dumps(data, indent=indent,
                      cls=UnknownTypeEncoder)
