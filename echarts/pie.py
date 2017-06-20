import random
from echarts.base import Base

class Pie(Base):

    def __init__(self, title="", subtitle="", **kwargs):
        super().__init__(title, subtitle, **kwargs)

    def add(self, *args, **kwargs):
        self._add(*args, **kwargs)

    def _add(self, name, attr, value, *,
            radius=None, center=None, rose_type=False, rand_data=False, **kwargs):
        if isinstance(attr, list) and isinstance(value, list):
            assert len(attr) == len(value)
            data = [{"name":z[0], "value":z[1]} for z in zip(attr, value)]
            if rand_data:
                random.shuffle(data)
            rad = ["0%", "75%"] if radius is None else ["{}%".format(radius[0]), "{}%".format(radius[1])]
            center = ['50%', '50%'] if center is None else ["{}%".format(center[0]), "{}%".format(center[1])]
            if rose_type:
                rose_type = "radius"
            fmat = {"series_name": "{a} ",
                    "data_name": "{b} ",
                    "data_value": "{c} ",
                    "percent": "{d}% "}
            fmat_result = [fmat.get(f) for f in kwargs.get('formatter', ("data_name", "percent"))]
            kwargs.update(formatter="".join(fmat_result))
            for a in attr:
                self._option.get('legend').get('data').append(a)
            self._option.get('series').append({
                "name": name,
                "type": "pie",
                "data": data,
                "radius": rad,
                "center": center,
                "roseType": rose_type,
                "label": self.Option.label(**kwargs),
            })
            self._option.get('legend').update(self.Option.legend(**kwargs))
            self._option.update(color=self.Option.color(self._colorlst, **kwargs))
        else:
            raise ValueError

    def config(self):
        pass


attr = ["衬衫", "羊毛衫", "雪纺衫", "裤子", "高跟鞋", "袜子"]
v1 = [11, 12, 13, 10, 10, 10]
v2 = [10, 10, 11, 12, 20, 18]

if __name__ == "__main__":
    pie = Pie()
    pie.add("商品A", attr, v1, center=[25, 50], rand_data=True, rad=[30, 70], rose_type=True, label_show=False)
    pie.add("商品B", attr, v2, center=[75, 50], label_show=True, rand_data=True, rad=[30, 70])
    pie.show_config()
    pie.render()