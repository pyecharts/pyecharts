import datetime
import random

import pyecharts.options as opts
from pyecharts.charts import Calendar

begin = datetime.date(2017, 1, 1)
end = datetime.date(2017, 12, 31)
data = [
    [str(begin + datetime.timedelta(days=i)), random.randint(1000, 25000)]
    for i in range((end - begin).days + 1)
]

c = Calendar()
c.add("A", data, calendar_opts=opts.CalendarOpts(range_="2017"))
c.set_global_opts(
    visualmap_opts=opts.VisualMapOpts(
        max_=20000, min_=500, orient="horizontal", is_piecewise=True, pos_top="230px"
    )
)
c.render()
