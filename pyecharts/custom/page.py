#!/usr/bin/env python
# coding=utf-8

from pyecharts import template


class Page(object):

    def __init__(self):
        self.__charts = []

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
