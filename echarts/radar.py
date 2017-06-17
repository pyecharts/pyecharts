from echarts.base import Base
from echarts.option import Option

class Radar(Base):

    def __init__(self, title="", subtitle="", **kwargs):
        super().__init__(title, subtitle, **kwargs)

    def config(self, indicator, **kwargs):
        indilst = [{"name": row[0], "max": row[1]} for row in indicator]
        self._option.update(radar={"indicator": indilst,
                                   "shape": kwargs.get("shape", ""),
                                   "name": {"textStyle": {"color": "#000"}},
                                   "splitLine": Option.split_line(**kwargs),
                                   "splitArea": Option.split_area(**kwargs),
                                   "axisLine": Option.axis_line(**kwargs)})

    def add(self, name, value, **kwargs):
        self._option.get('legend').get('data').append(name)
        self._option.get('series').append({
            "name": name,
            "type": "radar",
            "data": value,
            "symbol": None,
            "lineStyle": Option.line_style(**kwargs),
            "areaStyle": {"normal": {"opacity": kwargs.get('area_opacity', 0)}}
        })
        self._option.update(color=Option.color(self._colorlst, **kwargs))


r = [("销售", 6500),
     ("管理", 16000),
     ("信息技术", 30000),
     ("客服", 38000),
     ("研发", 52000),
     ("市场", 25000)]

v1 = [[4300, 10000, 28000, 35000, 50000, 19000]]
v2 = [[5000, 14000, 28000, 31000, 42000, 21000]]

if __name__ == "__main__":
    radar = Radar()
    radar.config(r, split_area_show=True)
    radar.add("预算分配", v1, label_color=["#000"])
    radar.add("实际开销", v2, label_color=["#4e79a7"])
    radar.render()
    radar.show_config()