#!/usr/bin/env python
# coding=utf-8

from pyecharts import template
from pyecharts.constants import DEFAULT_JS_LIBRARIES, DEFAULT_HOST


class Page(object):

    def __init__(self):
        self.__charts = []
        self._jshost = DEFAULT_HOST

    def add(self, achart_or_charts):
        """
        Append chart(s) to the rendering page

        :param achart_or_charts:
        :return:
        """
        if isinstance(achart_or_charts, list):
            self.__charts.extend(achart_or_charts)
        else:
            self.__charts.append(achart_or_charts)

    def render(self, path="render.html"):
        """
        Produce rendered charts in a html file

        :param path:
        :return:
        """
        template_name = "multicharts.html"
        chart_content = self.render_embed()
        tmp = template.JINJA2_ENV.get_template(template_name)
        html = tmp.render(multi_chart_content=chart_content)
        html = template.freeze_js(html)
        template.write_utf8_html_file(path, html)

    def render_embed(self):
        """
        Produce rendered charts in html for embedding purpose

        :return:
        """
        chart_content = ""
        for chart in self.__charts:
            chart_content += chart.render_embed()
        return chart_content

    def _repr_html_(self):
        _tmp = "notebook.html"
        doms = ""
        components = ""
        dependencies = set()
        for chart in self.__charts:
            doms += chart._render_notebook_dom_()
            components += chart._render_notebook_component_()
            dependencies = dependencies.union(set(chart._js_dependencies))
        require_conf_items = [
            "%s: '%s/%s'" % (key, self._jshost, DEFAULT_JS_LIBRARIES.get(key, key))
            for key in dependencies]
        require_libraries = ["'%s'" % key for key in dependencies]
        tmp = template.JINJA2_ENV.get_template(_tmp)
        html = tmp.render(
            single_chart=components, dom=doms,
            config_items=require_conf_items, libraries=require_libraries)
        return html
