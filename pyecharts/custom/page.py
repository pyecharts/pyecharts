# coding=utf-8

import pyecharts.utils as utils
import pyecharts.template as template
import pyecharts.constants as constants


class Page(list):
    """
    A composite object to present multiple charts vertically in a single page
    """

    def __init__(self, jshost=None, page_title=constants.PAGE_TITLE):
        list.__init__([])
        self._page_title = page_title
        self._jshost = jshost if jshost else constants.CONFIGURATION['HOST']

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
        tpl = template.JINJA2_ENV.get_template(template_name)
        context = {
            object_name: self
        }
        extra_context = extra_context or {}
        context.update(extra_context)
        html = tpl.render(**context)
        utils.write_utf8_html_file(path, html)

    def _render(self, path="render.html"):
        """
        Produce rendered charts in a html file

        :param path:
        :return:
        """
        template_name = "multicharts.html"
        chart_content = self.render_embed()
        dependencies = self._merge_dependencies()
        script_list = template.produce_html_script_list(dependencies)
        tmp = template.JINJA2_ENV.get_template(template_name)
        html = tmp.render(multi_chart_content=chart_content,
                          page_title=self._page_title,
                          script_list=script_list)
        html = utils.freeze_js(html)
        utils.write_utf8_html_file(path, html)

    def render_embed(self):
        """
        Produce rendered charts in html for embedding purpose

        :return:
        """
        chart_content = ""
        for chart in self:
            chart_content += chart.render_embed()
            chart_content += '<br>'
        return chart_content

    def get_js_dependencies(self):
        """
        Declare its javascript dependencies for embedding purpose
        """
        unordered_js_dependencies = self._merge_dependencies()
        return template.produce_html_script_list(unordered_js_dependencies)

    def _repr_html_(self):
        """

        :return:
        """
        _tmp = "notebook.html"
        doms = ""
        components = ""
        dependencies = self._merge_dependencies()
        for chart in self:
            doms += chart._render_notebook_dom_()
            components += chart._render_notebook_component_()

        require_config = template.produce_require_configuration(
            dependencies, self._jshost)
        tmp = template.JINJA2_ENV.get_template(_tmp)
        html = tmp.render(
            single_chart=components, dom=doms, **require_config)
        return html

    def _merge_dependencies(self):
        dependencies = set()
        for chart in self:
            dependencies = dependencies.union(chart._js_dependencies)
        # make sure echarts is the item in the list
        # require(['echarts'....], function(ec) {..}) need it to be first
        # but dependencies is a set so has no sequence
        if len(dependencies) > 1:
            dependencies.remove('echarts')
            dependencies = ['echarts'] + list(dependencies)
        return dependencies

    @property
    def js_dependencies(self):
        return self._merge_dependencies()

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
