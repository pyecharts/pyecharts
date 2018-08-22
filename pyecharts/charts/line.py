# coding=utf-8

from pyecharts.chart import Chart


class Line(Chart):
    """
    <<< 折线/面积图 >>>

    折线图是用折线将各个数据点标志连接起来的图表，用于展现数据的变化趋势。
    """

    def __init__(self, title="", subtitle="", **kwargs):
        super(Line, self).__init__(title, subtitle, **kwargs)

    def add(self, *args, **kwargs):
        self.__add(*args, **kwargs)
        return self

    def __add(
        self,
        name,
        x_axis,
        y_axis,
        is_symbol_show=True,
        symbol_size=4,
        is_smooth=False,
        is_stack=False,
        is_step=False,
        is_fill=False,
        **kwargs
    ):
        """

        :param name:
            系列名称，用于 tooltip 的显示，legend 的图例筛选。
        :param x_axis:
            x 坐标轴数据。
        :param y_axis:
            y 坐标轴数据。
        :param is_symbol_show:
            是否显示标记图形，默认为 True。
        :param is_smooth:
            是否平滑曲线显示，默认为 False。
        :param is_stack:
            数据堆叠，同个类目轴上系列配置相同的 stack 值可以堆叠放置。默认为 False。
        :param is_step:
            是否是阶梯线图。可以设置为 True 显示成阶梯线图。默认为 False。
            也支持设置成'start', 'middle', 'end'分别配置在当前点，当前点与下个
            点的中间下个点拐弯。
        :param is_fill:
            是否填充曲线所绘制面积，默认为 False。
        :param kwargs:
        """
        assert len(x_axis) == len(y_axis)
        kwargs.update(x_axis=x_axis, type="line", flag=True)
        chart = self._get_all_options(**kwargs)

        xaxis, yaxis = chart["xy_axis"]
        if is_stack:
            is_stack = "stack_" + str(self._option["series_id"])
        else:
            is_stack = ""
        self._option.update(xAxis=xaxis, yAxis=yaxis)
        self._option.get("legend")[0].get("data").append(name)
        # 合并 x 和 y 轴数据，避免当 X 轴的类型设置为 'value' 的时候，
        # X、Y 轴均显示 Y 轴数据
        _data = [list(z) for z in zip(x_axis, y_axis)]

        self._option.get("series").append(
            {
                "type": "line",
                "name": name,
                "symbol": chart["symbol"],
                "symbolSize": symbol_size,
                "smooth": is_smooth,
                "step": is_step,
                "stack": is_stack,
                "showSymbol": is_symbol_show,
                "data": _data,
                "label": chart["label"],
                "lineStyle": chart["line_style"],
                "areaStyle": chart["area_style"],
                "markPoint": chart["mark_point"],
                "markLine": chart["mark_line"],
                "seriesId": self._option.get("series_id"),
            }
        )
        self._config_components(**kwargs)
