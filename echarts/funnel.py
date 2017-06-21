from echarts.base import Base

class Funnel(Base):

    def __init__(self, title="", subtitle="", **kwargs):
        super().__init__(title, subtitle, **kwargs)

    def add(self, *args, **kwargs):
        self._add(*args, **kwargs)

    def _add(self, name, attr, value, **kwargs):
        if isinstance(attr, list) and isinstance(value, list):
            assert len(attr) == len(value)
            data = [{"name":z[0], "value":z[1]} for z in zip(attr, value)]
            for a in attr:
                self._option.get('legend').get('data').append(a)
            self._option.get('series').append({
                "name": name,
                "type": "funnel",
                "data": data,
                "label": self.Option.label(**kwargs),
            })
            self._option.get('legend').update(self.Option.legend(**kwargs))
            self._option.update(color=self.Option.color(self._colorlst, **kwargs))
        else:
            raise TypeError("attr and value must be list")


attr = ["衬衫", "羊毛衫", "雪纺衫", "裤子", "高跟鞋", "袜子"]
value = [20, 40, 60, 80, 100, 120]

if __name__ == "__main__":

    funnel = Funnel()
    funnel.add("商品", attr, value, label_show=True, label_pos="inside", label_text_color="#fff")
    funnel.show_config()
    funnel.render()