#coding=utf-8
from pyecharts.charts.map import Map


class ChoroplethMap(Map):
    """
    等值区域图
    """
    def add(self, name, attr, value, choropleth_legend,
            maptype='china',
            is_roam=True,
            is_map_symbol_show=False,
            name_map=None,
            **kwargs):
        """
        等值区域图必用 piece wise 的 visual map。没有商量。
        而且 visual_range_text 默认是 ['Legend']，
        visual_text_color 默认是 ['black'], 不过用户可以改。

        :param name:
            系列名称，用于 tooltip 的显示，legend 的图例筛选。
        :param attr:
            属性名称。
        :param value:
            属性所对应的值。
        :param choropleth_legend:
            等值区域图的系列名称
        :param maptype:
            地图类型。与 map 一致，不在重复解释。
        :param is_roam:
            是否开启鼠标缩放和平移漫游。默认为 True
            如果只想要开启缩放或者平移，可以设置成'scale'或者'move'。设置成 True 为都开启。
        :param is_map_symbol_show:
            是否显示地图标记红点，默认为 True。
        :param name_map:
            用自定义的地图名称。默认为 None，也就是用地图自带地名。
        :param kwargs:

        """
        all_unique_values = list(set(value))
        new_values = []
        for item in value:
            index = all_unique_values.index(item)
            new_values.append(index)
        pieces = []
        for key, value in choropleth_legend.items():
            index = all_unique_values.index(key)
            pieces.append({
                "min": index,
                "max": index + 0.1,
                "label": value
            })
        kwargs['is_piecewise'] = True
        kwargs['is_visualmap'] = True
        if 'visual_range_text' not in kwargs:
            kwargs['visual_range_text'] = ['Legend']
        if 'visual_text_color' not in kwargs:
            kwargs['visual_text_color'] = ['black']
        Map.add(self, name, attr, new_values,
                maptype=maptype,
                is_roam=is_roam,
                is_map_symbol_show=is_map_symbol_show,
                name_map=name_map,
                pieces=pieces,
                **kwargs)
