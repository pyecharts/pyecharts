from pyecharts import Bar, Line
from pyecharts.options import *

bar = (
    Bar()
    .add_xaxis(["A", "B", "C"])
    .add_yaxis("bar0", [1, 2, 4])
    .add_yaxis("bar1", [2, 3, 6], label_opts=LabelOpts(is_show=False))
    .set_series_opts(
        markpoint_opts=MarkPointOpts(
            data=[MarkPointData(type_="max"), MarkPointData(type_="min")]
        )
    )
    .set_global_opts(
        title_opts=TitleOpts(title="Bar 示例图"),
        toolbox_opts=ToolboxOpst(is_show=False, pos_left="80%"),
    )
).render("bar.html")

line = (
    Line()
    .add_xaxis(["A", "B", "C"])
    .add_yaxis("bar0", [1, 2, 4])
    .add_yaxis("bar1", [2, 3, 6])
    .set_series_opts(
        markpoint_opts=MarkPointOpts(
            data=[MarkPointData(type_="max"), MarkPointData(type_="min")]
        )
    )
    .set_global_opts(
        title_opts=TitleOpts(title="Line 示例图"),
        toolbox_opts=ToolboxOpst(is_show=False, pos_left="80%"),
    )
)
line.render("line.html")
