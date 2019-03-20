from pyecharts.charts import Geo, Map
from pyecharts.options import *

geo = Geo()
geo.add("geo", [("广州", 10)])
geo.set_global_opts()
geo.render()

# map = Map()
# map.add("geo", [("广东", 10)])
# map.set_global_opts(tooltip_opts=TooltipOpts())
# map.render()
