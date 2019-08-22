from example.page_example import (
    bar_datazoom_slider,
    grid_mutil_yaxis,
    line_markpoint,
    pie_rosetype,
)
from pyecharts.charts import Tab

tab = Tab()
tab.add(bar_datazoom_slider(), "bar-example")
tab.add(line_markpoint(), "line-example")
tab.add(pie_rosetype(), "pie-example")
tab.add(grid_mutil_yaxis(), "grid-example")
tab.render()
