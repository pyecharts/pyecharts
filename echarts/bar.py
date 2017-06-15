from echarts.base import Base

class Bar(Base):

    def __init__(self, title="", subtitle="", **kwargs):
        super().__init__(title, subtitle, **kwargs)
        self._option.update(series={"type":"bar"})

    def add(self, x_axis, value, **kwargs):
        if isinstance(x_axis, list) and isinstance(value, list):
            assert len(x_axis) == len(value)
            kwargs.update(x_axis=x_axis)
            xaxis, yaxis = Base._xy_axis(**kwargs)
            # dimensions
            self._option.update(xAxis=xaxis, yAxis=yaxis)
            self._option.get("series").update(data=value, label=Base._label(**kwargs))
            self._option.update(color=Base._color(**kwargs))
        else:
            raise ValueError

    def config(self):
        pass


attr = ["衬衫", "羊毛衫", "雪纺衫", "裤子", "高跟鞋", "袜子"]
v = [5, 20, 36, 10, 10, 100]

if __name__ == "__main__":
    bar = Bar()
    bar.add(attr, v, label_show=True)
    bar.show_config()
    bar.render()
