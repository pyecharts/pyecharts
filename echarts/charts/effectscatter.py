from echarts.charts.scatter import Scatter

class EffectScatter(Scatter):

    def __init__(self, title="", subtitle="", **kwargs):
        super().__init__(title, subtitle, **kwargs)

    def add(self, *args, **kwargs):
        self.__add(*args, **kwargs)

    def __add(self, name, x_value, y_value, *, symbol_size=10,
             effect_brushtype="stroke", effect_scale=2.5, effect_period=4, **kwargs):
        if isinstance(x_value, list) and isinstance(y_value, list):
            assert len(x_value) == len(y_value)
            xaxis, yaxis = self.Option.xy_axis("scatter", **kwargs)
            self._option.update(xAxis=xaxis, yAxis=yaxis)
            self._option.get('legend').get('data').append(name)
            self._option.get('series').append({
                "type": "effectScatter",
                "name": name,
                "showEffectOn":"render",
                "rippleEffect":{
                    "brushType": effect_brushtype,
                    "scale": effect_scale,
                    "period":effect_period
                },
                "symbol": self.Option.symbol(**kwargs),
                "symbolSize": symbol_size,
                "data": [list(z) for z in zip(x_value, y_value)],
                "label": self.Option.label(**kwargs),
            })
            self._option.get('legend').update(self.Option.legend(**kwargs))
            self._option.update(color=self.Option.color(self._colorlst, **kwargs))
        else:
            raise TypeError("x_axis and y_axis must be list")


v1 = [10, 20, 30, 40, 50, 60]
v2 = [10, 20, 30, 40, 50, 60]

v3 = [25, 20, 15, 10, 5]
v4 = [25, 20, 15, 10, 5]

if __name__ == "__main__":
    effectscatter = EffectScatter()
    effectscatter.add("a",v3,v4,symbol_size=20, effect_scale=6, effect_period=10, symbol="pin")
    # effectscatter.add("a", v1, v2, symbol_size=20)
    # effectscatter.add("b", v1[::-1], v2, symbol_size=20)
    effectscatter.add("b", v3[::-1], v4, symbol_size=20, effect_scale=6, effect_period=5, symbol="pin")
    effectscatter.show_config()
    effectscatter.render()