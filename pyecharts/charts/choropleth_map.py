# coding=utf-8
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
        等值区域图必用 piece wise 的 visual map，并且 visual_range_color 不起作用。
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
        __classes__ = list(set(value))
        __class_indices__ = []
        for __item__ in value:
            # exchange text value with unique internal index
            __index__ = __classes__.index(__item__)
            __class_indices__.append(__index__)

        __piece_specs__ = []
        __piece_colors__ = []
        for __label__ in choropleth_legend:
            # associate label and color with the
            # unique internal index
            __index__ = __classes__.index(__label__['tag'])
            __piece_specs__.append({
                "min": __index__,
                "max": __index__ + 0.1,
                "label": __label__['label']
            })
            __piece_colors__.append(__label__['color'])

        # dictate the arguments for Map.add()
        kwargs['is_piecewise'] = True
        kwargs['is_visualmap'] = True
        kwargs['visual_range_color'] = __piece_colors__
        if 'visual_range_text' not in kwargs:
            kwargs['visual_range_text'] = ['Legend']
        if 'visual_text_color' not in kwargs:
            kwargs['visual_text_color'] = ['black']

        Map.add(self, name, attr, __class_indices__,
                maptype=maptype,
                is_roam=is_roam,
                is_map_symbol_show=is_map_symbol_show,
                name_map=name_map,
                pieces=__piece_specs__,
                **kwargs)
