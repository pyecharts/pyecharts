from echarts.base import Base

class Funnel(Base):

    def __init__(self, title="", subtitle="", **kwargs):
        super().__init__(title, subtitle, **kwargs)

    def add(self, *args, **kwargs):
        self.__add(*args, **kwargs)

    def __add(self, name, attr, value, **kwargs):
        """

        :param name:
            图例名称
        :param attr:
            属性名称
        :param value:
            属性所对应的值
        :param kwargs:
        """
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
