import pyecharts.options as opts
from pyecharts.charts import Bar, Line

attr = ["{}月".format(i) for i in range(1, 13)]
v1 = [2.0, 4.9, 7.0, 23.2, 25.6, 76.7, 135.6, 162.2, 32.6, 20.0, 6.4, 3.3]
v2 = [2.6, 5.9, 9.0, 26.4, 28.7, 70.7, 175.6, 182.2, 48.7, 18.8, 6.0, 2.3]
v3 = [2.0, 2.2, 3.3, 4.5, 6.3, 10.2, 20.3, 23.4, 23.0, 16.5, 12.0, 6.2]

bar = Bar()
bar.add_xaxis(attr).add_yaxis("蒸发量", v1).add_yaxis("降水量", v2)
bar.set_global_opts(yaxis_opt=opts.AxisOpts(formatter="{value} ml"))
bar.extend_axis(yaxis=opts.AxisOpts(formatter="{value} °C", interval=5))

line = Line()
line.add_xaxis(attr).add_yaxis("平均温度", v3, yaxis_index=1)
bar.overlap(line).render()
