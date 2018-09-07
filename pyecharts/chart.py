# coding=utf-8

import random

import pyecharts.constants as constants
from pyecharts.base import Base
from pyecharts.echarts.option import get_base_options


class Chart(Base):
    """
    `Chart`类是所有非自定义类的基类，继承自 `Base` 类
    """

    def __init__(
        self,
        title,
        subtitle,
        width=800,
        height=400,
        title_pos="auto",
        title_top="auto",
        title_color=None,
        subtitle_color=None,
        title_text_size=18,
        subtitle_text_size=12,
        background_color=None,
        page_title=constants.PAGE_TITLE,
        renderer=constants.CANVAS_RENDERER,
        extra_html_text_label=None,
        is_animation=True,
    ):
        """

        :param title:
            主标题文本，支持 \n 换行，默认为 ""
        :param subtitle:
            副标题文本，支持 \n 换行，默认为 ""
        :param width:
            画布宽度，默认为 800（px）
        :param height:
            画布高度，默认为 400（px）
        :param title_pos:
            标题距离左侧距离，默认为'left'，有'auto', 'left', 'right',
            'center'可选，也可为百分比或整数
        :param title_top:
            标题距离顶部距离，默认为'top'，有'top', 'middle', 'bottom'可选，
            也可为百分比或整数
        :param title_color:
            主标题文本颜色，默认为 '#000'
        :param subtitle_color:
            副标题文本颜色，默认为 '#aaa'
        :param title_text_size:
            主标题文本字体大小，默认为 18
        :param subtitle_text_size:
            副标题文本字体大小，默认为 12
        :param background_color:
            画布背景颜色，默认为 '#fff'
        :param page_title:
            指定生成的 html 文件中 <title> 标签的值。默认为 'Echarts'
        :param renderer:
            指定使用渲染方式，有 'svg' 和 'canvas' 可选，默认为 'canvas'。
            3D 图仅能使用 'canvas'。
        :param extra_html_text_label:
            额外的 HTML 文本标签，(<p> 标签)。类型为 list，list[0] 为文本内容，
            list[1] 为字体风格样式（选填）。如 ["this is a p label", "color:red"]
        :param is_animation:
            是否开启动画，默认为 True。V0.5.9+
        """
        super(Chart, self).__init__(
            width=width,
            height=height,
            renderer=renderer,
            page_title=page_title,
            extra_html_text_label=extra_html_text_label,
            is_animation=is_animation,
        )
        self._colorlst = [
            "#c23531",
            "#2f4554",
            "#61a0a8",
            "#d48265",
            "#749f83",
            "#ca8622",
            "#bda29a",
            "#6e7074",
            "#546570",
            "#c4ccd3",
            "#f05b72",
            "#ef5b9c",
            "#f47920",
            "#905a3d",
            "#fab27b",
            "#2a5caa",
            "#444693",
            "#726930",
            "#b2d235",
            "#6d8346",
            "#ac6767",
            "#1d953f",
            "#6950a1",
            "#918597",
            "#f6f5ec",
        ]
        self._option.update(
            title=[
                {
                    "text": title,
                    "subtext": subtitle,
                    "left": title_pos,
                    "top": title_top,
                    "textStyle": {
                        "color": title_color,
                        "fontSize": title_text_size,
                    },
                    "subtextStyle": {
                        "color": subtitle_color,
                        "fontSize": subtitle_text_size,
                    },
                }
            ],
            toolbox={
                "show": True,
                "orient": "vertical",
                "left": "95%",
                "top": "center",
                "feature": {
                    "saveAsImage": {"show": True, "title": "save as image"},
                    "restore": {"show": True, "title": "restore"},
                    "dataView": {"show": True, "title": "data view"},
                },
            },
            series_id=random.randint(1, 9000000),
            tooltip={},
            series=[],
            legend=[{"data": []}],
            backgroundColor=background_color,
            animation=self.is_animation,
        )

    def add(
        self,
        angle_data=None,
        angle_range=None,
        angleaxis_label_interval=None,
        area_color=None,
        area_opacity=None,
        axis_range=None,
        bar_category_gap=None,
        border_color=None,
        boundary_gap=None,
        center=None,
        calendar_date_range=None,
        calendar_cell_size=None,
        coordinate_region=None,
        datazoom_type=None,
        datazoom_range=None,
        datazoom_orient=None,
        datazoom_xaxis_index=None,
        datazoom_yaxis_index=None,
        datazoom_extra_type=None,
        datazoom_extra_range=None,
        datazoom_extra_orient=None,
        datazoom_extra_xaxis_index=None,
        datazoom_extra_yaxis_index=None,
        effect_brushtype=None,
        effect_period=None,
        effect_scale=None,
        extra_data=None,
        extra_name=None,
        funnel_gap=None,
        funnel_sort=None,
        geo_emphasis_color=None,
        geo_normal_color=None,
        geo_cities_coords=None,
        geo_effect_period=None,
        geo_effect_traillength=None,
        geo_effect_color=None,
        geo_effect_symbol=None,
        geo_effect_symbolsize=None,
        graph_layout=None,
        graph_gravity=None,
        graph_edge_length=None,
        graph_repulsion=None,
        graph_edge_symbol=None,
        graph_edge_symbolsize=None,
        grid_width=None,
        grid_height=None,
        grid_top=None,
        grid_bottom=None,
        grid_left=None,
        grid_right=None,
        grid3d_width=None,
        grid3d_height=None,
        grid3d_depth=None,
        grid3d_opacity=None,
        grid3d_shading=None,
        grid3d_rotate_speed=None,
        grid3d_rotate_sensitivity=None,
        is_angleaxis_show=None,
        is_area_show=None,
        is_axisline_show=None,
        is_calculable=None,
        is_calendar_heatmap=None,
        is_clockwise=None,
        is_convert=None,
        is_datazoom_show=None,
        is_datazoom_extra_show=None,
        is_fill=None,
        is_focusnode=None,
        is_geo_effect_show=None,
        is_grid3d_rotate=None,
        is_label_show=None,
        is_label_emphasis=None,
        is_legend_show=None,
        is_liquid_animation=None,
        is_liquid_outline_show=None,
        is_more_utils=None,
        is_map_symbol_show=None,
        is_piecewise=None,
        is_radiusaxis_show=None,
        is_random=None,
        is_roam=None,
        is_rotatelabel=None,
        is_smooth=None,
        is_splitline_show=None,
        is_stack=None,
        is_step=None,
        is_symbol_show=None,
        is_toolbox_show=None,
        is_visualmap=None,
        is_xaxislabel_align=None,
        is_yaxislabel_align=None,
        is_xaxis_inverse=None,
        is_yaxis_inverse=None,
        is_xaxis_boundarygap=None,
        is_yaxis_boundarygap=None,
        is_xaxis_show=None,
        is_yaxis_show=None,
        item_color=None,
        label_color=None,
        label_pos=None,
        label_text_color=None,
        label_text_size=None,
        label_formatter=None,
        label_emphasis_textcolor=None,
        label_emphasis_textsize=None,
        label_emphasis_pos=None,
        legend_orient=None,
        legend_pos=None,
        legend_top=None,
        legend_selectedmode=None,
        legend_text_size=None,
        legend_text_color=None,
        line_curve=None,
        line_opacity=None,
        line_type=None,
        line_width=None,
        line_color=None,
        liquid_color=None,
        maptype=None,
        mark_line=None,
        mark_line_raw=None,
        mark_line_symbolsize=None,
        mark_line_valuedim=None,
        mark_line_coords=None,
        mark_point=None,
        mark_point_raw=None,
        mark_point_symbol=None,
        mark_point_symbolsize=None,
        mark_point_textcolor=None,
        mark_point_valuedim=None,
        pieces=None,
        radius_data=None,
        radius=None,
        rosetype=None,
        rotate_step=None,
        scale_range=None,
        shape=None,
        start_angle=None,
        symbol_size=None,
        symbol=None,
        sankey_node_width=None,
        sankey_node_gap=None,
        type=None,
        tooltip_trigger=None,
        tooltip_trigger_on=None,
        tooltip_axispointer_type=None,
        tooltip_formatter=None,
        tooltip_text_color=None,
        tooltip_font_size=None,
        tooltip_background_color=None,
        tooltip_border_color=None,
        tooltip_border_width=None,
        tree_layout=None,
        tree_symbol=None,
        tree_symbol_size=None,
        tree_orient=None,
        tree_top=None,
        tree_left=None,
        tree_bottom=None,
        tree_right=None,
        tree_collapse_interval=None,
        tree_label_position=None,
        tree_label_vertical_align=None,
        tree_label_align=None,
        tree_label_text_size=None,
        tree_label_rotate=None,
        tree_leaves_position=None,
        tree_leaves_vertical_align=None,
        tree_leaves_align=None,
        tree_leaves_text_size=None,
        tree_leaves_rotate=None,
        treemap_left_depth=None,
        treemap_drilldown_icon=None,
        treemap_visible_min=None,
        visual_orient=None,
        visual_range_color=None,
        visual_range_size=None,
        visual_range_text=None,
        visual_range=None,
        visual_text_color=None,
        visual_pos=None,
        visual_top=None,
        visual_type=None,
        visual_split_number=None,
        visual_dimension=None,
        word_gap=None,
        word_size_range=None,
        x_axis=None,
        xaxis_margin=None,
        xaxis_interval=None,
        xaxis_force_interval=None,
        xaxis_pos=None,
        xaxis_name_gap=None,
        xaxis_name_size=None,
        xaxis_name_pos=None,
        xaxis_name=None,
        xaxis_rotate=None,
        xaxis_min=None,
        xaxis_max=None,
        xaxis_type=None,
        xaxis_label_textsize=None,
        xaxis_label_textcolor=None,
        xaxis_line_color=None,
        xaxis_line_width=None,
        xaxis3d_name=None,
        xaxis3d_name_size=None,
        xaxis3d_name_gap=None,
        xaxis3d_min=None,
        xaxis3d_max=None,
        xaxis3d_interval=None,
        xaxis3d_margin=None,
        yaxis_margin=None,
        yaxis_interval=None,
        yaxis_force_interval=None,
        yaxis_pos=None,
        yaxis_formatter=None,
        yaxis_rotate=None,
        yaxis_min=None,
        yaxis_max=None,
        yaxis_name_gap=None,
        yaxis_name_size=None,
        yaxis_name_pos=None,
        yaxis_type=None,
        yaxis_name=None,
        yaxis_label_textsize=None,
        yaxis_label_textcolor=None,
        yaxis_line_color=None,
        yaxis_line_width=None,
        yaxis3d_name=None,
        yaxis3d_name_size=None,
        yaxis3d_name_gap=None,
        yaxis3d_min=None,
        yaxis3d_max=None,
        yaxis3d_interval=None,
        yaxis3d_margin=None,
        zaxis3d_name=None,
        zaxis3d_name_size=None,
        zaxis3d_name_gap=None,
        zaxis3d_min=None,
        zaxis3d_max=None,
        zaxis3d_margin=None,
        **kwargs
    ):
        """
        `add()` 方法只是用于提供自动参数补全
        """
        return self

    def _config_components(
        self,
        is_visualmap=False,
        is_more_utils=False,
        is_toolbox_show=True,
        **kwargs
    ):
        """
        图形组件配置项

        :param is_visualmap:
            指定是否使用 visualMap 组件
        :param is_datazoom_show:
            指定是否使用 dataZoom 组件
        :param is_more_utils:
            指定是否提供更多的实用小工具
        :param is_toolbox_show:
            指定是否显示工具箱
        :param kwargs:
        """
        if self.theme == constants.LIGHT_THEME:
            kwargs.update(colorlst=self._colorlst)
        chart = get_base_options(**kwargs)
        self._option.update(color=chart["color"])

        # legend
        self._option.get("legend")[0].update(chart["legend"])

        # tooltip
        self._option.update(tooltip=chart["tooltip"])

        # dataZoom，勿改动
        if kwargs.get("is_datazoom_show", False) is True:
            self._option.update(dataZoom=chart["datazoom"])
        if kwargs.get("is_datazoom_extra_show", False) is True:
            _dz = self._option.get("dataZoom", [])
            _dz.extend(chart["datazoom_extra"])
            self._option.update(dataZoom=_dz)

        # visualMap
        if is_visualmap:
            self._option.update(visualMap=chart["visual_map"])

        # toolbox
        if is_more_utils:
            self._option.get("toolbox").get("feature").update(
                magicType={
                    "show": True,
                    "type": ["line", "bar", "stack", "tiled"],
                    "title": {
                        "line": "折线图",
                        "bar": "柱状图",
                        "stack": "堆叠",
                        "tiled": "平铺",
                    },
                },
                dataZoom={
                    "show": True,
                    "title": {"zoom": "区域缩放", "back": "缩放还原"},
                },
            )

        if not is_toolbox_show:
            self._option.pop("toolbox", None)


class Chart3D(Chart):
    """
    `Chart3D`类是所有 3D 类图表的基类，继承自 `Chart` 类
    """

    def __init__(self, title="", subtitle="", **kwargs):
        kwargs["renderer"] = constants.CANVAS_RENDERER
        super(Chart3D, self).__init__(title, subtitle, **kwargs)
        self._js_dependencies.add("echartsgl")
        self._3d_chart_type = None  # 3d chart type, don't use it directly

    def add(self, *args, **kwargs):
        self.__chart3d_add(*args, **kwargs)

    def __chart3d_add(
        self,
        name,
        data,
        grid3d_opacity=1,
        grid3d_shading=None,
        xaxis3d_type="value",
        yaxis3d_type="value",
        zaxis3d_type="value",
        **kwargs
    ):
        """

        :param name:
            系列名称，用于 tooltip 的显示，legend 的图例筛选。
        :param data:
            数据项，数据中，每一行是一个『数据项』，每一列属于一个『维度』。
        :param grid3d_opacity:
            3D 笛卡尔坐标系组的透明度（线的透明度），默认为 1，完全不透明。
        :param grid3d_shading:
            三维柱状图中三维图形的着色效果。
            color：
                只显示颜色，不受光照等其它因素的影响。
            lambert：
                通过经典的 lambert 着色表现光照带来的明暗。
            realistic：
                真实感渲染，配合 light.ambientCubemap 和 postEffect 使用可以让
                展示的画面效果和质感有质的提升。ECharts GL 中使用了基于物理的渲
                染（PBR）来表现真实感材质。
        :param xaxis3d_type:
            空间直角 3D 图表 x 轴类型
        :param yaxis3d_type:
            空间直角 3D 图表 y 轴类型
        :param zaxis3d_type:
            空间直角 3D 图表 z 轴类型
        :param kwargs:
        """
        chart = self._get_all_options(
            xaxis3d_type=xaxis3d_type,
            yaxis3d_type=yaxis3d_type,
            zaxis3d_type=zaxis3d_type,
            **kwargs
        )

        self._option.get("legend")[0].get("data").append(name)
        self._option.update(
            xAxis3D=chart["xaxis3D"],
            yAxis3D=chart["yaxis3D"],
            zAxis3D=chart["zaxis3D"],
            grid3D=chart["grid3D"],
        )

        self._option.get("series").append(
            {
                "type": self._3d_chart_type,
                "name": name,
                "data": data,
                "label": chart["label"],
                "shading": grid3d_shading,
                "itemStyle": {"opacity": grid3d_opacity},
            }
        )
        self._config_components(**kwargs)
