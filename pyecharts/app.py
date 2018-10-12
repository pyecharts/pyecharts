# coding=utf8

from pyecharts.conf import PyEchartsConfig
from contextlib import contextmanager

import pyecharts.constants as constants

# TODO Merge
ONLINE_ASSETS_JS = "https://pyecharts.github.io/assets/js/"

# TODO Make private
CURRENT_CONFIG = PyEchartsConfig()


def configure(
    jshost=None,
    hosted_on_github=None,
    echarts_template_dir=None,
    force_js_embed=None,
    output_image=None,
    global_theme=None,
):
    """
    Config all items for pyecharts when use chart.render() or page.render().

    :param jshost: the host for echarts related javascript libraries
    :param hosted_on_github use js files in github or not
    :param echarts_template_dir: the directory for custom html templates
    :param force_js_embed: embed javascript in html file or not
    :param output_image: Non None value asks pyecharts to use
                         pyecharts-snapshots to render as image directly.
                         Values such as 'svg', 'jpeg', 'png' changes
                         chart presentation in jupyter notebook to those image
                         formats, instead of 'html' format.
    :param global_theme: Default Theme
    """
    if jshost:
        CURRENT_CONFIG.jshost = jshost
    elif hosted_on_github is True:
        CURRENT_CONFIG.hosted_on_github = True
    if echarts_template_dir:
        CURRENT_CONFIG.echarts_template_dir = echarts_template_dir
    if force_js_embed is not None:
        CURRENT_CONFIG.force_js_embed = force_js_embed
    if output_image in constants.JUPYTER_PRESENTATIONS:
        CURRENT_CONFIG.jupyter_presentation = output_image
    if global_theme is not None:
        CURRENT_CONFIG.theme = global_theme


def online(host=None):
    """
    Set the jshost

    :param host: remote js host
    """
    if host is None:
        configure(hosted_on_github=True)
    else:
        configure(jshost=host)


def enable_nteract(host=None):
    # self.jshost 为 None 时应该使用远程 js
    # "https://pyecharts.github.io/assets/js"
    CURRENT_CONFIG.is_run_on_nteract = True
    _host = ONLINE_ASSETS_JS
    if host:
        _host = host
    configure(
        output_image=constants.NTERACT, jshost=_host
    )


@contextmanager
def jupyter_image(jupyter_presentation):
    """
    Temporarily change jupyter's default presentation
    """
    # TODO Remove
    previous_presentation = CURRENT_CONFIG.jupyter_presentation
    try:
        CURRENT_CONFIG.jupyter_presentation = jupyter_presentation
        yield

    finally:
        CURRENT_CONFIG.jupyter_presentation = previous_presentation


def use_config():
    pass
