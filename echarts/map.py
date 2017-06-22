from echarts.base import Base

class Map(Base):

    def __init__(self, title="", subtitle="", **kwargs):
        super().__init__(title, subtitle, **kwargs)

    def add(self, *args, **kwargs):
        self._add(*args, **kwargs)

    def _add(self,
             name, attr, value, isroam=True, maptype='china', **kwargs):
        if isinstance(attr, list) and isinstance(value, list):
            assert len(attr) == len(value)
            data = [{"name": z[0], "value": z[1]} for z in zip(attr, value)]
            self._option.get('series').append({
                "name": name,
                "type": "map",
                "mapType": maptype,
                "data": data,
                "roam": isroam
            })
            self._option.get('visualMap').update(self.Option.visual_map(**kwargs))
            self._option.get('legend').update(self.Option.legend(**kwargs))
            self._option.update(color=self.Option.color(self._colorlst, **kwargs))

if __name__ == "__main__":
    value = [20, 190]
    attr = ['汕头市', '肇庆市']
    map = Map(width=1200, height=600)
    map.add("地图", attr, value, maptype='广东')
    map.show_config()
    map.render()