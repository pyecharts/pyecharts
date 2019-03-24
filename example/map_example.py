from pyecharts import options as opts
from pyecharts.charts import Map, Timeline

map = Map()
value1 = [155, 10, 66, 78]
attr = ["福建", "山东", "北京", "上海"]
map.add("", [list(z) for z in zip(attr, value1)], "china")
map.set_global_opts(visualmap_opts=opts.VisualMapOpts())


map1 = Map()
value2 = [155, 10, 20, 78]
attr = ["福建", "山东", "北京", "汕头"]
map1.add("", [list(z) for z in zip(attr, value2)], "china")
map1.set_global_opts(visualmap_opts=opts.VisualMapOpts())

t = Timeline()
t.add(map, "2018")
t.add(map1, "2019")
t.render()
