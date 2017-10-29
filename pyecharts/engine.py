#!/usr/bin/env python
# coding=utf-8
from __future__ import unicode_literals

from jinja2 import Environment, FileSystemLoader, contextfunction,environmentfunction
from pyecharts.utils import get_resource_dir, json_dumps
from pyecharts import constants


@environmentfunction
def echarts_js_dependencies(env, *args):
    """
    Render script html nodes in external link mode.
    :param env:
    :param args:
    :return:
    """
    dependencies = []
    for a in args:
        if hasattr(a, 'js_dependencies'):
            dependencies.extend(a.js_dependencies)
        else:
            dependencies.append(a)

    jshost = constants.CONFIGURATION['HOST']
    js_links = ['{}/{}.js'.format(jshost, x) for x in dependencies]
    return '\n'.join(['<script type="text/javascript" src="{}"></script>'.format(j) for j in js_links])


@environmentfunction
def echarts_js_dependencies_embed(env, *args):
    """
    Render script html nodes in embed mode,Only used for local files.
    :param env:
    :param args:
    :return:
    """
    dependencies = []
    for a in args:
        if hasattr(a, 'js_dependencies'):
            dependencies.extend(a.js_dependencies)
        else:
            dependencies.append(a)

    local_host = get_resource_dir('templates\\js\\echarts')  # Now only local host
    js_links = ['{}/{}.js'.format(local_host, x) for x in dependencies]
    js_file_contents = []
    for path in js_links:
        with open(path, 'rb') as f:
            c = f.read()
            js_file_contents.append(c.decode('utf8'))
    return '\n'.join(['<script type="text/javascript">\n{}\n</script>'.format(c) for c in js_file_contents])


@environmentfunction
def echarts_container(env, chart):
    """
    Render a div html element for a chart.
    :param env:
    :param chart: A pyecharts.base.Base object
    :return:
    """

    def ex_wh(x):
        """
        Extend width/height to all values.See http://www.w3school.com.cn/cssref/pr_dim_width.asp
        :param x:
        :return:
        """
        if isinstance(x, (int, float)):
            return '{}px'.format(x)
        else:
            return x

    return '<div id="{chart_id}" style="width:{width};height:{height};"></div>'.format(
        chart_id=chart.chart_id,
        width=ex_wh(chart.width),
        height=ex_wh(chart.height)
    )


@environmentfunction
def echarts_js_content(env, chart):
    """
    Render script html node for echarts initial code.
    :param env:
    :param chart:
    :return:
    """
    content_fmt = '''
    var myChart_{chart_id} = echarts.init(document.getElementById('{chart_id}'));
    var option_{chart_id} = {options};
    myChart_{chart_id}.setOption(option_{chart_id});
    '''
    js_content = content_fmt.format(
        chart_id=chart.chart_id,
        options=json_dumps(chart.options, indent=4)
    )
    return '<script type="text/javascript">\n{}\n</script>'.format(js_content)


@environmentfunction
def echarts_js_content_wrap(env, chart):
    """
    Render echarts initial code for a chart.
    :param env:
    :param chart:
    :return:
    """
    content_fmt = '''
    var myChart_{chart_id} = echarts.init(document.getElementById('{chart_id}'));
    var option_{chart_id} = {options};
    myChart_{chart_id}.setOption(option_{chart_id});
    '''
    js_content = content_fmt.format(
        chart_id=chart.chart_id,
        options=json_dumps(chart.options, indent=4)
    )
    return js_content


class EchartsEnvironment(Environment):
    """Built-in jinja2 template engine for pyecharts

    """

    def __init__(self, *args, **kwargs):
        super(EchartsEnvironment, self).__init__(
            keep_trailing_newline=True,
            trim_blocks=True,
            lstrip_blocks=True,
            *args,
            **kwargs)

        # Add PyEChartsConfig
        self.globals.update({
            'echarts_js_dependencies': echarts_js_dependencies,
            'echarts_js_dependencies_embed': echarts_js_dependencies_embed,
            'echarts_container': echarts_container,
            'echarts_js_content': echarts_js_content,
            'echarts_js_content_wrap': echarts_js_content_wrap
        })


def configure(jshost=None, **kwargs):
    if jshost:
        constants.CONFIGURATION['HOST'] = jshost
