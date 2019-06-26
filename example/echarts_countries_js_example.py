from pyecharts import options as opts
from pyecharts.charts import Geo
from pyecharts.datasets import register_url

register_url("https://echarts-maps.github.io/echarts-countries-js/")

g = (
    Geo()
    .add_schema(maptype="瑞士")
    .set_global_opts(title_opts=opts.TitleOpts(title="瑞士"))
)
g.render()
