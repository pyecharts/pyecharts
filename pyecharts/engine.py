#!/usr/bin/env python
# coding=utf-8
from __future__ import unicode_literals
import os
from jinja2 import Environment, environmentfunction
from pyecharts.utils import json_dumps
from pyecharts import constants
from pyecharts.conf import CURRENT_CONFIG


class Helpers(object):
    @staticmethod
    def merge_js_dependencies(*args):
        """Merge js dependencies to a list
        :param args:
        :return:
        """
        dependencies = []

        def _add(_x):
            if _x not in dependencies:
                dependencies.append(_x)

        for a in args:
            if hasattr(a, 'js_dependencies'):
                for d in a.js_dependencies:
                    _add(d)
            else:
                _add(a)
        return dependencies

    @staticmethod
    def read_file_contents_from_local(js_names):
        contents = []
        for name in js_names:
            path = os.path.join(constants.SCRIPT_LOCAL_JSHOST, name + '.js')
            with open(path, 'rb') as f:
                c = f.read()
                contents.append(c.decode('utf8'))
        return contents

    @staticmethod
    def generate_js_link(jshost, js_names):
        return ['{}/{}.js'.format(jshost, x) for x in js_names]


@environmentfunction
def echarts_js_dependencies(env, *args):
    """
    Render script html nodes in external link mode.
    :param env:
    :param args:
    :return:
    """
    dependencies = Helpers.merge_js_dependencies(*args)
    js_names = [constants.DEFAULT_JS_LIBRARIES.get(x, x) for x in dependencies]

    if CURRENT_CONFIG.js_embed:
        contents = Helpers.read_file_contents_from_local(js_names)
        return '\n'.join(['<script type="text/javascript">\n{}\n</script>'.format(c) for c in contents])
    else:
        jshost = CURRENT_CONFIG.get_current_jshost_for_script()
        js_links = Helpers.generate_js_link(jshost, js_names)
        return '\n'.join(['<script type="text/javascript" src="{}"></script>'.format(j) for j in js_links])


@environmentfunction
def echarts_js_dependencies_embed(env, *args):
    """
    Render script html nodes in embed mode,Only used for local files.
    :param env:
    :param args:
    :return:
    """
    dependencies = Helpers.merge_js_dependencies(*args)
    js_names = [constants.DEFAULT_JS_LIBRARIES.get(x, x) for x in dependencies]
    contents = Helpers.read_file_contents_from_local(js_names)
    return '\n'.join(['<script type="text/javascript">\n{}\n</script>'.format(c) for c in contents])


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


def generate_js_content(*charts):
    """
    Generate the initial code fragment for one or some chart instances.
    :param charts:
    :return:
    """
    contents = []
    for chart in charts:
        content_fmt = '''
        var myChart_{chart_id} = echarts.init(document.getElementById('{chart_id}'));
        var option_{chart_id} = {options};
        myChart_{chart_id}.setOption(option_{chart_id});
        '''
        js_content = content_fmt.format(
            chart_id=chart.chart_id,
            options=json_dumps(chart.options, indent=4)
        )
        contents.append(js_content)
    contents = '\n'.join(contents)
    return contents


@environmentfunction
def echarts_js_content(env, *charts):
    """
    Render script html node for echarts initial code.
    :param env:
    :param chart:
    :return:
    """
    return '<script type="text/javascript">\n{}\n</script>'.format(generate_js_content(*charts))


@environmentfunction
def echarts_js_content_wrap(env, *charts):
    """
    Render echarts initial code for a chart.
    :param env:
    :param charts:
    :return:
    """
    return generate_js_content(*charts)


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


def configure(
        jshost=None,
        echarts_template_dir=None,
        force_js_embed=None,
        **kwargs
):
    """
    Config all items for pyecharts.
    :param jshost:
    :param echarts_template_dir:
    :param force_js_embed:
    :param kwargs:
    :return:
    """
    if jshost:
        constants.CONFIGURATION['HOST'] = jshost
        CURRENT_CONFIG.jshost = jshost
    if echarts_template_dir:
        CURRENT_CONFIG.echarts_template_dir = echarts_template_dir
    if force_js_embed is not None:
        CURRENT_CONFIG.force_js_embed = force_js_embed
