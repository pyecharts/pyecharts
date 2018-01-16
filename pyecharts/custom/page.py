# coding=utf-8

import pyecharts.utils as utils
import pyecharts.engine as engine
from pyecharts.conf import CURRENT_CONFIG
import pyecharts.constants as constants


class Page(list):
    """
    A composite object to present multiple charts vertically in a single page
    """

    def __init__(self, page_title=constants.PAGE_TITLE):
        list.__init__([])
        self._page_title = page_title

    def add(self, achart_or_charts):
        """
        Append chart(s) to the rendering page

        :param achart_or_charts:
        :return:
        """
        if isinstance(achart_or_charts, list):
            self.extend(achart_or_charts)
        else:
            self.append(achart_or_charts)

    def render(self,
               path='render.html',
               template_name='simple_page.html',
               object_name='page',
               extra_context=None):
        context = {object_name: self}
        context.update(extra_context or {})
        html = engine.render(template_name, **context)
        utils.write_utf8_html_file(path, html)

    def render_embed(self):
        """
        Produce rendered charts in html for embedding purpose

        :return:
        """
        return '<br/> '.join([chart.render_embed() for chart in self])

    def get_js_dependencies(self):
        """
        Declare its javascript dependencies for embedding purpose
        """
        return CURRENT_CONFIG.produce_html_script_list(
            self.js_dependencies)

    def _repr_html_(self):
        """

        :return:
        """
        doms = components = ""
        dependencies = self.js_dependencies
        for chart in self:
            doms += chart._render_notebook_dom_()
            components += chart._render_notebook_component_()

        require_config = CURRENT_CONFIG.produce_require_configuration(
            dependencies)
        return engine.render_notebook(
            "notebook.html",
            single_chart=components,
            dom=doms,
            **require_config)

    @property
    def js_dependencies(self):
        # Treat self as a list,not a page
        return utils.merge_js_dependencies(*self)

    @property
    def page_title(self):
        return self._page_title

    @classmethod
    def from_charts(cls, *args):
        """
        A shortcut class method for building page object from charts.
        :param args:
        :return:
        """
        p = cls()
        p.extend(args)
        return p
