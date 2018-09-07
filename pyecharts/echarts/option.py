# coding=utf-8
from __future__ import unicode_literals

import random

import pyecharts.echarts as option

base_fs = []    # _config_components() 方法中被调用
other_fs = []   # add() 方法中被调用
SYMBOLS = ("rect", "roundRect", "triangle", "diamond", "pin", "arrow")


def collect_other_func(func):
    other_fs.append(func)
    return func


def collect_base_func(func):
    base_fs.append(func)
    return func


@collect_base_func
def datazoom(
    is_datazoom_show=False,
    datazoom_type="slider",
    datazoom_range=None,
    datazoom_orient="horizontal",
    datazoom_xaxis_index=None,
    datazoom_yaxis_index=None,
    **kwargs
):
    """
    dataZoom 组件 用于区域缩放，从而能自由关注细节的数据信息，或者概览数据整
    体，或者去除离群点的影响。

    :param is_datazoom_show:
        是否使用区域缩放组件，默认为 False
    :param datazoom_type:
        区域缩放组件类型，默认为'slider'，有'slider', 'inside', 'both'可选
    :param datazoom_range:
        区域缩放的范围，默认为[50, 100]
    :param datazoom_orient:
        datazoom 组件在直角坐标系中的方向，默认为 'horizontal'，效果显示在 x 轴。
        如若设置为 'vertical' 的话效果显示在 y 轴。
    :param datazoom_xaxis_index:
        datazoom 组件控制的 x 轴索引
        默认控制第一个 x 轴，如没特殊需求无须显示指定。单个为 int 类型而控制多个为 list
        类型，如 [0, 1] 表示控制第一个和第二个 x 轴。
    :param datazoom_yaxis_index:
        datazoom 组件控制的 y 轴索引
        默认控制第一个 y 轴，如没特殊需求无须显示指定。单个为 int 类型而控制多个为 list
        类型，如 [0, 1] 表示控制第一个和第二个 x 轴。
    :param kwargs:
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
        "yAxisIndex": datazoom_yaxis_index,
    }
    if datazoom_type == "both":
        _datazoom.append(_datazoom_config.copy())
        datazoom_type = "inside"
    _datazoom_config["type"] = datazoom_type
    _datazoom.append(_datazoom_config)
    return _datazoom


@collect_base_func
def datazoom_extra(
    is_datazoom_extra_show=False,
    datazoom_extra_type="slider",
    datazoom_extra_range=None,
    datazoom_extra_orient="vertical",
    datazoom_extra_xaxis_index=None,
    datazoom_extra_yaxis_index=None,
    **kwargs
):
    """
    额外的 dataZoom 条，直接 X/Y 轴同时使用 dataZoom 效果
    """
    if is_datazoom_extra_show:
        return datazoom(
            is_datazoom_show=True,
            datazoom_type=datazoom_extra_type,
            datazoom_range=datazoom_extra_range,
            datazoom_orient=datazoom_extra_orient,
            datazoom_xaxis_index=datazoom_extra_xaxis_index,
            datazoom_yaxis_index=datazoom_extra_yaxis_index,
        )


@collect_base_func
def color(colorlst=None, is_random=False, label_color=None, **kwargs):
    """

    :param colorlst:
        全局颜色列表
    :param is_random:
        指定是否随机打乱全局颜色列表
    :param label_color:
        追加的颜色列表
    :param kwargs:
    """
    if colorlst is None:
        colorlst = []
    if label_color:
        for color in reversed(list(label_color)):
            colorlst.insert(0, color)
    if is_random:
        random.shuffle(colorlst)
    return colorlst


@collect_base_func
def tooltip(**kwargs):
    return option.Tooltip(**kwargs)


@collect_base_func
def legend(
    is_legend_show=True,
    legend_orient="horizontal",
    legend_pos="center",
    legend_top="top",
    legend_selectedmode="multiple",
    legend_text_size=12,
    legend_text_color=None,
    **kwargs
):
    """
    图例组件。图例组件展现了不同系列的标记(symbol)，颜色和名字。可以通过点击图例
    控制哪些系列不显示。

    :param is_legend_show:
        是否显示顶端图例，默认为 True
    :param legend_orient:
        图例列表的布局朝向，默认为'horizontal'，有'horizontal', 'vertical'可选
    :param legend_pos:
        图例组件离容器左侧的距离，默认为'center'，有'left', 'center', 'right'可选，
        也可以为百分数，如 "%60"
    :param legend_top:
        图例组件离容器上侧的距离，默认为'top'，有'top', 'center', 'bottom'可选，
        也可以为百分数，如 "%60"
    :param legend_selectedmode:
        图例选择的模式，控制是否可以通过点击图例改变系列的显示状态。默认为'multiple'，
        可以设成 'single' 或者 'multiple' 使用单选或者多选模式。
        也可以设置为 False 关闭显示状态。
    :param legend_text_size:
        图例名称字体大小
    :param legend_text_color:
        图例名称字体颜色
    :param kwargs:
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
        },
    }
    return _legend


@collect_base_func
def visual_map(
    visual_type="color",
    visual_range=None,
    visual_text_color=None,
    visual_range_text=None,
    visual_range_color=None,
    visual_range_size=None,
    visual_orient="vertical",
    visual_pos="left",
    visual_top="bottom",
    visual_split_number=5,
    visual_dimension=None,
    is_calculable=True,
    is_piecewise=False,
    pieces=None,
    **kwargs
):
    """
    是视觉映射组件，用于进行『视觉编码』，也就是将数据映射到视觉元素（视觉通道）

    :param visual_type:
        制定组件映射方式，默认为'color‘，即通过颜色来映射数值。有'color', 'size'可选。
        'size'通过数值点的大小，也就是图形点的大小来映射数值。
    :param visual_range:
        指定组件的允许的最小值与最大值。默认为 [0, 100]
    :param visual_text_color:
        两端文本颜色。
    :param visual_range_text:
        两端文本。默认为 ['low', 'hight']
    :param visual_range_size:
        数值映射的范围，也就是图形点大小的范围。默认为 [20, 50]
    :param visual_range_color:
        过渡颜色。默认为 ['#50a3ba', '#eac763', '#d94e5d']
    :param visual_orient:
        visualMap 组件条的方向，默认为'vertical'，有'vertical', 'horizontal'可选。
    :param visual_pos:
        visualmap 组件条距离左侧的位置，默认为'left'。有'right', 'center',
        'right'可选，也可为百分数或整数。
    :param visual_top:
        visualmap 组件条距离顶部的位置，默认为'top'。有'top', 'center',
        'bottom'可选，也可为百分数或整数。
    :param visual_split_number:
        分段型中分割的段数，在设置为分段型时生效。默认分为 5 段。
    :param visual_dimension:
        指定用数据的『哪个维度』，映射到视觉元素上。默认映射到最后一个维度。索引从 0 开始。
        在直角坐标系中，x 轴为第一个维度（0），y 轴为第二个维度（1）。
    :param is_calculable:
        是否显示拖拽用的手柄（手柄能拖拽调整选中范围）。默认为 True
    :param is_piecewise:
        是否将组件转换为分段型（默认为连续型），默认为 False
    :param pieces:
        自定义『分段式视觉映射组件（visualMapPiecewise）』的每一段的范围，
        以及每一段的文字，以及每一段的特别的样式（仅在 is_piecewise 为 True
        时生效）。例如：
        pieces: [
            {min: 1500}, // 不指定 max，表示 max 为无限大（Infinity）。
            {min: 900, max: 1500},
            {min: 310, max: 1000},
            {min: 200, max: 300},
            {min: 10, max: 200, label: '10 到 200（自定义label）'},
            // 表示 value 等于 123 的情况。
            {value: 123, label: '123（自定义特殊颜色）', color: 'grey'}
            {max: 5}     // 不指定 min，表示 min 为无限大（-Infinity）。
        ]
    :param kwargs:
    """
    _min, _max = 0, 100
    if visual_range:
        if len(visual_range) == 2:
            _min, _max = visual_range

    _tlow, _thigh = "low", "high"
    if visual_range_text:
        if len(visual_range_text) == 2:
            _tlow, _thigh = visual_range_text

    _inrange_op = {}
    if visual_type == "color":
        range_color = ["#50a3ba", "#eac763", "#d94e5d"]
        if visual_range_color:
            if len(visual_range_color) >= 2:
                range_color = visual_range_color
        _inrange_op.update(color=range_color)

    if visual_type == "size":
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
    if is_piecewise:
        _visual_map.update(pieces=pieces)
    return _visual_map


@collect_other_func
def label(
    type=None,
    is_label_show=False,
    is_label_emphasis=True,
    label_pos=None,
    label_text_color=None,
    label_text_size=12,
    label_formatter=None,
    label_emphasis_pos=None,
    label_emphasis_textcolor=None,
    label_emphasis_textsize=12,
    **kwargs
):
    """
    图形上的文本标签，可用于说明图形的一些数据信息，比如值，名称等。

    :param type:
        图形类型
    :param is_label_emphasis:
        是否高亮显示标签，默认显示。高亮标签即选中数据时显示的信息项。
    :param is_label_show:
        是否正常显示标签，默认不显示。标签即各点的数据项信息
    :param label_pos:
        标签的位置，Bar 图默认为'top'。有'top', 'left', 'right', 'bottom',
        'inside', 'outside'可选
    :param label_text_color:
        标签字体颜色，默认为 "#000"
    :param label_text_size:
        标签字体大小，默认为 12
    :param label_formatter:
        模板变量有 {a}, {b}，{c}，{d}，{e}，分别表示系列名，数据名，数据值等。
        使用示例，如 label_formatter='{a}'
        在 trigger 为 'axis' 的时候，会有多个系列的数据，此时可以通过 {a0}, {a1}, {a2}
        这种后面加索引的方式表示系列的索引。不同图表类型下的 {a}，{b}，{c}，{d} 含义不一样。
        其中变量 {a}, {b}, {c}, {d} 在不同图表类型下代表数据含义为：
            折线（区域）图、柱状（条形）图、K线图 :
                {a}（系列名称），{b}（类目值），{c}（数值）, {d}（无）
            散点图（气泡）图 :
                {a}（系列名称），{b}（数据名称），{c}（数值数组）, {d}（无）
            地图 :
                {a}（系列名称），{b}（区域名称），{c}（合并数值）, {d}（无）
            饼图、仪表盘、漏斗图:
                {a}（系列名称），{b}（数据项名称），{c}（数值）, {d}（百分比）
    :param label_emphasis_pos:
        高亮标签的位置，Bar 图默认为'top'。有'top', 'left', 'right', 'bottom',
        'inside', 'outside'可选
    :param label_emphasis_textcolor:
        高亮标签字体颜色，默认为 "#fff"
    :param label_emphasis_textsize:
        高亮标签字体大小，默认为 12
    :param kwargs:
    """
    _label = {
        "normal": option.NormalLabel(
            visibility=is_label_show,
            position=label_pos,
            text_color=label_text_color,
            text_size=label_text_size,
            formatter=label_formatter,
            chart_type=type,
        ),
        "emphasis": option.EmphasisLabel(
            visibility=is_label_emphasis,
            position=label_emphasis_pos,
            text_color=label_emphasis_textcolor,
            text_size=label_emphasis_textsize,
            chart_type=type,
        ),
    }

    return _label


@collect_other_func
def line_style(
    type=None,
    line_width=1,
    line_opacity=1,
    line_curve=0,
    line_type="solid",
    line_color=None,
    **kwargs
):
    """
    带线图形的线的风格选项

    :param type:
        图形类型
    :param line_width:
        线的宽度，默认为 1
    :param line_opacity:
        线的透明度，0 为完全透明，1 为完全不透明。默认为 1
    :param line_curve:
        线的弯曲程度，0 为完全不弯曲，1 为最弯曲。默认为 0
    :param line_type:
        线的类型，有'solid', 'dashed', 'dotted'可选。默认为'solid'
    :param line_color:
        线的颜色
    :param kwargs:
    """
    if line_color is None and type == "graph":
        line_color = "#aaa"

    _line_style = {
        "normal": option.Line(
            width=line_width,
            opacity=line_opacity,
            curve=line_curve,
            line_type=line_type,
            color=line_color,
            chart_type=type,
        )
    }
    return _line_style


@collect_other_func
def split_line(is_splitline_show=True, **kwargs):
    """

    :param is_splitline_show:
        指定是否显示分割线
    :param kwargs:
    """
    _split_line = {
        "show": is_splitline_show,
        "lineStyle": line_style(**kwargs),
    }
    return _split_line


@collect_other_func
def axis_line(is_axisline_show=True, **kwargs):
    """

    :param is_axisline_show:
        指定是否显示坐标轴线
    :param kwargs:
    """
    _axis_line = {"show": is_axisline_show, "lineStyle": line_style(**kwargs)}
    return _axis_line


@collect_other_func
def split_area(is_area_show=True, **kwargs):
    """

    :param is_area_show:
        指定是否显示标记区域
    :param kwargs:
    """
    _split_area = {"show": is_area_show, "areaStyle": area_style(**kwargs)}
    return _split_area


@collect_other_func
def area_style(flag=False, area_opacity=None, area_color=None, **kwargs):
    """

    :param flag:
        判断符
    :param area_opacity:
        区域透明度。支持从 0 到 1 的数字，为 0 时不绘制该图形。
    :param area_color:
        填充的颜色
    :param kwargs:
    """
    if area_opacity is None:
        area_opacity = 0 if flag else 1
    _area_style = {"opacity": area_opacity, "color": area_color}
    return _area_style


@collect_other_func
def xy_axis(
    type=None,
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
    xaxis_label_textsize=12,
    xaxis_label_textcolor=None,
    xaxis_formatter=None,
    xaxis_line_color=None,
    xaxis_line_width=1,
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
    yaxis_label_textsize=12,
    yaxis_label_textcolor=None,
    yaxis_formatter="",
    yaxis_line_color=None,
    yaxis_line_width=1,
    is_convert=False,
    is_xaxis_inverse=False,
    is_yaxis_inverse=False,
    is_xaxislabel_align=False,
    is_yaxislabel_align=False,
    is_xaxis_boundarygap=True,
    is_yaxis_boundarygap=True,
    is_xaxis_show=True,
    is_yaxis_show=True,
    is_splitline_show=True,
    **kwargs
):
    """
    直角坐标系中的 x、y 轴(Line、Bar、Scatter、EffectScatter、Kline)。

    :param type:
        图形类型。
    :param x_axis:
        x 轴数据项。
    :param xaxis_margin:
        x 轴刻度标签与轴线之间的距离。默认为 8
    :param xaxis_name_size:
        x 轴名称体大小，默认为 14
    :param xaxis_name_gap:
        x 轴名称与轴线之间的距离，默认为 25
    :param xaxis_name:
        x 轴名称
    :param xaxis_name_pos:
        x 轴名称位置，有'start'，'middle'，'end'可选
    :param xaxis_rotate:
        x 轴刻度标签旋转的角度，在类目轴的类目标签显示不下的时候可以通过旋转防止标
        签之间重叠。默认为 0，即不旋转。旋转的角度从 -90 度到 90 度。
    :param xaxis_min:
        x 坐标轴刻度最小值，默认为自适应。使用特殊值 "dataMin" 可自定以数
        据中最小值为 x 轴最小值。
    :param xaxis_max:
        x 坐标轴刻度最大值，默认为自适应。使用特殊值 "dataMax" 可自定以数
        据中最小值为 x 轴最大值。
    :param xaxis_type:
        x 坐标轴类型
            'value'：数值轴，适用于连续数据。
            'category'：类目轴，适用于离散的类目数据。
            'log'：对数轴。适用于对数数据。
    :param xaxis_interval:
        x 轴刻度标签的显示间隔，在类目轴中有效。默认会采用标签不重叠的策略间隔显示标签。
        设置成 0 强制显示所有标签。设置为 1，表示『隔一个标签显示一个标签』，
        如果值为 2，表示隔两个标签显示一个标签，以此类推
    :param xaxis_force_interval:
        强制设置 x 坐标轴分割间隔。如设置为 50 则刻度为 [0, 50, 150, ...]，设置为 "auto"
        则只显示两个刻度。一般情况下不建议设置这个参数！！
        因为 splitNumber 是预估的值，实际根据策略计算出来的刻度可能无法达到想要的效果，
        这时候可以使用 interval 配合 min、max 强制设定刻度划分。在类目轴中无效。
    :param xaxis_pos:
        x 坐标轴位置，有'top','bottom'可选
    :param xaxis_label_textsize:
        x 坐标轴标签字体大小
    :param xaxis_label_textcolor:
        x 坐标轴标签字体颜色
    :param xaxis_formatter:
        x 轴标签格式器，如 '天'，则 x 轴的标签为数据加'天'(3 天，4 天),默认为 ""
        xaxis_formatter -> function
        ```python
        def label_formatter(params):
            return params.value + ' [Good!]'
        ```
        回调函数格式，更多内容请参考 [高级用法篇](zh-cn/advanced)
        ```
        (params: Object|Array) => string
        参数 params 是 formatter 需要的单个数据集。格式如下：
        {
            componentType: 'series',
            // 系列类型
            seriesType: string,
            // 系列在传入的 option.series 中的 index
            seriesIndex: number,
            // 系列名称
            seriesName: string,
            // 数据名，类目名
            name: string,
            // 数据在传入的 data 数组中的 index
            dataIndex: number,
            // 传入的原始数据项
            data: Object,
            // 传入的数据值
            value: number|Array,
            // 数据图形的颜色
            color: string,
        }
        ```
    :param xaxis_line_color:
        x 坐标轴线线的颜色，默认为 None
    :param xaxis_line_width:
        x 坐标轴线线的宽度，默认为 1
    :param yaxis_margin:
        y 轴刻度标签与轴线之间的距离。默认为 8
    :param yaxis_name_size:
        y 轴名称体大小，默认为 14
    :param yaxis_name_gap:
        y 轴名称与轴线之间的距离，默认为 25
    :param yaxis_name:
        y 轴名称
    :param yaxis_name_pos:
        y 轴名称位置，有'start', 'middle'，'end'可选
    :param yaxis_rotate:
        y 轴刻度标签旋转的角度，在类目轴的类目标签显示不下的时候可以通过旋转防止标
        签之间重叠。默认为 0，即不旋转。旋转的角度从 -90 度到 90 度。
    :param yaxis_min:
        y 坐标轴刻度最小值，默认为自适应。使用特殊值 "dataMin" 可自定以数
        据中最小值为 y 轴最小值。
    :param yaxis_max:
        y 坐标轴刻度最大值，默认为自适应。使用特殊值 "dataMax" 可自定以数
        据中最小值为 y 轴最大值。
    :param yaxis_type:
        y 坐标轴类型
            'value'：数值轴，适用于连续数据。
            'category'：类目轴，适用于离散的类目数据。
            'log'：对数轴。适用于对数数据。
    :param yaxis_interval:
        y 轴刻度标签的显示间隔，在类目轴中有效。默认会采用标签不重叠的策略间隔显示标签。
        设置成 0 强制显示所有标签。设置为 1，表示『隔一个标签显示一个标签』，
        如果值为 2，表示隔两个标签显示一个标签，以此类推
    :param yaxis_force_interval:
        强制设置 y 坐标轴分割间隔。如设置为 50 则刻度为 [0, 50, 150, ...]，设置为 "auto"
        则只显示两个刻度。一般情况下不建议设置这个参数！！
        因为 splitNumber 是预估的值，实际根据策略计算出来的刻度可能无法达到想要的效果，
        这时候可以使用 interval 配合 min、max 强制设定刻度划分。在类目轴中无效。
    :param yaxis_pos:
        y 坐标轴位置，有'left','right'可选
    :param yaxis_label_textsize:
        y 坐标轴标签字体大小
    :param yaxis_label_textcolor:
        y 坐标轴标签字体颜色
    :param yaxis_formatter:
        y 轴标签格式器，如 '天'，则 y 轴的标签为数据加'天'(3 天，4 天),默认为 ""
        yaxis_formatter -> function
        ```python
        def label_formatter(params):
            return params.value + ' [Good!]'
        ```
        回调函数格式，更多内容请参考 [高级用法篇](zh-cn/advanced)
        ```
        (params: Object|Array) => string
        参数 params 是 formatter 需要的单个数据集。格式如下：
        {
            componentType: 'series',
            // 系列类型
            seriesType: string,
            // 系列在传入的 option.series 中的 index
            seriesIndex: number,
            // 系列名称
            seriesName: string,
            // 数据名，类目名
            name: string,
            // 数据在传入的 data 数组中的 index
            dataIndex: number,
            // 传入的原始数据项
            data: Object,
            // 传入的数据值
            value: number|Array,
            // 数据图形的颜色
            color: string,
        }
        ``
    :param yaxis_line_color:
        y 坐标轴线线的颜色，默认为 None
    :param yaxis_line_width:
        y 坐标轴线线的宽度，默认为 1
    :param is_convert:
        是否交换 x 轴与 y 轴
    :param is_xaxis_inverse:
        是否反向 x 坐标轴，默认为 False
    :param is_yaxis_inverse:
        是否反向 y 坐标轴，默认为 False
    :param is_xaxislabel_align:
        x 轴刻度线和标签是否对齐，默认为 False
    :param is_yaxislabel_align:
        y 轴刻度线和标签是否对齐，默认为 False
    :param is_xaxis_boundarygap:
        x 轴两边留白策略，适用于类目轴。类目轴中 boundaryGap 可以配置为 True 和 False。
        默认为 True，这时候刻度只是作为分隔线，标签和数据点都会在两个刻度之间的带(band)
        中间，即两边留白。
    :param is_yaxis_boundarygap:
        y 轴两边留白策略，适用于类目轴。类目轴中 boundaryGap 可以配置为 True 和 False。
        默认为 True，这时候刻度只是作为分隔线，标签和数据点都会在两个刻度之间的带(band)
        中间，即两边留白。
    :param is_xaxis_show:
        是否显示 x 轴
    :param is_yaxis_show:
        是否显示 y 轴
    :param is_splitline_show:
        是否显示 y 轴网格线，默认为 True。
    :param kwargs:
    """
    _xAxis = option.XAxis(
        name=xaxis_name,
        visibility=is_xaxis_show,
        name_location=xaxis_name_pos,
        name_gap=xaxis_name_gap,
        name_size=xaxis_name_size,
        position=xaxis_pos,
        boundary_gap=is_xaxis_boundarygap,
        label_alignment=is_xaxislabel_align,
        inverse=is_xaxis_inverse,
        value_range=[xaxis_min, xaxis_max],
        axis_type=xaxis_type,
        axis_line_color=xaxis_line_color,
        axis_line_width=xaxis_line_width,
        chart_type=type,
    )
    _xAxis["axisLabel"] = option.XAxisLabel(
        interval=xaxis_interval,
        rotate=xaxis_rotate,
        margin=xaxis_margin,
        text_size=xaxis_label_textsize,
        text_color=xaxis_label_textcolor,
        formatter=xaxis_formatter,
    )
    _yAxis = option.YAxis(
        name=yaxis_name,
        visibility=is_yaxis_show,
        name_location=yaxis_name_pos,
        name_gap=yaxis_name_gap,
        name_size=yaxis_name_size,
        position=yaxis_pos,
        boundary_gap=is_yaxis_boundarygap,
        label_alignment=is_yaxislabel_align,
        inverse=is_yaxis_inverse,
        value_range=[yaxis_min, yaxis_max],
        split_line=is_splitline_show,
        axis_type=yaxis_type,
        axis_line_color=yaxis_line_color,
        axis_line_width=yaxis_line_width,
        chart_type=type,
    )
    _yAxis["axisLabel"] = option.YAxisLabel(
        interval=yaxis_interval,
        rotate=yaxis_rotate,
        margin=yaxis_margin,
        text_size=yaxis_label_textsize,
        text_color=yaxis_label_textcolor,
        formatter=yaxis_formatter,
    )

    if is_convert:
        xaxis_type, yaxis_type = _yAxis["type"], _xAxis["type"]
        _xAxis["type"] = xaxis_type
        _yAxis.update(data=x_axis, type=yaxis_type)
    else:
        _xAxis["data"] = x_axis

    # 强制分割数值轴，在多 x、y 轴中可以使用强制分割使标刻线对齐
    if xaxis_force_interval is not None:
        _xAxis["interval"] = xaxis_force_interval
    if yaxis_force_interval is not None:
        _yAxis["interval"] = yaxis_force_interval

    # 返回字典
    return [_xAxis], [_yAxis]


def _mark(
    data,
    mark_point_raw=None,
    mark_point_symbol="pin",
    mark_point_symbolsize=50,
    mark_point_textcolor="#fff",
    mark_line_raw=None,
    mark_line_symbolsize=10,
    mark_line_valuedim="",
    mark_line_coords=None,
    mark_point_valuedim="",
    _is_markline=False,
    **kwargs
):
    """
    图形标记组件，用于标记指定的特殊数据，有标记线和标记点两种

    :param data:
        标记点
            默认有'min', 'max', 'average'可选。支持自定义标记点，具体使用如下
            [
                {
                    "coord": [a1, b1],
                    "name": "first markpoint"
                },
                {
                    "coord": [a2, b2],
                    "name": "second markpoint"
                }
            ]
            需自己传入标记点字典，共有两个键值对，'coord' 对应为 x y 轴坐标，'name' 为标记点名称
        标记线
            只支持默认的 'min', 'max', 'average'
    :param mark_point_raw:
        原生格式的 markPoint 数据，数据类型为 [{}, {}, ...]。
        格式请参考 http://echarts.baidu.com/option.html#series-line.markPoint.data
    :param mark_point_symbol:
        标记点图形，，默认为'pin'，有'circle', 'rect', 'roundRect', 'triangle',
        'diamond', 'pin', 'arrow'可选
    :param mark_point_symbolsize:
        标记点图形大小，默认为 50
    :param mark_point_textcolor:
        标记点字体颜色，默认为'#fff'
    :param mark_line_raw:
        原生格式的 markLine 数据，数据类型为 [{}, {}, ...]。
        格式请参考 http://echarts.baidu.com/option.html#series-line.markLine.data
    :param mark_line_symbolsize:
        标记线图形大小，默认为 15
    :param mark_line_valuedim:
        标记线指定在哪个维度上指定最大值最小值。这可以是维度的直接名称，Line 时可以
        是 x、angle 等、Kline 图时可以是 open、close、highest、lowest。
        可同时制定多个维度，如
            mark_line=['min', 'max'], mark_line_valuedim=['lowest', 'highest']
            则表示 min 使用 lowest 维度，max 使用 highest 维度，以此类推
    :param mark_line_coords:
        标记线指定起点坐标和终点坐标，如 [[10, 10], [30, 30]]，两个点分别为横
        纵坐标轴点。
    :param mark_point_valuedim:
        标记点指定在哪个维度上指定最大值最小值。这可以是维度的直接名称，Line 时可以
        是 x、angle 等、Kline 图时可以是 open、close、highest、lowest。
        可同时制定多个维度，如
          mark_point=['min', 'max'], mark_point_valuedim=['lowest', 'highest']
        则表示 min 使用 lowest 维度，max 使用 highest 维度，以此类推
    :param _is_markline:
        指定是否为 markline
    """
    if _is_markline:
        if mark_line_raw:
            return {"data": mark_line_raw}
    else:
        if mark_point_raw:
            return {"data": mark_point_raw}

    mark = {"data": []}
    if data:
        _markpv = _marklv = [None for _ in range(len(data))]
        _markpv[: len(mark_point_valuedim)] = mark_point_valuedim
        _marklv[: len(mark_line_valuedim)] = mark_line_valuedim
        for index, d in enumerate(list(data)):
            # 自定义坐标点数据
            if isinstance(d, dict):
                _coord = d.get("coord", None)
                _pname = d.get("name", None)
                _marktmp = {
                    "coord": _coord,
                    "value": _coord[1],
                    "name": _pname,
                    "symbol": mark_point_symbol,
                    "symbolSize": mark_point_symbolsize,
                    "label": {
                        "normal": {
                            "textStyle": {"color": mark_point_textcolor}
                        }
                    },
                }
                mark.get("data").append(_marktmp)
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
                        "valueDim": _marklv[index],
                    }
                    if _type:
                        mark.get("data").append(_marktmp)
                        mark.update(symbolSize=mark_line_symbolsize)
                else:
                    _marktmp = {
                        "type": _type,
                        "name": _name,
                        "valueDim": _markpv[index],
                    }
                    _marktmp.update(
                        symbol=mark_point_symbol,
                        symbolSize=mark_point_symbolsize,
                        label={
                            "normal": {
                                "textStyle": {"color": mark_point_textcolor}
                            }
                        },
                    )
                    if _type:
                        mark.get("data").append(_marktmp)

    if mark_line_coords and len(mark_line_coords) == 2:
        return {
            "data": [
                [
                    {"coord": mark_line_coords[0]},
                    {"coord": mark_line_coords[1]},
                ]
            ]
        }

    return mark


@collect_other_func
def mark_point(mark_point=None, **kwargs):
    """
    标记点配置项

    :param mark_point:
        默认有'min', 'max', 'average'可选。支持自定义标记点，具体使用如下
            [
                {
                    "coord": [a1, b1],
                    "name": "first markpoint"
                },
                {
                    "coord": [a2, b2],
                    "name": "second markpoint"
                }
            ]
            需自己传入标记点字典，共有两个键值对，'coord' 对应为 x y 轴坐标，'name' 为标记点名称
    :param kwargs:
    """
    return _mark(mark_point, **kwargs)


@collect_other_func
def mark_line(mark_line=None, **kwargs):
    """ 标记线配置项

    :param mark_line:
        只支持默认的 'min', 'max', 'average'
    :param kwargs:
    """
    return _mark(mark_line, _is_markline=True, **kwargs)


@collect_other_func
def symbol(type=None, symbol="", **kwargs):
    """

    :param symbol:
        标记类型, 有'rect', 'roundRect', 'triangle', 'diamond',
         'pin', 'arrow'可选
    :param kwargs:
    """
    if symbol is None:  # Radar
        symbol = "none"
    elif type == "line" and symbol == "":  # Line
        symbol = "emptyCircle"
    elif symbol not in SYMBOLS:
        symbol = "circle"
    return symbol


@collect_other_func
def effect(
    effect_brushtype="stroke", effect_scale=2.5, effect_period=4, **kwargs
):
    """
    涟漪动画配置项

    :param effect_brushtype:
        波纹绘制方式，有'stroke', 'fill'可选。默认为'stroke'
    :param effect_scale:
        动画中波纹的最大缩放比例。默认为 2.5
    :param effect_period:
        动画持续的时间。默认为 4（s）
    :param kwargs:
    """
    _effect = {
        "brushType": effect_brushtype,
        "scale": effect_scale,
        "period": effect_period,
    }
    return _effect


@collect_other_func
def grid(
    grid_width=None,
    grid_height=None,
    grid_top=None,
    grid_bottom=None,
    grid_left=None,
    grid_right=None,
    **kwargs
):
    """
    Grid 类组件配置项

    :param grid_width:
        grid 组件的宽度。默认自适应。
    :param grid_height:
        grid 组件的高度。默认自适应。
    :param grid_top:
         grid 组件离容器顶部的距离。默认为 None, 有'top', 'center', 'middle'可选，
         也可以为百分数或者整数
    :param grid_bottom:
        grid 组件离容器底部的距离。默认为 None, 有'top', 'center', 'middle'可选，
        也可以为百分数或者整数
    :param grid_left:
        grid 组件离容器左侧的距离。默认为 None, 有'left', 'center', 'right'可选，
        也可以为百分数或者整数
    :param grid_right:
        grid 组件离容器右侧的距离。默认为 None, 有'left', 'center', 'right'可选
        也可以为百分数或者整数
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


@collect_other_func
def grid3D(
    grid3d_width=100,
    grid3d_height=100,
    grid3d_depth=100,
    grid3d_rotate_speed=10,
    grid3d_rotate_sensitivity=1,
    is_grid3d_rotate=False,
    **kwargs
):
    """
    3D 笛卡尔坐标系组配置项，适用于 3D 图形。

    :param grid3d_width:
        三维笛卡尔坐标系组件在三维场景中的高度。默认为 100
    :param grid3d_height:
        三维笛卡尔坐标系组件在三维场景中的高度。默认为 100
    :param grid3d_depth:
        三维笛卡尔坐标系组件在三维场景中的高度。默认为 100
    :param grid3d_rotate_speed:
        物体自传的速度。单位为角度 / 秒，默认为 10 ，也就是 36 秒转一圈。
    :param is_grid3d_rotate:
        是否开启视角绕物体的自动旋转查看。默认为 False
    :param grid3d_rotate_sensitivity:
        旋转操作的灵敏度，值越大越灵敏。默认为 1, 设置为 0 后无法旋转。
    :param kwargs:
    """
    _grid3D = {
        "boxWidth": grid3d_width,
        "boxHeight": grid3d_height,
        "boxDepth": grid3d_depth,
        "viewControl": {
            "autoRotate": is_grid3d_rotate,
            "autoRotateSpeed": grid3d_rotate_speed,
            "rotateSensitivity": grid3d_rotate_sensitivity,
        },
    }
    return _grid3D


@collect_other_func
def xaxis3D(
    xaxis3d_type=None,
    xaxis3d_name="",
    xaxis3d_name_size=16,
    xaxis3d_name_gap=20,
    xaxis3d_min=None,
    xaxis3d_max=None,
    xaxis3d_interval="auto",
    xaxis3d_margin=8,
    **kwargs
):
    """
    3D x 轴配置项

    :param xaxis3d_type:
        3D x 轴类型
    :param xaxis3d_name:
        x 轴名称，默认为 ""
    :param xaxis3d_name_size:
        x 轴名称体大小，默认为 16
    :param xaxis3d_name_gap:
        x 轴名称与轴线之间的距离，默认为 25
    :param xaxis3d_min:
        x 坐标轴刻度最小值，默认为自适应。
    :param xaxis3d_max:
        x 坐标轴刻度最大值，默认为自适应。
    :param xaxis3d_interval:
        x 轴刻度标签的显示间隔，在类目轴中有效。默认会采用标签不重叠的策略间隔显示标签。
        设置成 0 强制显示所有标签。设置为 1，表示『隔一个标签显示一个标签』，如果值
        为 2，表示隔两个标签显示一个标签，以此类推
    :param xaxis3d_margin:
        x 轴刻度标签与轴线之间的距离。默认为 8
    """
    _xaxis3D = {
        "name": xaxis3d_name,
        "nameGap": xaxis3d_name_gap,
        "nameTextStyle": {"fontSize": xaxis3d_name_size},
        "type": xaxis3d_type,
        "min": xaxis3d_min,
        "max": xaxis3d_max,
        "axisLabel": {"margin": xaxis3d_margin, "interval": xaxis3d_interval},
    }
    return _xaxis3D


@collect_other_func
def yaxis3D(
    yaxis3d_type=None,
    yaxis3d_name="",
    yaxis3d_name_size=16,
    yaxis3d_name_gap=20,
    yaxis3d_min=None,
    yaxis3d_max=None,
    yaxis3d_interval="auto",
    yaxis3d_margin=8,
    **kwargs
):
    """
    3D y 轴配置项

    :param yaxis3d_type:
        3D x 轴类型
    :param yaxis3d_name:
        y 轴名称，默认为 ""
    :param yaxis3d_name_size:
        y 轴名称体大小，默认为 16
    :param yaxis3d_name_gap:
        y 轴名称与轴线之间的距离，默认为 25
    :param yaxis3d_min:
        y 坐标轴刻度最小值，默认为自适应。
    :param yaxis3d_max:
        y 坐标轴刻度最大值，默认为自适应。
    :param yaxis3d_interval:
        y 轴刻度标签的显示间隔，在类目轴中有效。默认会采用标签不重叠的策略间隔显示标签。
        设置成 0 强制显示所有标签。设置为 1，表示『隔一个标签显示一个标签』，如果值
        为 2，表示隔两个标签显示一个标签，以此类推
    :param yaxis3d_margin:
        y 轴刻度标签与轴线之间的距离。默认为 8
    """
    _yaxis3D = {
        "name": yaxis3d_name,
        "nameGap": yaxis3d_name_gap,
        "nameTextStyle": {"fontSize": yaxis3d_name_size},
        "type": yaxis3d_type,
        "min": yaxis3d_min,
        "max": yaxis3d_max,
        "axisLabel": {"margin": yaxis3d_margin, "interval": yaxis3d_interval},
    }
    return _yaxis3D


@collect_other_func
def zaxis3D(
    zaxis3d_type=None,
    zaxis3d_name="",
    zaxis3d_name_size=16,
    zaxis3d_name_gap=20,
    zaxis3d_min=None,
    zaxis3d_max=None,
    zaxis3d_margin=8,
    **kwargs
):
    """
    3D y 轴配置项

    :param zaxis3d_type:
        3D y 轴类型
    :param zaxis3d_name:
        z 轴名称，默认为 ""
    :param zaxis3d_name_size:
        z 轴名称体大小，默认为 16
    :param zaxis3d_name_gap:
        z 轴名称与轴线之间的距离，默认为 25
    :param zaxis3d_min:
        z 坐标轴刻度最小值，默认为自适应。
    :param zaxis3d_max:
        z 坐标轴刻度最大值，默认为自适应。
    :param zaxis3d_margin:
        z 轴刻度标签与轴线之间的距离。默认为 8
    """
    _zaxis3D = {
        "name": zaxis3d_name,
        "nameGap": zaxis3d_name_gap,
        "nameTextStyle": {"fontSize": zaxis3d_name_size},
        "type": zaxis3d_type,
        "min": zaxis3d_min,
        "max": zaxis3d_max,
        "axisLabel": {"margin": zaxis3d_margin},
    }
    return _zaxis3D


@collect_other_func
def calendar(calendar_date_range=None, calendar_cell_size=None, **kwargs):
    """

    :param calendar_date_range:
        日历热力图的日期, "2016" 表示 2016 年, ["2016-5-5", "2017-5-5"]
        表示 2016 年 5 月 5 日至 2017 年 5 月 5 日
    :param calendar_cell_size:
        日历每格框的大小，可设置单值 或数组 第一个元素是宽 第二个元素是高，支持
        设置自适应 "auto"。默认为 ["auto", 20]
    :param kwargs:
    """

    if calendar_cell_size is None:
        calendar_cell_size = ["auto", 20]

    _calendar = {"range": calendar_date_range, "cellSize": calendar_cell_size}
    return _calendar


def get_base_options(**kwargs):
    """
    返回图形实例的所有配置项
    """
    _funcs = {}
    for f in base_fs:
        _funcs[f.__name__] = f(**kwargs)
    return _funcs


def get_other_options(**kwargs):
    """
    返回图形实例的所有配置项
    """
    _funcs = {}
    for f in other_fs:
        _funcs[f.__name__] = f(**kwargs)
    return _funcs
