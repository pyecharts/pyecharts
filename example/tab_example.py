from example.page_example import bar_datazoom_slider, line_markpoint, pie_rosetype
from pyecharts.charts import Tab


def tab_base():
    tab = Tab()
    tab.add(bar_datazoom_slider(), "bar-example")
    tab.add(line_markpoint, "line-example")
    tab.add(pie_rosetype(), "pie-example")
    tab.render()
