# coding=utf-8

from ...charts.chart import Chart
from ...options import InitOpts, LineStyleOpts
from ...types import *


class Parallel(Chart):
    """
    <<< 平行坐标系 >>>

    平行坐标系是一种常用的可视化高维数据的图表。
    """

    def __init__(self, init_opts: InitOpts = InitOpts()):
        super().__init__(init_opts=init_opts)

    def set_schema(self, schema: ListTuple, c_schema=None):
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
            self.options.update(parallelAxis=_schema)
        if c_schema:
            self.options.update(parallelAxis=c_schema)
        return self

    def add(
        self,
        name: str,
        data: ListTuple,
        linestyle_opts: LineStyleOpts = LineStyleOpts(),
    ):
        self.options.update(
            parallel={"left": "5%", "right": "13%", "bottom": "10%", "top": "20%"}
        )
        self._append_legend(name)
        self.options.get("series").append(
            {
                "type": "parallel",
                "coordinateSystem": "parallel",
                "lineStyle": linestyle_opts,
                "name": name,
                "data": data,
            }
        )
