#!/usr/bin/env python
#coding=utf-8
from __future__ import unicode_literals

import random

fs = []

def collectfuncs(func):
    fs.append(func)
    return func


@collectfuncs
def label(type=None,
          is_emphasis=True,
          is_label_show=False,
          label_pos=None,
          label_text_color="#000",
          label_text_size=12,
          formatter=None,
          **kwargs):
    """ Text label of , to explain some data information about graphic item like value, name and so on.
        In ECharts 3, to make the configuration structure flatter,
        labelis taken to be at the same level with itemStyle, and has two status normal and emphasis as itemStyle does.

    :param type:
        Chart type
    :param is_emphasis:
        It specifies whether to show laebl in emphasis status.
    :param is_label_show:
        It specifies whether to show laebl in normal status.
    :param label_pos:
        Label position.It can be 'top', 'left', 'right', 'bottom', 'inside','outside'
    :param label_text_color:
        Label text color.
    :param label_text_size:
        Label font size.
    :param formatter:
        Data label formatter,it can be 'series', 'name', 'value', 'precent' 
    :param kwargs:
    :return:
    """
    if label_pos is None:
        label_pos = "outside" if type in ["pie", "graph"] else "top"
    _label = {
        "normal": {"show": is_label_show,
                   "position": label_pos,
                   "textStyle": {"color": label_text_color,
                                 "fontSize": label_text_size}},
        "emphasis": {"show": is_emphasis}
    }
    fmat = {"series": "{a} ", "name": "{b} ", "value": "{c} ", "percent": "{d}% "}
    if formatter is None:
        _formatter = "{b} {d}%" if type == "pie" else None
    else:
        _formatter = "".join([fmat.get(f) for f in formatter if fmat.get(f, None)])
    if type != "graph":
        _label.get("normal").update(formatter=_formatter)
    return _label


@collectfuncs
def color(colorlst=None,
          is_random=False,
          label_color=None,
          **kwargs):
    """

    :param colorlst:
        Global color list
    :param is_random:
        It specifies whether to random global color list.
    :param label_color:
        color append to global color list
    :param kwargs:
    :return:
    """
    if colorlst is None:
        colorlst = []
    if label_color:
        for color in reversed(list(label_color)):
            colorlst.insert(0, color)
    if is_random:
        random.shuffle(colorlst)
    return colorlst


@collectfuncs
def line_style(line_width=1,
               line_opacity=1,
               line_curve=0,
               line_type="solid",
               **kwargs):
    """

    :param line_width:
        Line width.
    :param line_opacity:
        Opacity of the component. Supports value from 0 to 1, and the component will not be drawn when set to 0.
    :param line_curve:
        Edge curvature, which supports value from 0 to 1. The larger the value, the greater the curvature. -> Graph
    :param line_type:
        Line type,it can be 'solid', 'dashed', 'dotted'
    :param kwargs:
    :return:
    """
    _line_style = {
        "normal": {"width": line_width,
                   "opacity": line_opacity,
                   "curveness": line_curve,
                   "type": line_type}
    }
    return _line_style


@collectfuncs
def split_line(is_splitline_show=True, **kwargs):
    """

    :param is_splitline_show:
        It specifies whether to show split line.
    :param kwargs:
    :return:
    """
    _split_line = {
        "show": is_splitline_show,
        "lineStyle": line_style(**kwargs)
    }
    return _split_line


@collectfuncs
def axis_line(is_axisline_show=True, **kwargs):
    """

    :param is_axisline_show:
        It specifies whether to show axis line.
    :param kwargs:
    :return:
    """
    _axis_line = {
        "show": is_axisline_show,
        "lineStyle": line_style(**kwargs)
    }
    return _axis_line


@collectfuncs
def split_area(is_area_show=True, **kwargs):
    """

    :param is_area_show:
        It specifies whether to show split area.
    :param kwargs:
    :return:
    """
    _split_area = {
        "show": is_area_show,
        "areaStyle": area_style(**kwargs)
    }
    return _split_area


@collectfuncs
def area_style(flag=False,
               area_opacity=None,
               area_color=None,
               **kwargs):
    """

    :param flag:
        chart type flag
    :param area_opacity:
        Opacity of the component. Supports value from 0 to 1, and the component will not be drawn when set to 0.
    :param area_color:
        Fill color.
    :param kwargs:
    :return:
    """
    if area_opacity is None:
        area_opacity = 0 if flag else 1
    _area_style = {
        "opacity": area_opacity,
        "color": area_color
    }
    return _area_style


@collectfuncs
def xy_axis(type=None,
            xy_text_size=14,
            namegap=25,
            xaxis_name="",
            xaxis_name_pos="middle",
            xaxis_rotate=0,
            xaxis_min=None,
            xaxis_max=None,
            xaxis_type=None,
            interval="auto",
            yaxis_name="",
            yaxis_name_pos="middle",
            yaxis_rotate=0,
            yaxis_min=None,
            yaxis_max=None,
            yaxis_type=None,
            is_convert=False,
            x_axis=None,
            yaxis_formatter="",
            **kwargs):
    """

    :param type:
        Chart type
    :param xy_text_size:
        axis name font size
    :param namegap:
        Gap between axis name and axis line.
    :param xaxis_name:
        Name of xAxis
    :param xaxis_name_pos:
        Location of xAxis name.It can be 'start'，'middle'，'end'
    :param xaxis_rotate:
        Rotation degree of xaxis label, which is especially useful when there is no enough space for category axis.
        Rotation degree is from -90 to 90.
    :param xaxis_min:
        The minimun value of xaxis.
    :param xaxis_max:
        The maximun value of xaxis.
    :param xaxis_type:
        Type of xaxis
        'value' Numerical axis, suitable for continuous data.
        'category' Category axis, suitable for discrete category data. Data should only be set via data for this type.
        'time' Time axis, suitable for continuous time series data. As compared to value axis,
               it has a better formatting for time and a different tick calculation method. For example,
               it decides to use month, week, day or hour for tick based on the range of span.
        'log' Log axis, suitable for log data.
    :param interval:
        The display interval of the axis scale label is valid in the category axis.
        By default, labels are displayed using labels that do not overlap the labels
        Set to 0 to force all labels to be displayed
        and label is one by one if setting as 1; If 2, it will be one label separates from each other, and so on.
    :param yaxis_name:
        Name of yAxis
    :param yaxis_name_pos:
        Location of yAxis name.It can be 'start'，'middle'，'end'
    :param yaxis_rotate:
        Rotation degree of yaxis label, which is especially useful when there is no enough space for category axis.
        Rotation degree is from -90 to 90.
    :param yaxis_min:
        The minimun value of yaxis.
    :param yaxis_max:
        The maximun value of yaxis.
    :param yaxis_type:
        Type of yaxis
        'value' Numerical axis, suitable for continuous data.
        'category' Category axis, suitable for discrete category data. Data should only be set via data for this type.
        'time' Time axis, suitable for continuous time series data. As compared to value axis,
               it has a better formatting for time and a different tick calculation method. For example,
               it decides to use month, week, day or hour for tick based on the range of span.
        'log' Log axis, suitable for log data.
    :param is_convert:
        It specifies whether to convert xAxis and yAxis.
    :param x_axis:
        xAxis data
    :param yaxis_formatter:
        Formatter of axis label, which supports string template and callback function.
        example: '{value} kg'
    :param kwargs:
    :return:
    """
    _xAxis = {
        "name": xaxis_name,
        "nameLocation": xaxis_name_pos,
        "nameGap": namegap,
        "nameTextStyle": {"fontSize": xy_text_size},
        "axisLabel": {
            "interval": interval,
            "rotate": xaxis_rotate,
        },
        "min": xaxis_min,
        "max": xaxis_max
    }
    _yAxis = {
        "name": yaxis_name,
        "nameLocation": yaxis_name_pos,
        "nameGap": namegap,
        "nameTextStyle": {"fontSize": xy_text_size},
        "axisLabel": {
            "formatter": "{value} " + yaxis_formatter,
            "rotate": yaxis_rotate,
        },
        "min": yaxis_min,
        "max": yaxis_max
    }

    if type == "scatter":
        if xaxis_type is None:
            xaxis_type = "value"
        if yaxis_type is None:
            yaxis_type = "value"
    else:       # line/bar
        if xaxis_type is None:
            xaxis_type = "category"
        if yaxis_type is None:
            yaxis_type = "value"

    if is_convert:
        xaxis_type, yaxis_type = yaxis_type, xaxis_type
        _xAxis.update(type=xaxis_type)
        _yAxis.update(data=x_axis, type=yaxis_type)
    else:
        _xAxis.update(data=x_axis, type=xaxis_type)
        _yAxis.update(type=yaxis_type)
    if type == "scatter":
        _xAxis.update(data=x_axis, type=xaxis_type)
        _yAxis.update(type=yaxis_type)
    return [_xAxis], [_yAxis]


def _mark(data,
          mark_point_symbol='pin',
          mark_point_symbolsize=50,
          mark_point_textcolor='#fff',
          _is_markline=False,
          **kwargs):
    """

    :param data:
        mark data, it can be 'min', 'max', 'average'
    :param mark_point_symbol:
        mark symbol, it cna be 'circle', 'rect', 'roundRect', 'triangle', 'diamond', 'pin', 'arrow'
    :param mark_point_symbolsize:
        mark symbol size
    :param mark_point_textcolor:
        mark point text color
    :param _is_markline:
        It specifies whether is markline or not.
    :return:
    """
    mark = {"data": []}
    if data:
        for d in list(data):
            _type, _name = "", ""
            if "max" in d:
                _type, _name = "max", "最大值"
            elif "min" in d:
                _type, _name = "min", "最小值"
            elif "average" in d:
                _type, _name = "average", "平均値"
            if _is_markline:
                _m = {
                    "type": _type,
                    "name": _name,
                }
            else:
                _m = {
                    "type": _type,
                    "name": _name,
                    "symbol": mark_point_symbol,
                    "symbolSize": mark_point_symbolsize,
                    "label": {"normal": {"textStyle": {"color": mark_point_textcolor}}}
                }
            if type:
                mark.get("data").append(_m)
    return mark


@collectfuncs
def mark_point(mark_point=None, **kwargs):
    """

    :param mark_point:
        mark point data, it can be 'min', 'max', 'average'
    :param kwargs:
    :return:
    """
    return _mark(mark_point, **kwargs)


@collectfuncs
def mark_line(mark_line=None, **kwargs):
    """

    :param mark_line:
        mark line data,it can be 'min', 'max', 'average'
    :param kwargs:
    :return:
    """
    return _mark(mark_line, _is_markline=True)


@collectfuncs
def legend(is_legend_show=True,
           legend_orient="horizontal",
           legend_pos="center",
           legend_top='top',
           legend_selectedmode='multiple',
           **kwargs):
    """ Legend component.
        Legend component shows symbol, color and name of different series.
        You can click legends to toggle displaying series in the chart.
        In ECharts 3, a single echarts instance may contain multiple legend components,
        which makes it easier for the layout of multiple legend components.
    :param is_legend_show:
        It specifies whether to show the legend component.
    :param legend_orient:
        The layout orientation of legend.It can be 'horizontal', 'vertical'
    :param legend_pos:
        Distance between legend component and the left side of the container.
        legend_pos value can be instant pixel value like 20;
        it can also be percentage value relative to container width like '20%';
        and it can also be 'left', 'center', or 'right'.
    :param legend_top:
        Distance between legend component and the top side of the container.
        legend_top value can be instant pixel value like 20;
        it can also be percentage value relative to container width like '20%';
        and it can also be 'top', 'middle', or 'bottom'.
    :param legend_selectedmode:
        State table of selected legend. 'single' or 'multiple'
    :param kwargs:
    :return:
    """
    _legend = {
        "selectedMode": legend_selectedmode,
        "show": is_legend_show,
        "left": legend_pos,
        "top": legend_top,
        "orient": legend_orient
    }
    return _legend


@collectfuncs
def visual_map(visual_type='color',
               visual_range=None,
               visual_text_color=None,
               visual_range_text=None,
               visual_range_color=None,
               visual_range_size=None,
               visual_orient='vertical',
               visual_pos="left",
               visual_top="bottom",
               is_calculable=True,
               **kwargs):
    """ visualMap is a type of component for visual encoding, which maps the data to visual channels

    :param visual_type:
        visual map type, 'color' or 'size'
        color: For visual channel color, array is used, like: ['#333', '#78ab23', 'blue'],
        which means a color ribbon is formed based on the three color stops,and dataValues will be mapped to the ribbon.
        size: For visual channel size, array is used, like: [20, 50],
        which means a size ribbon is formed based on the two value stops, and dataValues will be mapped to the ribbon.
    :param visual_range:
        pecify the min and max dataValue for the visualMap component.
    :param visual_text_color:
        visualMap text color.
    :param visual_range_text:
        The label text on both ends, such as ['High', 'Low']
    :param visual_range_size:
        For visual channel size, array is used, like: [20, 50].
    :param visual_range_color:
        For visual channel color, array is used, like: ['#333', '#78ab23', 'blue'].
    :param visual_orient:
        How to layout the visualMap component, 'horizontal' or 'vertical'.
    :param visual_pos:
        Distance between visualMap component and the left side of the container.
        visual_pos value can be instant pixel value like 20;
        it can also be percentage value relative to container width like '20%';
        and it can also be 'left', 'center', or 'right'.
    :param visual_top:
        Distance between visualMap component and the top side of the container.
        visual_top value can be instant pixel value like 20;
        it can also be percentage value relative to container width like '20%';
        and it can also be 'top', 'middle', or 'bottom'.
    :param is_calculable:
        Whether show handles, which can be dragged to adjust "selected range".
    :param kwargs:
    :return:
    """
    # defalut min and max value of visual_range is [0, 100]
    _min, _max = 0, 100
    if visual_range:
        if len(visual_range) == 2:
            _min, _max = visual_range

    # defalut label text on both ends is ['low', 'high']
    _tlow, _thigh = "low", "high"
    if visual_range_text:
        if len(visual_range_text) == 2:
            _tlow, _thigh = visual_range_text

    _inrange_op = {}
    if visual_type == 'color':
        range_color = ['#50a3ba', '#eac763', '#d94e5d']
        if visual_range_color:
            if len(visual_range_color) >= 2:
                range_color = visual_range_color
        _inrange_op.update(color=range_color)

    if visual_type == 'size':
        range_size = [20, 50]
        if visual_range_size:
            if len(visual_range_size) >= 2:
                range_size = visual_range_size
        _inrange_op.update(symbolSize=range_size)

    _visual_map = {
        "type": "continuous",
        "min": _min,
        "max": _max,
        "text": [_thigh, _tlow],
        "textStyle": {"color": visual_text_color},
        "inRange": _inrange_op,
        "calculable": is_calculable,
        "orient": visual_orient,
        "left": visual_pos,
        "top": visual_top
    }
    return _visual_map


def gen_color():
    """ random generation color -> WordCloud

    :return:
    """
    return "rgb(%s,%s,%s)" % (random.randint(0, 160),
                              random.randint(0, 160),
                              random.randint(0, 160))


@collectfuncs
def symbol(type=None, symbol="", **kwargs):
    """

    :param symbol:
        symbol type, it can be 'rect', 'roundRect', 'triangle', 'diamond', 'pin', 'arrow'.
    :param kwargs:
    :return:
    """
    if symbol is None:  # Radar
        symbol = 'none'
    elif type == "line" and symbol == "":  # Line
        symbol = "emptyCircle"
    elif symbol not in ('rect', 'roundRect', 'triangle', 'diamond', 'pin', 'arrow'):
        symbol = 'circle'
    return symbol


@collectfuncs
def effect(effect_brushtype="stroke",
           effect_scale=2.5,
           effect_period=4,
           **kwargs):
    """

    :param effect_brushtype:
        The brush type for ripples. options: 'stroke' and 'fill'.
    :param effect_scale:
        The maximum zooming scale of ripples in animation.
    :param effect_period:
        The duration of animation.
    :param kwargs:
    :return:
    """
    _effect = {
        "brushType": effect_brushtype,
        "scale": effect_scale,
        "period":effect_period
    }
    return _effect


@collectfuncs
def datazoom(is_datazoom_show=False,
             datazoom_type='slider',
             datazoom_range=None,
             datazoom_orient='horizontal',
             **kwargs):
    """

    :param is_datazoom_show:
        It specifies whether to use the datazoom component.
    :param datazoom_type:
        datazoom type, 'slider' or 'inside'
    :param datazoom_range:
        The range percentage of the window out of the data extent, in the range of 0 ~ 100.
    :param datazoom_orient:
        Specify whether the layout of dataZoom component is horizontal or vertical.'horizontal' or 'vertical'
        What's more,it indicates whether the horizontal axis or vertical axis is controlled
        by default in catesian coordinate system.
    :param kwargs:
    :return:
    """
    _min, _max = 50, 100
    if datazoom_range:
        if len(datazoom_range) == 2:
            _min, _max = datazoom_range
    if datazoom_type not in ("slider", "inside"):
        datazoom_type = "slider"
    _datazoom = {
        "show": is_datazoom_show,
        "type": datazoom_type,
        "start": _min,
        "end": _max,
        "orient": datazoom_orient
    }
    return [_datazoom]


@collectfuncs
def grid(grid_width=None,
         grid_height=None,
         grid_top=None,
         grid_bottom=None,
         grid_left=None,
         grid_right=None,
         **kwargs):
    """
    :param series:
        other chart series data
    :param grid_width:
        Width of grid component. Adaptive by default.
    :param grid_height:
        Height of grid component. Adaptive by default.
    :param grid_top:
        Distance between grid component and the top side of the container.
        grid_top value can be instant pixel value like 20;
        it can also be percentage value relative to container width like '20%';
        and it can also be 'top', 'middle', or 'bottom'.
        If the grid_top value is set to be 'top', 'middle', or 'bottom',
        then the component will be aligned automatically based on position.
    :param grid_bottom:
        Distance between grid component and the bottom side of the container.
        grid_bottom value can be instant pixel value like 20;
        it can also be percentage value relative to container width like '20%'.
    :param grid_left:
        Distance between grid component and the left side of the container.
        grid_left value can be instant pixel value like 20;
        it can also be percentage value relative to container width like '20%';
        and it can also be 'left', 'center', or 'right'.
        If the grid_left value is set to be 'left', 'center', or 'right',
        then the component will be aligned automatically based on position.
    :param grid_right:
        Distance between grid component and the right side of the container.
        grid_right value can be instant pixel value like 20;
        it can also be percentage value relative to container width like '20%'.
    :return:
    """
    _grid = {}
    if grid_width is not None:
        _grid.update(width=grid_width)
    if grid_height is not None:
        _grid.update(height=grid_height)
    if grid_top is not None:
        _grid.update(top=grid_top)
    if grid_bottom is not None:
        _grid.update(bottom=grid_bottom)
    if grid_left is not None:
        _grid.update(left=grid_left)
    if grid_right is not None:
        _grid.update(right=grid_right)
    return _grid


@collectfuncs
def grid3D(grid3D_width=100,
           grid3D_height=100,
           grid3D_depth=100,
           grid3D_rotate_speed=10,
           grid3D_rotate_sensitivity=1,
           is_grid3D_rotate=False,
           **kwargs):
    """

    :param grid3D_width:
        3D axis width
    :param grid3D_height:
        3D axis height
    :param grid3D_depth:
        3D axis depth
    :param grid3D_rotate_speed:
        3D charts rotate speed
    :param is_grid3D_rotate:
        whether rotate 3D charts
    :param grid3D_rotate_sensitivity:
        3D charts rotete sensitivity, The greater the value, the more sensitive.
    :param kwargs:
    :return:
    """
    _grid3D = {
        "boxWidth": grid3D_width,
        "boxHeight": grid3D_height,
        "boxDepth": grid3D_depth,
        "viewControl": {
            "autoRotate": is_grid3D_rotate,
            "autoRotateSpeed": grid3D_rotate_speed,
            "rotateSensitivity": grid3D_rotate_sensitivity
        }
    }
    return _grid3D


def get_all_options(**kwargs):
    """ Return all options of charts

    :param kwargs:
    :return:
    """
    _funcs = {}
    for f in fs:
        _funcs[f.__name__] = f(**kwargs)
    return _funcs
