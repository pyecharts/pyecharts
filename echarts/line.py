from echarts.base import Base

class Line(Base):

    def __init__(self, title="", subtitle="", *, width=800, height=440):
        super().__init__(title, subtitle, width=width, height=height)
        self._option.update(
            series=[]
        )
        self._option.update(
            legend={"data":[]}
        )

    def add(self, name, x_axis, value, *, xaxis_name="", yaxis_name="",
            xaxis_name_pos="middle", yaxis_name_pos="middle", interval="auto",
            label_show=False, label_pos="top", label_text_size=12,
            label_text_color="#000", label_color=None):

        if isinstance(x_axis, list) and isinstance(value, list):
            assert len(x_axis) == len(value)
            if label_pos not in ("top", "left", "right", "bottom", "inside"):
                label_pos = "top"
            if xaxis_name_pos not in("start", "middle", "end"):
                xaxis_name_pos = "middle"
            if yaxis_name_pos not in("start", "middle", "end"):
                yaxis_name_pos = "middle"
            self._option.update(
                xAxis={"data": x_axis, "name": xaxis_name, "nameLocation": xaxis_name_pos,
                       "nameGap":25, "nameTextStyle":{"fontSize":14},
                       "axisLabel": {"interval": interval}}
            )
            self._option.update(
                yAxis={"name": yaxis_name, "nameLocation": yaxis_name_pos, "nameGap":25,
                       "nameTextStyle": {"fontSize":14}}
            )
            self._option.get('legend').get('data').append(name)
            self._option.get('series').append({
                "name":name, "smooth":True, "type":"line", "data":value,
                "label": {"normal":{"show":label_show, "position":label_pos,
                                    "textStyle":{"color":label_text_color,
                                                 "fontSize":label_text_size}}}
            })
            if label_color is not None:
                for color in reversed(list(label_color)):
                    self._colorlst.insert(0, color)
                self._option.update(
                    color=self._colorlst
                )
        else:
            raise ValueError

    def config(self):
        pass


attr = ["衬衫", "羊毛衫", "雪纺衫", "裤子", "高跟鞋", "袜子"]
value_A = [5, 20, 36, 10, 10, 100]
value_B = [55, 60, 16, 14, 15, 80]

if __name__ == "__main__":
    line = Line("岗位地点分布折线图", "")
    line.add("商家A", attr, value_A, label_show=True)
    line.add("商家B", attr, value_B, label_show=True)
    line.show_config()
    line.render()
