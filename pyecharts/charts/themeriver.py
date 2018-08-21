# coding=utf-8

from pyecharts.chart import Chart


class ThemeRiver(Chart):
    """
    <<< 主题河流图 >>>

    主题河流图是一种特殊的流图, 它主要用来表示事件或主题等在一段时间内的变化。
    """

    def __init__(self, title="", subtitle="", **kwargs):
        super(ThemeRiver, self).__init__(title, subtitle, **kwargs)

    def add(self, *args, **kwargs):
        self.__add(*args, **kwargs)
        return self

    def __add(self, name, data, **kwargs):
        """

        :param name:
            系列名称，用于 tooltip 的显示，legend 的图例筛选。类型必须为 list。
        :param data:
            数据项，数据中，每一行是一个『数据项』，每一列属于一个『维度』。
            每个数据项至少需要三个维度，如 ['2015/11/08', 10, 'DQ']，分别为
            [时间，数值，种类（图例名）]。
        :param kwargs:
        """
        chart = self._get_all_options(**kwargs)
        self._option.get("legend")[0].get("data").extend(name)

        self._option.get("series").append(
            {
                "type": "themeRiver",
                "name": name,
                "data": data,
                "label": chart["label"],
                "seriesId": self._option.get("series_id"),
            }
        )

        self._option.update(singleAxis={"type": "time"})
        self._config_components(**kwargs)
        self._option.get("tooltip").update(trigger="axis")
