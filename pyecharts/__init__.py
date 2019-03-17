# coding=utf-8
# flake8: noqa

from pyecharts._version import __version__, __author__

# Simple Charts
from pyecharts.charts.basic_charts.bar import Bar
from pyecharts.charts.basic_charts.boxplot import Boxplot
from pyecharts.charts.basic_charts.effectscatter import EffectScatter
from pyecharts.charts.basic_charts.funnel import Funnel
from pyecharts.charts.basic_charts.gauge import Gauge
from pyecharts.charts.basic_charts.geo import Geo
from pyecharts.charts.basic_charts.geolines import GeoLines
from pyecharts.charts.basic_charts.graph import Graph
from pyecharts.charts.basic_charts.heatmap import HeatMap
from pyecharts.charts.basic_charts.kline import Kline
from pyecharts.charts.basic_charts.line import Line
from pyecharts.charts.basic_charts.liquid import Liquid
from pyecharts.charts.basic_charts.map import Map
from pyecharts.charts.basic_charts.parallel import Parallel
from pyecharts.charts.basic_charts.pie import Pie
from pyecharts.charts.basic_charts.polar import Polar
from pyecharts.charts.basic_charts.radar import Radar
from pyecharts.charts.basic_charts.sankey import Sankey
from pyecharts.charts.basic_charts.scatter import Scatter
from pyecharts.charts.basic_charts.themeriver import ThemeRiver
from pyecharts.charts.basic_charts.tree import Tree
from pyecharts.charts.basic_charts.treemap import TreeMap
from pyecharts.charts.basic_charts.wordcloud import WordCloud

# Composite Charts

# from pyecharts.charts.composite_charts.grid import Grid
from pyecharts.charts.composite_charts.overlap import Overlap
from pyecharts.charts.composite_charts.timeline import Timeline

# custom component

from pyecharts.charts.composite_charts.page import Page

# misc
# from pyecharts.conf import online
# from pyecharts.conf import enable_nteract
# from pyecharts.conf import configure

# from pyecharts.conf import jupyter_image

# alias
Candlestick = Kline
