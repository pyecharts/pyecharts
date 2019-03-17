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

    def add(self, *args, **kwargs):
        """

        :param args:
            如果指定；额 is_has_calendar_heatmap 属性为 True，则定义如下
                :param name:
                    系列名称，用于 tooltip 的显示，legend 的图例筛选。
                :param data:
                    数据项，数据中，每一行是一个『数据项』，每一列属于一个『维度』。
            不指定，默认情况定义如下:
                :param name:
                    系列名称，用于 tooltip 的显示，legend 的图例筛选。
                :param x_axis:
                    x 坐标轴数据。需为类目轴，也就是不能是数值。
                :param y_axis:
                    y 坐标轴数据。需为类目轴，也就是不能是数值。
                :param data:
                    数据项，数据中，每一行是一个『数据项』，每一列属于一个『维度』。
        :param kwargs:
        """
        _is_calendar = kwargs.get("is_calendar_heatmap", None) is True
        if _is_calendar:
            name, data = args
        else:
            name, x_axis, y_axis, data = args

        if "yaxis_formatter" not in kwargs:
            kwargs["yaxis_formatter"] = None
            self._append_legend(name)

        self.options.get("series").append(
            {
                "type": "heatmap",
                "name": name,
                "data": data,
                "label": chart["label"],
                "seriesId": self._option.get("series_id"),
            }
        )

        if _is_calendar:
            self.options.get("toolbox").update(left="98%", top="26%")
            self.options.get("series")[0].update(coordinateSystem="calendar")
            self.options.update(calendar=chart["calendar"])
        else:
            xaxis, yaxis = chart["xy_axis"]
            self.options.update(xAxis=xaxis, yAxis=yaxis)
            self.options.get("xAxis")[0].update(
                type="category", data=x_axis, splitArea={"show": True}
            )
            self.options.get("yAxis")[0].update(
                type="category", data=y_axis, splitArea={"show": True}
            )
