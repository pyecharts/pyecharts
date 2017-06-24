from echarts.base import Base

class Map(Base):

    def __init__(self, title="", subtitle="", **kwargs):
        super().__init__(title, subtitle, **kwargs)

    def add(self, *args, **kwargs):
        self._add(*args, **kwargs)

    def _add(self, name, attr, value, *,
             is_roam=True, maptype='china', **kwargs):
        if isinstance(attr, list) and isinstance(value, list):
            assert len(attr) == len(value)
            _data = []
            for data in zip(attr, value):
                _name, _value = data
                _data.append({"name": _name, "value": _value})
            self._option.get('legend').get('data').append(name)
            self._option.get('series').append({
                "type": "map",
                "name": name,
                "symbol": self.Option.symbol(**kwargs),
                "mapType": maptype,
                "data": _data,
                "roam": is_roam
            })
            self._option.update(visualMap=self.Option.visual_map(**kwargs))
            self._option.get('legend').update(self.Option.legend(**kwargs))
            self._option.update(color=self.Option.color(self._colorlst, **kwargs))

if __name__ == "__main__":
    value = [20, 190]
    attr = ['福州市', '厦门市']
    map = Map(width=1200, height=600)
    map.add("地图", attr, value, maptype='广东')
    map.show_config()
    map.render()