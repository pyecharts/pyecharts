# coding=utf-8
import warnings

from pyecharts.chart import Chart


class Radar(Chart):
    """
    <<< 雷达图 >>>

    雷达图主要用于表现多变量的数据。
    """

    def __init__(self, title="", subtitle="", **kwargs):
        super(Radar, self).__init__(title, subtitle, **kwargs)

    def set_radar_component(
        self,
        schema=None,
        c_schema=None,
        shape="",
        radar_text_color="#333",
        radar_text_size=12,
        **kwargs
    ):
        """ config rader component options

        :param schema:
            默认雷达图的指示器，用来指定雷达图中的多个维度，会对数据处理成。
            {name:xx, value:xx} 的字典
        :param c_schema:
            用户自定义雷达图的指示器，用来指定雷达图中的多个维度
                name: 指示器名称
                min: 指示器最小值
                max: 指示器最大值
        :param shape:
            雷达图绘制类型，有'polygon'（多边形）和'circle'可选。
        :param radar_text_color:
            雷达图数据项字体颜色，默认为'#000'。
        :param radar_text_size:
            雷达图m数据项字体大小，默认为 12。
        :param kwargs:
        """
        chart = self._get_all_options(**kwargs)
        indicator = []
        if schema:
            for s in schema:
                _name, _max = s
                indicator.append({"name": _name, "max": _max})
        if c_schema:
            indicator = c_schema
        self._option.update(
            radar={
                "indicator": indicator,
                "shape": shape,
                "name": {
                    "textStyle": {
                        "color": radar_text_color,
                        "fontSize": radar_text_size,
                    }
                },
                "splitLine": chart["split_line"],
                "splitArea": chart["split_area"],
                "axisLine": chart["axis_line"],
            }
        )
        return self

    def config(
        self,
        schema=None,
        c_schema=None,
        shape="",
        radar_text_color="#333",
        radar_text_size=12,
        **kwargs
    ):
        """The old alias for set_schema.
        """
        deprecated_tpl = "The {} is deprecated, please use {} instead!"
        warnings.warn(
            deprecated_tpl.format("config", "set_schema"), DeprecationWarning
        )
        return self.set_radar_component(
            schema=schema,
            c_schema=c_schema,
            shape=shape,
            radar_text_color=radar_text_color,
            radar_text_size=radar_text_size,
            **kwargs
        )

    def add(self, *args, **kwargs):
        self.__add(*args, **kwargs)
        return self

    def __add(self, name, value, item_color=None, **kwargs):
        """

        :param name:
            系列名称，用于 tooltip 的显示，legend 的图例筛选
        :param value:
            数据项。数据中，每一行是一个『数据项』，每一列属于一个『维度』
        :param item_color:
            指定单图例颜色
        :param kwargs:
        """
        kwargs.update(flag=True, type="radar")
        chart = self._get_all_options(**kwargs)
        self._option.get("legend")[0].get("data").append(name)

        self._option.get("series").append(
            {
                "type": "radar",
                "name": name,
                "data": value,
                "symbol": chart["symbol"],
                "label": chart["label"],
                "itemStyle": {"normal": {"color": item_color}},
                "lineStyle": chart["line_style"],
                "areaStyle": chart["area_style"],
            }
        )
        self._config_components(**kwargs)
