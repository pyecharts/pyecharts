from echarts.base import Base

class Funnel(Base):

    def __init__(self, title="", subtitle="", **kwargs):
        super().__init__(title, subtitle, **kwargs)

    def add(self, *args, **kwargs):
        self.__add(*args, **kwargs)

    def __add(self, name, attr, value, **kwargs):
        if isinstance(attr, list) and isinstance(value, list):
            assert len(attr) == len(value)
            _data = []
            for data in zip(attr, value):
                _name, _value = data
                _data.append({"name": _name, "value": _value})
            for a in attr:
                self._option.get('legend').get('data').append(a)
            self._option.get('series').append({
                "type": "funnel",
                "name": name,
                "data": _data,
                "label": self.Option.label(**kwargs),
            })
            self._legend_visualmap_colorlst(**kwargs)
        else:
            raise TypeError("attr and value must be list")

if __name__ == "__main__":
    attr = ["衬衫", "羊毛衫", "雪纺衫", "裤子", "高跟鞋", "袜子"]
    value = [20, 40, 60, 80, 100, 120]

    funnel = Funnel()
    funnel.add("商品", attr, value, is_label_show=True, label_pos="inside", label_text_color="#fff")
    funnel.show_config()
    funnel.render()