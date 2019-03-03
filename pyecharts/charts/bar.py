# coding=utf-8

from typing import Any

from pyecharts.chart import Chart


class Bar(Chart):
    """
    <<< 柱状图/条形图 >>>

    柱状/条形图，通过柱形的高度/条形的宽度来表现数据的大小。
    """

    def __init__(self, title="", subtitle="", **kwargs):
        super().__init__(title, subtitle, **kwargs)
        self.options.update(yAxis={})

    def add_xaxis(self, xaxis_data: Any):
        self.options.update(xAxis=dict(data=xaxis_data))
        return self

    def add_yaxis(self, series_name: str, yaxis_data: Any):
        self.options.get("legend")[0].get("data").append(series_name)
        self.options.get("series").append(
            {
                "type": "bar",
                "name": series_name,
                "data": yaxis_data,
                # "seriesId": self._option.get("series_id"),
            }
        )
        return self

    def set_series_opts(self):
        return self

    def set_global_opts(self):
        return self

    def add(self, *args, **kwargs):
        self.__add(*args, **kwargs)
        return self

    def __add(
        self, name, x_axis, y_axis, is_stack=False, bar_category_gap="20%", **kwargs
    ):
        """

        :param name:
            系列名称，用于 tooltip 的显示，legend 的图例筛选。
        :param x_axis:
            x 坐标轴数据。
        :param y_axis:
            y 坐标轴数据。
        :param is_stack:
            数据堆叠，同个类目轴上系列配置相同的 stack 值可以堆叠放置。默认为 False。
        :param kwargs:
        """
        # assert len(x_axis) == len(y_axis)
        kwargs.update(x_axis=x_axis)
        chart = self._get_all_options(**kwargs)

        if is_stack:
            is_stack = "stack_" + str(self._option["series_id"])
        else:
            is_stack = ""
        xaxis, yaxis = chart["xy_axis"]
        self._option.update(xAxis=xaxis, yAxis=yaxis)
        self._option.get("legend")[0].get("data").append(name)

        self._option.get("series").append(
            {
                "type": "bar",
                "name": name,
                "data": y_axis,
                "stack": is_stack,
                "barCategoryGap": bar_category_gap,
                "label": chart["label"],
                "markPoint": chart["mark_point"],
                "markLine": chart["mark_line"],
                "seriesId": self._option.get("series_id"),
            }
        )
        self._config_components(**kwargs)


Bar().add_xaxis(["A", "B", "C"]).add_yaxis("bar0", [1, 2, 4]).add_yaxis("bar1", [2, 3, 6]).render("render.html")
