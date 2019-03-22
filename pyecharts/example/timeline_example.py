from pyecharts import options as opts
from pyecharts.charts import Bar, Timeline

bar_attr = ["衬衫", "羊毛衫", "雪纺衫", "裤子", "高跟鞋", "袜子"]
v1 = [5, 20, 36, 10, 75, 90]
v2 = [10, 25, 8, 60, 20, 80]
bar1 = Bar()
bar1.add_xaxis(bar_attr).add_yaxis("商家A", v1).add_yaxis("商家B", v2).set_global_opts(
    title_opts={"text": "2018asdasdasd"}
)

bar_attr = ["衬衫", "羊毛衫", "雪纺衫", "裤子", "高跟鞋", "袜子"]
v1 = [5, 20, 36, 10, 75, 901]
v2 = [10, 25, 8, 60, 20, 801]
bar2 = Bar()
bar2.add_xaxis(bar_attr).add_yaxis("商家A", v1).add_yaxis("商家B", v2).set_global_opts(
    title_opts={"text": "2019asdasdasd"}
)

t = Timeline()
t.add(bar1, "2018").add(bar2, "2019").render()
