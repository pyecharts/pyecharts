# coding=utf-8
from __future__ import unicode_literals

from jinja2 import Environment, FileSystemLoader, environmentfunction, Markup

import pyecharts.conf as conf
import pyecharts.utils as utils

LINK_SCRIPT_FORMATTER = '<script type="text/javascript" src="{}"></script>'
EMBED_SCRIPT_FORMATTER = '<script type="text/javascript">\n{}\n</script>'
CHART_DIV_FORMATTER = '<div id="{chart_id}" style="width:{width};height:{height};"></div>'  # flake8: noqa
CHART_CONFIG_FORMATTER = """
var myChart_{chart_id} = echarts.init(document.getElementById('{chart_id}'), null, {{renderer: '{renderer}'}});
var option_{chart_id} = {options};
myChart_{chart_id}.setOption(option_{chart_id});
"""


@environmentfunction
def echarts_js_dependencies(env, *args):
    """ Render script html nodes in external link mode.

    :param env:
    :param args:
    """
    current_config = env.pyecharts_config
    dependencies = utils.merge_js_dependencies(*args)

    if current_config.js_embed:
        contents = current_config.read_file_contents_from_local(dependencies)

        return Markup(
            '\n'.join([EMBED_SCRIPT_FORMATTER.format(c) for c in contents])
        )
    else:
        js_links = current_config.generate_js_link(dependencies)
        return Markup(
            '\n'.join([LINK_SCRIPT_FORMATTER.format(j) for j in js_links])
        )


@environmentfunction
def echarts_js_dependencies_embed(env, *args):
    """ Render script html nodes in embed mode,Only used for local files.

    :param env:
    :param args:
    """
    current_config = env.pyecharts_config
    dependencies = utils.merge_js_dependencies(*args)
    contents = current_config.read_file_contents_from_local(dependencies)
    return Markup(
        '\n'.join([EMBED_SCRIPT_FORMATTER.format(c) for c in contents])
    )


@environmentfunction
def echarts_container(env, chart):
    """ Render a div html element for a chart.

    :param env:
    :param chart: A pyecharts.base.Base object
    """

    return Markup(
        CHART_DIV_FORMATTER.format(
            chart_id=chart.chart_id,
            width=utils.to_css_length(chart.width),
            height=utils.to_css_length(chart.height)
        ))


def generate_js_content(*charts):
    """ Generate the initial code fragment for one or some chart instances.

    :param charts:
    :return:
    """
    contents = []
    for chart in charts:
        js_content = CHART_CONFIG_FORMATTER.format(
            chart_id=chart.chart_id,
            renderer=chart.renderer,
            options=utils.json_dumps(chart.options, indent=4)
        )
        contents.append(js_content)
    contents = '\n'.join(contents)
    return contents


@environmentfunction
def echarts_js_content(env, *charts):
    """ Render script html node for echarts initial code.

    :param env:
    :param chart:
    """
    return Markup(EMBED_SCRIPT_FORMATTER.format(generate_js_content(*charts)))


@environmentfunction
def echarts_js_content_wrap(env, *charts):
    """ Render echarts initial code for a chart.

    :param env:
    :param charts:
    """
    return Markup(generate_js_content(*charts))


# Public API,see document for more detail.

ECHAERTS_TEMPLATE_FUNCTIONS = {
    'echarts_js_dependencies': echarts_js_dependencies,
    'echarts_js_dependencies_embed': echarts_js_dependencies_embed,
    'echarts_container': echarts_container,
    'echarts_js_content': echarts_js_content,
    'echarts_js_content_wrap': echarts_js_content_wrap
}


class BaseEnvironment(Environment):
    """
    Add config and echarts template functions to a Environment object.
    """

    def __init__(self, *args, **kwargs):
        self.pyecharts_config = kwargs.pop('pyecharts_config', None)
        if self.pyecharts_config is None:
            raise TypeError(
                'no pyecharts_config for this environment specified')
        super(BaseEnvironment, self).__init__(*args, **kwargs)
        self.globals.update(ECHAERTS_TEMPLATE_FUNCTIONS)


class EchartsEnvironment(BaseEnvironment):
    """
    Built-in jinja2 template engine for pyecharts
    This class provides some shortcut methods for rendering charts.
    """

    def __init__(self, pyecharts_config=None, *args, **kwargs):
        pyecharts_config = pyecharts_config or conf.PyEchartsConfig()
        loader = kwargs.pop('loader', None)
        if loader is None:
            loader = FileSystemLoader(pyecharts_config.echarts_template_dir)
        super(EchartsEnvironment, self).__init__(
            pyecharts_config=pyecharts_config,
            keep_trailing_newline=True,
            trim_blocks=True,
            lstrip_blocks=True,
            loader=loader,
            *args,
            **kwargs)

    def render_container_and_echarts_code(self, chart):
        """
        Render <div> and <script> code fragment for a chart.
        :param chart:
        :return:
        """
        tpl_string = """
        {{ echarts_container(chart) }}
        {{ echarts_js_content(chart) }}
        """
        tpl = self.from_string(tpl_string)
        return tpl.render(chart=chart)

    def render_chart_to_file(
            self,
            chart,
            object_name='chart',
            path='render.html',
            template_name='simple_chart.html',
            extra_context=None
    ):
        """
        Render a chart or page to local html files.

        :param chart: A Chart or Page object
        :param object_name: Variable name for chart/page used in template
        :param path: The destination file which the html code write to
        :param template_name: The name of template file.
        :param extra_context: A dictionary containing extra data.
        :return: None
        """
        context = {object_name: chart}
        context.update(extra_context or {})
        tpl = self.get_template(template_name)
        html = tpl.render(**context)
        utils.write_utf8_html_file(path, html)

    def render_chart_to_notebook(self, **context):
        """
        Return html string for rendering a chart/page to a notebook cell.

        :param context: A dictionary containing data.
        :return: A unicode string that will be displayed in notebook cell.
        """
        tpl = self.get_template('notebook.html')
        return tpl.render(**context)


def create_default_environment():
    """
    Create environment object with pyecharts default single PyEchartsConfig.

    :return: A new EchartsEnvironment object.
    """
    config = conf.CURRENT_CONFIG
    echarts_env = EchartsEnvironment(
        pyecharts_config=config,
        loader=FileSystemLoader(
            [config.echarts_template_dir, conf.DEFAULT_TEMPLATE_DIR])
    )
    return echarts_env
