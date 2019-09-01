from example.page_example import (
    bar_datazoom_slider,
    grid_mutil_yaxis,
    line_markpoint,
    pie_rosetype,
    table_base,
)
from pyecharts.charts import Tab


def tab_base():
    tab = Tab()
    tab.add(bar_datazoom_slider(), "bar-example")
    tab.add(line_markpoint(), "line-example")
    tab.add(pie_rosetype(), "pie-example")
    tab.add(grid_mutil_yaxis(), "grid-example")
    tab.add(table_base(), "table-example")
    tab.render()
