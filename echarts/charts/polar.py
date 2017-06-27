from echarts.base import Base

class Polar(Base):

    def __init__(self, title="", subtitle="", **kwargs):
        super().__init__(title, subtitle, **kwargs)

    def add(self, *args, **kwargs):
        self.__add(*args, **kwargs)

    def __add(self, name, data, *,
              angle_data=None,
              radius_data=None,
              type='line',
              symbol_size=4,
              start_angle=90,
              rotate_step=0,
              boundary_gap=True,
              is_axisline_show=False,
              is_splitline_show=True,
              clockwise=True, **kwargs):
        polar_type = 'value' if type == "line" else "category"
        self._option.get('legend').get('data').append(name)
        self._option.get('series').append({
            "type": type,
            "name": name,
            "coordinateSystem": 'polar',
            "symbol": self.Option.symbol(type, **kwargs),
            "symbolSize": symbol_size,
            "data": data,
            "label": self.Option.label(**kwargs),
        })
        self._option.update(
            angleAxis={
                "type": polar_type,
                "data": angle_data,
                "clockwise": clockwise,
                "startAngle": start_angle,
                "boundaryGap": boundary_gap,
                "splitLine": {"show": is_splitline_show,
                              "lineStyle": self.Option.line_style(**kwargs)},
                "axisLine": {"show": is_axisline_show}
            }
        )
        self._option.update(
            radiusAxis={
                "type": polar_type,
                "data": radius_data,
                "axisLine": {"show": is_axisline_show},
                "axisLabel": {"rotate": rotate_step}
            }
        )
        self._option.update(polar={})
        self._legend_visualmap_colorlst(**kwargs)

if __name__ == "__main__":
    import math
    data = []
    for i in range(101):
        theta = i / 100 * 360
        r = 5 * (1 + math.sin(theta / 180 * math.pi))
        data.append([r, theta, i])
    hour = [i for i in range(1, 25)]

    polar = Polar(width=1200, height=600)
    polar.add("For my honey", data, angle_data=hour, boundary_gap=False, start_angle=0)
    polar.show_config()
    polar.render()