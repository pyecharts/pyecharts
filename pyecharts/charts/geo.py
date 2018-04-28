# coding=utf-8

from pyecharts.chart import Chart
from pyecharts.datasets.coordinates import get_coordinate


class Geo(Chart):
    """
    <<< 地理坐标系 >>>

    地理坐标系组件用于地图的绘制，支持在地理坐标系上绘制散点图，线集。
    """

    def __init__(self, title="", subtitle="", **kwargs):
        super(Geo, self).__init__(title, subtitle, **kwargs)
        self._coordinates = {}

    def add_coordinate(self, name, longitude, latitude):
        """
        Add a geo coordinate for a position.
        :param name: The name of a position
        :param longitude: The longitude of coordinate.
        :param latitude: The latitude of coordinate.
        :return:
        """
        self._coordinates.update({name: [longitude, latitude]})

    def get_coordinate(self, name, raise_exception=False):
        """
        Return coordinate for the city name.
        :param name: City name or any custom name string.
        :param raise_exception: Whether to raise exception if not exist.
        :return: A list like [longitude, latitude] or None
        """
        if name in self._coordinates:
            return self._coordinates[name]

        coordinate = get_coordinate(name)
        if coordinate is None and raise_exception:
            raise ValueError('No coordinate is specified for {}'.format(name))

        return coordinate

    def add(self, *args, **kwargs):
        self.__add(*args, **kwargs)

    def __add(
        self,
        name,
        attr,
        value,
        type="scatter",
        maptype='china',
        symbol_size=12,
        border_color="#111",
        geo_normal_color="#323c48",
        geo_emphasis_color="#2a333d",
        geo_cities_coords=None,
        is_roam=True,
        **kwargs
    ):
        """

        :param name:
            系列名称，用于 tooltip 的显示，legend 的图例筛选。
        :param attr:
            属性名称。
        :param value:
            属性所对应的值。
        :param type:
            图例类型，有'scatter', 'effectscatter', 'heatmap'可选。
        :param maptype:
            地图类型。 支持 china、world、安徽、澳门、北京、重庆、福建、福建、甘肃、
            广东，广西、广州、海南、河北、黑龙江、河南、湖北、湖南、江苏、江西、吉林、
            辽宁、内蒙古、宁夏、青海、山东、上海、陕西、山西、四川、台湾、天津、香港、
            新疆、西藏、云南、浙江，以及 [363个二线城市](https://github.com/chfw/
            echarts-china-cities-js#featuring-citiesor-for-single-download]地图。
            提醒：
                在画市级地图的时候，城市名字后面的‘市’要省去了，比如，石家庄市的
                ‘市’不要提，即‘石家庄’就可以了。
        :param symbol_size:
            标记图形大小。
        :param border_color:
            地图边界颜色。
        :param geo_normal_color:
            正常状态下地图区域的颜色。
        :param geo_emphasis_color:
            高亮状态下地图区域的颜色。
        :param geo_cities_coords:
            用户自定义地区经纬度，类似如 {'阿城': [126.58, 45.32],} 这样的字典，当用
            于提供了该参数时，将会覆盖原有预存的区域坐标信息。
        :param is_roam:
            是否开启鼠标缩放和平移漫游。默认为 True。
            如果只想要开启缩放或者平移，可以设置成'scale'或者'move'。设置成 True 为都开启。
        :param kwargs:
        """
        assert len(attr) == len(value)
        kwargs.update(type="geo")
        chart = self._get_all_options(**kwargs)

        if geo_cities_coords:
            for name, coord in geo_cities_coords.items():
                self.add_coordinate(name, coord[0], coord[1])

        _data = []
        for _name, _value in zip(attr, value):
            _coordinate = self.get_coordinate(_name, raise_exception=True)
            _data_value = [_coordinate[0], _coordinate[1], _value]
            _data.append({"name": _name, "value": _data_value})
        self._option.update(
            geo={
                "map": maptype,
                "roam": is_roam,
                "label": {
                    "emphasis": {"show": True, "textStyle": {"color": "#eee"}}
                },
                "itemStyle": {
                    "normal": {
                        "areaColor": geo_normal_color,
                        "borderColor": border_color,
                    },
                    "emphasis": {"areaColor": geo_emphasis_color},
                },
            }
        )
        self._option.get('legend')[0].get('data').append(name)

        if type == "scatter":
            self._option.get('series').append(
                {
                    "type": type,
                    "name": name,
                    "coordinateSystem": 'geo',
                    "symbol": chart['symbol'],
                    "symbolSize": symbol_size,
                    "data": _data,
                    "label": chart['label'],
                }
            )

        elif type == "effectScatter":
            self._option.get('series').append(
                {
                    "type": type,
                    "name": name,
                    "coordinateSystem": 'geo',
                    "showEffectOn": "render",
                    "rippleEffect": chart['effect'],
                    "symbol": chart['symbol'],
                    "symbolSize": symbol_size,
                    "data": _data,
                    "label": chart['label'],
                }
            )

        elif type == "heatmap":
            self._option.get('series').append(
                {
                    "type": type,
                    "name": name,
                    "coordinateSystem": 'geo',
                    "data": _data,
                }
            )

        self._add_chinese_map(maptype)
        self._config_components(**kwargs)
