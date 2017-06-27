from echarts.base import Base

class Line(Base):

    def __init__(self, title="", subtitle="", **kwargs):
        super().__init__(title, subtitle, **kwargs)

    def add(self, *args, **kwargs):
        self.__add(*args, **kwargs)

    def __add(self, name, x_axis, y_axis, *,
              is_symbol_show=True,
              is_smooth=False,
              is_stack=False,
              is_step=False,
              is_fill=False, **kwargs):
        """

        :param name:
            图例名称
        :param x_axis:
            x 坐标轴数据
        :param y_axis:
            y 坐标轴数据
        :param is_symbol_show:
            是否显示标记图形
        :param is_smooth:
            是否平滑曲线显示
        :param is_stack:
            数据堆叠，同个类目轴上系列配置相同的 stack 值可以堆叠放置
        :param is_step:
            是否是阶梯线图。可以设置为 true 显示成阶梯线图。
            也支持设置成 'start', 'middle', 'end' 分别配置在当前点，当前点与下个点的中间点，下个点拐弯。
        :param is_fill:
            是否填充曲线所绘制面积
        :param kwargs:
        """
        if isinstance(x_axis, list) and isinstance(y_axis, list):
            assert len(x_axis) == len(y_axis)
            kwargs.update(x_axis=x_axis)
            xaxis, yaxis = self.Option.xy_axis(**kwargs)
            is_stack = "stack" if is_stack else ""
            _area_style = {"normal": self.Option.area_style(**kwargs)} if is_fill else {}
            self._option.update(xAxis=xaxis, yAxis=yaxis)
            self._option.get('legend').get('data').append(name)
            self._option.get('series').append({
                "type": "line",
                "name": name,
                "symbol": self.Option.symbol("line", **kwargs),
                "smooth": is_smooth,
                "step": is_step,
                "stack": is_stack,
                "showSymbol": is_symbol_show,
                "data": y_axis,
                "label": self.Option.label(**kwargs),
                "lineStyle": self.Option.line_style(**kwargs),
                "areaStyle": _area_style,
                "markPoint": self.Option.mark_point(**kwargs),
                "markLine": self.Option.mark_line(**kwargs)
            })
            self._legend_visualmap_colorlst(**kwargs)
        else:
            raise TypeError("x_axis and y_axis must be list")
