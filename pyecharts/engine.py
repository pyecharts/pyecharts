# coding=utf-8
from __future__ import unicode_literals

import os

from jinja2 import Environment, FileSystemLoader, environmentfunction, Markup
from pyecharts.utils import json_dumps
from pyecharts import constants
from pyecharts.conf import PyEchartsConfig


class Helpers(object):
    @staticmethod
    def merge_js_dependencies(*args):
        """ Merge js dependencies to a list

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
        if len(dependencies) > 1:
            dependencies.remove('echarts')
            dependencies = ['echarts'] + list(dependencies)
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
    """ Render script html nodes in external link mode.

    :param env:
    :param args:
    """
    current_config = env.pyecharts_config
    dependencies = Helpers.merge_js_dependencies(*args)
    js_names = [constants.DEFAULT_JS_LIBRARIES.get(x, x) for x in dependencies]

    if current_config.js_embed:
        contents = Helpers.read_file_contents_from_local(js_names)
        embed_script_tpl_str = '<script type="text/javascript">\n{}\n</script>'
        return Markup(
            '\n'.join([embed_script_tpl_str.format(c) for c in contents])
        )
    else:
        jshost = current_config.jshost
        js_links = Helpers.generate_js_link(jshost, js_names)
        link_script_tpl_str = '<script type="text/javascript" src="{}"></script>'
        return Markup(
            '\n'.join([link_script_tpl_str.format(j) for j in js_links])
        )


@environmentfunction
def echarts_js_dependencies_embed(env, *args):
    """ Render script html nodes in embed mode,Only used for local files.

    :param env:
    :param args:
    """
    dependencies = Helpers.merge_js_dependencies(*args)
    js_names = [constants.DEFAULT_JS_LIBRARIES.get(x, x) for x in dependencies]
    contents = Helpers.read_file_contents_from_local(js_names)
    embed_script_tpl_str = '<script type="text/javascript">\n{}\n</script>'
    return Markup(
        '\n'.join([embed_script_tpl_str.format(c) for c in contents])
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
        '<div id="{chart_id}" style="width:{width};height:{height};"></div>'.format(
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
    """ Render script html node for echarts initial code.

    :param env:
    :param chart:
    """
    return Markup('<script type="text/javascript">\n{}\n</script>'.format(
        generate_js_content(*charts)))


@environmentfunction
def echarts_js_content_wrap(env, *charts):
    """ Render echarts initial code for a chart.

    :param env:
    :param charts:
    """
    return generate_js_content(*charts)


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
            raise TypeError('no pyecharts_config for this environment specified')
        super(BaseEnvironment, self).__init__(*args, **kwargs)
        self.globals.update(ECHAERTS_TEMPLATE_FUNCTIONS)


class EchartsEnvironment(BaseEnvironment):
    """
    Built-in jinja2 template engine for pyecharts
    """

    def __init__(self, pyecharts_config=None, *args, **kwargs):
        pyecharts_config = pyecharts_config or PyEchartsConfig()
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
