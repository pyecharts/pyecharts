from echarts.base import Base
from echarts.option import get_all_options

class Bar(Base):
    """
    <<< 柱状/条形图 >>>
    柱状/条形图 通过 柱形的高度/条形的宽度 来表现数据的大小。
    """

    def __init__(self, title="", subtitle="", **kwargs):
        super().__init__(title, subtitle, **kwargs)

    def add(self, *args, **kwargs):
        self.__add(*args, **kwargs)

    def __add(self, name, x_axis, y_axis, *,
              is_stack=False, **kwargs):
        """

        :param name:
            图例名称
        :param x_axis:
            x 坐标轴数据
        :param y_axis:
            y 坐标轴数据
        :param is_stack:
            数据堆叠，同个类目轴上系列配置相同的 stack 值可以堆叠放置
        :param kwargs:
        """
        if isinstance(x_axis, list) and isinstance(y_axis, list):
            assert len(x_axis) == len(y_axis)
            kwargs.update(x_axis=x_axis)
            chart = get_all_options(**kwargs)
            is_stack = "stack" if is_stack else ""
            xaxis, yaxis = chart['xy_axis']
            self._option.update(xAxis=xaxis, yAxis=yaxis)
            self._option.get('legend').get('data').append(name)
            self._option.get('series').append({
                "type": "bar",
                "name": name,
                "data": y_axis,
                "stack": is_stack,
                "label": chart['label'],
                "markPoint": chart['mark_point'],
                "markLine": chart['mark_line']
            })
            self._legend_visualmap_colorlst(**kwargs)
        else:
            raise TypeError("x_axis and y_axis must be list")
