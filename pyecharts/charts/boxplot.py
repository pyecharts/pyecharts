# coding=utf-8

from pyecharts.chart import Chart


class Boxplot(Chart):
    """
    <<< 箱形图 >>>

    箱形图是一种用作显示一组数据分散情况资料的统计图。它能显示出一组数据
    的最大值、最小值、中位数、下四分位数及上四分位数。
    """

    def __init__(self, title="", subtitle="", **kwargs):
        super(Boxplot, self).__init__(title, subtitle, **kwargs)

    def add(self, *args, **kwargs):
        self.__add(*args, **kwargs)
        return self

    def __add(self, name, x_axis, y_axis, **kwargs):
        """

        :param name:
            系列名称，用于 tooltip 的显示，legend 的图例筛选。
        :param x_axis:
            x 坐标轴数据。
        :param y_axis:
            y 坐标轴数据，二维数组的每一数组项（上例中的每行）是渲染一个 box。
            它含有五个量值，依次是：[min, Q1, median (or Q2), Q3, max]。
        :param kwargs:
        """
        kwargs.update(x_axis=x_axis)
        chart = self._get_all_options(**kwargs)

        xaxis, yaxis = chart["xy_axis"]
        self._option.update(xAxis=xaxis, yAxis=yaxis)
        self._option.get("legend")[0].get("data").append(name)

        self._option.get("series").append(
            {
                "type": "boxplot",
                "name": name,
                "data": y_axis,
                "label": chart["label"],
                "markPoint": chart["mark_point"],
                "markLine": chart["mark_line"],
                "seriesId": self._option.get("series_id"),
            }
        )
        self._config_components(**kwargs)

    @staticmethod
    def prepare_data(data):
        """ 将传入的嵌套列表中的数据转换为嵌套的 [min,  Q1,  median (or Q2),  Q3,  max]

        :param data:
            待转换的数据列表
        :return:
            转换后的数组
        """
        _data = []
        for d in data:
            try:
                _d, _result = sorted(d), []
                for i in range(1, 4):
                    n = i * (len(_d) + 1) / 4
                    m = n - int(n)
                    if m == 0:
                        _result.append(_d[int(n) - 1])
                    elif m == 1 / 4:
                        _result.append(
                            _d[int(n) - 1] * 0.75 + _d[int(n)] * 0.25
                        )
                    elif m == 1 / 2:
                        _result.append(_d[int(n) - 1] * 0.5 + _d[int(n)] * 0.5)
                    elif m == 3 / 4:
                        _result.append(
                            _d[int(n) - 1] * 0.25 + _d[int(n)] * 0.75
                        )
                _result.insert(0, _d[0])  # 最小值
                _result.append(_d[-1])  # 最大值
                _data.append(_result)
            except Exception:
                pass
        return _data
