from echarts.base import Base

class Map(Base):

    def __init__(self, title="", subtitle="", **kwargs):
        super().__init__(title, subtitle, **kwargs)

    def add(self, *args, **kwargs):
        self._add(*args, **kwargs)

    def _add(self, name, attr, value, maptype='china', **kwargs):
        if isinstance(attr, list) and isinstance(value, list):
            assert len(attr) == len(value)
            data = [{"name": z[0], "value": z[1]} for z in zip(attr, value)]
            self._option.get('series').append({
                "name": name,
                "type": "map",
                "mapType": maptype,
                "data": data,
            })
            self._option.get('visualMap').update(
                min=0,
                max=200,
                left="left",
                top="bottom",
                text=["高", "低"],
                calculable=True
            )
            self._option.get('legend').update(self.Option.legend(**kwargs))
            self._option.update(color=self.Option.color(self._colorlst, **kwargs))

if __name__ == "__main__":
    attr = ["广东", "福建"]
    value = [20, 190]

    map = Map()
    map.add("地图", attr, value)
    map.show_config()
    map.render()