# coding=utf-8
from __future__ import unicode_literals

from jinja2 import Environment, FileSystemLoader, Markup, environmentfunction
from lml.plugin import PluginInfo, PluginManager
from pyecharts_javascripthon.api import FUNCTION_TRANSLATOR, TRANSLATOR

import pyecharts.conf as conf
import pyecharts.constants as constants
import pyecharts.utils as utils

LINK_SCRIPT_FORMATTER = '<script type="text/javascript" src="{}"></script>'
EMBED_SCRIPT_FORMATTER = '<script type="text/javascript">\n{}\n</script>'
CHART_DIV_FORMATTER = (
    '<div id="{chart_id}" style="width:{width};height:{height};"></div>'
)  # flake8: noqa
CHART_CONFIG_FORMATTER = """
var myChart_{chart_id} = echarts.init(document.getElementById('{chart_id}'), '{theme}', {{renderer: '{renderer}'}});
{custom_function}
var option_{chart_id} = {options};
myChart_{chart_id}.setOption(option_{chart_id});
"""
CHART_EVENT_FORMATTER = """
myChart_{chart_id}.on("{event_name}", {handler_name});
"""
EXTRA_TEXT_FORMATTER = """<p style="{style}">{text}</p>"""


@environmentfunction
def echarts_js_dependencies(env, *args):
    """
    Render script html nodes in external link mode.
    """
    current_config = env.pyecharts_config
    dependencies = utils.merge_js_dependencies(*args)

    if current_config.js_embed:
        contents = current_config.read_file_contents_from_local(dependencies)

        return Markup(
            "\n".join([EMBED_SCRIPT_FORMATTER.format(c) for c in contents])
        )

    else:
        js_links = current_config.generate_js_link(dependencies)
        return Markup(
            "\n".join([LINK_SCRIPT_FORMATTER.format(j) for j in js_links])
        )


@environmentfunction
def echarts_js_dependencies_embed(env, *args):
    """
    Render script html nodes in embed mode,Only used for local files.
    """
    current_config = env.pyecharts_config
    dependencies = utils.merge_js_dependencies(*args)
    contents = current_config.read_file_contents_from_local(dependencies)
    return Markup(
        "\n".join([EMBED_SCRIPT_FORMATTER.format(c) for c in contents])
    )


@environmentfunction
def echarts_container(env, chart):
    """
    Render <p></p><div></div> html elements for a chart.

    :param env:
    :param chart: A pyecharts.base.Base object
    """
    _container_and_text = ""
    _text_label = chart.extra_html_text_label
    if _text_label:
        if len(_text_label) == 1 and isinstance(_text_label, list):
            _text_label.append("")
        _text, _style = _text_label
        _container_and_text += EXTRA_TEXT_FORMATTER.format(
            text=_text, style=_style
        )

    _container_and_text += CHART_DIV_FORMATTER.format(
        chart_id=chart.chart_id,
        width=utils.to_css_length(chart.width),
        height=utils.to_css_length(chart.height),
    )
    return Markup(_container_and_text)


def generate_js_content(*charts):
    """
    Generate the initial code fragment for one or some chart instances.
    """
    contents = []

    for chart in charts:
        FUNCTION_TRANSLATOR.reset()
        for handler in chart.event_handlers.values():
            FUNCTION_TRANSLATOR.feed(handler)

        javascript_snippet = TRANSLATOR.translate(chart.options)
        kwargs = dict(
            chart_id=chart.chart_id,
            renderer=chart.renderer,
            theme=chart.theme,
            custom_function=javascript_snippet.function_snippet,
            options=javascript_snippet.option_snippet,
        )
        js_content = CHART_CONFIG_FORMATTER.format(**kwargs)
        for event_name, handler in chart.event_handlers.items():
            # please note handler has been translated in previous block
            event_args = dict(
                event_name=event_name,
                chart_id=chart.chart_id,
                handler_name=handler.__name__,
            )
            js_content += CHART_EVENT_FORMATTER.format(**event_args)

        contents.append(js_content)
    contents = "\n".join(contents)
    return contents


@environmentfunction
def echarts_js_content(env, *charts):
    """
    Render script html node for echarts initial code.
    """
    return Markup(EMBED_SCRIPT_FORMATTER.format(generate_js_content(*charts)))


@environmentfunction
def echarts_js_content_wrap(env, *charts):
    """
    Render echarts initial code for a chart.
    """
    return Markup(generate_js_content(*charts))


# Public API,see document for more detail.

ECHAERTS_TEMPLATE_FUNCTIONS = {
    "echarts_js_dependencies": echarts_js_dependencies,
    "echarts_js_dependencies_embed": echarts_js_dependencies_embed,
    "echarts_container": echarts_container,
    "echarts_js_content": echarts_js_content,
    "echarts_js_content_wrap": echarts_js_content_wrap,
}


class BaseEnvironment(Environment):
    """
    Add config and echarts template functions to a Environment object.
    """

    def __init__(self, *args, **kwargs):
        self.pyecharts_config = kwargs.pop("pyecharts_config", None)
        if self.pyecharts_config is None:
            raise TypeError(
                "no pyecharts_config for this environment specified"
            )

        super(BaseEnvironment, self).__init__(*args, **kwargs)
        self.globals.update(ECHAERTS_TEMPLATE_FUNCTIONS)


@PluginInfo(constants.ENVIRONMENT_PLUGIN_TYPE, tags=[constants.DEFAULT_HTML])
class EchartsEnvironment(BaseEnvironment):
    """
    Built-in jinja2 template engine for pyecharts
    This class provides some shortcut methods for rendering charts.
    """

    def __init__(self, pyecharts_config=None, *args, **kwargs):
        pyecharts_config = pyecharts_config or conf.PyEchartsConfig()
        loader = kwargs.pop("loader", None)
        if loader is None:
            loader = FileSystemLoader(pyecharts_config.echarts_template_dir)
        super(EchartsEnvironment, self).__init__(
            pyecharts_config=pyecharts_config,
            keep_trailing_newline=True,
            trim_blocks=True,
            lstrip_blocks=True,
            loader=loader,
            *args,
            **kwargs
        )

    def render_container_and_echarts_code(self, chart):
        """
        Render <div> and <script> code fragment for a chart.
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
        object_name="chart",
        path="render.html",
        template_name="simple_chart.html",
        **kwargs
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
        kwargs[object_name] = chart
        tpl = self.get_template(template_name)
        html = tpl.render(**kwargs)
        utils.write_utf8_html_file(path, html)

    def render_chart_to_notebook(
        self, template_name="notebook.html", **context
    ):
        """
        Return html string for rendering a chart/page to a notebook cell.

        :param context: A dictionary containing data.
        :return: A unicode string that will be displayed in notebook cell.
        """
        tpl = self.get_template(template_name)
        return tpl.render(**context)


class EnvironmentManager(PluginManager):
    """
    Extend the rendering capability of pyecharts by having
    loosely coupled environments
    """

    def __init__(self):
        """
        Register with lml that this class manages 'pyecharts_environment'
        extension
        """
        super(EnvironmentManager, self).__init__(
            constants.ENVIRONMENT_PLUGIN_TYPE
        )

    def get_a_environment(self, file_type, **kwargs):
        """
        Factory method to choose the default html rendering EchartsEnvironment
        or image rendering SnapshotEnvironment from pyecharts-snapshot

        :param file_type: 'html', 'svg', 'png', 'jpeg', 'gif' or 'pdf'
        :param kwargs: the initialization parameters for Environment
        """
        _a_echarts_env_cls = super(EnvironmentManager, self).load_me_now(
            key=file_type
        )
        return _a_echarts_env_cls(**kwargs)


ENV_MANAGER = EnvironmentManager()


def create_default_environment(file_type):
    """
    Create environment object with pyecharts default single PyEchartsConfig.

    :return: A new EchartsEnvironment object.
    """
    default_template_dir = utils.get_resource_dir("templates")
    config = conf.CURRENT_CONFIG
    echarts_env = ENV_MANAGER.get_a_environment(
        file_type,
        pyecharts_config=config,
        loader=FileSystemLoader(
            [config.echarts_template_dir, default_template_dir]
        ),
    )
    return echarts_env
