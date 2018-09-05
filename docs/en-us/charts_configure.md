> Charts configuration: pyecharts configuration documents

* Chart initialization
* General options
    * xyAxis：x, y axis in cartesian coordinate system(Line, Bar, Scatter, EffectScatter, Kline)
    
    * dataZoom：dataZoom components for zoom-in and zoom-out. With them, it is possible to magnify a small area, to see the overall picture or to stay away from scattered points(Line, Bar, Scatter, EffectScatter, Kline) 
    
    * legend：legend component has different symbol, colour and name, and provide the interactive clicking functions to show or hide its associated data series.
    
    * label：text string on the chart, for marking the charts with sensible details, such as value, name.
    
    * lineStyle：line style for Line, Polar, Radar, Graph, Parallel.
    
    * grid3D：gird3D components in cartesian coordinate system(Bar3D, Line3D, Scatter3D, Surface3D)
    
    * axis3D: 3D Cartesian coordinate system X, Y, Z axis configuration items for 3D graphics. (Bar3D, Line3D, Scatter3D, Surface3D)
    
    * visualMap：It is a type of component for visual encoding, which maps the data to visual channels
    
    * markLine-markPoint: A graphic markup component that marks the specified special data, with both marker lines and marker points. (Bar, Line, Kline)
    
    * tooltip: prompt box component, used to pop up data content when moving or clicking the mouse
    
    * toolbox: right utility toolbox

## Chart initialization
>The parameter a chart type initialize accept (the same to all the chart type).

* title -> str  
    default -> ''  
    The main title text, supporting for \n for newlines.

* subtitle -> str  
    defalut -> ''  
    Subtitle text, supporting for \n for newlines.

* width -> int  
    defalut -> 800(px)  
    Canvas width

* height -> int  
    defalut -> 400(px)  
    Canvas height

* title_pos -> str/int  
    defalut => 'left'  
    Distance between grid component and the left side of the container.title_pos value can be instant pixel value like 20;  
    It can also be percentage value relative to container width like '20%';it can also be 'left', 'center', or 'right'.  
    If the title_pos value is set to be 'left', 'center', or 'right',then the component will be aligned automatically based on position.

* title_top -> str/int  
    default -> 'top'  
    Distance between grid component and the top side of the container.top value can be instant pixel value like 20.  
    It can also be percentage value relative to container width like '20%';it can also be 'top', 'middle', or 'bottom'.  
    If the left value is set to be 'top', 'middle', or 'bottom',then the component will be aligned automatically based on position.

* title_color -> str  
    defalut -> '#000'  
    main title text color.  

* subtitle_color -> str  
    defalut -> '#aaa'  
    subtitle text color.

* title_text_size -> int  
    defalut -> 18  
    main title font size

* subtitle_text_size -> int   
    defalut -> 12  
    subtitle text color.

* background_color -> str  
    defalut -> '#fff'   
    Background color of title, which is transparent by default.  
    Color can be represented in RGB, for example 'rgb(128, 128, 128)'. RGBA can be used when you need alpha channel, for example 'rgba(128, 128, 128, 0.5)'.
    You may also use hexadecimal format, for example '#ccc'.

* page_title -> str  
    You can specify the title for render.html. Default is 'Echarts'

* renderer -> str  
    Specify the use of rendering mode, there are 'svg' and 'canvas' optional, the default is 'canvas'. 3D drawings can only use 'canvas'.

* extra_html_text_label -> list  
    Additional HTML text tags, `(<p> tag)`. The type is list, list[0] is the text content, and list[1] is the font style (optional). Such as ["this is a p label", "color:red"]. **Only used in a single graphic or page class.**

* is_animation -> bool  
    Whether to turn on the animation, the default is True. V0.5.9+

## General options
> All general configurations are set in```add()```

### xyAxis
**x, y axis in cartesian coordinate system (Line, Bar, Scatter, EffectScatter, Kline)**

* is_convert -> bool  
    It specifies whether to convert xAxis and yAxis.

* is_xaxislabel_align -> bool  
    Whether the x-axis tick marks and labels are aligned, the default is False

* is_yaxislabel_align -> bool  
    Whether the y-axis tick marks and labels are aligned, the default is False

* is_xaxis_inverse -> bool  
    Whether to reverse the x axis, the default is False

* is_yaxis_inverse -> bool  
    Whether to reverse the y axis, the default is False

* is_xaxis_boundarygap -> bool  
    The white-axis strategy on both sides of the x-axis applies to the category axis. The boundaryGap in the category axis can be configured as True and False. The default is True. That means the scale is only used as a divider. Labels and data points will be in the middle of the band between the two scales, that is, white on both sides.

* is_yaxis_boundarygap -> bool  
    The white balance strategy on both sides of the y axis applies to the category axis. The boundaryGap in the category axis can be configured as True and False. The default is True. That means the scale is only used as a divider. Labels and data points will be in the middle of the band between the two scales, that is, white on both sides.

* is_xaxis_show -> bool  
    Whether to display the x axis

* is_yaxis_show -> bool  
    Whether to display the y axis

* is_splitline_show -> bool  
    Whether to display the y-axis grid line, the default is True.

* x_axis -> list  
    xAxis data

* xaxis_interval -> int  
    The display interval of the x-axis scale labels is valid in the category axis. By default, labels are displayed with intervals that do not overlap labels.
    Set to 0 to force all labels to be displayed. Set to 1, which means "Show one label per tab", if the value is 2, it means that one label is displayed between two labels, and so on.

* xaxis_force_interval -> int/str  
    Forces the x-axis split interval. If set to 50, the scale is [0, 50, 150, ...], and when set to "auto", only two scales are displayed. It is not recommended to set this parameter in general! !
    Because `splitNumber` is the estimated value, the scale calculated by the actual strategy may not achieve the desired effect. In this case, you can use `interval` and `min`, `max` to force the scale division. Invalid in the category axis.

* xaxis_margin -> int  
    The distance between the x-axis scale label and the axis line. Default is 8

* xaxis_name -> str  
    Name of xAxis

* xaxis_name_size -> int  
    Axis name font size, default is 14

* xaxis_name_gap -> int  
    Gap between axis name and axis line, default is 25

* xaxis_name_pos -> str  
    Location of xAxis name.It can be 'start'，'middle'，'end'

* xaxis_min -> int/float  
    The minimun value of xaxis. Default is adaptive. Use the special value "dataMin" to customize the minimum value in the data to the minimum value of the x-axis.

* xaxis_max -> int/float  
    The maximun value of xaxis. Default is adaptive. Use the special value "dataMax" to customize the minimum value in the data to the x-axis maximum

* xaxis_pos -> str  
    x axis position, with 'top', 'bottom' optional

* xaxis_label_textsize -> int  
    x axis label font size, default is 12

* xaxis_label_textcolor -> str  
    x axis label font color, default is "#000"

* xaxis_type -> str  
    Type of xaxis
    * 'value': Numerical axis, suitable for continuous data.
    * 'category': Category axis, suitable for discrete category data. Data should only be set via data for this type.
    * 'time': Time axis, suitable for continuous time series data. As compared to value axis,it has a better formatting for time and a different tick calculation method. For example,it decides to use month, week, day or hour for tick based on the range of span.
    * 'log': Log axis, suitable for log data.

* xaxis_rotate -> int  
    Rotation degree of xaxis label, which is especially useful when there is no enough space for category axis.Default is 0, ie no rotation. Rotation degree is from -90 to 90.

* xaxis_formatter -> str/function  
    The x-axis label formatter, such as 'day', the label of the x-axis is data plus 'day' (3 days, 4 days), the default is ""
    ```python
    def label_formatter(params):
        return params.value + ' [Good!]'
    ```
    Callback function format, please refer to [Advanced Usage](en-us/advanced) for more details.
    ```
    (params: Object|Array) => string
    参数 params 是 formatter 需要的单个数据集。格式如下：
    {
        componentType: 'series',
        // Series type
        seriesType: string,
        // The index of the series in the passed option.series
        seriesIndex: number,
        // Series name
        seriesName: string,
        // Data name, category name
        name: string,
        // The index of the data in the input data array
        dataIndex: number,
        // Input raw data item
        data: Object,
        // Input data value
        value: number|Array,
        // Data graphic color
        color: string,
    }
    ```

* xaxis_line_color -> str  
    The color of the x coordinate axis line. The default is None.

* xaxis_line_width -> int  
    The width of the x coordinate axis line, default is 1


* y_axis -> list  
    yAxis data

* yaxis_interval -> int  
    The display interval of the y-axis scale label is valid in the category axis. By default, labels are displayed with intervals that do not overlap labels.
    Set to 0 to force all labels to be displayed. Set to 1, which means "Show one label per tab", if the value is 2, it means that one label is displayed between two labels, and so on.

* yaxis_force_interval -> int/str  
    Forces the y-axis split interval. If set to 50, the scale is [0, 50, 150, ...], and when set to "auto", only two scales are displayed. It is not recommended to set this parameter in general! !
    Because `splitNumber` is the estimated value, the scale calculated by the actual strategy may not achieve the desired effect. In this case, you can use `interval` and `min`, `max` to force the scale division. Invalid in the category axis.

* yaxis_margin -> int  
    The distance between the y-axis scale label and the axis. Default is 8

* yaxis_formatter -> str/function   
    The y-axis label formatter, such as 'day', the label of the y-axis is data plus 'day' (3 days, 4 days), the default is ""
    ```python
    def label_formatter(params):
        Return params.value + ' [Good!]'
    ```
    Callback function format, please refer to [Advanced Usage](en-us/advanced) for more details.
    ```
    (params: Object|Array) => string
    The parameter params is the single data set required by the formatter. The format is as follows:
    {
        componentType: 'series',
        // series type
        seriesType: string,
        // The index of the series in the passed option.series
        seriesIndex: number,
        // series name
        seriesName: string,
        // data name, category name
        Name: string,
        // the index of the data in the passed in data array
        dataIndex: number,
        // input raw data item
        Data: Object,
        // input data value
        Value: number|Array,
        // color of the data graphic
        Color: string,
    }
    ```

* yaxis_name -> str  
    Name of yAxis

* yaxis_name_size -> int  
    y axis name body size, default is 14

* yaxis_name_gap -> int  
    The distance between the y axis name and the axis line. Default is 25

* yaxis_name_pos -> str  
    Location of yAxis name. It can be 'start'，'middle'，'end'

* yaxis_min -> int/float  
    The minimun value of yaxis. Use the special value `"dataMin"` to customize the minimum value in the data to the minimum value of the y-axis.

* yaxis_max -> int/float  
    The maximun value of yaxis. Use the special value `"dataMax"` to customize the maximum value in the data to the maximum value of the y-axis.

* yaxis_pos -> str  
    y coordinate position, with 'left', 'right' optional.

* yaxis_label_textsize -> int  
    y axis label font size, default is 12

* yaxis_label_textcolor -> str  
    y axis label font color, default is "#000"

* yaxis_type -> str  
    Type of yaxis
    * 'value': Numerical axis, suitable for continuous data.
    * 'category': Category axis, suitable for discrete category data. Data should only be set via data for this type.
    * 'time': Time axis, suitable for continuous time series data. As compared to value axis, it has a better formatting for time and a different tick calculation method. For example, it decides to use month, week, day or hour for tick based on the range of span.
    * 'log': Log axis, suitable for log data.

* yaxis_rotate -> int  
    Rotation degree of xaxis label, which is especially useful when there is no enough space for category axis.Rotation degree is from -90 to 90.

* yaxis_line_color -> str  
    The color of the y coordinate axis. Default is None.

* yaxis_line_width -> int  
    y coordinate axis width, default is 1


### dataZoom
**dataZoom components for zoom-in and zoom-out. With them, it is possible to magnify a small area, to see the overall picture or to stay away from scattered points(Line, Bar, Scatter, EffectScatter, Kline)**

Default dataZoom control bar
* is_datazoom_show -> bool  
    Whether to use the area zoom component, default is False

* datazoom_type -> str      
    Area zoom component type, defaults to 'slider', with 'slider', 'inside', 'both' optional  

* datazoom_range -> list  
    Range of area zoom, default is [50, 100]

* datazoom_orient -> str  
    The direction of datazoom component in the Cartesian coordinate system. Default is 'horizontal' and the effect is displayed on the x-axis. If set to 'vertical', the effect is displayed on the y-axis.

* datazoom_xaxis_index -> int/list  
    The x-axis index controlled by the datazoom component.
    The first x-axis is controlled by default, and no specification is required if there is no special requirement. A single type is int and multiple are controlled as a list type, such as [0, 1] to control the first and second x axes.

* datazoom_yaxis_index -> int/list  
    The y-axis index controlled by the datazoom component
    The first y axis is controlled by default, and no specification is required if there is no special requirement. A single type is int and multiple are controlled as a list type, such as [0, 1] to control the first and second x axes.

Extra dataZoom control strip
* is_datazoom_extrashow -> bool  
    Whether to use the extra area zoom component, default is False

* datazoom_extra_type -> str  
    Extra area zoom component type, default is 'slider', with 'slider', 'inside', 'both' optional

* datazoom_extra_range -> list  
    Range of extra area zoom, default is [50, 100]

* datazoom_extra_orient -> str  
    The direction of the extra datazoom component in the Cartesian coordinate system. The default is 'vertical' and the effect is displayed on the y axis. If set to 'horizontal', the effect is displayed on the x-axis.

* datazoom_extra_xaxis_index -> int/list  
    X-axis index controlled by additional datazoom component
    The first x-axis is controlled by default, and no specification is required if there is no special requirement. A single type is int and multiple are controlled as a list type, such as [0, 1] to control the first and second x axes.

* datazoom_extra_yaxis_index -> int/list  
    The y-axis index controlled by the extra datazoom component
    The first y axis is controlled by default, and no specification is required if there is no special requirement. A single type is int and multiple is controlled as a list type, such as [0, 1] to control the first and second x axes.


### legend
**legend component has different symbol, color and name, and provide the interactive clicking functions to show or hide its associated data series.**

* is_legend_show -> bool  
    Whether to display the top legend, default is True

* legend_orient -> str  
    The layout of the legend list, default is 'horizontal'.
    'horizontal', 'vertical' optional

* legend_pos -> str  
    defalut -> 'center'  
    Distance between legend component and the left side of the container.  
    legend_pos value can be instant pixel value like 20;it can also be percentage value relative to container width like '20%'; And it can also be 'left', 'center', or 'right'.

* legend_top -> str  
    defalut -> 'top'  
    Distance between legend component and the top side of the container.  
    legend_top value can be instant pixel value like 20;it can also be percentage value relative to container width like '20%';
    and it can also be 'top', 'middle', or 'bottom'.

* legend_selectedmode -> str/bool  
    State table of selected legend. 'single' or  'multiple'. Or use `False` to disable it.

* legend_text_size -> int  
    Legend name font size

* legend_text_color -> str  
    Legend name font color


### label
**Text string on the chart, for marking the charts with sensible details, such as value, name.**

* is_label_show -> bool  
    defalut -> False  
    It specifies whether to show laebl in normal status.

* is_label_emphasis -> bool  
    defalut -> True  
    It specifies whether to show label in emphasis status.

* label_pos -> str  
    defalut -> 'top'  
    Label position. It can be 'top', 'left', 'right', 'bottom', 'inside','outside'

* label_emphasis_pos -> str  
    Highlight the position of the label, the Bar map defaults to 'top'. Available with 'top', 'left', 'right', 'bottom', 'inside', 'outside'

* label_text_color -> str      
    defalut -> '#000'  
    Label text color.

* label_emphasis_textcolor -> str  
    default -> "#fff"  
    Highlight the label font color, 

* label_text_size -> int  
    defalut -> 12  
    Label font size.

* label_emphasis_textsize -> int  
    default -> 12   
    Highlight label font size.

* is_random -> bool  
    defalut -> False  
    It specifies whether to random global color list.

* label_color -> list  
    Customize the label color. It will modify global color list, and all chart legend colors can be config here. Such as Bar's column color, Line's line color, and so on.

* label_formatter -> str   
    Template variables are {a}, {b}, {c}, {d}, {e}, which represent the series name, data name, data value, and so on. For examples `label_formatter='{a}'`
    When the `trigger` is `'axis'`, there will be multiple series of data. In this case, the index of the series can be represented by {a0}, {a1}, {a2}. 
    {a}, {b}, {c}, {d} under different chart types have different meanings. The variables {a}, {b}, {c}, {d} represent the meaning of the data under different chart types:

    * Line (area), column (bar), K-line: {a} (series name), {b} (category value), {c} (value), {d} (none)
    * Scatter plot (bubble) graph: {a} (series name), {b} (data name), {c} (value array), {d} (none)
    * Maps: {a} (series name), {b} (area name), {c} (merged value), {d} (none)
    * Pie chart, dashboard, funnel chart: {a} (series name), {b} (data item name), {c} (value), {d} (percent)
    
* Label_formatter -> function  
    For details, please refer to xaxis_formatter -> function

**Note：** is_random random disorganize legend colour and list,it's kind of switch style? try it.


### lineStyle
**line style for Line, Polar, Radar, Graph, Parallel.**

* line_width -> int   
    default -> 1   
    Line width.

* line_opacity -> float   
    default -> 1  
    Opacity of the component. Supports value from 0 to 1, and the component will not be drawn when set to 0.

* line_curve -> float   
    default -> 0  
    Edge curvature, which supports value from 0 to 1. The larger the value, the greater curvature.

* line_type -> str       
    default -> 'solid'  
    Line type,it can be 'solid', 'dashed', 'dotted'

* line_color -> str  
    Line color


### grid3D
**gird3D components in cartesian coordinate system (Bar3D, Line3D, Scatter3D, Surface3D)**

* grid3d_width -> int  
    default -> 100       
    Width of grid3D component. 

* grid3d_height -> int  
    default -> 100   
    Height of grid3D component.

* grid3d_depth -> int  
    default -> 100  
    Depth of the three-dimensional Cartesian coordinate system component in a three-dimensional scene.

* is_grid3d_rotate -> bool  
    default -> False
    Whether to turn on the automatic rotation view of the angle around the object.

* grid3d_rotate_speed -> int  
    The speed of autobiography of objects. The unit is angle / second, default is 10, which is 36 seconds.

* grid3d_rotate_sensitivity -> int  
    The sensitivity of the rotation operation, the greater the value, the more sensitive. Default is 1, and it cannot be rotated after setting it to 0.

### axis3D
**3D Cartesian coordinate system X, Y, Z axis configuration items for 3D graphics. (Bar3D, Line3D, Scatter3D, Surface3D)**

#### 3D X-axis
* xaxis3d_name -> str  
    x axis name, default is ""

* xaxis3d_name_size -> int  
    x axis name body size, default is 16

* xaxis3d_name_gap -> int  
    The distance between the x-axis name and the axis. Default is 25

* xaxis3d_min -> int/float  
    x Axis scale minimum, default is adaptive.

* xaxis3d_max -> int/float  
    The maximum value of the x axis scale. Default is adaptive.

* xaxis3d_interval -> int  
    The display interval of the x-axis scale labels is valid in the category axis. By default, labels are displayed with policy intervals that do not overlap labels.  
    Set to 0 to force all labels to be displayed. Set to 1, which means "Show one label per tab", if the value is 2, it means that one label is displayed between two labels, and so on.

* xaxis3d_margin -> int  
    The distance between the x-axis scale label and the axis. Default is 8

#### 3D Y-axis

* yaxis3d_name -> str  
    y axis name, default is ""

* yaxis3d_name_size -> int  
    y axis name body size, default is 16

* yaxis3d_name_gap -> int  
    The distance between the y axis name and the axis. Default is 25

* yaxis3d_min -> int/float  
    y Axis scale minimum, default is adaptive.

* yaxis3d_max -> int/float  
    y Axis scale maximum, default is adaptive.

* yaxis3d_interval -> int  
    The display interval of the y-axis scale label is valid in the category axis. By default, labels are displayed with policy intervals that do not overlap labels.  
    Set to 0 to force all labels to be displayed. Set to 1, which means "Show one label per tab", if the value is 2, it means that one label is displayed between two labels, and so on.

* yaxis3d_margin -> int  
    The distance between the y-axis scale label and the axis. Default is 8

#### 3D Z axis

* zaxis3d_name -> str  
    z axis name, default is ""

* zaxis3d_name_size -> int  
    z axis name body size, default is 16

* zaxis3d_name_gap -> int  

    The distance between the z-axis name and the axis. The default is 25

* zaxis3d_min -> int/float  
    z Axis scale minimum, default is adaptive.

* zaxis3d_max -> int/float  
    The maximum value of the z coordinate scale, default is adaptive.

* zaxis3d_margin -> int  
    The distance between the z-axis scale label and the axis. The default is 8


### visualMap

**It is a type of component for visual encoding, which maps the data to visual channels.**

* is_visualmap -> bool  
    Whether to use the visual mapping component

* visual_type -> str  
    Formulate the component mapping method, default is 'color'. That is, the value is mapped by color. There are 'color' and 'size' is optional. 'size' maps values ​​by the size of the numeric point, which is the size of the graphic point.

* visual_range -> list  
    default -> [0, 100]  
    Specify the min and max dataValue for the visualMap component.

* visual_text_color -> str  
    visualMap text color.

* visual_range_text -> list  
    default -> ['low', 'hight']  
    The label text on both ends.

* visual_range_color -> list  
    default -> ['#50a3ba', '#eac763', '#d94e5d']  
    For visual channel color, array is used, like: ['#333', '#78ab23', 'blue'].

* visual_range_size -> list  
    default -> [20, 50]  
    For visual channel size, array is used.

* visual_orient -> str  
    default -> 'vertical'
    How to layout the visualMap component, 'horizontal' or 'vertical'.

* visual_pos -> str/int  
    default -> 'left'  
    Distance between visualMap component and the left side of the container.  
    visual_pos value can be instant pixel value like 20;it can also be percentage value relative to container width like '20%';and it can also be 'left', 'center', or 'right'.

* visual_top -> str/int  
    default -> 'top'  
    Distance between visualMap component and the top side of the container.  
    visual_top value can be instant pixel value like 20;it can also be percentage value relative to container width like '20%';and it can also be 'top', 'middle', or 'bottom'.

* visual_split_number -> int  
    default -> 5
    The number of segments split in the segmentation type. It takes effect when be set to segmentation. Default is divided into 5 segments.

* visual_dimension -> int  
    Specify which dimension of the data to use to map to the visual element. Default is mapped to the last dimension. The index starts at 0.  
    In a Cartesian coordinate system, the x-axis is the first dimension (0) and the y-axis is the second dimension (1).

* is_calculable -> bool  
    default -> True
    Whether show handles, which can be dragged to adjust "selected range".

* is_piecewise -> bool  
    default -> False
    Whether to convert the component to segmentation (the default is continuous)

* pieces -> list  
    Customize the scope of each segment of the "segmented visual mapping component (visualMapPiecewise)".  
    And the text of each paragraph, as well as the special style of each paragraph. (Only effective when is_piecewise is True) For example:
    ``` 
    pieces: [
        {min: 1500}, // If max is not specified, max is infinity.
        {min: 900, max: 1500},
        {min: 310, max: 1000},
        {min: 200, max: 300},
        {min: 10, max: 200, label: '10 到 200（自定义label）'},
        // Indicates that value is equal to 123.
        {value: 123, label: '123（自定义特殊颜色）', color: 'grey'}
        {max: 5}     // If min is not specified, min is infinity (-Infinity).
    ]
    ```

### tooltip
**Tip box component for popping data content when moving or clicking the mouse**

* tooltip_trigger -> str  
    Trigger type. Default is 'item'  
    * 'item': Data item graph triggering, mainly used in charts with no category axes such as scatter plots and pie charts.
    * 'axis': Axis triggering, mainly used in charts that use the category axis, such as histograms, line charts, etc.
    * 'none': Nothing triggers.

* tooltip_trigger_on -> str  
    The condition triggered by the prompt box. Default is "mousemove|click"
    * 'mousemove': Triggered when the mouse is moving.
    * 'click': Triggered when the mouse is clicked.
    * 'mousemove|click': Triggered when the mouse moves and clicks at the same time.
    * 'none': No trigger in 'mousemove' or 'click'.

* tooltip_axispointer_type -> str  
    Indicator type. Default is "line"
    * 'line': line indicator.
    * 'shadow': shadow indicator.
    * 'cross': Crosshair indicator. In fact, it is shorthand, which means that the axisPointer of two orthogonal axes is enabled.

* tooltip_formatter -> str  
    Template variables are {a}, {b}, {c}, {d}, {e}, which represent the series name, data name, data value, and so on.  
    When the trigger is 'axis', there will be multiple series of data. In this case, the index of the series can be represented by {a0}, {a1}, {a2}. {a}, {b}, {c}, {d} under different chart types have different meanings. The variables {a}, {b}, {c}, {d} represent the meaning of the data under different chart types:
    * Line (area), column (bar), K-line: {a} (series name), {b} (category value), {c} (value), {d} (none)
    * Scatter plot (bubble) graph: {a} (series name), {b} (data name), {c} (value array), {d} (none)
    * Maps: {a} (series name), {b} (area name), {c} (merged value), {d} (none)
    * Pie chart, dashboard, funnel chart: {a} (series name), {b} (data item name), {c} (value), {d} (percent)
    
* tooltip_formatter -> function  
    For details, please refer to xaxis_formatter -> function

* tooltip_text_color -> str  
    Prompt box font color, defaults is '#fff'

* tooltip_font_size -> int  
    Prompt box font size, default is 14

* tooltip_background_color -> str  
    The background color of the floating layer of the prompt box. Default is "rgba(50,50,50,0.7)"

* tooltip_border_color -> str  
    The border color of the floating layer of the prompt box. Default is "#333"

* tooltip_border_width -> int/float  
    The border of the floating layer of the prompt box is wide. Default is 0


### markLine-markPoint
**Graphic mark component for marking specified special data. There are marker line and marker point (Bar, Line, Kline)**

* mark_point -> list  
    Mark points, default is `'min'`. `'max'`, `'average'` is optional. Support custom mark points, the specific usage is as follows :  
    [{"coord": [a1, b1], "name": "first markpoint"}, {"coord": [a2, b2], "name": "second markpoint"}]  
    You need to pass in the point dictionary yourself. There are two key-value pairs. 'coord' corresponds to x y axis coordinates, and 'name' is the point name.

* mark_point_symbol -> str  
    Point graphic, default is `'pin'`. `'circle'`, `'rect'`, `'roundRect'`, `'triangle'`, `'diamond'`, `'pin'`, `'arrow'` optional

* mark_point_symbolsize -> int  
    Mark point graphic size, default is 50

* mark_point_textcolor -> str  
    Mark the dot font color, the default is '#fff'

* mark_line -> list  
    Marker line, default is `'min'`. `'max'`, `'average'` optional

* mark_line_symbolsize -> int  
    Mark line graphic size, default is 15

* mark_line_valuedim -> list  
    The marker line specifies in which dimension the maximum and minimum values ​​are specified. This can be the dimension name. The Line chart can be x, angle, etc. And the Kline chart can be open, close, highest, lowest.  
    Multiple dimensions can be developed at the same time, such as:  
    
    Mark_line=['min', 'max'],   
    mark_line_valuedim=['lowest', 'highest']   
    
    means min uses the lowest dimension, max uses the highest dimension, and so on

* mark_line_coords -> list  
    The marker line specifies the starting point coordinates and the ending point coordinates, such as [[10, 10], [30, 30]]. And the two points are the horizontal and vertical axis points.

* mark_point_valuedim -> list  
    The marker line specifies in which dimension the maximum and minimum values ​​are specified. This can be the dimension name, the Line chart can be x, angle, etc., and the Kline chart can be open, close, highest, lowest.  
    Multiple dimensions can be developed at the same time, such as:  

    Mark_point=['min', 'max'],   
    mark_point_valuedim=['lowest', 'highest']   
    
    means min uses the lowest dimension, max uses the highest dimension, and so on


### toolbox
**The right utility toolbox**

* is_toolbox_show - > bool  
    Specifies whether to display the right utility toolbox. The default is True.

* is_more_utils - > bool  
    Specifies whether to provide more utility buttons. By default, only the "Data View" and "Download" buttons are available.

**If you have read this document, you can read further [Chart Basic](en-us/charts_base)**
