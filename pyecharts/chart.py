# coding=utf-8

import random

from pyecharts.option import get_all_options
from pyecharts.base import Base
import pyecharts.constants as constants


class Chart(Base):

    def __init__(self, title, subtitle,
                 width=800,
                 height=400,
                 title_pos="auto",
                 title_top="auto",
                 title_color="#000",
                 subtitle_color="#aaa",
                 title_text_size=18,
                 subtitle_text_size=12,
                 background_color="#fff",
                 page_title=constants.PAGE_TITLE,
                 jshost=None):
        """

        :param title:
            The main title text, supporting for \n for newlines.
        :param subtitle:
            Subtitle text, supporting for \n for newlines.
        :param width:
            Canvas width
        :param height:
            Canvas height
        :param title_pos:
            Distance between grid component and the left side of the container.
            title_pos value can be instant pixel value like 20,
            percentage value relative to container width like '20%',
            or a descriptive string: 'left', 'center', or 'right'.
            If the title_pos value is set to be 'left', 'center', or 'right',
            then the component will be aligned automatically based on position.
        :param title_top:
            Distance between grid component and the top side of the container.
            top value can be instant pixel value like 20,
            percentage value relative to container width like '20%',
            or a descriptive string: 'top', 'middle', or 'bottom'.
            If the left value is set to be 'top', 'middle', or 'bottom',
            then the component will be aligned automatically based on position.
        :param title_color:
            main title text color.
        :param subtitle_color:
            subtitle text color.
        :param title_text_size:
            main title font size
        :param subtitle_text_size:
            subtitle font size
        :param background_color:
            Background color of title, which is transparent by default.
            Color can be represented in RGB, for example 'rgb(128, 128, 128)'.
            RGBA can be used when you need alpha channel,
            for example 'rgba(128, 128, 128, 0.5)'.
            You may also use hexadecimal format, for example '#ccc'.
        :param page_title:
            specify html <title> value
        :param jshost:
            custom javascript host for the particular chart only
        """
        super(Chart, self).__init__(
            width=width, height=height,
            title_pos=title_pos,
            title_top=title_top,
            title_color=title_color,
            subtitle_color=subtitle_color,
            title_text_size=title_text_size,
            subtitle_text_size=subtitle_text_size,
            background_color=background_color,
            page_title=page_title,
            jshost=jshost
        )
        self._colorlst = [
            '#c23531', '#2f4554', '#61a0a8', '#d48265', '#749f83',
            '#ca8622', '#bda29a', '#6e7074', '#546570', '#c4ccd3',
            '#f05b72', '#ef5b9c', '#f47920', '#905a3d', '#fab27b',
            '#2a5caa', '#444693', '#726930', '#b2d235', '#6d8346',
            '#ac6767', '#1d953f', '#6950a1', '#918597', '#f6f5ec']
        self._option.update(
            title=[{
                "text": title,
                "subtext": subtitle,
                "left": title_pos,
                "top": title_top,
                "textStyle": {
                    "color": title_color,
                    "fontSize": title_text_size
                },
                "subtextStyle": {
                    "color": subtitle_color,
                    "fontSize": subtitle_text_size
                }
            }],
            toolbox={
                "show": True,
                "orient": "vertical",
                "left": "95%",
                "top": "center",
                "feature": {
                    "saveAsImage": {
                        "show": True,
                        "title": "下载图片"
                    },
                    "restore": {"show": True},
                    "dataView": {"show": True},
                }
            },
            series_id=random.randint(1, 9000000),
            tooltip={},
            series=[],
            legend=[{"data": []}],
            backgroundColor=background_color
        )

    def add(self, angle_data=None,
            angle_range=None,
            area_color=None,
            area_opacity=None,
            axis_range=None,
            bar_category_gap=None,
            border_color=None,
            boundary_gap=None,
            center=None,
            calendar_date_range=None,
            calendar_cell_size=None,
            datazoom_type=None,
            datazoom_range=None,
            datazoom_orient=None,
            datazoom_xaxis_index=None,
            datazoom_yaxis_index=None,
            effect_brushtype=None,
            effect_period=None,
            effect_scale=None,
            extra_data=None,
            geo_emphasis_color=None,
            geo_normal_color=None,
            geo_cities_coords=None,
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
            is_fill=None,
            is_focusnode=None,
            is_grid3d_rotate=None,
            is_label_show=None,
            is_label_emphasis=None,
            is_legend_show=None,
            is_liquid_animation=None,
            is_liquid_outline_show=None,
            is_more_utils=None,
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
            is_map_symbol_show=None,
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
            mark_line_symbolsize=None,
            mark_line_valuedim=None,
            mark_point=None,
            mark_point_symbol=None,
            mark_point_symbolsize=None,
            mark_point_textcolor=None,
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
            tooltip_tragger=None,
            tooltip_tragger_on=None,
            tooltip_axispointer_type=None,
            tooltip_formatter=None,
            tooltip_text_color=None,
            tooltip_font_size=None,
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
            zaxis3d_margin=None, **kwargs):
        """ The base class's add() is just to provide a hint option"""
        pass

    def _config_components(self, is_visualmap=False,
                           is_more_utils=False,
                           **kwargs):
        """ config components of chart

        :param is_visualmap:
            It specifies whether to use the visualMap component.
        :param is_datazoom_show:
            It specifies whether to show the dataZoom component.
        :param is_more_utils:
            It specifies whether to show more utils in toolbox component.
        :param kwargs:
        """
        kwargs.update(colorlst=self._colorlst)
        chart = get_all_options(**kwargs)
        self._option.update(color=chart['color'])

        # legend component
        self._option.get('legend')[0].update(chart['legend'])
        # tooltip component
        self._option.update(tooltip=chart['tooltip'])

        # dataZoom component
        if kwargs.get('is_datazoom_show', None) is True:
            # do not change this line anymore
            self._option.update(dataZoom=chart['datazoom'])
        # visualMap component
        if is_visualmap:
            self._option.update(visualMap=chart['visual_map'])
        # toolbox component
        if is_more_utils:
            self._option.get('toolbox').get('feature').update(
                magicType={
                    "show": True,
                    "type": ['line', 'bar', 'stack', 'tiled'],
                    "title": {
                        "line": "折线图",
                        "bar": "柱状图",
                        "stack": "堆叠",
                        "tiled": "平铺"}},
                dataZoom={
                    "show": True,
                    "title": {
                        "zoom": "区域缩放",
                        "back": "缩放还原"}}
            )
