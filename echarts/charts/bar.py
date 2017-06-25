from echarts.base import Base

class Bar(Base):

    def __init__(self, title="", subtitle="", **kwargs):
        super().__init__(title, subtitle, **kwargs)

    def add(self, *args, **kwargs):
        self.__add(*args, **kwargs)

    def __add(self, name, x_axis, y_axis, *, is_stack=False, **kwargs):
        if isinstance(x_axis, list) and isinstance(y_axis, list):
            assert len(x_axis) == len(y_axis)
            kwargs.update(x_axis=x_axis)
            is_stack = "stack" if is_stack else ""
            xaxis, yaxis = self.Option.xy_axis(**kwargs)
            self._option.update(xAxis=xaxis, yAxis=yaxis)
            self._option.get('legend').get('data').append(name)
            self._option.get('series').append({
                "type": "bar",
                "name": name,
                "data": y_axis,
                "stack": is_stack,
                "label": self.Option.label(**kwargs),
                "markPoint": self.Option.mark_point(**kwargs),
                "markLine": self.Option.mark_line(**kwargs)
            })
            self._option.get('legend').update(self.Option.legend(**kwargs))
            self._option.update(color=self.Option.color(self._colorlst, **kwargs))
        else:
            raise TypeError("x_axis and y_axis must be list")


attr = ["衬衫", "羊毛衫", "雪纺衫", "裤子", "高跟鞋", "袜子"]
v1 = [5, 20, 36, 10, 75, 90]
v2 = [10, 25, 8, 60, 20, 80]
v3 = [first + second + 35 for first, second in zip(v1, v2)]

if __name__ == "__main__":
    from echarts.charts.line import Line
    bar = Bar("TITLE", "SUBTITLE")
    bar.add("B", attr, v2, is_stack=True)
    bar.add("A", attr, v1, is_stack=True)
    line = Line()
    line.add("C", attr, v3, is_label_show=True)
    bar.custom(line.get_series())
    bar.show_config()
    bar.render()
