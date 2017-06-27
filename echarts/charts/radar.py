from echarts.base import Base

class Radar(Base):

    def __init__(self, title="", subtitle="", **kwargs):
        super().__init__(title, subtitle, **kwargs)

    def config(self, indicator, *,
               shape="",
               rader_text_color="#000", **kwargs):
        """ 配置 rader 组件选项

        :param indicator:
            雷达图的指示器，用来指定雷达图中的多个变量（维度）
        :param shape:
            雷达图绘制类型，支持 polygon（多边形） 和 circle
        :param rader_text_color:
            雷达图数据项字体颜色
        :param kwargs:
        """
        _indicator = []
        for indi in indicator:
            _name, _max = indi
            _indicator.append({"name": _name, "max": _max})
        self._option.update(
            radar={"indicator": _indicator,
                   "shape": shape,
                   "name": {"textStyle": {"color": rader_text_color}},
                   "splitLine": self.Option.split_line(**kwargs),
                   "splitArea": self.Option.split_area(**kwargs),
                   "axisLine": self.Option.axis_line(**kwargs)}
        )

    def add(self, *args, **kwargs):
        self.__add(*args, **kwargs)

    def __add(self, name, value, *, item_color=None, **kwargs):
        """

        :param name:
            图例名称
        :param value:
            数据项，[[]]类型，包含列表的列表
        :param item_color:
            指定单图例颜色
        :param kwargs:
        """
        self._option.get('legend').get('data').append(name)
        self._option.get('series').append({
            "type": "radar",
            "name": name,
            "data": value,
            "symbol": self.Option.symbol(**kwargs),
            "itemStyle": {"normal": {"color": item_color}},
            "lineStyle": self.Option.line_style(**kwargs),
            "areaStyle": {"normal": self.Option.area_style(flag=True, **kwargs)}
        })
        self._legend_visualmap_colorlst(**kwargs)
