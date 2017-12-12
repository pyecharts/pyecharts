# coding=utf-8
from __future__ import unicode_literals

import os

from jinja2 import Environment, FileSystemLoader, environmentfunction, Markup

import pyecharts.utils as utils
import pyecharts.conf as conf


LINK_SCRIPT_FORMATTER = '<script type="text/javascript" src="{}"></script>'
EMBED_SCRIPT_FORMATTER = '<script type="text/javascript">\n{}\n</script>'
CHART_DIV_FORMATTER = '<div id="{chart_id}" style="width:{width};height:{height};"></div>' # flake8: noqa
CHART_CONFIG_FORMATTER = """
var myChart_{chart_id} = echarts.init(document.getElementById('{chart_id}'));
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
    dependencies = current_config.merge_js_dependencies(*args)
    js_names = [current_config.get_js_library(x) for x in dependencies]

    if current_config.js_embed:
        contents = current_config.read_file_contents_from_local(js_names)

        return Markup(
            '\n'.join([EMBED_SCRIPT_FORMATTER.format(c) for c in contents])
        )
    else:
        jshost = current_config.jshost
        js_links = current_config.generate_js_link(jshost, js_names)
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
    dependencies = current_config.merge_js_dependencies(*args)
    js_names = [current_config.get_js_library(x) for x in dependencies]
    contents = current_config.read_file_contents_from_local(js_names)
    return Markup(
        '\n'.join([EMBED_SCRIPT_FORMATTER.format(c) for c in contents])
    )


@environmentfunction
def echarts_container(env, chart):
    """ Render a div html element for a chart.

    :param env:
    :param chart: A pyecharts.base.Base object
    """

    def ex_wh(x):
        """ Extend width/height to all values.

        :param x:
        :return:
        """
        if isinstance(x, (int, float)):
            return '{}px'.format(x)
        else:
            return x

    return Markup(
        CHART_DIV_FORMATTER.format(
            chart_id=chart.chart_id,
            width=ex_wh(chart.width),
            height=ex_wh(chart.height)
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

    def configure_pyecharts(self, **kwargs):
        for k, v in kwargs.items():
            setattr(self.pyecharts_config, k, v)


def render(template_file, **context):
    echarts_env = EchartsEnvironment(
        pyecharts_config=conf.CURRENT_CONFIG,
        loader=FileSystemLoader(
            [conf.CURRENT_CONFIG.echarts_template_dir, conf.DEFAULT_TEMPLATE_DIR])
    )
    template = echarts_env.get_template(template_file)
    return template.render(**context)

