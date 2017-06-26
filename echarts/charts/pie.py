from echarts.base import Base

class Pie(Base):

    def __init__(self, title="", subtitle="", **kwargs):
        super().__init__(title, subtitle, **kwargs)

    def add(self, *args, **kwargs):
        self.__add(*args, **kwargs)

    def __add(self, name, attr, value, *,
              radius=None,
              center=None,
              rosetype="radius", **kwargs):
        if isinstance(attr, list) and isinstance(value, list):
            assert len(attr) == len(value)
            _data = []
            for data in zip(attr, value):
                _name, _value = data
                _data.append({"name": _name, "value": _value})
            _rmin, _rmax = "0%", "75%"
            if radius is not None:
                if len(radius) == 2:
                    _rmin, _rmax = ["{}%".format(r) for r in radius]
            _cmin, _cmax = "50%", "50%"
            if center is not None:
                if len(center) == 2:
                    _cmin, _cmax = ["{}%".format(c) for c in center]
            if rosetype not in ("radius", "area"):
                rosetype = "radius"
            for a in attr:
                self._option.get('legend').get('data').append(a)
            self._option.get('series').append({
                "type": "pie",
                "name": name,
                "data": _data,
                "radius": [_rmin, _rmax],
                "center": [_cmin, _cmax],
                "roseType": rosetype,
                "label": self.Option.label("pie", **kwargs),
            })
            self._option.get('legend').update(self.Option.legend(**kwargs))
            self._option.update(color=self.Option.color(self._colorlst, **kwargs))
        else:
            raise TypeError("attr and value must be list")


attr = ["衬衫", "羊毛衫", "雪纺衫", "裤子", "高跟鞋", "袜子"]
v1 = [11, 12, 13, 10, 10, 10]
v2 = [19, 21, 32, 20, 20, 33]

if __name__ == "__main__":
    pie = Pie()
    pie.add("商品A", attr, v1, center=[25, 50], is_random=True, radius=[30, 75], rosetype=True, is_label_show=True)
    pie.add("商品B", attr, v2, center=[75, 50], is_random=True, radius=[30, 75], rosetype=True)
    pie.show_config()
    pie.render()