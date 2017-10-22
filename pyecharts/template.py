#!/usr/bin/env python
# coding=utf-8
from __future__ import unicode_literals

from jinja2 import Environment, FileSystemLoader, contextfunction
import pyecharts.constants as constants
from pyecharts.utils import get_resource_dir, json_dumps


@contextfunction
def echarts_js_dependencies(context, *args):
    """
    Render script html nodes in external link mode.
    :param context:
    :param args:
    :return:
    """
    dependencies = []
    for a in args:
        if hasattr(a, 'js_dependencies'):
            dependencies.extend(a.js_dependencies)
        else:
            dependencies.append(a)

    jshost = args[0]._jshost
    js_links = ['{}/{}.js'.format(jshost, x) for x in dependencies]
    return '\n'.join(['<script type="text/javascript" src="{}"></script>'.format(j) for j in js_links])


@contextfunction
def echarts_js_dependencies_embed(context, *args):
    """
    Render script html nodes in embed mode,Only used for local files.
    :param context:
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


@contextfunction
def echarts_container(context, chart):
    """
    Render a div html element for a chart.
    :param context:
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


@contextfunction
def echarts_js_content(context, chart):
    content_fmt = '''
    var myChart_{chart_id} = echarts.init(document.getElementById('{chart_id}'));
    var option_{chart_id} = {options};
    myChart_{chart_id}.setOption(option_{chart_id});
    '''
    js_content = content_fmt.format(
        chart_id=chart.chart_id,
        options=json_dumps(chart.options)
    )
    return '<script type="text/javascript">\n{}\n</script>'.format(js_content)


@contextfunction
def echarts_js_content_wrap(context, chart):
    content_fmt = '''
    var myChart_{chart_id} = echarts.init(document.getElementById('{chart_id}'));
    var option_{chart_id} = {options};
    myChart_{chart_id}.setOption(option_{chart_id});
    '''
    js_content = content_fmt.format(
        chart_id=chart.chart_id,
        options=json_dumps(chart.options)
    )
    return js_content


# Single Singleton Instance for jinja2
JINJA2_ENV = Environment(
    loader=FileSystemLoader(get_resource_dir('templates')),
    keep_trailing_newline=True,
    trim_blocks=True,
    lstrip_blocks=True)

# Add jinja2 template functions

JINJA2_ENV.globals.update({
    'echarts_js_dependencies': echarts_js_dependencies,
    'echarts_js_dependencies_embed': echarts_js_dependencies_embed,
    'echarts_container': echarts_container,
    'echarts_js_content': echarts_js_content,
    'echarts_js_content_wrap': echarts_js_content_wrap
})


def produce_require_configuration(dependencies, jshost):
    """

    :param dependencies:
    :param jshost:
    :return:
    """
    _d = ensure_echarts_is_in_the_front(dependencies)
    # if no nick name register, we treat the location as location.js
    require_conf_items = [
        "'%s': '%s/%s'" % (key,
                           jshost,
                           constants.DEFAULT_JS_LIBRARIES.get(key, key))
        for key in _d]
    require_libraries = ["'%s'" % key for key in _d]
    return dict(
        config_items=require_conf_items,
        libraries=require_libraries
    )


def produce_html_script_list(dependencies):
    """

    :param dependencies:
    :return:
    """
    _d = ensure_echarts_is_in_the_front(dependencies)
    script_list = [
        '%s' % constants.DEFAULT_JS_LIBRARIES.get(key, key)
        for key in _d]
    return script_list


def ensure_echarts_is_in_the_front(dependencies):
    """
    make sure echarts is the item in the list
    require(['echarts'....], function(ec) {..}) need it to be first
    but dependencies is a set so has no sequence

    :param dependencies:
    :return:
    """
    if len(dependencies) > 1:
        dependencies.remove('echarts')
        dependencies = ['echarts'] + list(dependencies)
    elif len(dependencies) == 1:
        # make a new list
        dependencies = list(dependencies)
    else:
        raise Exception("No js library found. Nothing works!")
    return dependencies


def online(host=constants.DEFAULT_HOST):
    constants.CONFIGURATION['HOST'] = host
