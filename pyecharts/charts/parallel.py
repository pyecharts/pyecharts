# coding=utf-8

import warnings

from pyecharts.chart import Chart


class Parallel(Chart):
    """
    <<< 平行坐标系 >>>

    平行坐标系是一种常用的可视化高维数据的图表。
    """

    def __init__(self, title="", subtitle="", **kwargs):
        super(Parallel, self).__init__(title, subtitle, **kwargs)

    def add(self, *args, **kwargs):
        self.__add(*args, **kwargs)
        return self

    def set_schema(self, schema=None, c_schema=None):
        """

        :param schema:
            默认平行坐标系的坐标轴信息，如 ["dim_name1", "dim_name2", "dim_name3"]。
        :param c_schema:
            用户自定义平行坐标系的坐标轴信息。有以下属性可选。
            dim：维度索引
            name：维度名称
            type：维度类型，有'value', 'category'可选
                value：数值轴，适用于连续数据。
                category： 类目轴，适用于离散的类目数据。
            min：坐标轴刻度最小值。
            max：坐标轴刻度最大值。
            inverse：是否是反向坐标轴。默认为 False
            nameLocation：坐标轴名称显示位置。有'start', 'middle', 'end'可选
        """
        if schema:
            _schema = [{"dim": i, "name": v} for i, v in enumerate(schema)]
            self._option.update(parallelAxis=_schema)
        if c_schema:
            self._option.update(parallelAxis=c_schema)
        return self

    def config(self, schema=None, c_schema=None):
        """The old alias name for set_schema.
        """
        deprecated_tpl = "The {} is deprecated, please use {} instead!"
        warnings.warn(
            deprecated_tpl.format("config", "set_schema"), DeprecationWarning
        )
        return self.set_schema(schema=schema, c_schema=c_schema)

    def __add(self, name, data, **kwargs):
        """

        :param name:
            系列名称，用于 tooltip 的显示，legend 的图例筛选。
        :param data:
            数据项。数据中，每一行是一个『数据项』，每一列属于一个『维度』。
        :param kwargs:
        """
        chart = self._get_all_options(**kwargs)
        self._option.update(
            parallel={
                "left": "5%",
                "right": "13%",
                "bottom": "10%",
                "top": "20%",
            }
        )
        self._option.get("legend")[0].get("data").append(name)

        self._option.get("series").append(
            {
                "type": "parallel",
                "coordinateSystem": "parallel",
                "lineStyle": chart["line_style"],
                "name": name,
                "data": data,
            }
        )
        self._config_components(**kwargs)
