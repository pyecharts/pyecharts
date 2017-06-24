from echarts.base import Base

class Line(Base):

    def __init__(self, title="", subtitle="", **kwargs):
        super().__init__(title, subtitle, **kwargs)

    def add(self, *args, **kwargs):
        self._add(*args, **kwargs)

    def _add(self, name, x_axis, y_axis, *,
             is_symbol_show=True, is_smooth=False, is_stack=False, is_step=False, is_fill=False, **kwargs):
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
                "symbol": self.Option.symbol(**kwargs),
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
            self._option.get('legend').update(self.Option.legend(**kwargs))
            self._option.update(color=self.Option.color(self._colorlst, **kwargs))
        else:
            raise TypeError("x_axis and y_axis must be list")


attr = ["衬衫", "羊毛衫", "雪纺衫", "裤子", "高跟鞋", "袜子"]
value_A = [5, 20, 36, 10, 10, 100]
value_B = [55, 60, 16, 20, 15, 80]

if __name__ == "__main__":
    line = Line()
    line.add("商家A", attr, value_A, is_symbol_show=False, is_smooth=True, is_fill=True, area_opacity=0.2)
    line.add("商家B", attr, value_B, is_symbol_show=False, is_smooth=True, is_fill=True, area_opacity=0.2)
    line.show_config()
    line.render()
