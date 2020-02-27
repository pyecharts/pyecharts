from pyecharts import options as opts
from pyecharts.charts import Geo, Page
from pyecharts.datasets import register_url
from pyecharts.faker import Collector

C = Collector()


@C.funcs
def geo_echart_countries_js() -> Geo:
    register_url("https://echarts-maps.github.io/echarts-countries-js/")

    geo = (
        Geo()
        .add_schema(maptype="瑞士")
        .set_global_opts(title_opts=opts.TitleOpts(title="瑞士"))
    )
    return geo


@C.funcs
def geo_echart_china_js() -> Geo:
    register_url("https://echarts-maps.github.io/echarts-china-counties-js/")

    geo = (
        Geo()
        .add_schema(maptype="海淀区")
        .set_global_opts(title_opts=opts.TitleOpts(title="海淀区"))
    )
    return geo


Page().add(*[fn() for fn, _ in C.charts]).render()
