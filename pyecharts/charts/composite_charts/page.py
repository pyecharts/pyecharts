# coding=utf-8
import os
from collections import OrderedDict

from jinja2 import Markup

from ...commons import consts
from ...render import engine
from ...types import *


class Page:
    """
    <<< 同一网页按顺序展示多图 >>>

    A container object to present multiple charts vertically in a single page
    """

    def __init__(self, page_title="EChart"):
        """
        Create a page instance.
        :param page_title: The title of generated html file.
        :param name_chart_pair: named charts as {<name>:<chart>}
        """
        self.page_title = page_title
        self._charts = OrderedDict()

    def add(self, charts: List = None):
        if not isinstance(achart_or_charts, (list, tuple, set)):
            achart_or_charts = (achart_or_charts,)  # Make it a sequence
        for c in achart_or_charts:
            self.add_chart(chart=c)
        return self

    # List-Like Feature

    def __iter__(self):
        for chart in self._charts.values():
            yield chart

    def __len__(self):
        return len(self._charts)

    # Chart-Like Feature

    def render(
        self,
        path="render.html",
        template_name="simple_page.html",
        object_name="page",
        **kwargs
    ):
        _, ext = os.path.splitext(path)
        _file_type = ext[1:]
        if _file_type != consts.DEFAULT_HTML:
            raise NotImplementedError(
                "Rendering Page instance as image is not supported!"
            )

        env = engine.create_default_environment(consts.DEFAULT_HTML)
        env.render_chart_to_file(
            chart=self,
            object_name=object_name,
            path=path,
            template_name=template_name,
            **kwargs
        )

    def render_embed(self):
        """
        Produce rendered charts in html for embedding purpose
        """
        return Markup("<br/> ".join([chart.render_embed() for chart in self]))

    def get_js_dependencies(self):
        """
        Declare its javascript dependencies for embedding purpose
        """
        return CURRENT_CONFIG.produce_html_script_list(self.js_dependencies)

    def _repr_html_(self):
        """
        :return: html content for jupyter
        """
        dependencies = self.js_dependencies
        require_config = CURRENT_CONFIG.produce_require_configuration(dependencies)
        config_items = require_config["config_items"]
        libraries = require_config["libraries"]
        env = engine.create_default_environment(constants.DEFAULT_HTML)
        return env.render_chart_to_notebook(
            charts=self, config_items=config_items, libraries=libraries
        )
