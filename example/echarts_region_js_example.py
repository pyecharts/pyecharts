from pyecharts import options as opts
from pyecharts.charts import Geo
from pyecharts.datasets import register_url


def geo_echart_countries_js():
    register_url("https://echarts-maps.github.io/echarts-countries-js/")

    geo = (
        Geo()
        .add_schema(maptype="瑞士")
        .set_global_opts(title_opts=opts.TitleOpts(title="瑞士"))
    )
    geo.render()


def geo_echart_china_js():
    register_url("https://echarts-maps.github.io/echarts-china-counties-js/")

    geo = (
        Geo()
        .add_schema(maptype="海淀区")
        .set_global_opts(title_opts=opts.TitleOpts(title="海淀区"))
    )
    geo.render()
