import random
from echarts.base import Base

class Pie(Base):

    def __init__(self, title="", subtitle="", **kwargs):
        super().__init__(title, subtitle, **kwargs)

    def add(self, name, value, *, rad=None, rose_type=False, rand_data=False, **kwargs):
        if isinstance(name, list) and isinstance(value, list):
            assert len(name) == len(value)
            data = [{"name":z[0], "value":z[1]} for z in zip(name, value)]
            if rand_data:
                random.shuffle(data)
            rad = ["0%", "75%"] if rad is None else ["{}%".format(rad[0]), "{}%".format(rad[1])]
            if rose_type:
                rose_type = "radius"
            fmat = {"series_name": "{a} ",
                    "data_name": "{b} ",
                    "data_value": "{c} ",
                    "percent": "{d}% "}
            fmat_result = [fmat.get(f) for f in kwargs.get('formatter', ("data_name", "percent"))]
            kwargs.update(formatter="".join(fmat_result))
            self._option.get('legend').get('data').append(name)
            self._option.get('series').append({
                "name": name,
                "type": "pie",
                "data": data,
                "radius": rad,
                "roseType": rose_type,
                "label": self.Parms.label(**kwargs),
            })
            self._option.get('tooltip').update(formatter='{b0}: {c0}')
            self._option.get('legend').update(self.Parms.legend(**kwargs))
            self._option.update(color=self.Parms.color(self._colorlst, **kwargs))
        else:
            raise ValueError

    def config(self):
        pass


attr = ["衬衫", "羊毛衫", "雪纺衫", "裤子", "高跟鞋", "袜子"]
value = [11, 12, 13, 10, 10, 10]

if __name__ == "__main__":
    pie = Pie()
    pie.add(attr, value, label_show=True, rand_data=True, rad=[30, 70], rose_type=True)
    pie.show_config()
    pie.render()