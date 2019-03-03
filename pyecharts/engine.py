# coding=utf-8

import codecs
import os
from typing import Optional, Any

from jinja2 import Environment, FileSystemLoader


def write_utf8_html_file(file_name: str, html_content: str):
    with codecs.open(file_name, "w+", encoding="utf-8") as html_file:
        html_file.write(html_content)


GLOBAL_ENV = Environment(
    keep_trailing_newline=True,
    trim_blocks=True,
    lstrip_blocks=True,
    loader=FileSystemLoader("../templates"),
)

GLOBAL_ONLINE_HOST = "https://pyecharts.github.io/assets/js/"


class RenderEngine:
    def __init__(self, env: Optional[Environment] = None):
        self.env = env or GLOBAL_ENV

    @staticmethod
    def generate_js_link(chart: Any) -> Any:
        if not chart.jshost:
            chart.jshost = GLOBAL_ONLINE_HOST
        links = []
        for dep in chart.js_dependencies.items:
            # TODO: if?
            links.append(chart.jshost + dep)
        chart.dependencies = links
        return chart

    @staticmethod
    def gen_notebook_cfg(chart: Any) -> dict:
        items = []
        for dep in chart.js_dependencies.items:
            # TODO: if?
            items.append(dep)
        require_libraries = ["'{}'".format(dep) for dep in chart.js_dependencies.items]
        return dict(config_items=items, libraries=require_libraries)

    def render_chart_to_file(self, chart: Any, path: str, template_name: str):
        """
        Render a chart or page to local html files.

        :param chart: A Chart or Page object
        :param path: The destination file which the html code write to
        :param template_name: The name of template file.
        """
        tpl = self.env.get_template(template_name)
        html = tpl.render(chart=self.generate_js_link(chart))
        write_utf8_html_file(path, html)

    def render_chart_to_notebook(
        self, template_name: str = "notebook.html", **ctx: dict
    ) -> str:
        """
        Return html string for rendering a chart/page to a notebook cell.

        :param template_name: file name of template.
        :param ctx: A dictionary containing data.
        """
        tpl = self.env.get_template(template_name)
        return tpl.render(**ctx)
