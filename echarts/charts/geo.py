from echarts.base import Base

class Geo(Base):

    def __init__(self, title="", subtitle="", **kwargs):
        super().__init__(title, subtitle, **kwargs)

    def add(self, *args, **kwargs):
        self.__add(*args, **kwargs)

    def __add(self, name, attr, value, *,
              type="scatter",
              maptype='china',
              symbol_size=12,
              border_color="#111",
              geo_normal_color="#323c48",
              geo_emphasis_color="#2a333d",
              effect_brushtype="stroke",
              effect_scale=2.5,
              effect_period=4, **kwargs):
        if isinstance(attr, list) and isinstance(value, list):
            assert len(attr) == len(value)
            _data = []
            for data in zip(attr, value):
                _name, _value = data
                if _name in self._geo_cities:
                    _v = self._geo_cities.get(_name)
                    _v.append(_value)
                    _value = list(_v)
                _data.append({"name": _name, "value": _value})
            self._option.update(
                geo={
                    "map": maptype,
                    "label": {},
                    "itemStyle": {"normal": {
                        "areaColor": geo_normal_color,
                        "borderColor": border_color},
                                  "emphasis":{"areaColor": geo_emphasis_color}}
                })
            self._option.get('legend').get('data').append(name)
            if type == "scatter":
                self._option.get('series').append({
                    "type": type,
                    "name": name,
                    "coordinateSystem": 'geo',
                    "symbol": self.Option.symbol(**kwargs),
                    "symbolSize": symbol_size,
                    "data": _data,
                    "label": self.Option.label(**kwargs),
                })
            elif type == "effectscatter":
                self._option.get('series').append({
                    "type": "effectScatter",
                    "name": name,
                    "coordinateSystem": 'geo',
                    "showEffectOn": "render",
                    "rippleEffect": {
                        "brushType": effect_brushtype,
                        "scale": effect_scale,
                        "period": effect_period
                    },
                    "symbol": self.Option.symbol(**kwargs),
                    "symbolSize": symbol_size,
                    "data": _data,
                    "label": self.Option.label(**kwargs),
                })
            self._legend_visualmap_colorlst(**kwargs)

if __name__ == "__main__":
    value = [20, 190, 10]
    attr = ['福州', '厦门', '汕头']

    geo = Geo("全国主要城市空气质量", "data from pm2.5",
              title_color="#fff", title_pos="center", width=1300, height=620, background_color='#404a59')
    geo.add("", attr, value)
    geo.show_config()
    geo.render()

