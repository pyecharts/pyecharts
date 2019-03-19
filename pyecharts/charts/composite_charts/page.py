# coding=utf-8
import os
from collections import OrderedDict

from jinja2 import Markup

from ...commons import consts
from ...render.engine import RenderEngine
from ...commons.structures import OrderedSet
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
        self._charts = OrderedSet()
        self.js_dependencies = OrderedSet()

    def add(self, *charts):
        for c in charts:
            self._charts.add(c)
            for d in c.js_depencencies.items:
                self.js_dependencies.add(d)
        return self

    # List-Like Feature
    def __iter__(self):
        for chart in self._charts.items:
            yield chart

    def __len__(self):
        return len(self._charts.items)

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

    # def _repr_html_(self):
    #     """
    #     :return: html content for jupyter
    #     """
    #     dependencies = self.js_dependencies
    #     require_config = CURRENT_CONFIG.produce_require_configuration(dependencies)
    #     config_items = require_config["config_items"]
    #     libraries = require_config["libraries"]
    #     env = engine.create_default_environment(constants.DEFAULT_HTML)
    #     return env.render_chart_to_notebook(
    #         charts=self, config_items=config_items, libraries=libraries
    #     )

    def _repr_html_(self):
        require_config = self.__produce_require_dict()
        self.options = self.dump_options()
        return RenderEngine().render_chart_to_notebook(
            template_name="notebook.html",
            charts=self,
            config_items=require_config["config_items"],
            libraries=require_config["libraries"],
        )
