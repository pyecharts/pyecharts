> 图表配置篇：本篇文档为 pyecharts 的主要配置文档，介绍了关于 pyecharts 的详细配置项。

* 图形初始化
* 通用配置项
    * xyAxis：平面直角坐标系中的 x、y 轴。(Line、Bar、Scatter、EffectScatter、Kline)
    * dataZoom：dataZoom 组件 用于区域缩放，从而能自由关注细节的数据信息，或者概览数据整体，或者去除离群点的影响。(Line、Bar、Scatter、EffectScatter、Kline、Boxplot)
    * legend：图例组件。图例组件展现了不同系列的标记(symbol)，颜色和名字。可以通过点击图例控制哪些系列不显示。
    * label：图形上的文本标签，可用于说明图形的一些数据信息，比如值，名称等。
    * lineStyle：带线图形的线的风格选项(Line、Polar、Radar、Graph、Parallel)
    * grid3D：3D笛卡尔坐标系组配置项，适用于 3D 图形。（Bar3D, Line3D, Scatter3D, Surface3D)
    * axis3D：3D 笛卡尔坐标系 X，Y，Z 轴配置项，适用于 3D 图形。（Bar3D, Line3D, Scatter3D, Surface3D)
    * visualMap：是视觉映射组件，用于进行『视觉编码』，也就是将数据映射到视觉元素（视觉通道）
    * markLine-markPoint：图形标记组件，用于标记指定的特殊数据，有标记线和标记点两种。（Bar、Line、Kline）
    * tooltip：提示框组件，用于移动或点击鼠标时弹出数据内容
    * toolbox：右侧实用工具箱


## 图形初始化

> 图表类初始化所接受的参数（所有类型的图表都一样）。

* title -> str  
    默认 -> ""  
    主标题文本，支持 \n 换行。

* subtitle -> str  
    默认 -> ""  
    副标题文本，支持 \n 换行。

* width -> int  
    默认 -> 800（px）  
    画布宽度。

* height -> int  
    默认 -> 400（px）  
    画布高度。

* title_pos -> str/int  
    默认 -> 'left'  
    标题距离左侧距离，有'auto', 'left', 'right', 'center'可选，也可为百分比或整数

* title_top -> str/int  
    默认 -> 'top'  
    标题距离顶部距离，有'top', 'middle', 'bottom'可选，也可为百分比或整数

* title_color -> str
    默认 -> '#000'  
    主标题文本颜色。

* subtitle_color -> str  
    默认 ->  '#aaa'  
    副标题文本颜色。

* title_text_size -> int  
    默认 -> 18  
    主标题文本字体大小。

* subtitle_text_size -> int  
    默认 -> 12  
    副标题文本字体大小。

* background_color -> str  
    默认 -> '#fff'  
    画布背景颜色。

* page_title -> str  
    默认 -> 'Echarts'  
    指定生成的 html 文件中 `<title>` 标签的值。

* renderer -> str  
    默认 -> 'canvas'  
    指定使用渲染方式，有 'svg' 和 'canvas' 可选。3D 图仅能使用 'canvas'。

* extra_html_text_label -> list  
    额外的 HTML 文本标签，`(<p> 标签)`。类型为 list，list[0] 为文本内容，list[1] 为字体风格样式（选填）。如 ["this is a p label", "color:red"]。**仅限于在单个图形或者 page 类时使用。**

* is_animation -> bool  
    默认 -> True  
    是否开启动画。V0.5.9+

## 通用配置项

> 通用配置项均在 ```add()``` 中设置

### xyAxis
**平面直角坐标系中的 x、y 轴。(Line、Bar、Scatter、EffectScatter、Kline)**

* is_convert -> bool  
    是否交换 x 轴与 y 轴

* is_xaxislabel_align -> bool  
    默认 -> False  
    x 轴刻度线和标签是否对齐。

* is_yaxislabel_align -> bool  
    默认 -> False  
    y 轴刻度线和标签是否对齐。

* is_xaxis_inverse -> bool  
    默认 -> False  
    是否反向 x 坐标轴。

* is_yaxis_inverse -> bool  
    默认 -> False  
    是否反向 y 坐标轴。

* is_xaxis_boundarygap -> bool  
    默认 -> True  
    x 轴两边留白策略，适用于类目轴。类目轴中 boundaryGap 可以配置为 True 和 False。这时候刻度只是作为分隔线，标签和数据点都会在两个刻度之间的带(band)中间，即两边留白。

* is_yaxis_boundarygap -> bool  
    默认 -> True  
    y 轴两边留白策略，适用于类目轴。类目轴中 boundaryGap 可以配置为 True 和 False。这时候刻度只是作为分隔线，标签和数据点都会在两个刻度之间的带(band)中间，即两边留白。

* is_xaxis_show -> bool  
    是否显示 x 轴

* is_yaxis_show -> bool  
    是否显示 y 轴

* is_splitline_show -> bool  
    默认 -> True  
    是否显示 y 轴网格线。

* x_axis -> list  
    x 轴数据项

* xaxis_interval -> int  
    x 轴刻度标签的显示间隔，在类目轴中有效。默认会采用标签不重叠的策略间隔显示标签。  
    设置成 0 强制显示所有标签。设置为 1，表示『隔一个标签显示一个标签』，如果值为 2，表示隔两个标签显示一个标签，以此类推

* xaxis_force_interval -> int/str  
    强制设置 x 坐标轴分割间隔。如设置为 50 则刻度为 [0, 50, 150, ...]，设置为 "auto" 则只显示两个刻度。一般情况下不建议设置这个参数！！  
    因为 splitNumber 是预估的值，实际根据策略计算出来的刻度可能无法达到想要的效果，这时候可以使用 interval 配合 min、max 强制设定刻度划分。在类目轴中无效。

* xaxis_margin -> int  
    默认 -> 8  
    x 轴刻度标签与轴线之间的距离。

* xaxis_name -> str  
    x 轴名称

* xaxis_name_size -> int  
    默认 -> 14  
    x 轴名称体大小。

* xaxis_name_gap -> int  
    默认 -> 25  
    x 轴名称与轴线之间的距离。

* xaxis_name_pos -> str  
    x 轴名称位置，有'start'，'middle'，'end'可选

* xaxis_min -> int/float  
    x 坐标轴刻度最小值，默认为自适应。使用特殊值 "dataMin" 可自定以数据中最小值为 x 轴最小值。

* xaxis_max -> int/float  
    x 坐标轴刻度最大值，默认为自适应。使用特殊值 "dataMax" 可自定以数据中最小值为 x 轴最大值。

* xaxis_pos -> str  
    x 坐标轴位置，有'top','bottom'可选

* xaxis_label_textsize -> int  
    默认 -> 12  
    x 坐标轴标签字体大小。

* xaxis_label_textcolor -> str  
    默认 -> "#000"  
    x 坐标轴标签字体颜色。

* xaxis_type -> str  
    x 坐标轴类型  
    * 'value'：数值轴，适用于连续数据。
    * 'category'：类目轴，适用于离散的类目数据。
    * 'log'：对数轴。适用于对数数据。

* xaxis_rotate -> int  
    默认 -> 0（即不旋转）  
    x 轴刻度标签旋转的角度，在类目轴的类目标签显示不下的时候可以通过旋转防止标签之间重叠。旋转的角度从 -90 度到 90 度。

* xaxis_formatter -> str  
    默认 ->  ""  
    x 轴标签格式器，如 '天'，则 x 轴的标签为数据加'天'(3 天，4 天)。
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

* xaxis_line_color -> str  
    默认 -> None  
    x 坐标轴线线的颜色。

* xaxis_line_width -> int  
    默认 -> 1  
    x 坐标轴线线的宽度。

* y_axis -> list  
    y 坐标轴数据

* yaxis_interval -> int  
    y 轴刻度标签的显示间隔，在类目轴中有效。默认会采用标签不重叠的策略间隔显示标签。  
    设置成 0 强制显示所有标签。设置为 1，表示『隔一个标签显示一个标签』，如果值为 2，表示隔两个标签显示一个标签，以此类推

* yaxis_force_interval -> int/str  
    强制设置 y 坐标轴分割间隔。如设置为 50 则刻度为 [0, 50, 150, ...]，设置为 "auto" 则只显示两个刻度。一般情况下不建议设置这个参数！！  
    因为 splitNumber 是预估的值，实际根据策略计算出来的刻度可能无法达到想要的效果，这时候可以使用 interval 配合 min、max 强制设定刻度划分。在类目轴中无效。

* yaxis_margin -> int  
    默认 -> 8  
    y 轴刻度标签与轴线之间的距离。

* yaxis_formatter -> str  
    默认 -> ""  
    y 轴标签格式器，如 '天'，则 y 轴的标签为数据加'天'(3 天，4 天)。
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
    ```

* yaxis_name -> str  
    y 轴名称

* yaxis_name_size -> int  
    默认 -> 14  
    y 轴名称体大小。

* yaxis_name_gap -> int  
    默认 -> 25  
    y 轴名称与轴线之间的距离。

* yaxis_name_pos -> str  
    y 轴名称位置，有'start', 'middle'，'end'可选

* yaxis_min -> int/float  
    y 坐标轴刻度最小值，默认为自适应。使用特殊值 "dataMin" 可自定以数据中最小值为 y 轴最小值。

* yaxis_max -> int/float  
    y 坐标轴刻度最大值，默认为自适应。使用特殊值 "dataMax" 可自定以数据中最大值为 y 轴最大值。

* yaxis_pos -> str  
    y 坐标轴位置，有'left','right'可选

* yaxis_label_textsize -> int  
    默认 -> 12  
    y 坐标轴标签字体大小。

* yaxis_label_textcolor -> str  
    默认 -> "#000"  
    y 坐标轴标签字体颜色。

* yaxis_type -> str  
    y 坐标轴类型  
    * 'value'：数值轴，适用于连续数据。
    * 'category'：类目轴，适用于离散的类目数据。
    * 'log'：对数轴。适用于对数数据。

* yaxis_rotate -> int  
    默认 -> 0（即不旋转）  
    y 轴刻度标签旋转的角度，在类目轴的类目标签显示不下的时候可以通过旋转防止标签之间重叠。旋转的角度从 -90 度到 90 度。

* yaxis_line_color -> str  
    默认 -> None  
    y 坐标轴线线的颜色。

* yaxis_line_width -> int  
    默认 -> 1  
    y 坐标轴线线的宽度。


### dataZoom
**dataZoom 组件 用于区域缩放，从而能自由关注细节的数据信息，或者概览数据整体，或者去除离群点的影响。(Line、Bar、Scatter、EffectScatter、Kline)**

**默认的 dataZoom 控制条**

* is_datazoom_show -> bool  
    默认 -> False  
    是否使用区域缩放组件。

* datazoom_type -> str  
    默认 -> 'slider'  
    区域缩放组件类型，有'slider', 'inside', 'both'可选。

* datazoom_range -> list  
    默认 -> [50, 100]  
    区域缩放的范围。

* datazoom_orient -> str  
    默认 -> 'horizontal'（效果显示在 x 轴）  
    datazoom 组件在直角坐标系中的方向。如若设置为 'vertical' 的话效果显示在 y 轴。

* datazoom_xaxis_index -> int/list  
    datazoom 组件控制的 x 轴索引  
    默认控制第一个 x 轴，如没特殊需求无须显示指定。单个为 int 类型而控制多个为 list 类型，如 [0, 1] 表示控制第一个和第二个 x 轴。

* datazoom_yaxis_index -> int/list  
    datazoom 组件控制的 y 轴索引  
    默认控制第一个 y 轴，如没特殊需求无须显示指定。单个为 int 类型而控制多个为 list 类型，如 [0, 1] 表示控制第一个和第二个 x 轴。

**额外的 dataZoom 控制条**

* is_datazoom_extra_show -> bool  
    默认 -> False  
    是否使用额外区域缩放组件。

* datazoom_extra_type -> str  
    默认 ->  'slider'  
    额外区域缩放组件类型，有'slider', 'inside', 'both'可选

* datazoom_extra_range -> list  
    默认 -> [50, 100]  
    额外区域缩放的范围。

* datazoom_extra_orient -> str  
    额外 datazoom 组件在直角坐标系中的方向，默认为 'vertical'，效果显示在 y 轴。如若设置为 'horizontal' 的话效果显示在 x 轴。

* datazoom_extra_xaxis_index -> int/list  
    额外 datazoom 组件控制的 x 轴索引
    默认控制第一个 x 轴，如没特殊需求无须显示指定。单个为 int 类型而控制多个为 list 类型，如 [0, 1] 表示控制第一个和第二个 x 轴。

* datazoom_extra_yaxis_index -> int/list  
    额外 datazoom 组件控制的 y 轴索引
    默认控制第一个 y 轴，如没特殊需求无须显示指定。单个为 int 类型而控制多个为 list 类型，如 [0, 1] 表示控制第一个和第二个 x 轴。


### legend
**图例组件。图例组件展现了不同系列的标记(symbol)，颜色和名字。可以通过点击图例控制哪些系列不显示。**

* is_legend_show -> bool  
    默认 -> True  
    是否显示顶端图例。

* legend_orient -> str  
    默认 -> 'horizontal'  
    图例列表的布局朝向，有'horizontal', 'vertical'可选。

* legend_pos -> str  
    默认 -> 'center'  
    图例组件离容器左侧的距离，有'left', 'center', 'right'可选，也可以为百分数，如"60%"。

* legend_top -> str  
    默认 -> 'top'  
    图例组件离容器上侧的距离，有'top', 'center', 'bottom'可选，也可以为百分数，如"60%"。

* legend_selectedmode -> str/bool  
    默认 -> 'multiple'  
    图例选择的模式，控制是否可以通过点击图例改变系列的显示状态。可以设成 'single' 或者 'multiple' 使用单选或者多选模式。也可以设置为 False 关闭显示状态。

* legend_text_size -> int  
    图例名称字体大小。

* legend_text_color -> str  
    图例名称字体颜色。
    

### label
**图形上的文本标签，可用于说明图形的一些数据信息，比如值，名称等。**

* is_label_show -> bool  
    默认 -> False  
    是否正常显示标签。标签即各点的数据项信息。

* is_label_emphasis -> bool  
    默认 -> True  
    是否高亮显示标签。高亮标签即选中数据时显示的信息项。

* label_pos -> str  
    标签的位置，Bar 图默认为'top'。有'top', 'left', 'right', 'bottom', 'inside','outside'可选

* label_emphasis_pos -> str  
    高亮标签的位置，Bar 图默认为'top'。有'top', 'left', 'right', 'bottom', 'inside','outside'可选

* label_text_color -> str  
    默认 -> "#000"  
    标签字体颜色。

* label_emphasis_textcolor -> str  
    默认 -> "#fff"  
    高亮标签字体颜色。

* label_text_size -> int  
    默认 -> 12  
    标签字体大小。

* label_emphasis_textsize -> int  
    默认 -> 12  
    高亮标签字体大小。

* is_random -> bool  
    默认 -> False  
    是否随机排列颜色列表。

* label_color -> list  
    自定义标签颜色。全局颜色列表，所有图表的图例颜色均在这里修改。如 Bar 的柱状颜色，Line 的线条颜色等等。

* label_formatter -> str  
    模板变量有 {a}, {b}，{c}，{d}，{e}，分别表示系列名，数据名，数据值等。使用示例，如 `label_formatter='{a}'`  
    在 trigger 为 'axis' 的时候，会有多个系列的数据，此时可以通过 {a0}, {a1}, {a2} 这种后面加索引的方式表示系列的索引。不同图表类型下的 {a}，{b}，{c}，{d} 含义不一样。 其中变量 {a}, {b}, {c}, {d} 在不同图表类型下代表数据含义为：
    * 折线（区域）图、柱状（条形）图、K线图 : {a}（系列名称），{b}（类目值），{c}（数值）, {d}（无）
    * 散点图（气泡）图 : {a}（系列名称），{b}（数据名称），{c}（数值数组）, {d}（无）
    * 地图 : {a}（系列名称），{b}（区域名称），{c}（合并数值）, {d}（无）
    * 饼图、仪表盘、漏斗图: {a}（系列名称），{b}（数据项名称），{c}（数值）, {d}（百分比）
    
    label_formatter -> function  
    具体格式请参考 xaxis_formatter -> function

**Note：** is_random 可随机打乱图例颜色列表。


### lineStyle
**带线图形的线的风格选项(Line、Polar、Radar、Graph、Parallel)**

* line_width -> int  
    默认 -> 1  
    线的宽度。

* line_opacity -> float  
    默认 -> 1  
    线的透明度，0 为完全透明，1 为完全不透明。

* line_curve -> float  
    默认 -> 0  
    线的弯曲程度，0 为完全不弯曲，1 为最弯曲。

* line_type -> str  
    默认 -> 'solid'  
    线的类型，有'solid', 'dashed', 'dotted'可选。

* line_color -> str  
    线的颜色


### grid3D
**3D 笛卡尔坐标系组配置项，适用于 3D 图形。（Bar3D, Line3D, Scatter3D, Surface3D)**

* grid3d_width -> int  
    默认 -> 100  
    三维笛卡尔坐标系组件在三维场景中的高度。

* grid3d_height -> int  
    默认 -> 100  
    三维笛卡尔坐标系组件在三维场景中的高度。

* grid3d_depth -> int  
    默认 -> 100  
    三维笛卡尔坐标系组件在三维场景中的高度。

* is_grid3d_rotate -> bool  
    默认 -> False  
    是否开启视角绕物体的自动旋转查看。

* grid3d_rotate_speed -> int  
    默认 -> 10（36 秒转一圈）  
    物体自传的速度。单位为角度 / 秒。

* grid3d_rotate_sensitivity -> int  
    默认 -> 1  
    旋转操作的灵敏度，值越大越灵敏。设置为 0 后无法旋转。


### axis3D
**3D 笛卡尔坐标系 X，Y，Z 轴配置项，适用于 3D 图形。（Bar3D, Line3D, Scatter3D, Surface3D)**

#### 3D X 轴

* xaxis3d_name -> str  
    默认 -> ""  
    x 轴名称。

* xaxis3d_name_size -> int  
    默认 -> 10  
    x 轴名称体大小。

* xaxis3d_name_gap -> int  
    默认 -> 20  
    x 轴名称与轴线之间的距离。

* xaxis3d_min -> int/float  
    默认 -> 自适应  
    x 坐标轴刻度最小值。

* xaxis3d_max -> int/float  
    默认 -> 自适应  
    x 坐标轴刻度最大值。

* xaxis3d_interval -> int  
    x 轴刻度标签的显示间隔，在类目轴中有效。默认会采用标签不重叠的策略间隔显示标签。  
    设置成 0 强制显示所有标签。设置为 1，表示『隔一个标签显示一个标签』，如果值为 2，表示隔两个标签显示一个标签，以此类推

* xaxis3d_margin -> int  
    默认 -> 0  
    x 轴刻度标签与轴线之间的距离。

#### 3D Y 轴

* yaxis3d_name -> str  
    默认 -> ""  
    y 轴名称。

* yaxis3d_name_size -> int  
    默认 -> 16  
    y 轴名称体大小。

* yaxis3d_name_gap -> int  
    默认 -> 25  
    y 轴名称与轴线之间的距离。

* yaxis3d_min -> int/float  
    默认 -> 自适应  
    y 坐标轴刻度最小值。

* yaxis3d_max -> int/float  
    默认 -> 自适应  
    y 坐标轴刻度最大值。

* yaxis3d_interval -> int  
    y 轴刻度标签的显示间隔，在类目轴中有效。默认会采用标签不重叠的策略间隔显示标签。  
    设置成 0 强制显示所有标签。设置为 1，表示『隔一个标签显示一个标签』，如果值为 2，表示隔两个标签显示一个标签，以此类推

* yaxis3d_margin -> int  
    默认 -> 8  
    y 轴刻度标签与轴线之间的距离。

#### 3D Z 轴

* zaxis3d_name -> str  
    默认 -> ""  
    z 轴名称。

* zaxis3d_name_size -> int  
    默认 -> 16  
    z 轴名称体大小。

* zaxis3d_name_gap -> int  
    默认 -> 25  
    z 轴名称与轴线之间的距离。

* zaxis3d_min -> int/float  
    默认 -> 自适应  
    z 坐标轴刻度最小值。

* zaxis3d_max -> int/float  
    默认 -> 自适应  
    z 坐标轴刻度最大值。

* zaxis3d_margin -> int  
    默认 -> 8  
    z 轴刻度标签与轴线之间的距离。


### visualMap
**是视觉映射组件，用于进行『视觉编码』，也就是将数据映射到视觉元素（视觉通道）**

* is_visualmap -> bool  
    是否使用视觉映射组件

* visual_type -> str  
    制定组件映射方式，默认为'color‘，即通过颜色来映射数值。有'color', 'size'可选。'size'通过数值点的大小，也就是图形点的大小来映射数值。

* visual_range -> list  
    默认 -> [0, 100]  
    指定组件的允许的最小值与最大值。

* visual_text_color -> list  
    两端文本颜色。

* visual_range_text -> list  
    默认 -> ['low', 'hight']  
    两端文本。

* visual_range_color -> list  
    默认 -> ['#50a3ba', '#eac763', '#d94e5d']  
    过渡颜色。

* visual_range_size -> list  
    默认 -> [20, 50]  
    数值映射的范围，也就是图形点大小的范围。

* visual_orient -> str  
    默认 -> 'vertical'  
    visualMap 组件条的方向。有'vertical', 'horizontal'可选。

* visual_pos -> str/int  
    默认 -> 'left'  
    visualmap 组件条距离左侧的位置。有'right', 'center', 'right'可选，也可为百分数或整数。

* visual_top -> str/int  
    默认 -> 'top'  
    visualmap 组件条距离顶部的位置。有'top', 'center', 'bottom'可选，也可为百分数或整数。

* visual_split_number -> int  
    默认 -> 5  
    分段型中分割的段数，在设置为分段型时生效。

* visual_dimension -> int  
    指定用数据的『哪个维度』，映射到视觉元素上。默认映射到最后一个维度。索引从 0 开始。  
    在直角坐标系中，x 轴为第一个维度（0），y 轴为第二个维度（1）。

* is_calculable -> bool  
    默认 -> True  
    是否显示拖拽用的手柄（手柄能拖拽调整选中范围）。

* is_piecewise -> bool  
    默认 -> False    
    是否将组件转换为分段型（默认为连续型）。

* pieces -> list  
    自定义『分段式视觉映射组件（visualMapPiecewise）』的每一段的范围，  
    以及每一段的文字，以及每一段的特别的样式。（仅在 is_piecewise 为 True 时生效）例如： 
    ``` 
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
    ```

### tooltip
**提示框组件，用于移动或点击鼠标时弹出数据内容**

* tooltip_trigger -> str  
    默认 -> 'item'  
    触发类型。  
    * 'item': 数据项图形触发，主要在散点图，饼图等无类目轴的图表中使用。
    * 'axis': 坐标轴触发，主要在柱状图，折线图等会使用类目轴的图表中使用。
    * 'none': 什么都不触发。

* tooltip_trigger_on -> str  
    默认 -> "mousemove|click"  
    提示框触发的条件。
    * 'mousemove': 鼠标移动时触发。
    * 'click': 鼠标点击时触发。
    * 'mousemove|click': 同时鼠标移动和点击时触发。
    * 'none': 不在 'mousemove' 或 'click' 时触发

* tooltip_axispointer_type -> str  
    默认 -> "line"  
    指示器类型。
    * 'line': 直线指示器
    * 'shadow': 阴影指示器
    * 'cross': 十字准星指示器。其实是种简写，表示启用两个正交的轴的 axisPointer。

* tooltip_formatter -> str  
    模板变量有 {a}, {b}，{c}，{d}，{e}，分别表示系列名，数据名，数据值等。  
    在 trigger 为 'axis' 的时候，会有多个系列的数据，此时可以通过 {a0}, {a1}, {a2} 这种后面加索引的方式表示系列的索引。不同图表类型下的 {a}，{b}，{c}，{d} 含义不一样。 其中变量 {a}, {b}, {c}, {d} 在不同图表类型下代表数据含义为：
    * 折线（区域）图、柱状（条形）图、K线图 : {a}（系列名称），{b}（类目值），{c}（数值）, {d}（无）
    * 散点图（气泡）图 : {a}（系列名称），{b}（数据名称），{c}（数值数组）, {d}（无）
    * 地图 : {a}（系列名称），{b}（区域名称），{c}（合并数值）, {d}（无）
    * 饼图、仪表盘、漏斗图: {a}（系列名称），{b}（数据项名称），{c}（数值）, {d}（百分比）

    tooltip_formatter -> function  
    具体格式请参考 xaxis_formatter -> function

* tooltip_text_color -> str  
    默认 -> '#fff'  
    提示框字体颜色。

* tooltip_font_size -> int  
    默认 -> 14  
    提示框字体大小。

* tooltip_background_color -> str  
    默认 -> "rgba(50,50,50,0.7)"  
    提示框浮层的背景颜色。

* tooltip_border_color -> str  
    默认 -> "#333"  
    提示框浮层的边框颜色。

* tooltip_border_width -> int/float  
    默认 -> 0  
    提示框浮层的边框宽。


### markLine-markPoint
**图形标记组件，用于标记指定的特殊数据，有标记线和标记点两种（Bar、Line、Kline）**

* mark_point -> list  
    标记点，默认有'min', 'max', 'average'可选。支持自定义标记点，具体使用如下  
    [{"coord": [a1, b1], "name": "first markpoint"}, {"coord": [a2, b2], "name": "second markpoint"}]  
    需自己传入标记点字典，共有两个键值对，'coord' 对应为 x y 轴坐标， 'name' 为标记点名称。

* mark_point_raw -> list  
    原生格式的 markPoint 数据，数据类型为 [{}, {}, ...]。  
    格式请参考 http://echarts.baidu.com/option.html#series-line.markPoint.data

* mark_point_symbol -> str  
    默认 -> 'pin'  
    标记点图形，有'circle', 'rect', 'roundRect', 'triangle', 'diamond', 'pin', 'arrow'可选。

* mark_point_symbolsize -> int  
    默认 -> 50  
    标记点图形大小。

* mark_point_textcolor -> str  
    默认 -> '#fff'  
    标记点字体颜色。

* mark_line -> list  
    标记线，默认有'min', 'max', 'average'可选

* mark_line_raw -> list  
    原生格式的 markLine 数据，数据类型为 [{}, {}, ...]。  
    格式请参考 http://echarts.baidu.com/option.html#series-line.markLine.data

* mark_line_symbolsize -> int  
    默认 -> 15  
    标记线图形大小。

* mark_line_valuedim -> list  
    标记线指定在哪个维度上指定最大值最小值。这可以是维度的直接名称，Line 时可以是 x、angle 等、Kline 图时可以是 open、close、highest、lowest。  
    可同时制定多个维度，如:  
    mark_line=['min', 'max'], mark_line_valuedim=['lowest', 'highest'] 则表示 min 使用 lowest 维度，max 使用 highest 维度，以此类推

* mark_line_coords -> [list], 包含列表的列表  
    标记线指定起点坐标和终点坐标，如 [[10, 10], [30, 30]]，两个点分别为横纵坐标轴点。

* mark_point_valuedim -> list  
    标记线指定在哪个维度上指定最大值最小值。这可以是维度的直接名称，Line 时可以是 x、angle 等、Kline 图时可以是 open、close、highest、lowest。  
    可同时制定多个维度，如:  
    mark_point=['min', 'max'], mark_point_valuedim=['lowest', 'highest'] 则表示 min 使用 lowest 维度，max 使用 highest 维度，以此类推


### toolbox
**右侧实用工具箱**

* is_toolbox_show -> bool  
    默认 -> True  
    指定是否显示右侧实用工具箱。

* is_more_utils -> bool  
    指定是否提供更多的实用工具按钮。默认只提供『数据视图』和『下载』按钮

**如果你已阅读完本篇文档，可以进一步阅读 [基本图表篇](zh-cn/charts_base)**
