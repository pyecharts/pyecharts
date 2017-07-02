from echarts.base import Base
from echarts.option import gen_color

class WordCloud(Base):
    """
    <<< 词云图 >>>
    """
    def __init__(self, title="", subtitle="", **kwargs):
        super().__init__(title, subtitle, **kwargs)

    def add(self, *args, **kwargs):
        self.__add(*args, **kwargs)

    def __add(self, name, attr, value, *,
              shape="circle",
              word_gap=20,
              word_size_range=None,
              rotate_step=45):
        """

        :param name:
            图例名称
        :param attr:
            属性名称
        :param value:
            属性所对应的值
        :param shape:
            词云图轮廓，包括
            cardioid, diamond, triangle-forward, triangle, pentagon, star
        :param word_gap:
            单词间间隔
        :param word_size_range:
            单词字体大小范围
        :param rotate_step:
            旋转单词角度，默认为 45 度
        """
        if isinstance(attr, list) and isinstance(value, list):
            assert len(attr) == len(value)
            _data = []
            for data in zip(attr, value):
                _name, _value = data
                _data.append({
                    "name": _name,
                    "value": _value,
                    "textStyle": {
                        "normal": {"color": gen_color()}}
                })
            _min, _max = 12, 60
            if word_size_range is not None:
                if len(word_size_range) == 2:
                    _min, _max = word_size_range
            _rmin, _rmax = -90, 90
            if shape in ("cardioid", "diamond", "triangle-forward", "triangle", "pentagon", "star"):
                _rmin = _rmax = 0
            else:
                shape = "circle"
            self._option.get('series').append({
                "type": "wordCloud",
                "name": name,
                "shape": shape,
                "rotationRange": [_rmin, _rmax],
                "rotationStep": rotate_step,
                "girdSize": word_gap,
                "sizeRange": [_min, _max],
                "data": _data
            })
