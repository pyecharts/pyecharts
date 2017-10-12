#!/usr/bin/env python
# coding=utf-8
from __future__ import unicode_literals

import random

fs = []


def collectfuncs(func):
    fs.append(func)
    return func


@collectfuncs
def label(type=None,
          is_label_show=False,
          is_label_emphasis=True,
          label_pos=None,
          label_text_color="#000",
          label_text_size=12,
          label_formatter=None,
          label_emphasis_pos=None,
          label_emphasis_textcolor='#fff',
          label_emphasis_textsize=12,
          **kwargs):
    """ Text label of , to explain some data information about graphic item like value,
        name and so on.In ECharts 3, to make the configuration structure flatter,
        labelis taken to be at the same level with itemStyle, and has two status
        normal and emphasis as itemStyle does.

    :param type:
        Chart type
    :param is_label_emphasis:
        It specifies whether to show laebl in emphasis status.
    :param is_label_show:
        It specifies whether to show laebl in normal status.
    :param label_pos:
        Label position.It can be 'top', 'left', 'right', 'bottom', 'inside','outside'
    :param label_text_color:
        Label text color.
    :param label_text_size:
        Label font size.
    :param label_formatter:
        The template variables are {a}, {b}, {c}, {d} and {e}, which stands for series name,
        data name and data value and ect. When trigger is set to be 'axis',
        there may be data from multiple series.
        In this time, series index can be refered as {a0}, {a1}, or {a2}.
        {a}, {b}, {c}, {d} have different meanings for different series types:
        Line: (area) charts, bar (column) charts,
            K charts:
                {a} for series name, {b} for category name, {c} for data value, {d} for none;
        Scatter: (bubble) charts:
            {a} for series name, {b} for data name, {c} for data value, {d} for none;
        Map:
            {a} for series name, {b} for area name, {c} for merging data, {d} for none;
        Pie: charts, gauge charts, funnel charts: {a} for series name,
            {b} for data item name, {c} for data value, {d} for percentage.
    :param label_emphasis_pos:
        Label emphasis position.It can be 'top', 'left', 'right', 'bottom', 'inside','outside'
    :param label_emphasis_textcolor:
        Label emphasis text color.
    :param label_emphasis_textsize:
        Label emphasis font size.
    :param kwargs:
    :return:
    """
    if label_pos is None:
        label_pos = "outside" if type in ["pie", "graph"] else "top"
    _label = {
        "normal": {
            "show": is_label_show,
            "position": label_pos,
            "textStyle": {
                "color": label_text_color,
                "fontSize": label_text_size
            }},
        "emphasis": {
            "show": is_label_emphasis,
            "position": label_emphasis_pos,
            "textStyle": {
                "color": label_emphasis_textcolor,
                "fontSize": label_emphasis_textsize,
            }}
    }

    if label_formatter is None:
        if type == "pie":
            label_formatter = "{b}: {d}%"
    if type != "graph":
        _label.get("normal").update(formatter=label_formatter)
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
def line_style(type=None,
               line_width=1,
               line_opacity=1,
               line_curve=0,
               line_type="solid",
               line_color=None,
               **kwargs):
    """

    :param type:
        Chart type
    :param line_width:
        Line width.
    :param line_opacity:
        Opacity of the component.
        Supports value from 0 to 1, and the component will not be drawn when set to 0.
    :param line_curve:
        Edge curvature, which supports value from 0 to 1.
        The larger the value, the greater the curvature. -> Graph、Sankey
    :param line_type:
        Line type,it can be 'solid', 'dashed', 'dotted'
    :param line_color:
        color of line
    :param kwargs:
    :return:
    """
    if line_color is None and type == "graph":
        line_color = '#aaa'

    _line_style = {
        "normal": {
            "width": line_width,
            "opacity": line_opacity,
            "curveness": line_curve,
            "type": line_type,
            "color": line_color
        }
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
        Opacity of the component.
        Supports value from 0 to 1, and the component will not be drawn when set to 0.
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
            x_axis=None,
            xaxis_margin=8,
            xaxis_name_size=14,
            xaxis_name_gap=25,
            xaxis_name="",
            xaxis_name_pos="middle",
            xaxis_rotate=0,
            xaxis_min=None,
            xaxis_max=None,
            xaxis_type=None,
            xaxis_interval="auto",
            xaxis_force_interval=None,
            xaxis_pos=None,
            yaxis_margin=8,
            yaxis_name_size=14,
            yaxis_name_gap=25,
            yaxis_name="",
            yaxis_name_pos="middle",
            yaxis_rotate=0,
            yaxis_min=None,
            yaxis_max=None,
            yaxis_type=None,
            yaxis_interval="auto",
            yaxis_force_interval=None,
            yaxis_pos=None,
            yaxis_formatter="",
            is_convert=False,
            is_xaxis_inverse=False,
            is_yaxis_inverse=False,
            is_xaxislabel_align=False,
            is_yaxislabel_align=False,
            is_xaxis_boundarygap=True,
            is_yaxis_boundarygap=True,
            is_xaxis_show=True,
            is_yaxis_show=True,
            **kwargs):
    """
    :param type:
        Chart type
    :param x_axis:
        xAxis data
    :param xaxis_margin:
        The margin between the axis label and the xaxis line.
    :param xaxis_name_size:
        xaxis name font size
    :param xaxis_name_gap:
        Gap between axis name and xaxis line.
    :param xaxis_name:
        Name of xAxis
    :param xaxis_name_pos:
        Location of xAxis name.It can be 'start'，'middle'，'end'
    :param xaxis_rotate:
        Rotation degree of xaxis label, which is especially useful when
        there is no enough space for category axis.
        Rotation degree is from -90 to 90.
    :param xaxis_min:
        The minimun value of xaxis.
    :param xaxis_max:
        The maximun value of xaxis.
    :param xaxis_type:
        Type of xaxis
        'value':
            Numerical axis, suitable for continuous data.
        'category':
            Category axis, suitable for discrete category data.
            Data should only be set via data for this type.
        'log':
            Log axis, suitable for log data.
    :param xaxis_interval:
        The display interval of the axis scale label is valid in the category xaxis.
        By default, labels are displayed using labels that do not overlap the labels
        Set to 0 to force all labels to be displayed
        and label is one by one if setting as 1; If 2,it will be one label separates
        from each other, and so on.
    :param xaxis_force_interval:
        Compulsively set segmentation interval for xaxis.
        As splitNumber is a recommendation value, the calculated tick may not be
        the same as expected. In this case, interval should be used along with
        min and max to compulsively set tickings. But in most cases, we do not
        suggest using this, out automatic calculation is enough for most situations.
    :param xaxis_pos:
        The position of x axis.
        options: 'top' or 'bottom'
        The first x axis in grid defaults to be on the bottom of the grid, and
        the second x axis is on the other side against the first x axis.
    :param yaxis_margin:
        The margin between the axis label and the yaxis line.
    :param yaxis_name_size:
        yaxis name font size
    :param yaxis_name_gap:
        Gap between axis name and yaxis line.
    :param yaxis_name:
        Name of yAxis
    :param yaxis_name_pos:
        Location of yAxis name.It can be 'start'，'middle'，'end'
    :param yaxis_rotate:
        Rotation degree of yaxis label, which is especially useful
        when there is no enough space for category axis.
        Rotation degree is from -90 to 90.
    :param yaxis_min:
        The minimun value of yaxis.
    :param yaxis_max:
        The maximun value of yaxis.
    :param yaxis_type:
        Type of yaxis
        'value':
            Numerical axis, suitable for continuous data.
        'category':
            Category axis, suitable for discrete category data.
            Data should only be set via data for this type.
        'log':
            Log axis, suitable for log data.
    :param yaxis_interval:
        The display interval of the axis scale label is valid in the category yaxis.
        By default, labels are displayed using labels that do not overlap the labels
        Set to 0 to force all labels to be displayed
        and label is one by one if setting as 1; If 2,it will be one label separates
        from each other, and so on.
    :param yaxis_force_interval:
        Compulsively set segmentation interval for yaxis.
        As splitNumber is a recommendation value, the calculated tick may not be
        the same as expected. In this case, interval should be used along with
        min and max to compulsively set tickings. But in most cases, we do not
        suggest using this, out automatic calculation is enough for most situations.
    :param yaxis_pos:
        the position of y axis.
        options: 'left' or 'right'
        The first y axis in grid defaults to be the left ('left') of the grid, and
        the second y axis is on the other side against the first y axis.
    :param yaxis_formatter:
        Formatter of axis label, which supports string template and callback function.
        example: '{value} kg'
    :param is_convert:
        It specifies whether to convert xAxis and yAxis.
    :param is_xaxis_inverse:
        Whether xaxis is inversed
    :param is_yaxis_inverse:
        Whether yaxis is inversed
    :param is_xaxislabel_align:
        whether align xaxis tick with label
    :param is_yaxislabel_align:
        whether align yaxis tick with label
    :param is_xaxis_boundarygap:
        The boundary gap on both sides of a coordinate xAxis.
        The boundaryGap of category axis can be set to either true or false.
        Default value is set to be true, in which case axisTick is served
        only as a separation line, and labels and data appear only in
        the center part of two axis ticks, which is called band.
    :param is_yaxis_boundarygap:
        The boundary gap on both sides of a coordinate yAxis.
        The boundaryGap of category axis can be set to either true or false.
        Default value is set to be true, in which case axisTick is served
        only as a separation line, and labels and data appear only in
        the center part of two axis ticks, which is called band.
    :param is_xaxis_show:
        It specifies whether to show xAxis
    :param is_yaxis_show:
        It specifies whether to show yAxis
    :param kwargs:
    :return:
    """
    _xAxis = {
        "name": xaxis_name,
        "show": is_xaxis_show,
        "nameLocation": xaxis_name_pos,
        "nameGap": xaxis_name_gap,
        "nameTextStyle": {"fontSize": xaxis_name_size},
        "axisLabel": {
            "interval": xaxis_interval,
            "rotate": xaxis_rotate,
            "margin": xaxis_margin
        },
        "axisTick": {
            "alignWithLabel": is_xaxislabel_align
        },
        "inverse": is_xaxis_inverse,
        "position": xaxis_pos,
        "boundaryGap": is_xaxis_boundarygap,
        "min": xaxis_min,
        "max": xaxis_max
    }
    _yAxis = {
        "name": yaxis_name,
        "show": is_yaxis_show,
        "nameLocation": yaxis_name_pos,
        "nameGap": yaxis_name_gap,
        "nameTextStyle": {"fontSize": yaxis_name_size},
        "axisLabel": {
            "formatter": "{value} " + yaxis_formatter,
            "rotate": yaxis_rotate,
            "interval": yaxis_interval,
            "margin": yaxis_margin
        },
        "axisTick": {
            "alignWithLabel": is_yaxislabel_align
        },
        "inverse": is_yaxis_inverse,
        "position": yaxis_pos,
        "boundaryGap": is_yaxis_boundarygap,
        "min": yaxis_min,
        "max": yaxis_max
    }

    if xaxis_type is None:
        xaxis_type = "value" if type == "scatter" else "category"
    if yaxis_type is None:
        yaxis_type = "value"

    if is_convert:
        xaxis_type, yaxis_type = yaxis_type, xaxis_type
        _xAxis.update(type=xaxis_type)
        _yAxis.update(data=x_axis, type=yaxis_type)
    else:
        _xAxis.update(data=x_axis, type=xaxis_type)
        _yAxis.update(type=yaxis_type)

    # 强制分割数值轴，在多 x、y 轴中可以使用强制分割使标刻线对齐
    if xaxis_force_interval is not None:
        _xAxis.update(interval=xaxis_force_interval)
    if yaxis_force_interval is not None:
        _yAxis.update(interval=yaxis_force_interval)

    return [_xAxis], [_yAxis]


def _mark(data,
          mark_point_symbol='pin',
          mark_point_symbolsize=50,
          mark_point_textcolor='#fff',
          mark_line_symbolsize=10,
          mark_line_valuedim=None,
          _is_markline=False,
          **kwargs):
    """

    :param data:
        mark data, it can be 'min', 'max', 'average' or you cloud define by yourself
        you need a dict contains coord and name,
        coord: Coordinates of the starting point or ending point,
            Notice: For axis with axis.type 'category':
                If coord value is number, it represents index of axis.data.
                If coord value is string, it represents concrete value in axis.data.
                Please notice that in this case xAxis.data must not be written as
                [number, number, ...],but can only be written [string, string, ...].
                Otherwise it is not able to be located by markPoint / markLine.
        name: Markpoint name
    :param mark_point_symbol:
        mark symbol, it can be 'circle', 'rect', 'roundRect', 'triangle',
        'diamond', 'pin', 'arrow'
    :param mark_point_symbolsize:
        markPoint symbol size
    :param mark_point_textcolor:
        mark point text color
    :param mark_line_symbolsize:
        markLine symbol size
    :param mark_line_valuedim:
        Works only when type is assigned. It is used to state the dimension used to
        calculate maximum value or minimum value. It may be the direct name of a
        dimension, like x, or angle for line charts, or open, or close for candlestick charts.
    :param _is_markline:
        It specifies whether is markline or not.
    :return:
    """
    mark = {"data": []}
    if data:
        for d in list(data):
            # user-define markPoint
            if isinstance(d, dict):
                _coord = d.get('coord', None)
                _pname = d.get('name', None)
                _marktmp = {
                    "coord": _coord,
                    "name": _pname,
                    "symbol": mark_point_symbol,
                    "symbolSize": mark_point_symbolsize,
                    "label": {"normal": {
                        "textStyle": {"color": mark_point_textcolor}}
                    }}
                mark.get("data").append(_marktmp)
            # markPoint&markLine by default
            else:
                _type, _name = "", ""
                if "max" in d:
                    _type, _name = "max", "Maximum"
                elif "min" in d:
                    _type, _name = "min", "Minimum"
                elif "average" in d:
                    _type, _name = "average", "mean-Value"

                if _is_markline:
                    _marktmp = {
                        "type": _type,
                        "name": _name,
                        'valueDim': mark_line_valuedim,
                    }
                    if _type:
                        mark.get("data").append(_marktmp)
                        mark.update(symbolSize=mark_line_symbolsize)
                else:
                    _marktmp = {"type": _type, "name": _name}
                    _marktmp.update(
                        symbol=mark_point_symbol,
                        symbolSize=mark_point_symbolsize,
                        label={"normal": {
                            "textStyle": {"color": mark_point_textcolor}}
                        })
                    if _type:
                        mark.get("data").append(_marktmp)
    return mark


@collectfuncs
def mark_point(mark_point=None, **kwargs):
    """

    :param mark_point:
        mark point data, it can be 'min', 'max', 'average' or define by yourself
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
    return _mark(mark_line, _is_markline=True, **kwargs)


@collectfuncs
def legend(is_legend_show=True,
           legend_orient="horizontal",
           legend_pos="center",
           legend_top='top',
           legend_selectedmode='multiple',
           legend_text_size=12,
           legend_text_color='#333',
           **kwargs):
    """ Legend component shows symbol, color and name of different series.
        You can click legends to toggle displaying series in the chart.

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
    :param legend_text_size:
        legend text size
    :param legend_text_color:
        legend text color
    :param kwargs:
    :return:
    """
    _legend = {
        "selectedMode": legend_selectedmode,
        "show": is_legend_show,
        "left": legend_pos,
        "top": legend_top,
        "orient": legend_orient,
        "textStyle": {
            "fontSize": legend_text_size,
            "color": legend_text_color,
        }
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
               visual_split_number=5,
               visual_dimension=None,
               is_calculable=True,
               is_piecewise=False,
               **kwargs):
    """ visualMap is a type of component for visual encoding, which
        maps the data to visual channels

    :param visual_type:
        visual map type, 'color' or 'size'
        color:
            For visual channel color, array is used, like: ['#333', '#78ab23', 'blue'],
            which means a color ribbon is formed based on the three color stops,
            and dataValues will be mapped to the ribbon.
        size:
            For visual channel size, array is used, like: [20, 50],
            which means a size ribbon is formed based on the two value stops,
            and dataValues will be mapped to the ribbon.
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
    :param visual_split_number:
        Continuous data can be divide into pieces averagely according to splitNumber,
        that is, if splitNumber is 5, data will be sliced into 5 pieces.
    :param visual_dimension:
        Specify which dimension should be used to fetch dataValue from series.data,
        and then map them to visual channel.
    :param is_calculable:
        Whether show handles, which can be dragged to adjust "selected range".
    :param is_piecewise:
        Used to determine it is a piecewise visualMap component.
    :param kwargs:
    :return:
    """
    # default min and max value of visual_range is [0, 100]
    _min, _max = 0, 100
    if visual_range:
        if len(visual_range) == 2:
            _min, _max = visual_range

    # default label text on both ends is ['low', 'high']
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

    _type = "piecewise" if is_piecewise else "continuous"

    _visual_map = {
        "type": _type,
        "min": _min,
        "max": _max,
        "text": [_thigh, _tlow],
        "textStyle": {"color": visual_text_color},
        "inRange": _inrange_op,
        "calculable": is_calculable,
        "splitNumber": visual_split_number,
        "dimension": visual_dimension,
        "orient": visual_orient,
        "left": visual_pos,
        "top": visual_top,
        "showLabel": True,
    }
    return _visual_map


def gen_color():
    """ random generation color for << WordCloud >>

    :return:
    """
    return "rgb(%s,%s,%s)" % (random.randint(0, 160),
                              random.randint(0, 160),
                              random.randint(0, 160))


@collectfuncs
def symbol(type=None, symbol="", **kwargs):
    """

    :param symbol:
        symbol type, it can be 'rect', 'roundRect', 'triangle',
        diamond', 'pin', 'arrow'.
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
             datazoom_xaxis_index=None,
             datazoom_yaxis_index=None,
             **kwargs):
    """

    :param is_datazoom_show:
        It specifies whether to use the datazoom component.
    :param datazoom_type:
        datazoom type, 'slider', 'inside', or 'both'
    :param datazoom_range:
        The range percentage of the window out of the data extent,in
        the range of 0 ~ 100.
    :param datazoom_orient:
        Specify whether the layout of dataZoom component is horizontal or vertical.
        'horizontal' or 'vertical'.What's more,it indicates whether the horizontal
        axis or vertical axis is controlled.by default in catesian coordinate system.
    :param datazoom_xaxis_index:
        Specify which xAxis is/are controlled by the dataZoom-inside when
        catesian coordinate system is used.
    :param datazoom_yaxis_index:
        Specify which yAxis is/are controlled by the dataZoom-inside when
        catesian coordinate system is used.
    :param kwargs:
    :return:
    """
    _min, _max = 50, 100
    if datazoom_range:
        if len(datazoom_range) == 2:
            _min, _max = datazoom_range
    if datazoom_type not in ("slider", "inside", "both"):
        datazoom_type = "slider"
    _datazoom = []
    _datazoom_config = {
        "show": is_datazoom_show,
        "type": "slider",
        "start": _min,
        "end": _max,
        "orient": datazoom_orient,
        "xAxisIndex": datazoom_xaxis_index,
        "yAxisIndex": datazoom_yaxis_index
    }
    if datazoom_type == "both":
        _datazoom.append(_datazoom_config.copy())
        datazoom_type = 'inside'
    _datazoom_config['type'] = datazoom_type
    _datazoom.append(_datazoom_config)
    return _datazoom


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
def grid3D(grid3d_width=100,
           grid3d_height=100,
           grid3d_depth=100,
           grid3d_rotate_speed=10,
           grid3d_rotate_sensitivity=1,
           is_grid3d_rotate=False,
           **kwargs):
    """

    :param grid3d_width:
        3D axis width
    :param grid3d_height:
        3D axis height
    :param grid3d_depth:
        3D axis depth
    :param grid3d_rotate_speed:
        3D charts rotate speed
    :param is_grid3d_rotate:
        whether rotate 3D charts
    :param grid3d_rotate_sensitivity:
        3D charts rotete sensitivity, The greater the value, the more sensitive.
    :param kwargs:
    :return:
    """
    _grid3D = {
        "boxWidth": grid3d_width,
        "boxHeight": grid3d_height,
        "boxDepth": grid3d_depth,
        "viewControl": {
            "autoRotate": is_grid3d_rotate,
            "autoRotateSpeed": grid3d_rotate_speed,
            "rotateSensitivity": grid3d_rotate_sensitivity
        }
    }
    return _grid3D


@collectfuncs
def xaxis3D(xaxis3d_type=None,
            xaxis3d_name="",
            xaxis3d_name_size=16,
            xaxis3d_name_gap=20,
            xaxis3d_min=None,
            xaxis3d_max=None,
            xaxis3d_interval="auto",
            xaxis3d_margin=8,
            **kwargs):
    """

    :param xaxis3d_type:
        Type of 3d xaxis
    :param xaxis3d_name:
        Name of 3d xaxis
    :param xaxis3d_name_size:
        3d xaxis name font size
    :param xaxis3d_name_gap:
        Gap between axis name and 3d xaxis line.
    :param xaxis3d_min:
        The minimun value of 3d xaxis.
    :param xaxis3d_max:
        The maximun value of 3d xaxis.
    :param xaxis3d_interval:
        The display interval of the axis scale label is valid in the category 3d xaxis.
        By default, labels are displayed using labels that do not overlap the labels
        Set to 0 to force all labels to be displayed
        and label is one by one if setting as 1; If 2,it will be one label separates
        from each other, and so on.
    :param xaxis3d_margin:
        The margin between the axis label and the 3d xaxis line.
    :return:
    """
    _xaxis3D = {
        "name": xaxis3d_name,
        "nameGap": xaxis3d_name_gap,
        "nameTextStyle": {"fontSize": xaxis3d_name_size},
        "type": xaxis3d_type,
        "min": xaxis3d_min,
        "max": xaxis3d_max,
        "axisLabel": {
            "margin": xaxis3d_margin,
            "interval": xaxis3d_interval
        }
    }
    return _xaxis3D


@collectfuncs
def yaxis3D(yaxis3d_type=None,
            yaxis3d_name="",
            yaxis3d_name_size=16,
            yaxis3d_name_gap=20,
            yaxis3d_min=None,
            yaxis3d_max=None,
            yaxis3d_interval="auto",
            yaxis3d_margin=8,
            **kwargs):
    """

    :param yaxis3d_type:
        Type of 3d yaxis
    :param yaxis3d_name:
        Name of 3d yaxis
    :param yaxis3d_name_size:
        3d yaxis name font size
    :param yaxis3d_name_gap:
        Gap between axis name and 3d yaxis line.
    :param yaxis3d_min:
        The minimun value of 3d yaxis.
    :param yaxis3d_max:
        The maximun value of 3d yaxis.
    :param yaxis3d_interval:
        The display interval of the axis scale label is valid in the category 3d yaxis.
        By default, labels are displayed using labels that do not overlap the labels
        Set to 0 to force all labels to be displayed
        and label is one by one if setting as 1;If 2, it will be one label separates
        from each other, and so on.
    :param yaxis3d_margin:
        The margin between the axis label and the 3d yaxis line.
    :return:
    """
    _yaxis3D = {
        "name": yaxis3d_name,
        "nameGap": yaxis3d_name_gap,
        "nameTextStyle": {"fontSize": yaxis3d_name_size},
        "type": yaxis3d_type,
        "min": yaxis3d_min,
        "max": yaxis3d_max,
        "axisLabel": {
            "margin": yaxis3d_margin,
            "interval": yaxis3d_interval
        }
    }
    return _yaxis3D


@collectfuncs
def zaxis3D(zaxis3d_type=None,
            zaxis3d_name="",
            zaxis3d_name_size=16,
            zaxis3d_name_gap=20,
            zaxis3d_min=None,
            zaxis3d_max=None,
            zaxis3d_margin=8,
            **kwargs):
    """

    :param zaxis3d_type:
        Type of 3d zaxis
    :param zaxis3d_name:
        Name of 3d zaxis
    :param zaxis3d_name_size:
        3d zaxis name font size
    :param zaxis3d_name_gap:
        Gap between axis name and 3d zaxis line.
    :param zaxis3d_min:
        The minimun value of 3d zaxis.
    :param zaxis3d_max:
        The maximun value of 3d zaxis.
    :param zaxis3d_margin:
        The margin between the axis label and the 3d zaxis line.
    :return:
    """
    _zaxis3D = {
        "name": zaxis3d_name,
        "nameGap": zaxis3d_name_gap,
        "nameTextStyle": {"fontSize": zaxis3d_name_size},
        "type": zaxis3d_type,
        "min": zaxis3d_min,
        "max": zaxis3d_max,
        "axisLabel": {
            "margin": zaxis3d_margin,
        }
    }
    return _zaxis3D


@collectfuncs
def tooltip(type=None,
            tooltip_tragger="item",
            tooltip_tragger_on="mousemove|click",
            tooltip_axispointer_type="line",
            tooltip_formatter=None,
            tooltip_text_color="#fff",
            tooltip_font_size=14,
            **kwargs):
    """

    :param type:
        chart type
    :param tooltip_tragger:
        Type of triggering.
        Options:
            'item': Triggered by data item, which is mainly used for charts that don't have a
                    category axis like scatter charts or pie charts.
            'axis': Triggered by axes, which is mainly used for charts that have category axes,
                    like bar charts or line charts.
            'none': Trigger nothing.
    :param tooltip_tragger_on:
        Conditions to trigger tooltip. Options:
        Options:
            'mousemove': Trigger when mouse moves.
            'click': Trigger when mouse clicks.
            'mousemove|click': Trigger when mouse clicks and moves.
            'none': Do not triggered by 'mousemove' and 'click'.
    :param tooltip_axispointer_type:
        Indicator type.
        Options:
            'line': line indicator
            'shadow': shadow crosshair indicator
            'cross': crosshair indicator, which is actually the shortcut of enable two
                     axisPointers of two orthometric axes.
    :param tooltip_formatter:
        The template variables are {a}, {b}, {c}, {d} and {e},
        which stands for series name, data name and data value and ect.
        When trigger is set to be 'axis', there may be data from multiple series.
        In this time, series index can be refered as {a0}, {a1}, or {a2}.
    :param tooltip_text_color:
        text color.
    :param tooltip_font_size:
        font size
    :return:
    """
    if tooltip_formatter is None:
        if type == "gauge":
            tooltip_formatter = "{a} <br/>{b} : {c}%"
        elif type == "geo":
            tooltip_formatter = "{b}: {c}"

    _tooltip = {
        "trigger": tooltip_tragger,
        "triggerOn": tooltip_tragger_on,
        "axisPointer": {"type": tooltip_axispointer_type},
        "formatter": tooltip_formatter,
        "textStyle": {
            "color": tooltip_text_color,
            "fontSize": tooltip_font_size
        }
    }
    return _tooltip


@collectfuncs
def calendar(calendar_date_range=None,
             calendar_cell_size=None,
             **kwargs):
    """

    :param calendar_date_range:
        Required, range of Calendar coordinates, support multiple formats.
        Examples:
            # one year
                range: 2017
            # one month
                range: '2017-02'
            # a range
                range: ['2017-01-02', '2017-02-23']
            # note: they will be identified as ['2017-01-01', '2017-02-01']
                range: ['2017-01', '2017-02']
    :param calendar_cell_size:
        The size of each rect of calendar coordinates, can be set to a single
        value or array, the first element is width and the second element
        is height.Support setting self-adaptation: "auto"
    :param kwargs:
    :return:
    """

    if calendar_cell_size is None:
        calendar_cell_size = ['auto', 20]

    _calendar = {
        "range": calendar_date_range,
        "cellSize": calendar_cell_size
    }
    return _calendar


def get_all_options(**kwargs):
    """ Return all component options of charts

    :param kwargs:
    :return:
    """
    _funcs = {}
    for f in fs:
        _funcs[f.__name__] = f(**kwargs)
    return _funcs
