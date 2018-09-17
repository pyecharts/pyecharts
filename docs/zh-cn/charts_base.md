> 基本图表篇：本篇文档为 pyecharts 基本图表详情文档，介绍了关于 pyecharts 各类基本图表的细节。

**图表详细配置请参考 [图表配置篇](zh-cn/charts_configure)**

* 基本图表类
    * Bar（柱状图/条形图）
    * Bar3D（3D 柱状图）
    * Boxplot（箱形图）
    * EffectScatter（带有涟漪特效动画的散点图）
    * Funnel（漏斗图）
    * Gauge（仪表盘）
    * Geo（地理坐标系）
    * GeoLines（地理坐标系线图）
    * Graph（关系图）
    * HeatMap（热力图）
    * Kline/Candlestick（K线图）
    * Line（折线/面积图）
    * Line3D（3D 折线图）
    * Liquid（水球图）
    * Map（地图）
    * Parallel（平行坐标系）
    * Pie（饼图）
    * Polar（极坐标系）
    * Radar（雷达图）
    * Sankey（桑基图）
    * Scatter（散点图）
    * Scatter3D（3D 散点图）
    * Surface3D（3D 曲面图）
    * ThemeRiver（主题河流图）
    * Tree（树图）
    * TreeMap（矩形树图）
    * WordCloud（词云图）


## Bar（柱状图/条形图）
> 柱状/条形图，通过柱形的高度/条形的宽度来表现数据的大小。

Bar.add() 方法签名
```python
add(name, x_axis, y_axis,
    is_stack=False,
    bar_category_gap='20%', **kwargs)
```
* name -> str  
    图例名称
* x_axis -> list  
    x 坐标轴数据
* y_axis -> list  
    y 坐标轴数据  
* is_stack -> bool  
    数据堆叠，同个类目轴上系列配置相同的 stack 值可以堆叠放置  
* bar_category_gap -> int/str   
    类目轴的柱状距离，当设置为 0 时柱状是紧挨着（直方图类型），默认为 '20%'

**is_stack 实现数据堆叠**
```python
from pyecharts import Bar

attr = ["衬衫", "羊毛衫", "雪纺衫", "裤子", "高跟鞋", "袜子"]
v1 = [5, 20, 36, 10, 75, 90]
v2 = [10, 25, 8, 60, 20, 80]
bar = Bar("柱状图数据堆叠示例")
bar.add("商家A", attr, v1, is_stack=True)
bar.add("商家B", attr, v2, is_stack=True)
bar.render()
```
![bar-demo](https://user-images.githubusercontent.com/19553554/35081597-0c3e7212-fc50-11e7-8f72-af6c552223e8.gif)

**Note：** 全局配置项要在最后一个 ```add()``` 上设置，否侧设置会被冲刷掉。

**使用标记点和标记线**
```python
from pyecharts import Bar

bar = Bar("标记线和标记点示例")
bar.add("商家A", attr, v1, mark_point=["average"])
bar.add("商家B", attr, v2, mark_line=["min", "max"])
bar.render()
```
![bar-demo](https://user-images.githubusercontent.com/19553554/35081600-0ea23f0c-fc50-11e7-894b-65ad0f611a01.gif)

**is_convert 交换 XY 轴**
```python
from pyecharts import Bar

bar = Bar("x 轴和 y 轴交换")
bar.add("商家A", attr, v1)
bar.add("商家B", attr, v2, is_convert=True)
bar.render()
```
![bar-demo](https://user-images.githubusercontent.com/19553554/35081605-151472ce-fc50-11e7-8627-66929309b08c.png)

**dataZoom 效果，'slider' 类型**
```python
import random

attr = ["{}天".format(i) for i in range(30)]
v1 = [random.randint(1, 30) for _ in range(30)]
bar = Bar("Bar - datazoom - slider 示例")
bar.add("", attr, v1, is_label_show=True, is_datazoom_show=True)
bar.render()
```
![bar-demo](https://user-images.githubusercontent.com/19553554/35081742-ddcbf3e0-fc50-11e7-937e-f806fd12c83e.gif)

**dataZoom 效果，'inside' 类型**
```python
attr = ["{}天".format(i) for i in range(30)]
v1 = [random.randint(1, 30) for _ in range(30)]
bar = Bar("Bar - datazoom - inside 示例")
bar.add(
    "",
    attr,
    v1,
    is_datazoom_show=True,
    datazoom_type="inside",
    datazoom_range=[10, 25],
)
bar.render()
```
![bar-demo](https://user-images.githubusercontent.com/19553554/35081801-307b3d26-fc51-11e7-8ac7-eea2f2422402.gif)

**dataZoom 效果，'both' 类型**
```python
attr = ["{}天".format(i) for i in range(30)]
v1 = [random.randint(1, 30) for _ in range(30)]
bar = Bar("Bar - datazoom - inside 示例")
bar.add(
    "",
    attr,
    v1,
    is_datazoom_show=True,
    datazoom_type="both",
    datazoom_range=[10, 25],
)
bar.render()
```
![bar-demo](https://user-images.githubusercontent.com/19553554/35081813-37fc4072-fc51-11e7-9b5c-a3ca2f0d1fef.gif)

**多 dataZoom 效果，效果同时支持 X、Y 轴**
```python
days = ["{}天".format(i) for i in range(30)]
days_v1 = [random.randint(1, 30) for _ in range(30)]
bar = Bar("Bar - datazoom - xaxis/yaxis 示例")
bar.add(
    "",
    days,
    days_v1,
    # 默认为 X 轴，横向
    is_datazoom_show=True,
    datazoom_type="slider",
    datazoom_range=[10, 25],
    # 新增额外的 dataZoom 控制条，纵向
    is_datazoom_extra_show=True,
    datazoom_extra_type="slider",
    datazoom_extra_range=[10, 25],
    is_toolbox_show=False,
)
bar.render()
```
![bar-demo](https://user-images.githubusercontent.com/19553554/43352052-ec70fe82-924f-11e8-880b-832b8f95d701.gif)


**Note：** datazoom 适合所有平面直角坐标系图形，也就是(Line、Bar、Scatter、EffectScatter、Kline)  

**当 x 轴或者 y 轴的标签因为过于密集而导致全部显示出来会重叠的话，可采用使标签旋转的方法**
```python
attr = ["{}天".format(i) for i in range(20)]
v1 = [random.randint(1, 20) for _ in range(20)]
bar = Bar("坐标轴标签旋转示例")
bar.add("", attr, v1, xaxis_interval=0, xaxis_rotate=30, yaxis_rotate=30)
bar.render()
```
![bar-demo](https://user-images.githubusercontent.com/19553554/35081805-3258a2be-fc51-11e7-9cb1-d99c1a707bc5.png)

**Note：** 可通过设置 xaxis_min/xaxis_max/yaxis_min/yaxis_max 来调整 x 轴和 y 轴上的最大最小值。针对数值轴有效！  
**Note：** 可以通过 label_color 来设置柱状的颜色，如 ['#eee', '#000']，所有的图表类型的图例颜色都可通过 label_color 来修改。

**瀑布图示例**
```python
from pyecharts import Bar

attr = ["{}月".format(i) for i in range(1, 8)]
v1 = [0, 100, 200, 300, 400, 220, 250]
v2 = [1000, 800, 600, 500, 450, 400, 300]
bar = Bar("瀑布图示例")
# 利用第一个 add() 图例的颜色为透明，即 'rgba(0,0,0,0)'，并且设置 is_stack 标志为 True
bar.add("", attr, v1, label_color=['rgba(0,0,0,0)'], is_stack=True)
bar.add("月份", attr, v2, is_label_show=True, is_stack=True, label_pos='inside')
bar.render()
```
![bar-demo](https://user-images.githubusercontent.com/19553554/35081807-34a5568e-fc51-11e7-8199-3c3f8f43ba98.png)

**直方图示例**
```python
from pyecharts import Bar

attr = ["衬衫", "羊毛衫", "雪纺衫", "裤子", "高跟鞋", "袜子"]
v1 = [5, 20, 36, 10, 75, 90]
v2 = [10, 25, 8, 60, 20, 80]
bar = Bar("直方图示例")
bar.add("", attr * 2, v1 + v2, bar_category_gap=0)
bar.render()
```
![bar-demo](https://user-images.githubusercontent.com/19553554/35081820-3c6f2ad4-fc51-11e7-8600-9212e7e8b519.png)

**某地的降水量和蒸发量柱状图**
```python
from pyecharts import Bar

attr = ["{}月".format(i) for i in range(1, 13)]
v1 = [2.0, 4.9, 7.0, 23.2, 25.6, 76.7, 135.6, 162.2, 32.6, 20.0, 6.4, 3.3]
v2 = [2.6, 5.9, 9.0, 26.4, 28.7, 70.7, 175.6, 182.2, 48.7, 18.8, 6.0, 2.3]
bar = Bar("柱状图示例")
bar.add("蒸发量", attr, v1, mark_line=["average"], mark_point=["max", "min"])
bar.add("降水量", attr, v2, mark_line=["average"], mark_point=["max", "min"])
bar.render()
```
![bar-demo](https://user-images.githubusercontent.com/19553554/35081822-3e090748-fc51-11e7-8bba-b775d29671e4.png)

**额外的文本标签**
```python
from pyecharts import Bar

bar = Bar("柱状图", extra_html_text_label=["bar_extra_html_text_label", "color:red"])
bar.add("商家A", CLOTHES, clothes_v1, is_stack=True)
bar.add("商家B", CLOTHES, clothes_v2, is_stack=True)
bar.render()
```
![bar-demo](https://user-images.githubusercontent.com/19553554/43812932-31f22e0a-9af6-11e8-8fbe-c62b65daec41.png)

**控制 X/Y 轴坐标轴线颜色以及宽度**
```python
bar = Bar("柱状图")
bar.add(
    "商家A",
    CLOTHES,
    clothes_v1,
    xaxis_line_color="green",
    xaxis_line_width=5,
    xaxis_label_textcolor="black",
)
bar.render()
```
![bar-demo](https://user-images.githubusercontent.com/19553554/43877147-e30b5cf0-9bca-11e8-9bc7-c1cd7be58141.png)

**进行两次或多次 add 的时候，有一次的某项数据缺失，可用 0 填充**
```python
bar = Bar("折线图示例")
bar.add("商家A", CLOTHES, clothes_v1)
bar.add("商家B", CLOTHES, [55, 60, 16, 20, 0, 0])
bar.render()
```
![bar-demo](https://user-images.githubusercontent.com/19553554/44008022-e3708900-9ed0-11e8-94c5-68c8d96ebe60.png)


## Bar3D（3D 柱状图）
Bar3D.add() 方法签名

```python
add(name, x_axis, y_axis, data,
    grid3d_opacity=1,
    grid3d_shading='color', **kwargs)
```
* name -> str  
    图例名称
* x_axis -> str  
    x 坐标轴数据。需为类目轴，也就是不能是数值。
* y_axis -> str  
    y 坐标轴数据。需为类目轴，也就是不能是数值。
* data -> [list], 包含列表的列表  
    数据项，数据中，每一行是一个『数据项』，每一列属于一个『维度』
* grid3d_opacity -> int  
    3D 笛卡尔坐标系组的透明度（柱状的透明度），默认为 1，完全不透明。
* grid3d_shading -> str  
    三维柱状图中三维图形的着色效果。
    * color：只显示颜色，不受光照等其它因素的影响。
    * lambert：通过经典的 lambert 着色表现光照带来的明暗。
    * realistic：真实感渲染，配合 light.ambientCubemap 和 postEffect 使用可以让展示的画面效果和质感有质的提升。ECharts GL 中使用了基于物理的渲染（PBR) 来表现真实感材质。

```python
from pyecharts import Bar3D

bar3d = Bar3D("3D 柱状图示例", width=1200, height=600)
x_axis = [
    "12a", "1a", "2a", "3a", "4a", "5a", "6a", "7a", "8a", "9a", "10a", "11a",
    "12p", "1p", "2p", "3p", "4p", "5p", "6p", "7p", "8p", "9p", "10p", "11p"
    ]
y_axis = [
    "Saturday", "Friday", "Thursday", "Wednesday", "Tuesday", "Monday", "Sunday"
    ]
data = [
    [0, 0, 5], [0, 1, 1], [0, 2, 0], [0, 3, 0], [0, 4, 0], [0, 5, 0],
    [0, 6, 0], [0, 7, 0], [0, 8, 0], [0, 9, 0], [0, 10, 0], [0, 11, 2],
    [0, 12, 4], [0, 13, 1], [0, 14, 1], [0, 15, 3], [0, 16, 4], [0, 17, 6],
    [0, 18, 4], [0, 19, 4], [0, 20, 3], [0, 21, 3], [0, 22, 2], [0, 23, 5],
    [1, 0, 7], [1, 1, 0], [1, 2, 0], [1, 3, 0], [1, 4, 0], [1, 5, 0],
    [1, 6, 0], [1, 7, 0], [1, 8, 0], [1, 9, 0], [1, 10, 5], [1, 11, 2],
    [1, 12, 2], [1, 13, 6], [1, 14, 9], [1, 15, 11], [1, 16, 6], [1, 17, 7],
    [1, 18, 8], [1, 19, 12], [1, 20, 5], [1, 21, 5], [1, 22, 7], [1, 23, 2],
    [2, 0, 1], [2, 1, 1], [2, 2, 0], [2, 3, 0], [2, 4, 0], [2, 5, 0],
    [2, 6, 0], [2, 7, 0], [2, 8, 0], [2, 9, 0], [2, 10, 3], [2, 11, 2],
    [2, 12, 1], [2, 13, 9], [2, 14, 8], [2, 15, 10], [2, 16, 6], [2, 17, 5],
    [2, 18, 5], [2, 19, 5], [2, 20, 7], [2, 21, 4], [2, 22, 2], [2, 23, 4],
    [3, 0, 7], [3, 1, 3], [3, 2, 0], [3, 3, 0], [3, 4, 0], [3, 5, 0],
    [3, 6, 0], [3, 7, 0], [3, 8, 1], [3, 9, 0], [3, 10, 5], [3, 11, 4],
    [3, 12, 7], [3, 13, 14], [3, 14, 13], [3, 15, 12], [3, 16, 9], [3, 17, 5],
    [3, 18, 5], [3, 19, 10], [3, 20, 6], [3, 21, 4], [3, 22, 4], [3, 23, 1],
    [4, 0, 1], [4, 1, 3], [4, 2, 0], [4, 3, 0], [4, 4, 0], [4, 5, 1],
    [4, 6, 0], [4, 7, 0], [4, 8, 0], [4, 9, 2], [4, 10, 4], [4, 11, 4],
    [4, 12, 2], [4, 13, 4], [4, 14, 4], [4, 15, 14], [4, 16, 12], [4, 17, 1],
    [4, 18, 8], [4, 19, 5], [4, 20, 3], [4, 21, 7], [4, 22, 3], [4, 23, 0],
    [5, 0, 2], [5, 1, 1], [5, 2, 0], [5, 3, 3], [5, 4, 0], [5, 5, 0],
    [5, 6, 0], [5, 7, 0], [5, 8, 2], [5, 9, 0], [5, 10, 4], [5, 11, 1],
    [5, 12, 5], [5, 13, 10], [5, 14, 5], [5, 15, 7], [5, 16, 11], [5, 17, 6],
    [5, 18, 0], [5, 19, 5], [5, 20, 3], [5, 21, 4], [5, 22, 2], [5, 23, 0],
    [6, 0, 1], [6, 1, 0], [6, 2, 0], [6, 3, 0], [6, 4, 0], [6, 5, 0],
    [6, 6, 0], [6, 7, 0], [6, 8, 0], [6, 9, 0], [6, 10, 1], [6, 11, 0],
    [6, 12, 2], [6, 13, 1], [6, 14, 3], [6, 15, 4], [6, 16, 0], [6, 17, 0],
    [6, 18, 0], [6, 19, 0], [6, 20, 1], [6, 21, 2], [6, 22, 2], [6, 23, 6]
    ]
range_color = ['#313695', '#4575b4', '#74add1', '#abd9e9', '#e0f3f8', '#ffffbf',
               '#fee090', '#fdae61', '#f46d43', '#d73027', '#a50026']
bar3d.add(
    "",
    x_axis,
    y_axis,
    [[d[1], d[0], d[2]] for d in data],
    is_visualmap=True,
    visual_range=[0, 20],
    visual_range_color=range_color,
    grid3d_width=200,
    grid3d_depth=80,
)
bar3d.render()
```
![bar3d-demo](https://user-images.githubusercontent.com/19553554/35081629-36a8e046-fc50-11e7-8910-e02bf24008d9.gif)

data 中，如 [1, 2, 3] 表示 x 轴的索引为 1，即 "1a"；y 轴的索引为 2，即 "Thursday"；z 轴的数值为 3

**设置 ```grid3d_shading``` 可以让柱状更真实**
```python
bar3d = Bar3D("3D 柱状图示例", width=1200, height=600)
bar3d.add(
    "",
    x_axis,
    y_axis,
    [[d[1], d[0], d[2]] for d in data],
    is_visualmap=True,
    visual_range=[0, 20],
    visual_range_color=range_color,
    grid3d_width=200,
    grid3d_depth=80,
    grid3d_shading="lambert",
)
bar3d.render()
```
![bar3d-demo](https://user-images.githubusercontent.com/19553554/35081631-38a0cb02-fc50-11e7-9f74-3d487bd98a3a.gif)

**设置 ```is_grid3d_rotate``` 启动自动旋转功能**
```python
bar3d = Bar3D("3D 柱状图示例", width=1200, height=600)
bar3d.add(
    "",
    x_axis,
    y_axis,
    [[d[1], d[0], d[2]] for d in data],
    is_visualmap=True,
    visual_range=[0, 20],
    visual_range_color=range_color,
    grid3d_width=200,
    grid3d_depth=80,
    is_grid3d_rotate=True,
)
bar3d.render()
```
![bar3d-demo](https://user-images.githubusercontent.com/19553554/35081703-a70b544a-fc50-11e7-838a-53445cd8d203.gif)

**设置 ```grid3d_rotate_speed``` 调节旋转速度**
```python
bar3d = Bar3D("3D 柱状图示例", width=1200, height=600)
bar3d.add(
    "",
    x_axis,
    y_axis,
    [[d[1], d[0], d[2]] for d in data],
    is_visualmap=True,
    visual_range=[0, 20],
    visual_range_color=range_color,
    grid3d_width=200,
    grid3d_depth=80,
    is_grid3d_rotate=True,
    grid3d_rotate_speed=180,
)
bar3d.render()
```
![bar3d-demo](https://user-images.githubusercontent.com/19553554/35081705-a92a878c-fc50-11e7-8427-9066456db54c.gif)

**Note：** 关于 gird3D 部分的设置，请参照 **通用配置项** 中的介绍
**Note：** 可配合 axis3D 通用配置项 一起使用 


## Boxplot（箱形图）
> 箱形图是一种用作显示一组数据分散情况资料的统计图。它能显示出一组数据的最大值、最小值、中位数、下四分位数及上四分位数。

Boxplot.add() 方法签名
```python
add(name, x_axis, y_axis, **kwargs)
```
* name -> str  
    图例名称
* x_axis -> list  
    x 坐标轴数据
* y_axis -> [list], 包含列表的列表   
    y 坐标轴数据，二维数组的每一数组项（下例中的每行）是渲染一个 box，它含有五个量值，依次是：  
    [min,  Q1,  median (or Q2),  Q3,  max]

可自行计算出所需五个数值，也可通过内置 `prepare_data()` 转换，`prepare_data()` 会将传入的嵌套列表中的数据转换为嵌套的 [min,  Q1,  median (or Q2),  Q3,  max]，如下所示：
```python
from pyecharts import Boxplot

boxplot = Boxplot("箱形图")
x_axis = ['expr1', 'expr2', 'expr3', 'expr4', 'expr5']
y_axis = [
    [850, 740, 900, 1070, 930, 850, 950, 980, 980, 880,
    1000, 980, 930, 650, 760, 810, 1000, 1000, 960, 960],
    [960, 940, 960, 940, 880, 800, 850, 880, 900, 840,
    830, 790, 810, 880, 880, 830, 800, 790, 760, 800],
    [880, 880, 880, 860, 720, 720, 620, 860, 970, 950,
    880, 910, 850, 870, 840, 840, 850, 840, 840, 840],
    [890, 810, 810, 820, 800, 770, 760, 740, 750, 760,
    910, 920, 890, 860, 880, 720, 840, 850, 850, 780],
    [890, 840, 780, 810, 760, 810, 790, 810, 820, 850,
    870, 870, 810, 740, 810, 940, 950, 800, 810, 870]
]
_yaxis = boxplot.prepare_data(y_axis)       # 转换数据
boxplot.add("boxplot", x_axis, _yaxis)
boxplot.render()
```
![boxplot-demo](https://user-images.githubusercontent.com/19553554/35082364-4f4e98f8-fc54-11e7-9e53-1d6a66b67e46.png)

**或者直接在 add() 中转换**
```python
from pyecharts import Boxplot

boxplot = Boxplot("箱形图")
x_axis = ['expr1', 'expr2']
y_axis1 = [
    [850, 740, 900, 1070, 930, 850, 950, 980, 980, 880,
    1000, 980, 930, 650, 760, 810, 1000, 1000, 960, 960],
    [960, 940, 960, 940, 880, 800, 850, 880, 900, 840,
    830, 790, 810, 880, 880, 830, 800, 790, 760, 800],
]
y_axis2 = [
    [890, 810, 810, 820, 800, 770, 760, 740, 750, 760,
    910, 920, 890, 860, 880, 720, 840, 850, 850, 780],
    [890, 840, 780, 810, 760, 810, 790, 810, 820, 850,
    870, 870, 810, 740, 810, 940, 950, 800, 810, 870]
]
boxplot.add("category1", x_axis, boxplot.prepare_data(y_axis1))
boxplot.add("category2", x_axis, boxplot.prepare_data(y_axis2))
boxplot.render()
```
![boxplot-demo](https://user-images.githubusercontent.com/19553554/35082365-511fcc38-fc54-11e7-9826-d16231a401f4.png)


## EffectScatter（带有涟漪特效动画的散点图）
> 利用动画特效可以将某些想要突出的数据进行视觉突出。

EffectScatter.add() 方法签名
```python
add(name, x_axis, y_axis,
    symbol_size=10, **kwargs)
```
* name -> str  
    图例名称
* x_axis -> list  
    x 坐标轴数据
* y_axis -> list  
    y 坐标轴数据
* symbol_size -> int  
    标记图形大小，默认为 10
    
```python
from pyecharts import EffectScatter

v1 = [10, 20, 30, 40, 50, 60]
v2 = [25, 20, 15, 10, 60, 33]
es = EffectScatter("动态散点图示例")
es.add("effectScatter", v1, v2)
es.render()
```
![effectscatter-demo](https://user-images.githubusercontent.com/19553554/35090528-e4c9a04c-fc74-11e7-938a-d348bb1fdbf8.gif)

**动态散点图各种图形**
```python
es = EffectScatter("动态散点图各种图形示例")
es.add(
    "",
    [10],
    [10],
    symbol_size=20,
    effect_scale=3.5,
    effect_period=3,
    symbol="pin",
)
es.add(
    "",
    [20],
    [20],
    symbol_size=12,
    effect_scale=4.5,
    effect_period=4,
    symbol="rect",
)
es.add(
    "",
    [30],
    [30],
    symbol_size=30,
    effect_scale=5.5,
    effect_period=5,
    symbol="roundRect",
)
es.add(
    "",
    [40],
    [40],
    symbol_size=10,
    effect_scale=6.5,
    effect_brushtype="fill",
    symbol="diamond",
)
es.add(
    "",
    [50],
    [50],
    symbol_size=16,
    effect_scale=5.5,
    effect_period=3,
    symbol="arrow",
)
es.add(
    "",
    [60],
    [60],
    symbol_size=6,
    effect_scale=2.5,
    effect_period=3,
    symbol="triangle",
)
es.render()
```
![effectscatter-demo](https://user-images.githubusercontent.com/19553554/35090533-e7330076-fc74-11e7-9ba0-7cc4ff80e030.gif)

* symbol -> str  
    标记图形，有'rect', 'roundRect', 'triangle', 'diamond', 'pin', 'arrow'可选
* effect_brushtype -> str  
    波纹绘制方式，有'stroke', 'fill'可选。默认为'stroke'
* effect_scale -> float  
    动画中波纹的最大缩放比例。默认为 2.5
* effect_period -> float  
    动画持续的时间。默认为 4（s）


## Funnel（漏斗图）
Funnel.add() 方法签名
```python
add(name, attr, value,
    funnel_sort="ascending", funnel_gap=0, **kwargs)
```
* name -> str  
    图例名称
* attr -> list  
    属性名称
* value -> list  
    属性所对应的值
* funnel_sort -> str/func  
    数据排序， 可以取 'ascending'，'descending'，'none'（表示按 data 顺序，即不排序）。
* funnel_gap- > int  
    数据图形间距。默认为 0。

**标签显示在内部**
```python
from pyecharts import Funnel

attr = ["衬衫", "羊毛衫", "雪纺衫", "裤子", "高跟鞋", "袜子"]
value = [20, 40, 60, 80, 100, 120]
funnel = Funnel("漏斗图示例")
funnel.add(
    "商品",
    attr,
    value,
    is_label_show=True,
    label_pos="inside",
    label_text_color="#fff",
)
funnel.render()
```
![funnel-demo](https://user-images.githubusercontent.com/19553554/35090181-d6b0e886-fc73-11e7-8e00-dec8ac38c415.gif)

**标签显示在外部**
```python
funnel = Funnel("漏斗图示例", width=600, height=400, title_pos='center')
funnel.add(
    "商品",
    attr,
    value,
    is_label_show=True,
    label_pos="outside",
    legend_orient="vertical",
    legend_pos="left",
)
funnel.render()
```
![funnel-demo](https://user-images.githubusercontent.com/19553554/35090186-d8f50db6-fc73-11e7-9b7e-947580a621de.png)

**数据按升序排序**
```python
funnel = Funnel("漏斗图示例", width=600, height=400, title_pos='center')
funnel.add(
    "商品",
    CLOTHES,
    prices,
    is_label_show=True,
    label_pos="inside",
    label_text_color="#fff",
    funnel_sort="ascending"
)
funnel.render()
```
![funnel-demo](https://user-images.githubusercontent.com/19553554/44653464-6cc08880-aa21-11e8-9b78-a3090ada7be7.png)

**不排序数据**
```python
funnel = Funnel("漏斗图示例", width=600, height=400, title_pos='center')
funnel.add(
    "商品",
    CLOTHES,
    prices,
    is_label_show=True,
    label_pos="inside",
    label_text_color="#fff",
    funnel_sort="none"
)
funnel.render()
```
![funnel-demo](https://user-images.githubusercontent.com/19553554/44653675-fc663700-aa21-11e8-82f3-69c02d4a847d.png)

**指定图形间隔**
```python
funnel = Funnel("漏斗图示例", width=600, height=400, title_pos='center')
funnel.add(
    "商品",
    CLOTHES,
    prices,
    is_label_show=True,
    label_pos="inside",
    label_text_color="#fff",
    funnel_sort="ascending",
    funnel_gap=5,
)
funnel.render()
```
![funnel-demo](https://user-images.githubusercontent.com/19553554/44653847-6ed71700-aa22-11e8-8c08-e93d2e9e528d.png)


## Gauge（仪表盘）
Gauge.add() 方法签名
```python
add(name, attr, value,
    scale_range=None,
    angle_range=None, **kwargs)
```
* name -> str  
    图例名称
* attr -> list  
    属性名称
* value -> list  
    属性所对应的值
* scale_range -> list  
    仪表盘数据范围。默认为 [0, 100]
* angle_range -> list  
    仪表盘角度范围。默认为 [225, -45]
    
```python
from pyecharts import Gauge

gauge = Gauge("仪表盘示例")
gauge.add("业务指标", "完成率", 66.66)
gauge.render()
```
![gauge-demo](https://user-images.githubusercontent.com/19553554/35090190-daa33eee-fc73-11e7-9710-7844b12d3e6b.png)

```python
gauge = Gauge("仪表盘示例")
gauge.add(
    "业务指标",
    "完成率",
    166.66,
    angle_range=[180, 0],
    scale_range=[0, 200],
    is_legend_show=False,
)
gauge.render()
```
![gauge-demo](https://user-images.githubusercontent.com/19553554/35090193-dc199d22-fc73-11e7-8f4d-22477a3a22be.png)


## Geo（地理坐标系）
> 地理坐标系组件用于地图的绘制，支持在地理坐标系上绘制散点图，线集。

Geo.add() 方法签名
```python
add(name, attr, value,
    type="scatter",
    maptype='china',
    coordinate_region='中国',
    symbol_size=12,
    border_color="#111",
    geo_normal_color="#323c48",
    geo_emphasis_color="#2a333d",
    geo_cities_coords=None,
    is_roam=True, **kwargs)
```
* name -> str  
    图例名称
* attr -> list  
    属性名称
* value -> list   
    属性所对应的值
* type -> str  
    图例类型，有'scatter', 'effectScatter', 'heatmap'可选。默认为 'scatter'
* maptype -> str  
    地图类型。 从 v0.3.2+ 起，地图已经变为扩展包，支持全国省份，全国城市，全国区县，全球国家等地图，具体请参考 [地图自定义篇](zh-cn/customize_map)
* coordinate_region -> str  
    城市坐标所属国家。从 v0.5.7 引入，针对国际城市的地理位置的查找。默认为 `中国`。具体的国家/地区映射表参照 [countries_regions_db.json](https://github.com/pyecharts/pyecharts/blob/master/pyecharts/datasets/countries_regions_db.json)。更多地理坐标信息可以参考 [数据集篇](/zh-cn/datasets)
* symbol_size -> int  
    标记图形大小。默认为 12
* border_color -> str  
    地图边界颜色。默认为 '#111'
* geo_normal_color -> str  
    正常状态下地图区域的颜色。默认为 '#323c48'
* geo_emphasis_color -> str  
    高亮状态下地图区域的颜色。默认为 '#2a333d'
* geo_cities_coords -> dict  
    用户自定义地区经纬度，类似如 {'阿城': [126.58, 45.32],} 这样的字典。
* is_roam -> bool  
    是否开启鼠标缩放和平移漫游。默认为 True  
    如果只想要开启缩放或者平移，可以设置成'scale'或者'move'。设置成 True 为都开启

**Scatter 类型（连续型）**
```python
from pyecharts import Geo

data = [
    ("海门", 9),("鄂尔多斯", 12),("招远", 12),("舟山", 12),("齐齐哈尔", 14),("盐城", 15),
    ("赤峰", 16),("青岛", 18),("乳山", 18),("金昌", 19),("泉州", 21),("莱西", 21),
    ("日照", 21),("胶南", 22),("南通", 23),("拉萨", 24),("云浮", 24),("梅州", 25),
    ("文登", 25),("上海", 25),("攀枝花", 25),("威海", 25),("承德", 25),("厦门", 26),
    ("汕尾", 26),("潮州", 26),("丹东", 27),("太仓", 27),("曲靖", 27),("烟台", 28),
    ("福州", 29),("瓦房店", 30),("即墨", 30),("抚顺", 31),("玉溪", 31),("张家口", 31),
    ("阳泉", 31),("莱州", 32),("湖州", 32),("汕头", 32),("昆山", 33),("宁波", 33),
    ("湛江", 33),("揭阳", 34),("荣成", 34),("连云港", 35),("葫芦岛", 35),("常熟", 36),
    ("东莞", 36),("河源", 36),("淮安", 36),("泰州", 36),("南宁", 37),("营口", 37),
    ("惠州", 37),("江阴", 37),("蓬莱", 37),("韶关", 38),("嘉峪关", 38),("广州", 38),
    ("延安", 38),("太原", 39),("清远", 39),("中山", 39),("昆明", 39),("寿光", 40),
    ("盘锦", 40),("长治", 41),("深圳", 41),("珠海", 42),("宿迁", 43),("咸阳", 43),
    ("铜川", 44),("平度", 44),("佛山", 44),("海口", 44),("江门", 45),("章丘", 45),
    ("肇庆", 46),("大连", 47),("临汾", 47),("吴江", 47),("石嘴山", 49),("沈阳", 50),
    ("苏州", 50),("茂名", 50),("嘉兴", 51),("长春", 51),("胶州", 52),("银川", 52),
    ("张家港", 52),("三门峡", 53),("锦州", 54),("南昌", 54),("柳州", 54),("三亚", 54),
    ("自贡", 56),("吉林", 56),("阳江", 57),("泸州", 57),("西宁", 57),("宜宾", 58),
    ("呼和浩特", 58),("成都", 58),("大同", 58),("镇江", 59),("桂林", 59),("张家界", 59),
    ("宜兴", 59),("北海", 60),("西安", 61),("金坛", 62),("东营", 62),("牡丹江", 63),
    ("遵义", 63),("绍兴", 63),("扬州", 64),("常州", 64),("潍坊", 65),("重庆", 66),
    ("台州", 67),("南京", 67),("滨州", 70),("贵阳", 71),("无锡", 71),("本溪", 71),
    ("克拉玛依", 72),("渭南", 72),("马鞍山", 72),("宝鸡", 72),("焦作", 75),("句容", 75),
    ("北京", 79),("徐州", 79),("衡水", 80),("包头", 80),("绵阳", 80),("乌鲁木齐", 84),
    ("枣庄", 84),("杭州", 84),("淄博", 85),("鞍山", 86),("溧阳", 86),("库尔勒", 86),
    ("安阳", 90),("开封", 90),("济南", 92),("德阳", 93),("温州", 95),("九江", 96),
    ("邯郸", 98),("临安", 99),("兰州", 99),("沧州", 100),("临沂", 103),("南充", 104),
    ("天津", 105),("富阳", 106),("泰安", 112),("诸暨", 112),("郑州", 113),("哈尔滨", 114),
    ("聊城", 116),("芜湖", 117),("唐山", 119),("平顶山", 119),("邢台", 119),("德州", 120),
    ("济宁", 120),("荆州", 127),("宜昌", 130),("义乌", 132),("丽水", 133),("洛阳", 134),
    ("秦皇岛", 136),("株洲", 143),("石家庄", 147),("莱芜", 148),("常德", 152),("保定", 153),
    ("湘潭", 154),("金华", 157),("岳阳", 169),("长沙", 175),("衢州", 177),("廊坊", 193),
    ("菏泽", 194),("合肥", 229),("武汉", 273),("大庆", 279)]

geo = Geo(
    "全国主要城市空气质量",
    "data from pm2.5",
    title_color="#fff",
    title_pos="center",
    width=1200,
    height=600,
    background_color="#404a59",
)
attr, value = geo.cast(data)
geo.add(
    "",
    attr,
    value,
    visual_range=[0, 200],
    visual_text_color="#fff",
    symbol_size=15,
    is_visualmap=True,
)
geo.render()
```
![geo-demo](https://user-images.githubusercontent.com/19553554/35089650-7f06172e-fc72-11e7-9d4b-14437fb0d8fe.gif)

**Note：** 请配合 **通用配置项** 中的 Visualmap 使用

**Scatter 类型（分段型）**
```python
geo = Geo(
    "全国主要城市空气质量",
    "data from pm2.5",
    title_color="#fff",
    title_pos="center",
    width=1200,
    height=600,
    background_color="#404a59",
)
attr, value = geo.cast(data)
geo.add(
    "",
    attr,
    value,
    visual_range=[0, 200],
    visual_text_color="#fff",
    symbol_size=15,
    is_visualmap=True,
    is_piecewise=True,
    visual_split_number=6,
)
geo.render()
```
![geo-demo](https://user-images.githubusercontent.com/19553554/35089651-80d259a0-fc72-11e7-8af9-d96df53c0d49.gif)

**HeatMap 类型**
```python
geo = Geo(
    "全国主要城市空气质量",
    "data from pm2.5",
    title_color="#fff",
    title_pos="center",
    width=1200,
    height=600,
    background_color="#404a59",
)
attr, value = geo.cast(data)
geo.add(
    "",
    attr,
    value,
    type="heatmap",
    is_visualmap=True,
    visual_range=[0, 300],
    visual_text_color="#fff",
)
geo.render()
```
![geo-demo](https://user-images.githubusercontent.com/19553554/35089653-82498f88-fc72-11e7-9811-2aceccd4ed68.gif)

**EffectScatter 类型（全国）**
```python
from pyecharts import Geo

data = [
    ("海门", 9), ("鄂尔多斯", 12), ("招远", 12), ("舟山", 12), ("齐齐哈尔", 14), ("盐城", 15)
]
geo = Geo(
    "全国主要城市空气质量",
    "data from pm2.5",
    title_color="#fff",
    title_pos="center",
    width=1200,
    height=600,
    background_color="#404a59",
)
attr, value = geo.cast(data)
geo.add("", attr, value, type="effectScatter", is_random=True, effect_scale=5)
geo.render()
```
![geo-demo](https://user-images.githubusercontent.com/19553554/35089655-844c8902-fc72-11e7-8d1b-a0920ad5baa8.gif)

**EffectScatter 类型（广东）**
```python
from pyecharts import Geo

data = [("汕头市", 50), ("汕尾市", 60), ("揭阳市", 35), ("阳江市", 44), ("肇庆市", 72)]
geo = Geo(
    "广东城市空气质量",
    "data from pm2.5",
    title_color="#fff",
    title_pos="center",
    width=1200,
    height=600,
    background_color="#404a59",
)
attr, value = geo.cast(data)
geo.add(
    "",
    attr,
    value,
    maptype="广东",
    type="effectScatter",
    is_random=True,
    effect_scale=5,
    is_legend_show=False,
)
geo.render()
```
![geo-demo](https://user-images.githubusercontent.com/19553554/35089657-85d0b7bc-fc72-11e7-8b3d-8127dbe8f780.gif)

**使用 coordinate_region 指定检索坐标的国家/地区**
```python
from pyecharts import Geo

data = [("Oxford", 15), ("London", 12)]

geo = Geo(
    "英国主要城市空气质量",
    "data from pm2.5",
    title_color="#fff",
    title_pos="center",
    background_color="#404a59",
)
attr, value = geo.cast(data)
geo.add(
    "",
    attr,
    value,
    maptype="英国",
    # 使用 coordinate_region，指定检索英国范围内的坐标，如上述的 Oxford。
    # 默认为中国
    coordinate_region="英国",
    visual_range=[0, 200],
    visual_text_color="#fff",
    symbol_size=15,
    is_visualmap=True,
)

geo.render()
```
![geo-demo](https://user-images.githubusercontent.com/19553554/43998653-23b21a78-9e2d-11e8-8273-52fbeaacc6e8.png)


## GeoLines（地理坐标系线图）
> 用于带有起点和终点信息的线数据的绘制，主要用于地图上的航线，路线的可视化。

GeoLines.add() 方法签名
```python
add(name, data,
    maptype='china',
    coordinate_region="中国",
    symbol=None,
    symbol_size=12,
    border_color="#111",
    geo_normal_color="#323c48",
    geo_emphasis_color="#2a333d",
    geo_cities_coords=None,
    geo_effect_period=6,
    geo_effect_traillength=0,
    geo_effect_color='#fff',
    geo_effect_symbol='circle',
    geo_effect_symbolsize=5,
    is_geo_effect_show=True,
    is_roam=True, **kwargs)
```
* name -> str  
    图例名称
* data -> [list], 包含列表的列表  
    数据项，数据中，每一行是一个『数据项』，每一列属于一个『维度』。每一行包含两个或三个数据，如 ["广州", "北京"] 或 ["广州", "北京"，100]，则指定从广州到北京。第三个值用于表示该 line 的数值，该值可省略。
* maptype -> str  
    地图类型。 从 v0.3.2+ 起，地图已经变为扩展包，支持全国省份，全国城市，全国区县，全球国家等地图，具体请参考 [地图自定义篇](zh-cn/customize_map)
* coordinate_region -> str  
    城市坐标所属国家。从 v0.5.7 引入，针对国际城市的地理位置的查找。默认为 `中国`。具体的国家/地区映射表参照 [countries_regions_db.json](https://github.com/pyecharts/pyecharts/blob/master/pyecharts/datasets/countries_regions_db.json)。更多地理坐标信息可以参考 [数据集篇](/zh-cn/datasets)
* symbol -> str  
    线两端的标记类型，可以是一个数组分别指定两端，也可以是单个统一指定。
* symbol_size -> int  
    线两端的标记大小，可以是一个数组分别指定两端，也可以是单个统一指定。
* border_color -> str  
    地图边界颜色。默认为 '#111'
* geo_normal_color -> str  
    正常状态下地图区域的颜色。默认为 '#323c48'
* geo_emphasis_color -> str  
    高亮状态下地图区域的颜色。默认为 '#2a333d'
* geo_cities_coords -> dict  
    用户自定义地区经纬度，类似如 {'阿城': [126.58, 45.32],} 这样的字典。
* geo_effect_period -> int/float  
    特效动画的时间，单位为 s，默认为 6s
* geo_effect_traillength -> float  
    特效尾迹的长度。取从 0 到 1 的值，数值越大尾迹越长。默认为 0
* geo_effect_color -> str  
    特效标记的颜色。默认为 '#fff'
* geo_effect_symbol -> str  
     特效图形的标记。有 'circle', 'rect', 'roundRect', 'triangle', 'diamond', 'pin', 'arrow', 'plane' 可选。
* geo_effect_symbolsize -> int/list  
    特效标记的大小，可以设置成诸如 10 这样单一的数字，也可以用数组分开表示高和宽，例如 [20, 10] 表示标记宽为 20，高为 10。
* is_geo_effect_show -> bool  
    是否显示特效。
* is_roam -> bool  
    是否开启鼠标缩放和平移漫游。默认为 True  
    如果只想要开启缩放或者平移，可以设置成'scale'或者'move'。设置成 True 为都开启

**默认效果**  
这里使用了 Style 类，该类用于统一图表配置风格，具体文档可参考 [图表风格](zh-cn/custom_style)
```python
from pyecharts import GeoLines, Style

style = Style(
    title_top="#fff",
    title_pos = "center",
    width=1200,
    height=600,
    background_color="#404a59"
)

data_guangzhou = [
    ["广州", "上海"],
    ["广州", "北京"],
    ["广州", "南京"],
    ["广州", "重庆"],
    ["广州", "兰州"],
    ["广州", "杭州"]
]
geolines = GeoLines("GeoLines 示例", **style.init_style)
geolines.add("从广州出发", data_guangzhou, is_legend_show=False)
geolines.render()
```
![geolines-demo](https://user-images.githubusercontent.com/19553554/35082101-fb57aeb6-fc52-11e7-92c9-3e9a024e5749.gif)

**稍加配置**
```python
from pyecharts import GeoLines, Style

style_geo = style.add(
    is_label_show=True,
    line_curve=0.2,
    line_opacity=0.6,
    legend_text_color="#eee",
    legend_pos="right",
    geo_effect_symbol="plane",
    geo_effect_symbolsize=15,
    label_color=['#a6c84c', '#ffa022', '#46bee9'],
    label_pos="right",
    label_formatter="{b}",
    label_text_color="#eee",
)
geolines = GeoLines("GeoLines 示例", **style.init_style)
geolines.add("从广州出发", data_guangzhou, **style_geo)
geolines.render()

```
![geolines-demo](https://user-images.githubusercontent.com/19553554/35082102-fd8d884a-fc52-11e7-9e40-5f94098d4493.gif)

**指定数值**
```python
from pyecharts import GeoLines, Style

data_guangzhou = [
    ["广州", "上海", 10],
    ["广州", "北京", 20],
    ["广州", "南京", 30],
    ["广州", "重庆", 40],
    ["广州", "兰州", 50],
    ["广州", "杭州", 60],
]
lines = GeoLines("GeoLines 示例", **style.init_style)
lines.add(
    "从广州出发", data_guangzhou, tooltip_formatter="{a} : {c}", **style_geo
)
lines.render()
```
![geolines-demo](https://user-images.githubusercontent.com/19553554/40048098-eaa7b3aa-5863-11e8-98cd-dcd8526fe820.gif)

**多例模式**
```python
from pyecharts import GeoLines, Style

data_beijing = [
    ["北京", "上海"],
    ["北京", "广州"],
    ["北京", "南京"],
    ["北京", "重庆"],
    ["北京", "兰州"],
    ["北京", "杭州"]
]
geolines = GeoLines("GeoLines 示例", **style.init_style)
geolines.add("从广州出发", data_guangzhou, **style_geo)
geolines.add("从北京出发", data_beijing, **style_geo)
geolines.render()
```
![geolines-demo](https://user-images.githubusercontent.com/19553554/35082103-ff1f2aba-fc52-11e7-97b2-edf837db113e.gif)

**单例模式，指定 `legend_selectedmode="single"`**
```python
from pyecharts import GeoLines, Style

style_geo = style.add(
    is_label_show=True,
    line_curve=0.2,
    line_opacity=0.6,
    legend_text_color="#eee",
    legend_pos="right",
    geo_effect_symbol="plane",
    geo_effect_symbolsize=15,
    label_color=['#a6c84c', '#ffa022', '#46bee9'],
    label_pos="right",
    label_formatter="{b}",
    label_text_color="#eee",
    legend_selectedmode="single", #指定单例模式
)
geolines = GeoLines("GeoLines 示例", **style.init_style)
geolines.add("从广州出发", data_guangzhou, **style_geo)
geolines.add("从北京出发", data_beijing, **style_geo)
geolines.render()
```
![geolines-demo](https://user-images.githubusercontent.com/19553554/35082105-00885b92-fc53-11e7-8803-adc054037285.gif)


## Graph（关系图）
> 用于展现节点以及节点之间的关系数据。

Graph.add() 方法签名
```python
add(name, nodes, links,
    categories=None,
    is_focusnode=True,
    is_roam=True,
    is_rotatelabel=False,
    layout="force",
    graph_edge_length=50,
    graph_gravity=0.2,
    graph_repulsion=50, **kwargs)
```
* name -> str  
    图例名称
* nodes -> dict  
    关系图结点，包含的数据项有  
    * name：结点名称（必须有！）
    * x：节点的初始 x 值
    * y：节点的初始 y 值
    * value：结点数值 
    * category：结点类目
    * symbol：标记图形
    * symbolSize：标记图形大小
* links -> dict  
    结点间的关系数据，包含的数据项有  
    * source：边的源节点名称的字符串，也支持使用数字表示源节点的索引（必须有！）
    * target：边的目标节点名称的字符串，也支持使用数字表示源节点的索引（必须有！）
    * value：边的数值，可以在力引导布局中用于映射到边的长度
* categories -> list  
    结点分类的类目，结点可以指定分类，也可以不指定。  
    如果节点有分类的话可以通过 nodes[i].category 指定每个节点的类目，类目的样式会被应用到节点样式上
* is_focusnode -> bool  
    是否在鼠标移到节点上的时候突出显示节点以及节点的边和邻接节点。默认为 True
* is_roam -> bool/str  
    是否开启鼠标缩放和平移漫游。默认为 True  
    如果只想要开启缩放或者平移，可以设置成'scale'或者'move'。设置成 True 为都开启
* is_rotatelabel -> bool  
    是否旋转标签，默认为 False
* graph_layout -> str  
    关系图布局，默认为 'force'
    * none：不采用任何布局，使用节点中必须提供的 x， y 作为节点的位置。
    * circular：采用环形布局
    * force：采用力引导布局
* graph_edge_length -> int  
    力布局下边的两个节点之间的距离，这个距离也会受 repulsion 影响。默认为 50  
    支持设置成数组表达边长的范围，此时不同大小的值会线性映射到不同的长度。值越小则长度越长
* graph_gravity -> int  
    节点受到的向中心的引力因子。该值越大节点越往中心点靠拢。默认为 0.2
* graph_repulsion -> int  
    节点之间的斥力因子。默认为 50  
    支持设置成数组表达斥力的范围，此时不同大小的值会线性映射到不同的斥力。值越大则斥力越大
* graph_edge_symbol -> str/list  
    边两端的标记类型，可以是一个数组分别指定两端，也可以是单个统一指定。默认不显示标记，常见的可以设置为箭头，如下：edgeSymbol: ['circle', 'arrow']
* graph_edge_symbolsize -> int/list  
    边两端的标记大小，可以是一个数组分别指定两端，也可以是单个统一指定。

```python
from pyecharts import Graph

nodes = [{"name": "结点1", "symbolSize": 10},
         {"name": "结点2", "symbolSize": 20},
         {"name": "结点3", "symbolSize": 30},
         {"name": "结点4", "symbolSize": 40},
         {"name": "结点5", "symbolSize": 50},
         {"name": "结点6", "symbolSize": 40},
         {"name": "结点7", "symbolSize": 30},
         {"name": "结点8", "symbolSize": 20}]
links = []
for i in nodes:
    for j in nodes:
        links.append({"source": i.get('name'), "target": j.get('name')})
graph = Graph("关系图-力引导布局示例")
graph.add("", nodes, links, repulsion=8000)
graph.render()

```
![graph-demo](https://user-images.githubusercontent.com/19553554/35082109-05240854-fc53-11e7-9e92-dd9437c55383.png)

```python
graph = Graph("关系图-环形布局示例")
graph.add(
    "",
    nodes,
    links,
    is_label_show=True,
    graph_repulsion=8000,
    graph_layout="circular",
    label_text_color=None,
)
graph.render()
```
![graph-demo](https://user-images.githubusercontent.com/19553554/35082112-07074726-fc53-11e7-9f28-2d3b39c5e162.png)

**微博转发关系图**
```python
from pyecharts import Graph

import json
with open(os.path.join("fixtures", "weibo.json"), "r", encoding="utf-8") as f:
    j = json.load(f)
    nodes, links, categories, cont, mid, userl = j
graph = Graph("微博转发关系图", width=1200, height=600)
graph.add(
    "",
    nodes,
    links,
    categories,
    label_pos="right",
    graph_repulsion=50,
    is_legend_show=False,
    line_curve=0.2,
    label_text_color=None,
)
graph.render()
```
![graph-demo](https://user-images.githubusercontent.com/19553554/35081908-bb313aba-fc51-11e7-8ef5-df20be445d72.gif)

**Note：** 可配置 **lineStyle** 参数


## HeatMap（热力图）
> 热力图主要通过颜色去表现数值的大小，必须要配合 visualMap 组件使用。直角坐标系上必须要使用两个类目轴。

HeatMap.add() 方法签名
```python
add(*args, **kwargs)
```
如果指定了 `is_calendar_heatmap`（使用日历热力图）为 True，则参数为
* name -> str  
    图例名称
* data -> [list], 包含列表的列表  
    数据项，数据中，每一行是一个『数据项』，每一列属于一个『维度』
* calendar_date_range -> str/list  
    日历热力图的日期, "2016" 表示 2016 年, ["2016-5-5", "2017-5-5"] 表示 2016 年 5 月 5 日至 2017 年 5 月 5 日  
* calendar_cell_size -> list  
    日历每格框的大小，可设置单值 或数组 第一个元素是宽 第二个元素是高，支持设置自适应 "auto"。默认为 ["auto", 20]

默认为不指定，参数为
* name -> str  
    图例名称
* x_axis -> str  
    x 坐标轴数据。需为类目轴，也就是不能是数值。
* y_axis -> str  
    y 坐标轴数据。需为类目轴，也就是不能是数值。
* data -> [list], 包含列表的列表  
    数据项，数据中，每一行是一个『数据项』，每一列属于一个『维度』

**默认情况，不指定 `is_calendar_heatmap`**
```python
import random
from pyecharts import HeatMap

x_axis = [
    "12a", "1a", "2a", "3a", "4a", "5a", "6a", "7a", "8a", "9a", "10a", "11a",
    "12p", "1p", "2p", "3p", "4p", "5p", "6p", "7p", "8p", "9p", "10p", "11p"]
y_axis = [
    "Saturday", "Friday", "Thursday", "Wednesday", "Tuesday", "Monday", "Sunday"]
data = [[i, j, random.randint(0, 50)] for i in range(24) for j in range(7)]
heatmap = HeatMap()
heatmap.add(
    "热力图直角坐标系",
    x_axis,
    y_axis,
    data,
    is_visualmap=True,
    visual_text_color="#000",
    visual_orient="horizontal",
)
heatmap.render()
```
![heatmap-demo](https://user-images.githubusercontent.com/19553554/35090544-f306fcb8-fc74-11e7-8b0a-0284632c3c4d.gif)

**使用日历热力图，指定 `is_calendar_heatmap` 为 True**
```python
import datetime
import random
from pyecharts import HeatMap

begin = datetime.date(2017, 1, 1)
end = datetime.date(2017, 12, 31)
data = [
    [str(begin + datetime.timedelta(days=i)), random.randint(1000, 25000)]
    for i in range((end - begin).days + 1)
]
heatmap = HeatMap("日历热力图示例", "某人 2017 年微信步数情况", width=1100)
heatmap.add(
    "",
    data,
    is_calendar_heatmap=True,
    visual_text_color="#000",
    visual_range_text=["", ""],
    visual_range=[1000, 25000],
    calendar_cell_size=["auto", 30],
    is_visualmap=True,
    calendar_date_range="2017",
    visual_orient="horizontal",
    visual_pos="center",
    visual_top="80%",
    is_piecewise=True,
)
heatmap.render()
```
![heatmap-demo](https://user-images.githubusercontent.com/19553554/35090548-f51dfe0c-fc74-11e7-8a97-012fec231b85.gif)

**Note：** 热力图必须配合 通用配置项 中的 VisualMap 使用才有效果。


## Kline/Candlestick（K线图）
> 红涨蓝跌

Kline.add() 方法签名
```python
add(name, x_axis, y_axis, **kwargs)
```
* name -> str  
    图例名称
* x_axis -> list  
    x 坐标轴数据
* y_axis -> [list], 包含列表的列表   
    y 坐标轴数据。数据中，每一行是一个『数据项』，每一列属于一个『维度』。
    数据项具体为 [open, close, lowest, highest] （即：[开盘值, 收盘值, 最低值, 最高值]）

```python
from pyecharts import Kline

v1 = [[2320.26, 2320.26, 2287.3, 2362.94], [2300, 2291.3, 2288.26, 2308.38],
      [2295.35, 2346.5, 2295.35, 2345.92], [2347.22, 2358.98, 2337.35, 2363.8],
      [2360.75, 2382.48, 2347.89, 2383.76], [2383.43, 2385.42, 2371.23, 2391.82],
      [2377.41, 2419.02, 2369.57, 2421.15], [2425.92, 2428.15, 2417.58, 2440.38],
      [2411, 2433.13, 2403.3, 2437.42], [2432.68, 2334.48, 2427.7, 2441.73],
      [2430.69, 2418.53, 2394.22, 2433.89], [2416.62, 2432.4, 2414.4, 2443.03],
      [2441.91, 2421.56, 2418.43, 2444.8], [2420.26, 2382.91, 2373.53, 2427.07],
      [2383.49, 2397.18, 2370.61, 2397.94], [2378.82, 2325.95, 2309.17, 2378.82],
      [2322.94, 2314.16, 2308.76, 2330.88], [2320.62, 2325.82, 2315.01, 2338.78],
      [2313.74, 2293.34, 2289.89, 2340.71], [2297.77, 2313.22, 2292.03, 2324.63],
      [2322.32, 2365.59, 2308.92, 2366.16], [2364.54, 2359.51, 2330.86, 2369.65],
      [2332.08, 2273.4, 2259.25, 2333.54], [2274.81, 2326.31, 2270.1, 2328.14],
      [2333.61, 2347.18, 2321.6, 2351.44], [2340.44, 2324.29, 2304.27, 2352.02],
      [2326.42, 2318.61, 2314.59, 2333.67], [2314.68, 2310.59, 2296.58, 2320.96],
      [2309.16, 2286.6, 2264.83, 2333.29], [2282.17, 2263.97, 2253.25, 2286.33],
      [2255.77, 2270.28, 2253.31, 2276.22]]
kline = Kline("K 线图示例")
kline.add("日K", ["2017/7/{}".format(i + 1) for i in range(31)], v1)
kline.render()
```
![kline-demo](https://user-images.githubusercontent.com/19553554/35090067-9a247694-fc73-11e7-88bb-3b0f019a5e90.png)

**Kline + dataZoom**
```python
kline = Kline("K 线图示例")
kline.add(
    "日K",
    ["2017/7/{}".format(i + 1) for i in range(31)],
    v1,
    mark_point=["max"],
    is_datazoom_show=True,
)
kline.render()
```
![kline-demo](https://user-images.githubusercontent.com/19553554/35090072-9b6ca404-fc73-11e7-8abe-e5576d35c57a.gif)

**dataZoom 效果加在纵坐标轴上**
```python
kline = Kline("K 线图示例")
kline.add(
    "日K",
    ["2017/7/{}".format(i + 1) for i in range(31)],
    v1,
    mark_point=["max"],
    is_datazoom_show=True,
    datazoom_orient="vertical",
)
kline.render()
```
![kline-demo](https://user-images.githubusercontent.com/19553554/35090075-9d14041e-fc73-11e7-8b89-437ee75a9296.gif)

**指定 markLine 位于开盘或者收盘上**
```python
kline = Kline("K 线图示例")
kline.add(
    "日K",
    ["2017/7/{}".format(i + 1) for i in range(31)],
    v1,
    mark_line=["max"],
    mark_line_symbolsize=0,
    datazoom_orient="vertical",
    mark_line_valuedim="close",
)
kline.render()
```
![kline-demo](https://user-images.githubusercontent.com/19553554/35090078-9e901a44-fc73-11e7-835c-3408cc960bac.png)


## Line（折线/面积图）
> 折线图是用折线将各个数据点标志连接起来的图表，用于展现数据的变化趋势。

Line.add() 方法签名
```python
add(name, x_axis, y_axis,
    is_symbol_show=True,
    is_smooth=False,
    is_stack=False,
    is_step=False, **kwargs)
```
* name -> str  
    图例名称
* x_axis -> list  
    x 坐标轴数据
* y_axis -> list  
    y 坐标轴数据
* is_symbol_show -> bool  
    是否显示标记图形，默认为 True
* is_smooth -> bool  
    是否平滑曲线显示，默认为 False
* is_stack -> bool  
    数据堆叠，同个类目轴上系列配置相同的 stack 值可以堆叠放置。默认为 False
* is_step -> bool/str  
    是否是阶梯线图。可以设置为 True 显示成阶梯线图。默认为 False  
    也支持设置成'start', 'middle', 'end'分别配置在当前点，当前点与下个点的中间下个点拐弯。

```python
from pyecharts import Line

attr = ["衬衫", "羊毛衫", "雪纺衫", "裤子", "高跟鞋", "袜子"]
v1 = [5, 20, 36, 10, 10, 100]
v2 = [55, 60, 16, 20, 15, 80]
line = Line("折线图示例")
line.add("商家A", attr, v1, mark_point=["average"])
line.add("商家B", attr, v2, is_smooth=True, mark_line=["max", "average"])
line.render()
```
![line-demo](https://user-images.githubusercontent.com/19553554/35089953-4865fe2c-fc73-11e7-8c47-e917332d061c.gif)

**标记点其他配置**
```python
line = Line("折线图示例")
line.add(
    "商家A",
    attr,
    v1,
    mark_point=["average", "max", "min"],
    mark_point_symbol="diamond",
    mark_point_textcolor="#40ff27",
)
line.add(
    "商家B",
    attr,
    v2,
    mark_point=["average", "max", "min"],
    mark_point_symbol="arrow",
    mark_point_symbolsize=40,
)
line.render()
```
![line-demo](https://user-images.githubusercontent.com/19553554/35089954-49784dd8-fc73-11e7-8a5b-d9163857c4b1.png)

```python
line = Line("折线图示例")
line.add(
    "商家A",
    attr,
    v1,
    mark_point=["average", {"coord": ["裤子", 10], "name": "这是我想要的第一个标记点"}],
)
line.add(
    "商家B",
    attr,
    v2,
    is_smooth=True,
    mark_point=[{"coord": ["袜子", 80], "name": "这是我想要的第二个标记点"}],
)
line.render()
```
![line-demo](https://user-images.githubusercontent.com/19553554/35089957-4af28598-fc73-11e7-967b-cb6a431ed542.gif)

```python
line = Line("折线图-数据堆叠示例")
line.add("商家A", attr, v1, is_stack=True, is_label_show=True)
line.add("商家B", attr, v2, is_stack=True, is_label_show=True)
line.render()
```
![line-demo](https://user-images.githubusercontent.com/19553554/35089965-4f880100-fc73-11e7-9861-c43bd4d4bbe1.gif)

```python
line = Line("折线图-阶梯图示例")
line.add("商家A", attr, v1, is_step=True, is_label_show=True)
line.render()
```
![line-demo](https://user-images.githubusercontent.com/19553554/35089968-510f3304-fc73-11e7-9159-67ce6ace9fa3.png)

**使用 area_opacity：** area_opacity 用于指定区域透明度，0 为完全不透明（默认），1 为完全透明。
```python
line = Line("折线图-面积图示例")
line.add(
    "商家A",
    attr,
    v1,
    line_opacity=0.2,
    area_opacity=0.4,
    symbol=None,
)
line.add(
    "商家B",
    attr,
    v2,
    is_fill=True,
    area_color="#000",
    area_opacity=0.3,
    is_smooth=True,
)
line.render()
```
![line-demo](https://user-images.githubusercontent.com/19553554/35089973-53868fd8-fc73-11e7-8ff6-bfb452954267.png)

* area_opacity -> float  
    填充区域透明度
* area_color -> str  
    填充区域颜色

**Note：** 可配置 **lineStyle** 参数  
**Note：** 可以通过 label_color 来设置线条颜色，如 ['#eee', '#000']，所有的图表类型的图例颜色都可通过 label_color 来修改。

**如果是对数数据，推荐使用 ```yaxis_type``` 参数来设置 y 坐标轴为对数轴**
```python
import math, random
line = Line("折线图示例")
line.add("商家A", attr, [math.log10(random.randint(1, 99999)) for _ in range(6)])
line.add(
    "商家B",
    attr,
    [math.log10(random.randint(1, 99999999)) for _ in range(6)],
    yaxis_type="log",
)
line.render()
```
![line-demo](https://user-images.githubusercontent.com/19553554/35089976-5473125e-fc73-11e7-809c-adbfe6834b61.png)

**某地最低温和最高气温折线图**
```python
from pyecharts import Line

attr = ['周一', '周二', '周三', '周四', '周五', '周六', '周日']
line = Line("折线图示例")
line.add(
    "最高气温",
    attr,
    [11, 11, 15, 13, 12, 13, 10],
    mark_point=["max", "min"],
    mark_line=["average"],
)
line.add(
    "最低气温",
    attr,
    [1, -2, 2, 5, 3, 2, 0],
    mark_point=["max", "min"],
    mark_line=["average"],
    yaxis_formatter="°C",
)
line.render()
```
![line-demo](https://user-images.githubusercontent.com/19553554/35089980-5649aed0-fc73-11e7-9e8f-01ed75ad7418.gif)


## Line3D（3D 折线图）
Line3D.add() 方法签名
```python
add(name, data,
    grid3d_opacity=1, **kwargs)
```
* name -> str  
    图例名称
* data -> [list], 包含列表的列表  
    数据项，数据中，每一行是一个『数据项』，每一列属于一个『维度』
* grid3d_opacity -> int  
    3D 笛卡尔坐标系组的透明度（线的透明度），默认为 1，完全不透明。

**画个弹簧**
```python
from pyecharts import Line3D

import math
_data = []
for t in range(0, 25000):
    _t = t / 1000
    x = (1 + 0.25 * math.cos(75 * _t)) * math.cos(_t)
    y = (1 + 0.25 * math.cos(75 * _t)) * math.sin(_t)
    z = _t + 2.0 * math.sin(75 * _t)
    _data.append([x, y, z])
range_color = [
    '#313695', '#4575b4', '#74add1', '#abd9e9', '#e0f3f8', '#ffffbf',
    '#fee090', '#fdae61', '#f46d43', '#d73027', '#a50026']
line3d = Line3D("3D 折线图示例", width=1200, height=600)
line3d.add(
    "",
    _data,
    is_visualmap=True,
    visual_range_color=range_color,
    visual_range=[0, 30],
    grid3d_rotate_sensitivity=5,
)
line3d.render()
```
![line3d-demo](https://user-images.githubusercontent.com/19553554/35081902-b0bed8c6-fc51-11e7-9b3a-1d138c4eba13.gif)

**旋转弹簧**
```python
from pyecharts import Line3D

import math
_data = []
for t in range(0, 25000):
    _t = t / 1000
    x = (1 + 0.25 * math.cos(75 * _t)) * math.cos(_t)
    y = (1 + 0.25 * math.cos(75 * _t)) * math.sin(_t)
    z = _t + 2.0 * math.sin(75 * _t)
    _data.append([x, y, z])
range_color = [
    '#313695', '#4575b4', '#74add1', '#abd9e9', '#e0f3f8', '#ffffbf',
    '#fee090', '#fdae61', '#f46d43', '#d73027', '#a50026']
line3d = Line3D("3D 折线图示例", width=1200, height=600)
line3d.add(
    "",
    _data,
    is_visualmap=True,
    visual_range_color=range_color,
    visual_range=[0, 30],
    is_grid3d_rotate=True,
    grid3d_rotate_speed=180,
)
line3d.render()
```
![line3d-demo](https://user-images.githubusercontent.com/19553554/35081903-b3a4eada-fc51-11e7-97b1-33f1dd6ed79e.gif)

**Note：** 关于 gird3D 部分的设置，请参照通用配置项中的介绍 通用配置项  
**Note：** 可配合 axis3D 通用配置项 一起使用 


## Liquid（水球图）
> 主要用来突出数据的百分比。

Liquid.add() 方法签名
```python
add(name, data,
    shape='circle',
    liquid_color=None,
    is_liquid_animation=True,
    is_liquid_outline_show=True, **kwargs)
```
* name -> str  
    图例名称
* data -> list  
    数据项
* shape -> str  
    水球外形，有'circle', 'rect', 'roundRect', 'triangle', 'diamond', 'pin', 'arrow'可选。默认'circle'。也可以为自定义的 SVG 路径。
* liquid_color -> list  
    波浪颜色，默认的颜色列表为['#294D99', '#156ACF', '#1598ED', '#45BDFF']。
* is_liquid_animation -> bool  
    是否显示波浪动画，默认为 True。
* is_liquid_outline_show -> bool  
    是否显示边框，默认为 True。

```python
from pyecharts import Liquid

liquid = Liquid("水球图示例")
liquid.add("Liquid", [0.6])
liquid.render()
```
![liquid-demo](https://user-images.githubusercontent.com/19553554/35082172-536178a8-fc53-11e7-8c8b-1fa1312c8854.gif)

```python
from pyecharts import Liquid

liquid = Liquid("水球图示例")
liquid.add("Liquid", [0.6, 0.5, 0.4, 0.3], is_liquid_outline_show=False)
liquid.render()
```
![liquid-demo](https://user-images.githubusercontent.com/19553554/35082175-55337000-fc53-11e7-9e5b-24cd47288e8d.gif)

```python
from pyecharts import Liquid

liquid = Liquid("水球图示例")
liquid.add("Liquid", [0.6, 0.5, 0.4, 0.3],
           is_liquid_animation=False, shape='diamond')
liquid.render()
```
![liquid-demo](https://user-images.githubusercontent.com/19553554/35082178-567d2db6-fc53-11e7-965a-d60e72ab6bf4.png)

**自定义 SVG 路径**
```python
from pyecharts import Liquid

shape = ("path://M367.855,428.202c-3.674-1.385-7.452-1.966-11.146-1"
         ".794c0.659-2.922,0.844-5.85,0.58-8.719 c-0.937-10.407-7."
         "663-19.864-18.063-23.834c-10.697-4.043-22.298-1.168-29.9"
         "02,6.403c3.015,0.026,6.074,0.594,9.035,1.728 c13.626,5."
         "151,20.465,20.379,15.32,34.004c-1.905,5.02-5.177,9.115-9"
         ".22,12.05c-6.951,4.992-16.19,6.536-24.777,3.271 c-13.625"
         "-5.137-20.471-20.371-15.32-34.004c0.673-1.768,1.523-3.423"
         ",2.526-4.992h-0.014c0,0,0,0,0,0.014 c4.386-6.853,8.145-14"
         ".279,11.146-22.187c23.294-61.505-7.689-130.278-69.215-153"
         ".579c-61.532-23.293-130.279,7.69-153.579,69.202 c-6.371,"
         "16.785-8.679,34.097-7.426,50.901c0.026,0.554,0.079,1.121,"
         "0.132,1.688c4.973,57.107,41.767,109.148,98.945,130.793 c58."
         "162,22.008,121.303,6.529,162.839-34.465c7.103-6.893,17.826"
         "-9.444,27.679-5.719c11.858,4.491,18.565,16.6,16.719,28.643 "
         "c4.438-3.126,8.033-7.564,10.117-13.045C389.751,449.992,"
         "382.411,433.709,367.855,428.202z")
liquid = Liquid("水球图示例", width=1000, height=600)
liquid.add("Liquid", [0.6, 0.5, 0.4, 0.3],
           shape=shape, is_liquid_outline_show=False)
liquid.render()
```
![liquid-demo](https://user-images.githubusercontent.com/19553554/35082181-5863dfda-fc53-11e7-9807-507ac5639638.gif)


## Map（地图）
> 地图主要用于地理区域数据的可视化。

Map.add() 方法签名
```python
add(name, attr, value,
    maptype='china',
    is_roam=True,
    is_map_symbol_show=True, **kwargs)
```
* name -> str  
    图例名称
* attr -> list  
   属性名称
* value -> list  
   属性所对应的值
* maptype -> str  
    地图类型。 从 v0.3.2+ 起，地图已经变为扩展包，支持全国省份，全国城市，全国区县，全球国家等地图，具体请参考 [地图自定义篇](zh-cn/customize_map)
* is_roam -> bool/str  
   是否开启鼠标缩放和平移漫游。默认为 True  
   如果只想要开启缩放或者平移，可以设置成'scale'或者'move'。设置成 True 为都开启
* is_map_symbol_show -> bool  
    是否显示地图标记红点，默认为 True。
* name_map -> dict  
    [用自定义的地图名称](http://echarts.baidu.com/option.html#series-map.nameMap). 有些地图提供行政区号，`name_map` 可以帮助把它们转换成用户满意的地名。比如英国选区地图，伦敦选区的行政区号是 E14000639 ，把它转换成可读地名就需要这么一个字典：  
    ```
    name_map = {"E14000639": "Cities of London and Westminster"}
    ```

    以此类推，把英国选区所有的地名都转换一下，就需要个[更大一些的字典](https://github.com/chfw/echarts-united-kingdom-pypkg/blob/master/echarts_united_kingdom_pypkg/constants.py#L1)。

```python
from pyecharts import Map

value = [155, 10, 66, 78]
attr = ["福建", "山东", "北京", "上海"]
map = Map("全国地图示例", width=1200, height=600)
map.add("", attr, value, maptype='china')
map.render()
```
![map-demo](https://user-images.githubusercontent.com/19553554/35082377-718385f0-fc54-11e7-88c2-bd1df8bf112b.gif)

**显示各区域名称**
```python
from pyecharts import Map

value = [155, 10, 66, 78]
attr = ["福建", "山东", "北京", "上海"]
map = Map("全国地图示例", width=1200, height=600)
map.add("", attr, value, maptype='china', is_label_show=True)
map.render()
```
![map-demo](https://user-images.githubusercontent.com/19553554/35082379-7463a0f2-fc54-11e7-9bee-d71e8ec3acc8.png)

```python
from pyecharts import Map

value = [155, 10, 66, 78, 33, 80, 190, 53, 49.6]
attr = [
    "福建", "山东", "北京", "上海", "甘肃", "新疆", "河南", "广西", "西藏"
    ]
map = Map("Map 结合 VisualMap 示例", width=1200, height=600)
map.add(
    "",
    attr,
    value,
    maptype="china",
    is_visualmap=True,
    visual_text_color="#000",
)
map.render()
```
![map-demo](https://user-images.githubusercontent.com/19553554/35082380-75e1b89c-fc54-11e7-8169-75884ffb67fb.gif)

**Note：** 请配合 通用配置项 中的 Visualmap 使用

```python
from pyecharts import Map

value = [20, 190, 253, 77, 65]
attr = ['汕头市', '汕尾市', '揭阳市', '阳江市', '肇庆市']
map = Map("广东地图示例", width=1200, height=600)
map.add(
    "", attr, value, maptype="广东", is_visualmap=True, visual_text_color="#000"
)
map.render()
```
![map-demo](https://user-images.githubusercontent.com/19553554/35082381-786c8542-fc54-11e7-8886-5e4047fbeefd.gif)

```python
value = [95.1, 23.2, 43.3, 66.4, 88.5]
attr= ["China", "Canada", "Brazil", "Russia", "United States"]
map = Map("世界地图示例", width=1200, height=600)
map.add(
    "",
    attr,
    value,
    maptype="world",
    is_visualmap=True,
    visual_text_color="#000",
)
map.render()
```
![map-demo](https://user-images.githubusercontent.com/19553554/35082382-7a37df3e-fc54-11e7-93e8-f9c02e465a2f.gif)

**设置 `is_map_symbol_show=False` 取消显示标记红点**
```python
value = [95.1, 23.2, 43.3, 66.4, 88.5]
attr= ["China", "Canada", "Brazil", "Russia", "United States"]
map = Map("世界地图示例", width=1200, height=600)
map.add(
    "",
    attr,
    value,
    maptype="world",
    is_visualmap=True,
    visual_text_color="#000",
    is_map_symbol_show=False,
)
map.render()
```
![map-demo](https://user-images.githubusercontent.com/19553554/35082387-7d35893e-fc54-11e7-8482-60dc23d31836.png)

**设置 `name_map` 采用自己地图名称**
原版：
![map-demo](https://user-images.githubusercontent.com/4280312/36720467-16fb0a66-1ba0-11e8-8cbd-453d8f2462d3.png)
    
用 `name_map` 改动之后：

```python
#coding=utf-8
from __future__ import unicode_literals

from pyecharts import Map
from echarts_united_kingdom_pypkg import NM_WESTMINSTER_2016_UK

value = []
attr = []
map = Map('United Kingdom', width=800, height=600)
map.add(
    "",
    attr,
    value,
    maptype="英国选区2016",
    is_visualmap=True,
    visual_text_color="#000",
    name_map=NM_WESTMINSTER_2016_UK,
)
map.render()
```
![map-demo](https://user-images.githubusercontent.com/4280312/36720626-803ff194-1ba0-11e8-998b-548afbedc18e.png)

这个方便画图，因为很多数据和地区号直接挂钩，同时也容易做本地化。

设置 `pieces` 自定义 visualMap 组件标签
```python
value = [155, 10, 66, 78]
attr = ["福建", "山东", "北京", "上海"]
map = Map("全国地图示例", width=1200, height=600)
map.add("", attr, value, maptype='china',
        is_visualmap=True, is_piecewise=True,
        visual_text_color="#000",
        visual_range_text=["", ""],
        pieces=[
            {"max": 160, "min": 70, "label": "高数值"},
            {"max": 69, "min": 0, "label": "低数值"},
        ])
map.render()
```
![map-demo](https://user-images.githubusercontent.com/19553554/36943053-22748c70-1fbd-11e8-86dc-ac3d48f5c4e3.png)


## Parallel（平行坐标系）
> 平行坐标系是一种常用的可视化高维数据的图表。

Parallel.add() 方法签名
```python
add(name, data, **kwargs)
```
* name -> str  
    图例名称
* data -> [list], 包含列表的列表  
    数据项。数据中，每一行是一个『数据项』，每一列属于一个『维度』

Parallel.set_schema() / Parallel.config() 方法签名
```python
set_schema(schema=None, c_schema=None)
config(schema=None, c_schema=None)
```

> 从 v0.5.9 开始，原有 `config` 方法被废弃，推荐使用 set_schema 方法。

* schema  
    默认平行坐标系的坐标轴信息，如 ["dim_name1", "dim_name2", "dim_name3"]。
* c_schema  
    用户自定义平行坐标系的坐标轴信息。
    * dim -> int   
        维度索引
    * name -> str  
        维度名称
    * type -> str   
        维度类型，有'value', 'category'可选  
        value：数值轴，适用于连续数据。  
        category： 类目轴，适用于离散的类目数据。
    * min -> int  
        坐标轴刻度最小值。
    * max -> int  
        坐标轴刻度最大值。
    * inverse - bool  
        是否是反向坐标轴。默认为 False
    * nameLocation -> str  
        坐标轴名称显示位置。有'start', 'middle', 'end'可选

```python
from pyecharts import Parallel

schema = ["data", "AQI", "PM2.5", "PM10", "CO", "NO2"]
data = [
        [1, 91, 45, 125, 0.82, 34],
        [2, 65, 27, 78, 0.86, 45,],
        [3, 83, 60, 84, 1.09, 73],
        [4, 109, 81, 121, 1.28, 68],
        [5, 106, 77, 114, 1.07, 55],
        [6, 109, 81, 121, 1.28, 68],
        [7, 106, 77, 114, 1.07, 55],
        [8, 89, 65, 78, 0.86, 51, 26],
        [9, 53, 33, 47, 0.64, 50, 17],
        [10, 80, 55, 80, 1.01, 75, 24],
        [11, 117, 81, 124, 1.03, 45]
]
parallel = Parallel("平行坐标系-默认指示器")
parallel.config(schema) 
parallel.add("parallel", data, is_random=True)
parallel.render()
```
![parallel-demo](https://user-images.githubusercontent.com/19553554/35090275-17c3dcde-fc74-11e7-94d6-e497668dba0c.png)

```python
from pyecharts import Parallel

c_schema = [
    {"dim": 0, "name": "data"},
    {"dim": 1, "name": "AQI"},
    {"dim": 2, "name": "PM2.5"},
    {"dim": 3, "name": "PM10"},
    {"dim": 4, "name": "CO"},
    {"dim": 5, "name": "NO2"},
    {"dim": 6, "name": "CO2"},
    {"dim": 7, "name": "等级",
    "type": "category",
    "data": ['优', '良', '轻度污染', '中度污染', '重度污染', '严重污染']}
]
data = [
    [1, 91, 45, 125, 0.82, 34, 23, "良"],
    [2, 65, 27, 78, 0.86, 45, 29, "良"],
    [3, 83, 60, 84, 1.09, 73, 27, "良"],
    [4, 109, 81, 121, 1.28, 68, 51, "轻度污染"],
    [5, 106, 77, 114, 1.07, 55, 51, "轻度污染"],
    [6, 109, 81, 121, 1.28, 68, 51, "轻度污染"],
    [7, 106, 77, 114, 1.07, 55, 51, "轻度污染"],
    [8, 89, 65, 78, 0.86, 51, 26, "良"],
    [9, 53, 33, 47, 0.64, 50, 17, "良"],
    [10, 80, 55, 80, 1.01, 75, 24, "良"],
    [11, 117, 81, 124, 1.03, 45, 24, "轻度污染"],
    [12, 99, 71, 142, 1.1, 62, 42, "良"],
    [13, 95, 69, 130, 1.28, 74, 50, "良"],
    [14, 116, 87, 131, 1.47, 84, 40, "轻度污染"]
]
parallel = Parallel("平行坐标系-用户自定义指示器")
parallel.config(c_schema=c_schema)
parallel.add("parallel", data)
parallel.render()
```
![parallel-demo](https://user-images.githubusercontent.com/19553554/35090278-19ac1674-fc74-11e7-9aa1-2662296d3e22.png)

**Note：** 可配置 **lineStyle** 参数


## Pie（饼图）
> 饼图主要用于表现不同类目的数据在总和中的占比。每个的弧度表示数据数量的比例。

Pie.add() 方法签名
```python
add(name, attr, value,
    radius=None,
    center=None,
    rosetype=None, **kwargs)
```
* name -> str   
    图例名称
* attr -> list  
    属性名称
* value -> list  
    属性所对应的值
* radius -> list  
    饼图的半径，数组的第一项是内半径，第二项是外半径，默认为 [0, 75]  
    默认设置成百分比，相对于容器高宽中较小的一项的一半
* center -> list  
    饼图的中心（圆心）坐标，数组的第一项是横坐标，第二项是纵坐标，默认为 [50, 50]  
    默认设置成百分比，设置成百分比时第一项是相对于容器宽度，第二项是相对于容器高度
* rosetype -> str  
    是否展示成南丁格尔图，通过半径区分数据大小，有'radius'和'area'两种模式。默认为'radius'
    * radius：扇区圆心角展现数据的百分比，半径展现数据的大小
    * area：所有扇区圆心角相同，仅通过半径展现数据大小

```python
from pyecharts import Pie

attr = ["衬衫", "羊毛衫", "雪纺衫", "裤子", "高跟鞋", "袜子"]
v1 = [11, 12, 13, 10, 10, 10]
pie = Pie("饼图示例")
pie.add("", attr, v1, is_label_show=True)
pie.render()
```
![pie-demo](https://user-images.githubusercontent.com/19553554/35089599-5eed1ef6-fc72-11e7-8740-601880be9e16.gif)

```python
from pyecharts import Pie

attr = ["衬衫", "羊毛衫", "雪纺衫", "裤子", "高跟鞋", "袜子"]
v1 = [11, 12, 13, 10, 10, 10]
pie = Pie("饼图-圆环图示例", title_pos='center')
pie.add(
    "",
    attr,
    v1,
    radius=[40, 75],
    label_text_color=None,
    is_label_show=True,
    legend_orient="vertical",
    legend_pos="left",
)
pie.render()
```
![pie-demo](https://user-images.githubusercontent.com/19553554/35089631-70b6e7de-fc72-11e7-838d-f8b238bbc03f.png)

```python
from pyecharts import Pie

attr = ["衬衫", "羊毛衫", "雪纺衫", "裤子", "高跟鞋", "袜子"]
v1 = [11, 12, 13, 10, 10, 10]
v2 = [19, 21, 32, 20, 20, 33]
pie = Pie("饼图-玫瑰图示例", title_pos='center', width=900)
pie.add(
    "商品A",
    attr,
    v1,
    center=[25, 50],
    is_random=True,
    radius=[30, 75],
    rosetype="radius",
)
pie.add(
    "商品B",
    attr,
    v2,
    center=[75, 50],
    is_random=True,
    radius=[30, 75],
    rosetype="area",
    is_legend_show=False,
    is_label_show=True,
)
pie.render()
```
![pie-demo](https://user-images.githubusercontent.com/19553554/35089635-72585da2-fc72-11e7-835d-c9b64750d19d.png)

**饼中饼**
```python
import random
from pyecharts import Pie

attr = ['A', 'B', 'C', 'D', 'E', 'F']
pie = Pie("饼图示例", width=1000, height=600)
pie.add(
    "",
    attr,
    [random.randint(0, 100) for _ in range(6)],
    radius=[50, 55],
    center=[25, 50],
    is_random=True,
)
pie.add(
    "",
    attr,
    [random.randint(20, 100) for _ in range(6)],
    radius=[0, 45],
    center=[25, 50],
    rosetype="area",
)
pie.add(
    "",
    attr,
    [random.randint(0, 100) for _ in range(6)],
    radius=[50, 55],
    center=[65, 50],
    is_random=True,
)
pie.add(
    "",
    attr,
    [random.randint(20, 100) for _ in range(6)],
    radius=[0, 45],
    center=[65, 50],
    rosetype="radius",
)
pie.render()
```
![pie-demo](https://user-images.githubusercontent.com/19553554/35089639-73f0e2c4-fc72-11e7-9fba-84376a94314c.gif)

**多个饼图画在一张图内**
```python
from pyecharts import Pie

pie = Pie('各类电影中"好片"所占的比例', "数据来着豆瓣", title_pos='center')
style = Style()
pie_style = style.add(
    label_pos="center",
    is_label_show=True,
    label_text_color=None
)

pie.add(
    "", ["剧情", ""], [25, 75], center=[10, 30], radius=[18, 24], **pie_style
)
pie.add(
    "", ["奇幻", ""], [24, 76], center=[30, 30], radius=[18, 24], **pie_style
)
pie.add(
    "", ["爱情", ""], [14, 86], center=[50, 30], radius=[18, 24], **pie_style
)
pie.add(
    "", ["惊悚", ""], [11, 89], center=[70, 30], radius=[18, 24], **pie_style
)
pie.add(
    "", ["冒险", ""], [27, 73], center=[90, 30], radius=[18, 24], **pie_style
)
pie.add(
    "", ["动作", ""], [15, 85], center=[10, 70], radius=[18, 24], **pie_style
)
pie.add(
    "", ["喜剧", ""], [54, 46], center=[30, 70], radius=[18, 24], **pie_style
)
pie.add(
    "", ["科幻", ""], [26, 74], center=[50, 70], radius=[18, 24], **pie_style
)
pie.add(
    "", ["悬疑", ""], [25, 75], center=[70, 70], radius=[18, 24], **pie_style
)
pie.add(
    "",
    ["犯罪", ""],
    [28, 72],
    center=[90, 70],
    radius=[18, 24],
    legend_top="center",
    **pie_style
)
pie.render()
```
![pie-demo](https://user-images.githubusercontent.com/19553554/35089644-76cbcb9e-fc72-11e7-8b9e-d5bebc78e8a1.gif)


## Polar（极坐标系）
> 可以用于散点图和折线图。

Polar.add() 方法签名
```python
add(name, data,
    angle_data=None,
    radius_data=None,
    type='line',
    symbol_size=4,
    start_angle=90,
    rotate_step=0,
    boundary_gap=True,
    clockwise=True, **kwargs)
```
* name -> str  
    图例名称
* data -> [list], 包含列表的列表  
    数据项 [极径，极角 [数据值]]
* angle_data -> list  
    角度类目数据
* radius_data -> list  
    半径类目数据
* type -> str  
    图例类型，有'line', 'scatter', 'effectScatter', 'barAngle', 'barRadius'可选。默认为 'line'
* symbol_size -> int  
    标记图形大小，默认为 4。
* start_angle -> int  
    起始刻度的角度，默认为 90 度，即圆心的正上方。0 度为圆心的正右方
* rotate_step -> int  
    刻度标签旋转的角度，在类目轴的类目标签显示不下的时候可以通过旋转防止标签之间重叠  
    旋转的角度从 -90 度到 90 度。默认为 0
* boundary_gap -> bool  
    坐标轴两边留白策略  
    默认为 True，这时候刻度只是作为分隔线，标签和数据点都会在两个刻度之间的带(band)中间
* clockwise -> bool  
    刻度增长是否按顺时针，默认 True
* is_stack -> bool  
    数据堆叠，同个类目轴上系列配置相同的 stack 值可以堆叠放置
* axis_range -> list  
    坐标轴刻度范围。默认值为 [None, None]。
* angleaxis_label_interval -> int/str  
    坐标轴刻度标签的显示间隔，在类目轴中有效。  
    可以采用标签不重叠的策略间隔显示标签，即'auto'。可以设置成 0 强制显示所有标签。如果设置为 1，表示『隔一个标签显示一个标签』，如果值为 2，表示隔两个标签显示一个标签，以此类推。默认为 0。
* is_angleaxis_show -> bool  
    是否显示极坐标系的角度轴，默认为 True
* radiusaxis_z_index -> int
    radius 轴的 z 指数，默认为 50
* angleaxis_z_index -> int
    angel 轴的 z 指数，默认为 50
* is_radiusaxis_show -> bool  
    是否显示极坐标系的径向轴，默认为 True
* render_item -> function  
    开发者自己提供图形渲染的逻辑, 这个渲染逻辑一般命名为 [render_item](http://echarts.baidu.com/option.html#series-custom.renderItem)，参考 [高级用法篇](zh-cn/advanced)

```python
from pyecharts import Polar

import random
data = [(i, random.randint(1, 100)) for i in range(101)]
polar = Polar("极坐标系-散点图示例")
polar.add(
    "",
    data,
    boundary_gap=False,
    type="scatter",
    is_splitline_show=False,
    area_color=None,
    is_axisline_show=True,
)
polar.render()
```
![polar-demo](https://user-images.githubusercontent.com/19553554/35090448-aaf0d5a2-fc74-11e7-83c4-7b2f55090e98.png)

* is_splitline_show  -> bool  
    是否显示分割线，默认为 True
* is_axisline_show -> bool  
    是否显示坐标轴线，默认为 True
* area_opacity -> float  
    填充区域透明度
* area_color -> str  
    填充区域颜色

**Note：** 可配置 **lineStyle** 参数

```python
from pyecharts import Polar

import random
data_1 = [(10, random.randint(1, 100)) for i in range(300)]
data_2 = [(11, random.randint(1, 100)) for i in range(300)]
polar = Polar("极坐标系-散点图示例", width=1200, height=600)
polar.add("", data_1, type='scatter')
polar.add("", data_2, type='scatter')
polar.render()
```
![polar-demo](https://user-images.githubusercontent.com/19553554/35090451-abf708e0-fc74-11e7-8814-25ba5e72f542.png)

```python
from pyecharts import Polar

import random
data = [(i, random.randint(1, 100)) for i in range(10)]
polar = Polar("极坐标系-动态散点图示例", width=1200, height=600)
polar.add("", data, type='effectScatter', effect_scale=10, effect_period=5)
polar.render()
```
![polar-demo](https://user-images.githubusercontent.com/19553554/35090453-ad2b4d52-fc74-11e7-8ecd-cb64546d0d40.gif)

```python
from pyecharts import Polar

radius = ['周一', '周二', '周三', '周四', '周五', '周六', '周日']
polar = Polar("极坐标系-堆叠柱状图示例", width=1200, height=600)
polar.add(
    "A",
    [1, 2, 3, 4, 3, 5, 1],
    radius_data=radius,
    type="barRadius",
    is_stack=True,
)
polar.add(
    "B",
    [2, 4, 6, 1, 2, 3, 1],
    radius_data=radius,
    type="barRadius",
    is_stack=True,
)
polar.add(
    "C",
    [1, 2, 3, 4, 1, 2, 5],
    radius_data=radius,
    type="barRadius",
    is_stack=True,
)
polar.render()
```
![polar-demo](https://user-images.githubusercontent.com/19553554/35090457-afc0658e-fc74-11e7-9c58-24c780436287.gif)

```python
from pyecharts import Polar

angle = ['周一', '周二', '周三', '周四', '周五', '周六', '周日']
polar = Polar("极坐标系-堆叠柱状图示例", width=1200, height=600)
polar.add(
    "",
    [1, 2, 3, 4, 3, 5, 1],
    angle_data=angle,
    type="barAngle",
    is_stack=True,
)
polar.add(
    "",
    [2, 4, 6, 1, 2, 3, 1],
    angle_data=angle,
    type="barAngle",
    is_stack=True,
)
polar.add(
    "",
    [1, 2, 3, 4, 1, 2, 5],
    angle_data=angle,
    type="barAngle",
    is_stack=True,
)
polar.render()
```
![polar-demo](https://user-images.githubusercontent.com/19553554/35090460-b11ab380-fc74-11e7-836c-2e8197e32723.png)

**自定义渲染逻辑示例**
```python
from pyecharts import Polar

def render_item(params, api):
    values = [api.value(0), api.value(1)]
    coord = api.coord(values)
    size = api.size([1, 1], values)
    return {
        "type": "sector",
        "shape": {
            "cx": params.coordSys.cx,
            "cy": params.coordSys.cy,
            "r0": coord[2] - size[0] / 2,
            "r": coord[2] + size[0] / 2,
            "startAngle": coord[3] - size[1] / 2,
            "endAngle": coord[3] + size[1] / 2,
        },
        "style": api.style({"fill": api.visual("color")}),
    }

polar = Polar("自定义渲染逻辑示例", width=1200, height=600)
polar.add(
    "",
    [
        [
            random.randint(0, 6),
            random.randint(1, 24),
            random.randint(1, 24),
        ]
        for _ in range(100)
    ],
    render_item=render_item,
    type="custom",
    angle_data=X_TIME,
    radius_data=WEEK,
    is_visualmap=True,
    visual_range=[0, 30]
)
polar.render()
```
![polar-demo](https://user-images.githubusercontent.com/19553554/40104662-820a82ee-5923-11e8-8052-9bd8fcb70623.png)


## Radar（雷达图）
> 雷达图主要用于表现多变量的数据。

Radar.add() 方法签名
```python
add(name, value,
    item_color=None, **kwargs)
```
* name -> list  
    图例名称
* value -> [list], 包含列表的列表  
    数据项。数据中，每一行是一个『数据项』，每一列属于一个『维度』
* item_color -> str  
    指定单图例颜色

Radar.set_radar_component() / Radar.config() 方法签名
```python

set_radar_component(schema=None,
    c_schema=None,
    shape="",
    rader_text_color="#000", **kwargs):
	
config(schema=None,
    c_schema=None,
    shape="",
    rader_text_color="#000", **kwargs):
```

> 从 v0.5.9 开始，原有的 `config` 被废弃，推荐使用 `set_radar_component` 方法。

* schema -> list  
    默认雷达图的指示器，用来指定雷达图中的多个维度，会对数据处理成 {name:xx, value:xx} 的字典
* c_schema -> dict  
    用户自定义雷达图的指示器，用来指定雷达图中的多个维度
    * name: 指示器名称
    * min: 指示器最小值
    * max: 指示器最大值
* shape -> str  
    雷达图绘制类型，有'polygon'（多边形）和'circle'可选
* rader_text_color -> str  
    雷达图数据项字体颜色，默认为'#000'
* radar_text_size -> int  
    雷达图数据项字体大小，默认为 12

```python
from pyecharts import Radar

schema = [ 
    ("销售", 6500), ("管理", 16000), ("信息技术", 30000),
    ("客服", 38000), ("研发", 52000), ("市场", 25000)
]
v1 = [[4300, 10000, 28000, 35000, 50000, 19000]]
v2 = [[5000, 14000, 28000, 31000, 42000, 21000]]
radar = Radar()
radar.config(schema)
radar.add("预算分配", v1, is_splitline=True, is_axisline_show=True)
radar.add("实际开销", v2, label_color=["#4e79a7"], is_area_show=False,
          legend_selectedmode='single')
radar.render()
```
![radar-demo](https://user-images.githubusercontent.com/19553554/35082333-20046172-fc54-11e7-944a-b6e25bf5dd2a.gif)

* is_area_show -> bool  
    是否显示填充区域
* area_opacity -> float  
    填充区域透明度
* area_color -> str  
    填充区域颜色
* is_splitline_show  -> bool  
    是否显示分割线，默认为 True
* is_axisline_show -> bool  
    是否显示坐标轴线，默认为 True

**Note：** 可配置 **lineStyle** 参数

```python
value_bj = [
    [55, 9, 56, 0.46, 18, 6, 1], [25, 11, 21, 0.65, 34, 9, 2],
    [56, 7, 63, 0.3, 14, 5, 3], [33, 7, 29, 0.33, 16, 6, 4],
    [42, 24, 44, 0.76, 40, 16, 5], [82, 58, 90, 1.77, 68, 33, 6],
    [74, 49, 77, 1.46, 48, 27, 7], [78, 55, 80, 1.29, 59, 29, 8],
    [267, 216, 280, 4.8, 108, 64, 9], [185, 127, 216, 2.52, 61, 27, 10],
    [39, 19, 38, 0.57, 31, 15, 11], [41, 11, 40, 0.43, 21, 7, 12],
    [64, 38, 74, 1.04, 46, 22, 13], [108, 79, 120, 1.7, 75, 41, 14],
    [108, 63, 116, 1.48, 44, 26, 15], [33, 6, 29, 0.34, 13, 5, 16],
    [94, 66, 110, 1.54, 62, 31, 17], [186, 142, 192, 3.88, 93, 79, 18],
    [57, 31, 54, 0.96, 32, 14, 19], [22, 8, 17, 0.48, 23, 10, 20],
    [39, 15, 36, 0.61, 29, 13, 21], [94, 69, 114, 2.08, 73, 39, 22],
    [99, 73, 110, 2.43, 76, 48, 23], [31, 12, 30, 0.5, 32, 16, 24],
    [42, 27, 43, 1, 53, 22, 25], [154, 117, 157, 3.05, 92, 58, 26],
    [234, 185, 230, 4.09, 123, 69, 27],[160, 120, 186, 2.77, 91, 50, 28],
    [134, 96, 165, 2.76, 83, 41, 29], [52, 24, 60, 1.03, 50, 21, 30],
]
value_sh = [
    [91, 45, 125, 0.82, 34, 23, 1], [65, 27, 78, 0.86, 45, 29, 2],
    [83, 60, 84, 1.09, 73, 27, 3], [109, 81, 121, 1.28, 68, 51, 4],
    [106, 77, 114, 1.07, 55, 51, 5], [109, 81, 121, 1.28, 68, 51, 6],
    [106, 77, 114, 1.07, 55, 51, 7], [89, 65, 78, 0.86, 51, 26, 8],
    [53, 33, 47, 0.64, 50, 17, 9], [80, 55, 80, 1.01, 75, 24, 10],
    [117, 81, 124, 1.03, 45, 24, 11], [99, 71, 142, 1.1, 62, 42, 12],
    [95, 69, 130, 1.28, 74, 50, 13], [116, 87, 131, 1.47, 84, 40, 14],
    [108, 80, 121, 1.3, 85, 37, 15], [134, 83, 167, 1.16, 57, 43, 16],
    [79, 43, 107, 1.05, 59, 37, 17], [71, 46, 89, 0.86, 64, 25, 18],
    [97, 71, 113, 1.17, 88, 31, 19], [84, 57, 91, 0.85, 55, 31, 20],
    [87, 63, 101, 0.9, 56, 41, 21], [104, 77, 119, 1.09, 73, 48, 22],
    [87, 62, 100, 1, 72, 28, 23], [168, 128, 172, 1.49, 97, 56, 24],
    [65, 45, 51, 0.74, 39, 17, 25], [39, 24, 38, 0.61, 47, 17, 26],
    [39, 24, 39, 0.59, 50, 19, 27], [93, 68, 96, 1.05, 79, 29, 28],
    [188, 143, 197, 1.66, 99, 51, 29], [174, 131, 174, 1.55, 108, 50, 30],
]
c_schema= [{"name": "AQI", "max": 300, "min": 5},
           {"name": "PM2.5", "max": 250, "min": 20},
           {"name": "PM10", "max": 300, "min": 5},
           {"name": "CO", "max": 5},
           {"name": "NO2", "max": 200},
           {"name": "SO2", "max": 100}]
radar = Radar()
radar.config(c_schema=c_schema, shape='circle')
radar.add("北京", value_bj, item_color="#f9713c", symbol=None)
radar.add("上海", value_sh, item_color="#b3e4a1", symbol=None,
          legend_selectedmode='single')
radar.render()
```
![radar-demo](https://user-images.githubusercontent.com/19553554/35082335-224c23ca-fc54-11e7-910a-0914699ac06e.gif)

**Note：** symblo=None 可隐藏标记图形（小圆圈）

**图例多例模式**
```python
radar = Radar()
radar.config(c_schema=c_schema, shape='circle')
radar.add("北京", value_bj, item_color="#f9713c", symbol=None)
radar.add("上海", value_sh, item_color="#b3e4a1", symbol=None)
radar.render()
```
![radar-demo](https://user-images.githubusercontent.com/19553554/35082343-269d9440-fc54-11e7-9675-4c125bbca75d.gif)


## Sankey（桑基图）
> 桑基图是一种特殊的流图, 它主要用来表示原材料、能量等如何从初始形式经过中间过程的加工、转化到达最终形式。

Sankey.add() 方法签名
```python
add(name, nodes, links,
    sankey_node_width=20,
    sankey_node_gap=8, **kwargs)
```
* name -> str  
     图例名称
* nodes -> list  
    桑基图结点，必须包含的数据项有：
    * name：数据项名称
    * value：数据项数值
* links -> list  
    桑基图结点关系
    * source：边的源节点名称（必须有！）
    * target：边的目标节点名称（必须有！）
    * value：边的数值，决定边的宽度。
 * sankey_node_width -> int  
    图中每个矩形节点的宽度。默认为 20
 * sankey_node_gap -> int  
    图中每一列任意两个矩形节点之间的间隔。默认为 8

**简单示例**
```python
from pyecharts import Sankey

nodes = [
    {'name': 'category1'}, {'name': 'category2'}, {'name': 'category3'},
    {'name': 'category4'}, {'name': 'category5'}, {'name': 'category6'},
]

links = [
    {'source': 'category1', 'target': 'category2', 'value': 10},
    {'source': 'category2', 'target': 'category3', 'value': 15},
    {'source': 'category3', 'target': 'category4', 'value': 20},
    {'source': 'category5', 'target': 'category6', 'value': 25}
]
sankey = Sankey("桑基图示例", width=1200, height=600)
sankey.add(
    "sankey",
    nodes,
    links,
    line_opacity=0.2,
    line_curve=0.5,
    line_color="source",
    is_label_show=True,
    label_pos="right",
)
sankey.render()
```
![sankey-demo](https://user-images.githubusercontent.com/19553554/35090344-5b701286-fc74-11e7-8c53-9a5d0e6797e5.png)

**使用官方提供的 json 数据**
```python
import os
import json

from pyecharts import Sankey

with codecs.open(os.path.join("fixtures", "energy.json"), "r", encoding="utf-8") as f:
    j = json.load(f)
sankey = Sankey("桑基图示例", width=1200, height=600)
sankey.add(
    "sankey",
    nodes=j["nodes"],
    links=j["links"],
    line_opacity=0.2,
    line_curve=0.5,
    line_color="source",
    is_label_show=True,
    label_pos="right",
)
sankey.render()
```
![sankey-demo](https://user-images.githubusercontent.com/19553554/35090346-5c79d1da-fc74-11e7-869b-7db7ecf42d9e.png)


## Scatter（散点图）
> 直角坐标系上的散点图可以用来展现数据的 x，y 之间的关系，如果数据项有多个维度，可以用颜色来表现，利用 geo 组件。

Scatter.add() 方法签名
```python
add(name, x_axis, y_axis,
    extra_data=None,
    symbol_size=10, **kwargs)
```
* name -> str  
    图例名称
* x_axis -> list  
    x 坐标轴数据
* y_axis -> list  
    y 坐标轴数据
* extra_data -> list[int]  
    第三维度数据，x 轴为第一个维度，y 轴为第二个维度。（可在 visualmap 中将视图元素映射到第三维度）
* extra_name -> list[str]  
    额外的数据项的名称，可以为每个数据点指定一个名称。
* symbol_size -> int  
    标记图形大小，默认为 10

```python
from pyecharts import Scatter

v1 = [10, 20, 30, 40, 50, 60]
v2 = [10, 20, 30, 40, 50, 60]
scatter = Scatter("散点图示例")
scatter.add("A", v1, v2)
scatter.add("B", v1[::-1], v2)
scatter.render()
```
![scatter-demo](https://user-images.githubusercontent.com/19553554/35090352-5f4bae42-fc74-11e7-9158-6fa70e5abf5d.png)

**利用 Visualmap 组件，通过颜色映射数值**
```python
scatter = Scatter("散点图示例")
scatter.add("A", v1, v2)
scatter.add("B", v1[::-1], v2, is_visualmap=True)
scatter.render()
```
![scatter-demo](https://user-images.githubusercontent.com/19553554/35090355-60bc82b0-fc74-11e7-8cc2-4f10c1c8193e.gif)

**利用 Visualmap 组件，通过图形点大小映射数值**
```python
scatter = Scatter("散点图示例")
scatter.add("A", v1, v2)
scatter.add(
    "B",
    v1[::-1],
    v2,
    is_visualmap=True,
    visual_type="size",
    visual_range_size=[20, 80],
)
scatter.render()
```
![scatter-demo](https://user-images.githubusercontent.com/19553554/35090360-62d94cfe-fc74-11e7-869f-ae3a3281f27b.gif)

**利用 Visualmap 组件映射到第三维度数据**
```python
data = [
        [28604, 77, 17096869],
        [31163, 77.4, 27662440],
        [1516, 68, 1154605773],
        [13670, 74.7, 10582082],
        [28599, 75, 4986705],
        [29476, 77.1, 56943299],
        [31476, 75.4, 78958237],
        [28666, 78.1, 254830],
        [1777, 57.7, 870601776],
        [29550, 79.1, 122249285],
        [2076, 67.9, 20194354],
        [12087, 72, 42972254],
        [24021, 75.4, 3397534],
        [43296, 76.8, 4240375],
        [10088, 70.8, 38195258],
        [19349, 69.6, 147568552],
        [10670, 67.3, 53994605],
        [26424, 75.7, 57110117],
        [37062, 75.4, 252847810]
    ]

x_lst = [v[0] for v in data]
y_lst = [v[1] for v in data]
extra_data = [v[2] for v in data]
sc = Scatter()
sc.add(
    "scatter",
    x_lst,
    y_lst,
    extra_data=extra_data,
    is_visualmap=True,
    visual_dimension=2,
    visual_orient="horizontal",
    visual_type="size",
    visual_range=[254830, 1154605773],
    visual_text_color="#000",
)
sc.render()
```
![scatter-demo](https://user-images.githubusercontent.com/19553554/35090364-63f2ef78-fc74-11e7-950b-75ebd13e1f03.gif)

**为每个坐标点指定一个名称，可用于 tooltip 展示**
```python

def custom_formatter(params):
    return params.value[3]

data = [
    [28604, 77, 17096],
    [31163, 77.4, 27662],
    [1516, 68, 11546],
]
x_lst = [v[0] for v in data]
y_lst = [v[1] for v in data]
extra_data = [v[2] for v in data]
extra_name = ["point A", "point B", "point C"]
sc = Scatter()
sc.add(
    "scatter",
    x_lst,
    y_lst,
    extra_data=extra_data,
    extra_name=extra_name,
    is_visualmap=True,
    visual_dimension=2,
    visual_orient="horizontal",
    visual_type="size",
    visual_range=[17000, 28000],
    visual_text_color="#000",
    tooltip_formatter=custom_formatter,
)
sc.render()
```
![scatter-demo](https://user-images.githubusercontent.com/19553554/43563684-e5e3cc34-9655-11e8-9792-0aa03a9233c6.gif)

**Note：** 请配合 通用配置项 中的 Visualmap 使用

**散点图默认的坐标轴都为数值轴，如果想实现横坐标为类目轴，可通过 `xaxis_type` 修改**
```python
scatter = Scatter("散点图示例")
scatter.add("A", ["a", "b", "c", "d", "e", "f"], v2)
scatter.add("B", ["a", "b", "c", "d", "e", "f"], v1[::-1], xaxis_type="category")
scatter.render()
```
![scatter-demo](https://user-images.githubusercontent.com/19553554/35090414-916add4e-fc74-11e7-83c1-d428387e8101.png)

**Scatter 还内置了画画方法**
```python
draw(path, color=None)
''' 
将图片上的像素点转换为数组，如 color 为（255,255,255）时只保留非白色像素点的坐标信息  
返回两个 k_lst, v_lst 两个列表刚好作为散点图的数据项
'''
```
* path -> str  
    转换图片的地址 
* color -> str  
    所要排除的颜色

首先你需要准备一张图片，如

![pyecharts-text](https://user-images.githubusercontent.com/19553554/35104421-c25a02f2-fca3-11e7-868d-d70bd86fdd76.png)

```python
from pyecharts import Scatter

scatter = Scatter("散点图示例")
v1, v2 = scatter.draw("../images/pyecharts-0.png")
scatter.add("pyecharts", v1, v2, is_random=True)
scatter.render()
```
![pyecharts-render](https://user-images.githubusercontent.com/19553554/35104426-c4ac81ce-fca3-11e7-9b46-7fd729ec3ece.png)


## Scatter3D（3D 散点图）
Scatter3D.add() 方法签名
```python
add(name, data,
    grid3d_opacity=1, **kwargs)
```
* name -> str  
    图例名称
* data -> [list], 包含列表的列表  
    数据项，数据中，每一行是一个『数据项』，每一列属于一个『维度』
* grid3d_opacity -> int  
    3D 笛卡尔坐标系组的透明度（点的透明度），默认为 1，完全不透明。

```python
from pyecharts import Scatter3D

import random
data = [
    [random.randint(0, 100),
    random.randint(0, 100),
    random.randint(0, 100)] for _ in range(80)
]
range_color = [
    '#313695', '#4575b4', '#74add1', '#abd9e9', '#e0f3f8', '#ffffbf',
    '#fee090', '#fdae61', '#f46d43', '#d73027', '#a50026']
scatter3D = Scatter3D("3D 散点图示例", width=1200, height=600)
scatter3D.add("", data, is_visualmap=True, visual_range_color=range_color)
scatter3D.render()
```
![scatter3d-demo](https://user-images.githubusercontent.com/19553554/35081974-1ece83ca-fc52-11e7-86d7-bec5c4d3e2c8.gif)

**Note：** 关于 gird3D 部分的设置，请参照通用配置项中的介绍 通用配置项  
**Note：** 可配合 axis3D 通用配置项 一起使用 


## Surface3D（3D 曲面图）
Surface3D.add() 方法签名
```python
add(name, data,
    grid3d_opacity=1, **kwargs)
```
* name -> str  
    图例名称
* data -> [list]/ndarray, 包含列表的列表  
    数据项，数据中，每一行是一个『数据项』，每一列属于一个『维度』
* grid3d_opacity -> int  
    3D 笛卡尔坐标系组的透明度（点的透明度），默认为 1，完全不透明。
    
```python
import math

from pyecharts import Surface3D


def create_surface3d_data():
    for t0 in range(-60, 60, 1):
        y = t0 / 60
        for t1 in range(-60, 60, 1):
            x = t1 / 60
            if math.fabs(x) < 0.1 and math.fabs(y) < 0.1:
                z = '-'
            else:
                z = math.sin(x * math.pi) * math.sin(y * math.pi)
            yield [x, y, z]

range_color = [
    "#313695",
    "#4575b4",
    "#74add1",
    "#abd9e9",
    "#e0f3f8",
    "#ffffbf",
    "#fee090",
    "#fdae61",
    "#f46d43",
    "#d73027",
    "#a50026",
]

_data = list(create_surface3d_data())
surface3d = Surface3D("3D 曲面图示例", width=1200, height=600)
surface3d.add(
    "",
    _data,
    is_visualmap=True,
    visual_range_color=range_color,
    visual_range=[-3, 3],
    grid3d_rotate_sensitivity=5,
)
surface3d.render()
```
![surface3d-demo](https://user-images.githubusercontent.com/19553554/44899702-0dba8680-ad35-11e8-95fd-4bc21e673b8b.gif)

**曲面波图**
```python
import math

from pyecharts import Surface3D


def create_surface3d_data():
    for t0 in range(-30, 30, 1):
        y = t0 / 10
        for t1 in range(-30, 30, 1):
            x = t1 / 10
            z = math.sin(x * x + y * y) * x / 3.14
            yield [x, y, z]

data = list(create_surface3d_data())
surface3D = Surface3D("3D 曲面图", width=1200, height=600)
surface3D.add(
    "",
    data,
    is_visualmap=True,
    visual_range=[-1, 1],
    visual_range_color=range_color,
)

surface3D.render()
```
![surface3d-demo](https://user-images.githubusercontent.com/19553554/44898394-60923f00-ad31-11e8-81a7-5d35214490cd.gif)

**Note：** 关于 gird3D 部分的设置，请参照通用配置项中的介绍 通用配置项  
**Note：** 可配合 axis3D 通用配置项 一起使用 


## ThemeRiver（主题河流图）
> 主题河流图是一种特殊的流图, 它主要用来表示事件或主题等在一段时间内的变化。

ThemeRiver.add() 方法签名
```python
add(name, data)
```
* name -> list  
    图例名称，必须为 list 类型，list 中每个值为数据项中的种类。
* data -> [list], 包含列表的列表  
    数据项，数据中，每一行是一个『数据项』，每一列属于一个『维度』。每个数据项至少需要三个维度，如 ['2015/11/08', 10, 'DQ']，分别为 [时间，数值，种类（图例名）]

```python
from pyecharts import ThemeRiver

data = [
    ['2015/11/08', 10, 'DQ'], ['2015/11/09', 15, 'DQ'], ['2015/11/10', 35, 'DQ'],
    ['2015/11/14', 7, 'DQ'], ['2015/11/15', 2, 'DQ'], ['2015/11/16', 17, 'DQ'],
    ['2015/11/17', 33, 'DQ'], ['2015/11/18', 40, 'DQ'], ['2015/11/19', 32, 'DQ'],
    ['2015/11/20', 26, 'DQ'], ['2015/11/21', 35, 'DQ'], ['2015/11/22', 40, 'DQ'],
    ['2015/11/23', 32, 'DQ'], ['2015/11/24', 26, 'DQ'], ['2015/11/25', 22, 'DQ'],
    ['2015/11/08', 35, 'TY'], ['2015/11/09', 36, 'TY'], ['2015/11/10', 37, 'TY'],
    ['2015/11/11', 22, 'TY'], ['2015/11/12', 24, 'TY'], ['2015/11/13', 26, 'TY'],
    ['2015/11/14', 34, 'TY'], ['2015/11/15', 21, 'TY'], ['2015/11/16', 18, 'TY'],
    ['2015/11/17', 45, 'TY'], ['2015/11/18', 32, 'TY'], ['2015/11/19', 35, 'TY'],
    ['2015/11/20', 30, 'TY'], ['2015/11/21', 28, 'TY'], ['2015/11/22', 27, 'TY'],
    ['2015/11/23', 26, 'TY'], ['2015/11/24', 15, 'TY'], ['2015/11/25', 30, 'TY'],
    ['2015/11/26', 35, 'TY'], ['2015/11/27', 42, 'TY'], ['2015/11/28', 42, 'TY'],
    ['2015/11/08', 21, 'SS'], ['2015/11/09', 25, 'SS'], ['2015/11/10', 27, 'SS'],
    ['2015/11/11', 23, 'SS'], ['2015/11/12', 24, 'SS'], ['2015/11/13', 21, 'SS'],
    ['2015/11/14', 35, 'SS'], ['2015/11/15', 39, 'SS'], ['2015/11/16', 40, 'SS'],
    ['2015/11/17', 36, 'SS'], ['2015/11/18', 33, 'SS'], ['2015/11/19', 43, 'SS'],
    ['2015/11/20', 40, 'SS'], ['2015/11/21', 34, 'SS'], ['2015/11/22', 28, 'SS'],
    ['2015/11/14', 7, 'QG'], ['2015/11/15', 2, 'QG'], ['2015/11/16', 17, 'QG'],
    ['2015/11/17', 33, 'QG'], ['2015/11/18', 40, 'QG'], ['2015/11/19', 32, 'QG'],
    ['2015/11/20', 26, 'QG'], ['2015/11/21', 35, 'QG'], ['2015/11/22', 40, 'QG'],
    ['2015/11/23', 32, 'QG'], ['2015/11/24', 26, 'QG'], ['2015/11/25', 22, 'QG'],
    ['2015/11/26', 16, 'QG'], ['2015/11/27', 22, 'QG'], ['2015/11/28', 10, 'QG'],
    ['2015/11/08', 10, 'SY'], ['2015/11/09', 15, 'SY'], ['2015/11/10', 35, 'SY'],
    ['2015/11/11', 38, 'SY'], ['2015/11/12', 22, 'SY'], ['2015/11/13', 16, 'SY'],
    ['2015/11/14', 7, 'SY'], ['2015/11/15', 2, 'SY'], ['2015/11/16', 17, 'SY'],
    ['2015/11/17', 33, 'SY'], ['2015/11/18', 40, 'SY'], ['2015/11/19', 32, 'SY'],
    ['2015/11/20', 26, 'SY'], ['2015/11/21', 35, 'SY'], ['2015/11/22', 4, 'SY'],
    ['2015/11/23', 32, 'SY'], ['2015/11/24', 26, 'SY'], ['2015/11/25', 22, 'SY'],
    ['2015/11/26', 16, 'SY'], ['2015/11/27', 22, 'SY'], ['2015/11/28', 10, 'SY'],
    ['2015/11/08', 10, 'DD'], ['2015/11/09', 15, 'DD'], ['2015/11/10', 35, 'DD'],
    ['2015/11/11', 38, 'DD'], ['2015/11/12', 22, 'DD'], ['2015/11/13', 16, 'DD'],
    ['2015/11/14', 7, 'DD'], ['2015/11/15', 2, 'DD'], ['2015/11/16', 17, 'DD'],
    ['2015/11/17', 33, 'DD'], ['2015/11/18', 4, 'DD'], ['2015/11/19', 32, 'DD'],
    ['2015/11/20', 26, 'DD'], ['2015/11/21', 35, 'DD'], ['2015/11/22', 40, 'DD'],
    ['2015/11/23', 32, 'DD'], ['2015/11/24', 26, 'DD'], ['2015/11/25', 22, 'DD']
]
tr = ThemeRiver("主题河流图示例图")
tr.add(['DQ', 'TY', 'SS', 'QG', 'SY', 'DD'], data, is_label_show=True)
tr.render()
```
![themeriver-demo](https://user-images.githubusercontent.com/19553554/35090642-3aaf6eba-fc75-11e7-8560-d36f1d225f6d.gif)

**Note：** 可以看到，每个数据项中的第三个数值就是该项的种类，而种类可以在 `add()` 第一个参数指定。


## Tree（树图）
> 树图主要用来可视化树形数据结构，是一种特殊的层次类型，具有唯一的根节点，左子树，和右子树。

Tree.add() 方法签名
```python
add(name, data,
    tree_layout="orthogonal",
    tree_symbol="emptyCircle",
    tree_symbol_size=7,
    tree_orient="LR",
    tree_top="12%",
    tree_left="12%",
    tree_bottom="12%",
    tree_right="12%",
    tree_collapse_interval=0,
    tree_label_position="left",
    tree_label_vertical_align="middle",
    tree_label_align="right",
    tree_label_text_size=12,
    tree_label_rotate=0,
    tree_leaves_position="right",
    tree_leaves_vertical_align="middle",
    tree_leaves_align="left",
    tree_leaves_text_size=12,
    tree_leaves_rotate=0,
    **kwargs
    )
```
* name -> str  
    系列名称，用于 tooltip 的显示，legend 的图例筛选。
* data -> list  
    树图的数据项是 **一棵树**，每个节点包括`value`（可选）, `name`, `children`（也是树，可选）如下所示
    ```
    [
        {
            value: 1212,    # 数值
            # 子节点
            children: [
                {
                    # 子节点数值
                    value: 2323,
                    # 子节点名
                    name: 'description of this node',
                    children: [...],
                },
                {
                    value: 4545,
                    name: 'description of this node',
                    children: [
                        {
                            value: 5656,
                            name: 'description of this node',
                            children: [...]
                        },
                        ...
                    ]
                }
            ]
        },
        ...
    ]
    ```
* tree_layout -> str  
    树图的布局，有 正交 和 径向 两种。这里的 正交布局 就是我们通常所说的水平 和 垂直 方向，对应的参数取值为 'orthogonal' 。而 径向布局 是指以根节点为圆心，每一层节点为环，一层层向外发散绘制而成的布局，对应的参数取值为 'radial' 。默认为 “orthogonal”。
* tree_symbol -> str  
    标记的图形。ECharts 提供的标记类型包括 'emptyCircle', 'circle', 'rect', 'roundRect', 'triangle', 'diamond', 'pin', 'arrow', 'none'。默认为 “emptyCircle”。
* tree_symbol_size -> int/list  
    标记的大小，可以设置成诸如 10 这样单一的数字，也可以用数组分开表示宽和高，例如 [20, 10] 表示标记宽为 20，高为 10。默认为 7。
* tree_orient -> str  
    树图中 正交布局 的方向，也就是说只有在 layout = 'orthogonal' 的时候，该配置项才生效。对应有 水平 方向的 从左到右，从右到左；以及垂直方向的从上到下，从下到上。取值分别为 'LR' , 'RL', 'TB', 'BT'。注意，之前的配置项值 'horizontal' 等同于 'LR'， 'vertical' 等同于 'TB'。默认为 “LR”
* tree_top -> str  
    tree 组件离容器顶部的距离。可以是像 20 这样的具体像素值，可以是像 '20%' 这样相对于容器高宽的百分比。默认为 “12%”
* tree_left -> str  
    tree 组件离容器左侧的距离。可以是像 20 这样的具体像素值，可以是像 '20%' 这样相对于容器高宽的百分比。默认为 “12%”
* tree_bottom -> str  
    tree 组件离容器底部的距离。可以是像 20 这样的具体像素值，可以是像 '20%' 这样相对于容器高宽的百分比。默认为 “12%”
* tree_right -> str  
    tree 组件离容器右侧的距离。可以是像 20 这样的具体像素值，可以是像 '20%' 这样相对于容器高宽的百分比。默认为 “12%”
* tree_collapse_interval -> int  
    折叠节点间隔，当节点过多时可以解决节点显示过杂间隔。默认为 0
* tree_label_position -> str/list  
    标签的位置。默认为 “left”
    ```
    * [x, y]
    通过相对的百分比或者绝对像素值表示标签相对于图形包围盒左上角的位置。 示例：
    // 绝对的像素值
    position: [10, 10],
    // 相对的百分比
    position: ['50%', '50%']
    * 'top'
    * 'left'
    * 'right'
    * 'bottom'
    * 'inside'
    * 'insideLeft'
    * 'insideRight'
    * 'insideTop'
    * 'insideBottom'
    * 'insideTopLeft'
    * 'insideBottomLeft'
    * 'insideTopRight'
    * 'insideBottomRight'
    ```
* tree_label_vertical_align -> str  
    父节点文字垂直对齐方式，默认自动。可选：'top'，'middle'，'bottom'
* tree_label_align -> str  
    父节点文字水平对齐方式，默认自动。可选：'left'，'center'，'right'
* tree_label_text_size -> int  
    父节点文字的字体大小
* tree_label_rotate -> int  
    父节点标签旋转。从 -90 度到 90 度。正值是逆时针。默认为 0
* tree_leaves_position -> str  
    距离图形元素的距离。当 position 为字符描述值（如 'top'、'insideRight'）时候有效。参加 tree_label_position
* tree_leaves_vertical_align -> str  
    叶节点文字垂直对齐方式，默认自动。可选：'top'，'middle'，'bottom'
* tree_leaves_align -> str  
    叶节点文字水平对齐方式，默认自动。可选：'left'，'center'，'right'
* tree_leaves_text_size -> int  
    叶节点文字的字体大小
* tree_leaves_rotate -> int  
    叶节点标签旋转。从 -90 度到 90 度。正值是逆时针。默认为 0

**简单示例**

首先假设你有一份数据需要生产树图，大概长这样
```

     |----B     |----E----|----I
     |          |
     |----C-----|----F         |----J
A----|                         |
     |----D-----|----G----|----|----K
                |
                |----H
```
你需要来编写成 JSON 数据，节点都是以 {name, children} 为基础的递归嵌套模式，如下
```json
data = [
    {
        "children": [
            {
                "children": [],
                "name": "B"
            },
            {
                "children": [
                    {
                        "children": [
                            {
                                "children": [],
                                "name": "I"
                            }
                        ],
                        "name": "E"
                    },
                    {
                        "children": [],
                        "name": "F"
                    }
                ],
                "name": "C"
            },
            {
                "children": [
                    {
                        "children": [
                            {
                                "children": [],
                                "name": "J"
                            },
                            {
                                "children": [],
                                "name": "K"
                            }
                        ],
                        "name": "G"
                    },
                    {
                        "children": [],
                        "name": "H"
                    }
                ],
                "name": "D"
            }
        ],
        "name": "A"
    }
]
```
生成树图
```python
from pyecharts import Tree

tree = Tree("树图示例")
tree.add("", data)
tree.render()
```
![tree-demo](https://user-images.githubusercontent.com/19553554/44004354-fc603b0a-9e93-11e8-9437-778a1e4a3001.png)

**使用 tree_collapse_interva 控制折叠节点间隔**

当节点过多时可以解决节点显示过杂间隔。以官方提供的 flare.json 数据为例，tree_collapse_interval 为 0 时（表示全部节点均不折叠），文字都挤在一起了
```python
import os
import json
import codecs

from pyecharts import Tree

with codecs.open(
    os.path.join("fixtures", "flare.json"), "r", encoding="utf-8"
) as f:
    j = json.load(f)
tree = Tree(width=1200, height=800)
tree.add("", data)
tree.render()
```
![tree-demo](https://user-images.githubusercontent.com/19553554/44004551-a41321f8-9e96-11e8-9837-ddf930394240.png)

设置 tree_collapse_interval 为 2（表示间隔折叠节点），图明显就好看多了
```python
import os
import json
import codecs

from pyecharts import Tree

with codecs.open(
    os.path.join("fixtures", "flare.json"), "r", encoding="utf-8"
) as f:
    j = json.load(f)
data = [j]

tree = Tree(width=1200, height=800)
tree.add("", data, tree_collapse_interval=2)
tree.render()
```
![tree-demo](https://user-images.githubusercontent.com/19553554/44004598-5636d74e-9e97-11e8-8a5c-92de6278880d.gif)

**指定方向，从右到左**
```python
tree = Tree(width=1200, height=800)
tree.add("", data, tree_orient="RL", tree_collapse_interval=2)
tree.render()
```
![tree-demo](https://user-images.githubusercontent.com/19553554/44004607-8cd0ff3c-9e97-11e8-97b1-c4bd343ce49c.png)

**指定方向，从上到下**
```python
tree = Tree(width=1200, height=800)
tree.add(
    "",
    data,
    tree_collapse_interval=2,
    tree_orient="TB",
    tree_label_rotate=-90,
    tree_leaves_rotate=-90
)
tree.render
```
![tree-demo](https://user-images.githubusercontent.com/19553554/44004803-5537bada-9e9b-11e8-83f1-4c8b4df81d1e.png)

**指定布局** 
```python
tree = Tree(width=1200, height=800)
tree.add("", data, tree_collapse_interval=2, tree_layout="radial")
tree.render()
```
![tree-demo](https://user-images.githubusercontent.com/19553554/44004643-15e284ee-9e98-11e8-93f6-8103c3af42f4.png)

**调整容器布局**
```python
tree = Tree(width=1200, height=800)
tree.add("", data, tree_collapse_interval=2, tree_top="15%", tree_right="20%")
tree.render()
```
![tree-demo](https://user-images.githubusercontent.com/19553554/44004651-399e4ab2-9e98-11e8-93b5-8ab6e9926408.png)


## TreeMap（矩形树图）
> 矩形树图是一种常见的表达『层级数据』『树状数据』的可视化形式。它主要用面积的方式，便于突出展现出『树』的各层级中重要的节点。

TreeMap.add() 方法签名
```python
add(name, data,
    treemap_left_depth=None,
    treemap_drilldown_icon="▶",
    treemap_visible_min=10)
```
* name -> str  
    图例名称
* data -> list  
    矩形树图的数据项是 **一棵树**，每个节点包括`value`, `name`（可选）, `children`（也是树，可选）如下所示
    ```
    [
        {
            value: 1212,    # 数值
            # 子节点
            children: [
                {
                    # 子节点数值
                    value: 2323,
                    # 子节点名
                    name: 'description of this node',
                    children: [...],
                },
                {
                    value: 4545,
                    name: 'description of this node',
                    children: [
                        {
                            value: 5656,
                            name: 'description of this node',
                            children: [...]
                        },
                        ...
                    ]
                }
            ]
        },
        ...
    ]
    ```
* treemap_left_depth -> int  
    leafDepth 表示『展示几层』，层次更深的节点则被隐藏起来。设置了 leafDepth 后，下钻（drill down）功能开启。drill down 功能即点击后才展示子层级。例如，leafDepth 设置为 1，表示展示一层节点。
* treemap_drilldown_icon -> str  
    当节点可以下钻时的提示符。只能是字符。默认为 '▶'
* treemap_visible_min -> int  
    如果某个节点的矩形的面积，小于这个数值（单位：px平方），这个节点就不显示。

```python
from pyecharts import TreeMap

data = [
    {
        "value": 40,
        "name": "我是A",
    },
    {
        "value": 180,
        "name": "我是B",
        "children": [
            {
                "value": 76,
                "name": "我是B.children",
                "children": [
                    {
                        "value": 12,
                        "name": "我是B.children.a",
                    },
                    {
                        "value": 28,
                        "name": "我是B.children.b",
                    },
                    {
                        "value": 20,
                        "name": "我是B.children.c",
                    },
                    {
                        "value": 16,
                        "name": "我是B.children.d",
                    }]
            }]}
]

treemap = TreeMap("矩形树图-默认示例", width=1200, height=600)
treemap.add("演示数据", data, is_label_show=True, label_pos='inside')
treemap.render()
```
![treemap-demo](https://user-images.githubusercontent.com/19553554/35082247-b6f5ff88-fc53-11e7-84ca-bcb1f621ec68.png)

```python
treemap = TreeMap("矩形树图-下钻示例", width=1200, height=600)
treemap.add("演示数据", data, is_label_show=True, label_pos='inside',
            treemap_left_depth=1)
treemap.render()
```
![treemap-demo](https://user-images.githubusercontent.com/19553554/35082249-b862ecf0-fc53-11e7-85eb-8021de696a66.gif)

```python
from pyecharts import TreeMap

treemap = TreeMap("矩形树图示例", width=1200, height=600)
import os
import json
with open(os.path.join("..", "json", "treemap.json"), "r", encoding="utf-8") as f:
        data = json.load(f)
treemap.add("演示数据", data, is_label_show=True, label_pos='inside')
treemap.render()
```
![treemap-demo](https://user-images.githubusercontent.com/19553554/35082251-b9e23982-fc53-11e7-8341-e7da1842389f.gif)


## WordCloud（词云图）
WordCloud.add() 方法签名
```python
add(name, attr, value,
    shape="circle",
    word_gap=20,
    word_size_range=None,
    rotate_step=45)
```
* name -> str  
    图例名称
* attr -> list  
    属性名称
* value -> list  
    属性所对应的值
* shape -> list  
    词云图轮廓，有'circle', 'cardioid', 'diamond', 'triangle-forward', 'triangle', 'pentagon', 'star'可选
* word_gap -> int  
    单词间隔，默认为 20。
* word_size_range -> list  
    单词字体大小范围，默认为 [12, 60]。
* rotate_step -> int  
    旋转单词角度，默认为 45

```python
from pyecharts import WordCloud

name = [
    'Sam S Club', 'Macys', 'Amy Schumer', 'Jurassic World', 'Charter Communications',
    'Chick Fil A', 'Planet Fitness', 'Pitch Perfect', 'Express', 'Home', 'Johnny Depp',
    'Lena Dunham', 'Lewis Hamilton', 'KXAN', 'Mary Ellen Mark', 'Farrah Abraham',
    'Rita Ora', 'Serena Williams', 'NCAA baseball tournament', 'Point Break']
value = [
    10000, 6181, 4386, 4055, 2467, 2244, 1898, 1484, 1112,
    965, 847, 582, 555, 550, 462, 366, 360, 282, 273, 265]
wordcloud = WordCloud(width=1300, height=620)
wordcloud.add("", name, value, word_size_range=[20, 100])
wordcloud.render()
```
![wordcloud-demo](https://user-images.githubusercontent.com/19553554/35081546-cfe57770-fc4f-11e7-878a-e76d274afcbd.png)

```python
wordcloud = WordCloud(width=1300, height=620)
wordcloud.add("", name, value, word_size_range=[30, 100],
              shape='diamond')
wordcloud.render()
```
![wordcloud-demo](https://user-images.githubusercontent.com/19553554/35081549-d2bde37e-fc4f-11e7-98b2-4cdc019433b1.png)

**Note：** 当且仅当 shape 为默认的'circle'时 rotate_step 参数才生效

**如果你已阅读完本篇文档，可以进一步阅读 [自定义图表篇](zh-cn/charts-custom)**
