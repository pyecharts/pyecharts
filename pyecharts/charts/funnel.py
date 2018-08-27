# coding=utf-8

from pyecharts.chart import Chart


class Funnel(Chart):
    """
    <<< 漏斗图 >>>
    """

    def __init__(self, title="", subtitle="", **kwargs):
        super(Funnel, self).__init__(title, subtitle, **kwargs)

    def add(self, *args, **kwargs):
        self.__add(*args, **kwargs)
        return self

    def __add(
        self,
        name,
        attr,
        value,
        funnel_sort="descending",
        funnel_gap=0,
        **kwargs
    ):
        """

        :param name:
            系列名称，用于 tooltip 的显示，legend 的图例筛选。
        :param attr:
            属性名称。
        :param value:
            属性所对应的值。
        :param funnel_sort:
            数据排序， 可以取 'ascending'，'descending'，'none'（表示按 data 顺序）。
        :param funnel_gap:
            数据图形间距。
        :param kwargs:
        """
        assert len(attr) == len(value)
        chart = self._get_all_options(**kwargs)

        _data = []
        for data in zip(attr, value):
            _name, _value = data
            _data.append({"name": _name, "value": _value})
        for element in attr:
            self._option.get("legend")[0].get("data").append(element)
        _dset = set(self._option.get("legend")[0].get("data"))
        self._option.get("legend")[0].update(data=list(_dset))

        self._option.get("series").append(
            {
                "type": "funnel",
                "name": name,
                "data": _data,
                "sort": funnel_sort,
                "gap": funnel_gap,
                "label": chart["label"],
            }
        )
        self._config_components(**kwargs)
