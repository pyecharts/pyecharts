import pyecharts.options as opts
from pyecharts.charts import Bar, Grid, Line

bar_attr = ["衬衫", "羊毛衫", "雪纺衫", "裤子", "高跟鞋", "袜子"]
v1 = [5, 20, 36, 10, 75, 90]
v2 = [10, 25, 8, 60, 20, 80]
bar = Bar()
bar.add_xaxis(bar_attr).add_yaxis("商家A", v1).add_yaxis("商家B", v2)

line_attr = ["周一", "周二", "周三", "周四", "周五", "周六", "周日"]
line = Line()
line.add_xaxis(line_attr)
line.add_yaxis("最高气温", [11, 11, 15, 13, 12, 13, 10])
line.add_yaxis("最低气温", [1, -2, 2, 5, 3, 2, 0])

grid = Grid()
grid.add(bar, opts.GridOpts(bottom="60%"))
grid.add(line, opts.GridOpts(top="60%"))
grid.render()
