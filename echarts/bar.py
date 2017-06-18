from echarts.base import Base

class Bar(Base):

    def __init__(self, title="", subtitle="", **kwargs):
        super().__init__(title, subtitle, **kwargs)

    def add(self, name, x_axis, y_axis, **kwargs):
        if isinstance(x_axis, list) and isinstance(y_axis, list):
            assert len(x_axis) == len(y_axis)
            kwargs.update(x_axis=x_axis)
            xaxis, yaxis = self.Parms.xy_axis(**kwargs)
            # dimensions
            self._option.update(xAxis=xaxis, yAxis=yaxis)
            self._option.get('legend').get('data').append(name)
            self._option.get('series').append({
                "name": name,
                "smooth": True,
                "type": "bar",
                "data": y_axis,
                "label": self.Parms.label(**kwargs),
                "markPoint": self.Parms.mark_point(**kwargs),
                "markLine": self.Parms.mark_line(**kwargs)
            })
            self._option.get('legend').update(orient=kwargs.get('orient', 'horizontal'))
            self._option.update(color=self.Parms.color(self._colorlst, **kwargs))
        else:
            raise ValueError

    def config(self):
        pass


attr = ["衬衫", "羊毛衫", "雪纺衫", "裤子", "高跟鞋", "袜子"]
v1 = [5, 20, 36, 10, 10, 100]
v2 = [10, 25, 8, 60, 50, 150]

if __name__ == "__main__":
    bar = Bar()
    bar.add("A", attr, v1, label_text_size=20)
    # bar.add("B", attr, v2, orient="vertical", mark_line=["average"])
    bar.show_config()
    bar.render()
