# coding=utf-8

from pyecharts.charts.chart import Chart

from ...options import *


class HeatMap(Chart):
    """
    <<< 热力图 >>>

    热力图主要通过颜色去表现数值的大小，必须要配合 visualMap 组件使用。
    直角坐标系上必须要使用两个类目轴。
    """

    def __init__(self, init_opts: InitOpts = InitOpts()):
        super().__init__(init_opts=init_opts)

    def add(
        self,
        label_opt: LabelOpts = LabelOpts(),
        splitline_opt: SplitLineOpts = SplitLineOpts(),
    ):

        if isinstance(label_opt, LabelOpts):
            label_opt = label_opt.opts
        if isinstance(splitline_opt, SplitLineOpts):
            splitline_opt = splitline_opt.opts

        _is_calendar = kwargs.get("is_calendar_heatmap", None) is True
        if _is_calendar:
            name, data = args
        else:
            name, x_axis, y_axis, data = args

        if "yaxis_formatter" not in kwargs:
            kwargs["yaxis_formatter"] = None
            self._append_legend(name)

        self.options.get("series").append(
            {"type": "heatmap", "name": name, "data": data, "label": label_opt}
        )

        if _is_calendar:
            self.options.get("toolbox").update(left="98%", top="26%")
            self.options.get("series")[0].update(coordinateSystem="calendar")
            self.options.update(calendar=chart["calendar"])
        else:
            xaxis, yaxis = chart["xy_axis"]
            self.options.update(xAxis=xaxis, yAxis=yaxis)
            self.options.get("xAxis")[0].update(
                type="category", data=x_axis, splitArea=splitline_opt
            )
            self.options.get("yAxis")[0].update(
                type="category", data=y_axis, splitArea=splitline_opt
            )
