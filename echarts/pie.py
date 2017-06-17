from echarts.base import Base
import random

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
            if rose_type is True: rose_type = "radius"
            fmat = {"series_name": "{a} ", "data_name": "{b} ", "data_value": "{c} ", "percent": "{d}% "}
            fmat_result = [fmat.get(f) for f in kwargs.get('formatter', ("data_name", "percent"))]
            kwargs.update(formatter="".join(fmat_result))
            self._option.get('legend').get('data').append(name)
            self._option.get('series').append({
                "name": name,
                "type": "pie",
                "data": data,
                "radius": rad,
                "roseType": rose_type,
                "label": Base._label(**kwargs),
            })
            self._option.update(color=Base._color(**kwargs))
        else:
            raise ValueError

    def config(self):
        pass


# attr = ["衬衫", "羊毛衫", "雪纺衫", "裤子", "高跟鞋", "袜子"]
# value = [11, 12, 13, 10, 10, 10]

down = ["70cm", "75cm", "80cm", "85cm", "90cm", "95cm"]
down_v = [32743, 74499, 56619, 31839, 4382, 674]

if __name__ == "__main__":
    pie = Pie("异地招聘-工资范围分布", "[x, y] 包含边界值 x 和 y")
    pie.add(down, down_v, label_show=True, rand_data=True, rad=[30,70])
    pie.show_config()
    pie.render()