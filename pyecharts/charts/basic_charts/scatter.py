# coding=utf-8

from pyecharts.commons.types import *
from pyecharts.charts.chart import Chart
from pyecharts.options import *


class Scatter(Chart):
    """
    <<< 散点图 >>>

    直角坐标系上的散点图可以用来展现数据的 x，y 之间的关系，如果数据项有多个维度，
    可以用颜色来表现，利用 geo 组件。
    """

    def __init__(self, init_opts: InitOpts = InitOpts()):
        super().__init__(init_opts=init_opts)
        self.options.update(yAxis={})
        self.__xaxis_data = None

    def add_xaxis(self, xaxis_data: Any):
        self.options.update(xAxis={"data": xaxis_data})
        self.__xaxis_data = xaxis_data
        return self

    def add_yaxis(self, name: str, y_axis: List, symbol_size=10, **kwargs):
        assert len(x_axis) == len(y_axis)
        kwargs.update(type="scatter", x_axis=x_axis)
        chart = self._get_all_options(**kwargs)

        xaxis, yaxis = chart["xy_axis"]
        # show split line, because by default split line is hidden for xaxis
        xaxis[0]["splitLine"]["show"] = True
        self._option.update(xAxis=xaxis, yAxis=yaxis)
        self._option.get("legend")[0].get("data").append(name)

        zip_lst = [x_axis, y_axis]
        for e in (extra_data, extra_name):
            if e:
                # 确保提供的额外的数据或名称长度相同
                assert len(e) == len(x_axis)
                zip_lst.append(e)
        _data = [list(z) for z in zip(*zip_lst)]

        self.options.get("series").append(
            {
                "type": "scatter",
                "name": name,
                "symbol": chart["symbol"],
                "symbolSize": symbol_size,
                "data": _data,
                "label": chart["label"],
                "markPoint": chart["mark_point"],
                "markLine": chart["mark_line"],
                "seriesId": self._option.get("series_id"),
            }
        )
