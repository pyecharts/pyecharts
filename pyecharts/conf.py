# coding=utf-8

# from __future__ import unicode_literals
from contextlib import contextmanager

from pyecharts import consts

# ONLINE_ASSETS_JS = "https://pyecharts.github.io/assets/js/"
#
#
# class PyEchartsConfig:
#     def __init__(self, echarts_template_dir: str = ".", jshost: str = ""):
#         self.echarts_template_dir = echarts_template_dir
#         self.jshost = jshost or ONLINE_ASSETS_JS
#         self.jupyter_presentation: str = consts.FILE_TYPES["html"]
#
#     def generate_js_link(self, deps: list) -> list:
#         # self.jshost 为 None 时应该使用远程 js
#         # "https://pyecharts.github.io/assets/js"
#         if not self.jshost:
#             self.jshost = ONLINE_ASSETS_JS
#         links = []
#         for dep in deps:
#             # TODO: if?
#             links.append(self.jshost + dep)
#         return links
#
#     def gen_notebook_cfg(self, deps) -> dict:
#         items = []
#         for dep in deps:
#             # TODO: if?
#             items.append(dep)
#         require_libraries = ["'{}'".format(key) for key in deps]
#         return dict(config_items=items, libraries=require_libraries)


# def remove_trailing_slashes(jshost):
#     """
#     Delete the end separator character if exists.
#     """
#     if jshost and jshost[-1] in ("/", "\\"):
#         return jshost[:-1]
#
#     else:
#         return jshost
#
#
# CURRENT_CONFIG = PyEchartsConfig()


# def configure(
#     jshost=None,
#     hosted_on_github=None,
#     echarts_template_dir=None,
#     force_js_embed=None,
#     output_image=None,
#     global_theme=None,
# ):
#     """
#     Config all items for pyecharts when use chart.render() or page.render().
#
#     :param jshost: the host for echarts related javascript libraries
#     :param echarts_template_dir: the directory for custom html templates
#     :param force_js_embed: embed javascript in html file or not
#     :param output_image: Non None value asks pyecharts to use
#                          pyecharts-snapshots to render as image directly.
#                          Values such as 'svg', 'jpeg', 'png' changes
#                          chart presentation in jupyter notebook to those image
#                          formats, instead of 'html' format.
#     """
#     if jshost:
#         CURRENT_CONFIG.jshost = jshost
#     elif hosted_on_github is True:
#         CURRENT_CONFIG.hosted_on_github = True
#     if echarts_template_dir:
#         CURRENT_CONFIG.echarts_template_dir = echarts_template_dir
#     if force_js_embed is not None:
#         CURRENT_CONFIG.force_js_embed = force_js_embed
#     if output_image in consts.JUPYTER_PRESENTATIONS:
#         CURRENT_CONFIG.jupyter_presentation = output_image
#     if global_theme is not None:
#         CURRENT_CONFIG.theme = global_theme
#
#
# def enable_nteract(host=None):
#     # self.jshost 为 None 时应该使用远程 js
#     # "https://pyecharts.github.io/assets/js"
#     _host = ONLINE_ASSETS_JS
#     if host:
#         _host = host
#     configure(output_image=consts.NTERACT, jshost=remove_trailing_slashes(_host))
#
#
# @contextmanager
# def jupyter_image(jupyter_presentation):
#     """
#     Temporarily change jupyter's default presentation
#     """
#     previous_presentation = CURRENT_CONFIG.jupyter_presentation
#     try:
#         CURRENT_CONFIG.jupyter_presentation = jupyter_presentation
#         yield
#
#     finally:
#         CURRENT_CONFIG.jupyter_presentation = previous_presentation
