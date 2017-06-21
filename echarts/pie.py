import random
from echarts.base import Base

class Pie(Base):

    def __init__(self, title="", subtitle="", **kwargs):
        super().__init__(title, subtitle, **kwargs)

    def add(self, *args, **kwargs):
        self._add(*args, **kwargs)

    def _add(self, name, attr, value, *,
            radius=None, center=None, isrosetype=False, **kwargs):
        if isinstance(attr, list) and isinstance(value, list):
            assert len(attr) == len(value)
            data = [{"name":z[0], "value":z[1]} for z in zip(attr, value)]
            rad = ["0%", "75%"] if radius is None else ["{}%".format(radius[0]), "{}%".format(radius[1])]
            cent = ['50%', '50%'] if center is None else ["{}%".format(center[0]), "{}%".format(center[1])]
            if isrosetype:
                isrosetype = "radius"
            fmat = {"series": "{a} ",
                    "name": "{b} ",
                    "value": "{c} ",
                    "percent": "{d}% "}
            fmat_result = [fmat.get(f) for f in kwargs.get('formatter', ("name", "percent"))]
            kwargs.update(formatter="".join(fmat_result))
            for a in attr:
                self._option.get('legend').get('data').append(a)
            self._option.get('series').append({
                "name": name,
                "type": "pie",
                "data": data,
                "radius": rad,
                "center": cent,
                "roseType": isrosetype,
                "label": self.Option.label(**kwargs),
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
    pie.add("商品A", attr, v1, center=[25, 50], israndom=True, radius=[30, 75], isrosetype=True)
    pie.add("商品B", attr, v2, center=[75, 50], israndom=True, radius=[30, 75], isrosetype=True)
    pie.show_config()
    pie.render()