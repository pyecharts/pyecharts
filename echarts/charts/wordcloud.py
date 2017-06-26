from echarts.base import Base

class WordCloud(Base):

    def __init__(self, title="", subtitle="", **kwargs):
        super().__init__(title, subtitle, **kwargs)

    def add(self, *args, **kwargs):
        self.__add(*args, **kwargs)

    def __add(self, name, attr, value, *,
              shape="circle",
              word_gap=20,
              word_size_range=None,
              rotate_step=45):
        if isinstance(attr, list) and isinstance(value, list):
            assert len(attr) == len(value)
            _data = []
            for data in zip(attr, value):
                _name, _value = data
                _data.append({
                    "name": _name,
                    "value": _value,
                    "textStyle": {
                        "normal": {"color": self.Option.gen_color()}}
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


name = ['Sam S Club', 'Macys', 'Amy Schumer', 'Jurassic World', 'Charter Communications',
        'Chick Fil A', 'Planet Fitness', 'Pitch Perfect', 'Express', 'Home', 'Johnny Depp',
        'Lena Dunham', 'Lewis Hamilton', 'KXAN', 'Mary Ellen Mark', 'Farrah Abraham',
        'Rita Ora', 'Serena Williams', 'NCAA baseball tournament', 'Point Break']
value = [10000, 6181, 4386, 4055, 2467, 2244, 1898, 1484, 1112, 965, 847, 582, 555,
         550, 462, 366, 360, 282, 273, 265]

if __name__ == "__main__":
    wordcloud = WordCloud(width=1200, height=600)
    wordcloud.add("", name, value, word_size_range=[20, 100])
    wordcloud.show_config()
    wordcloud.render()