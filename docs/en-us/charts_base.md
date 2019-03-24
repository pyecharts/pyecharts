> Chart Basic: This document is a pyecharts basic chart details document that introduces the details of the basic charts for pyecharts.

**For detailed configuration of the chart, please refer to [Chart Configuration](en-us/charts_configure)**  

* Basic chart class
    * Bar
    * Bar3D
    * Boxplot
    * EffectScatter
    * Funnel
    * Gauge
    * Geo
    * GeoLines
    * Graph
    * HeatMap
    * Kline (Candlestick)
    * Line
    * Line3D
    * Liquid
    * Map
    * Parallel
    * Pie
    * Polar
    * Radar
    * Sankey
    * Scatter
    * Scatter3D
    * Surface3D
    * ThemeRiver
    * Tree
    * TreeMap
    * WordCloud


## Bar
> Bar chart shows different data through the height of a bar, which is used in rectangular coordinate with at least 1 category axis.

Bar.add() signatures
```python
add(name, x_axis, y_axis,
    is_stack=False,
    bar_category_gap='20%', **kwargs)
```
* name -> str  
    name of chart

* x_axis -> list  
    data of xAixs

* y_axis -> list  
    data of yAxis

* is_stack -> bool  
    defalut -> False   
    Data stacking, the stack values ​​of the same series configuration on the same category axis can be stacked

* bar_category_gap -> int/str  
    default -> '20%'  
    The columnar distance of the category axis. When set to 0, the columns are next to each other(histogram type), 

**is_stack implements data stacking**
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

**Tip：**  Global configuration item needs set in the last ```add()``` or the setting will lose efficacy.

```python
from pyecharts import Bar

bar = Bar("标记线和标记点示例")
bar.add("商家A", attr, v1, mark_point=["average"])
bar.add("商家B", attr, v2, mark_line=["min", "max"])
bar.render()
```
![bar-1](https://user-images.githubusercontent.com/19553554/35081600-0ea23f0c-fc50-11e7-894b-65ad0f611a01.gif)

**is_convert exchange XY axis**
```python
from pyecharts import Bar

bar = Bar("x 轴和 y 轴交换")
bar.add("商家A", attr, v1)
bar.add("商家B", attr, v2, is_convert=True)
bar.render()
```
![bar-demo](https://user-images.githubusercontent.com/19553554/35081605-151472ce-fc50-11e7-8627-66929309b08c.png)

**dataZoom effect, 'slider' type**
```python
import random

attr = ["{}天".format(i) for i in range(30)]
v1 = [random.randint(1, 30) for _ in range(30)]
bar = Bar("Bar - datazoom - slider 示例")
bar.add("", attr, v1, is_label_show=True, is_datazoom_show=True)
bar.render()
```
![bar-demo](https://user-images.githubusercontent.com/19553554/35081742-ddcbf3e0-fc50-11e7-937e-f806fd12c83e.gif)

**dataZoom effect, 'inside' type**
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

**dataZoom effect，'both' type**
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

**Multiple dataZoom effect，support X and Y axis at the same time**
```python
days = ["{}天".format(i) for i in range(30)]
days_v1 = [random.randint(1, 30) for _ in range(30)]
bar = Bar("Bar - datazoom - xaxis/yaxis 示例")
bar.add(
    "",
    days,
    days_v1,
    # default is X axis，horizontal
    is_datazoom_show=True,
    datazoom_type="slider",
    datazoom_range=[10, 25],
    # add extra dataZoom control bar，vertical
    is_datazoom_extra_show=True,
    datazoom_extra_type="slider",
    datazoom_extra_range=[10, 25],
    is_toolbox_show=False,
)
bar.render()
```
![bar-demo](https://user-images.githubusercontent.com/19553554/43352052-ec70fe82-924f-11e8-880b-832b8f95d701.gif)

**Note：** datazoom could be applied for all 2D Cartesian coordinates, ie(Line、Bar、Scatter、EffectScatter、Kline)  


**When the x-axis or y-axis labels are too dense to cause all the displays to overlap, the method of rotating the labels can be used**
```python
attr = ["{}天".format(i) for i in range(20)]
v1 = [random.randint(1, 20) for _ in range(20)]
bar = Bar("坐标轴标签旋转示例")
bar.add("", attr, v1, xaxis_interval=0, xaxis_rotate=30, yaxis_rotate=30)
bar.render()
```
![bar-demo](https://user-images.githubusercontent.com/19553554/35081805-3258a2be-fc51-11e7-9cb1-d99c1a707bc5.png)

**Note：** The maximum and minimum values ​​on the x and y axes can be adjusted by setting `xaxis_min` / `xaxis_max` / `yaxis_min` / `yaxis_max`. Effective for the value axis!  

**Note：** Through label_color to set column's color, like ['#eee', '#000'], any type of chart's legend color can revise by label_color.  

**Waterfall example**

```python
from pyecharts import Bar

attr = ["{}月".format(i) for i in range(1, 8)]
v1 = [0, 100, 200, 300, 400, 220, 250]
v2 = [1000, 800, 600, 500, 450, 400, 300]
bar = Bar("瀑布图示例")
# the first add() legend to be transparent, ie 'rgba(0,0,0,0)', and set the is_stack flag is True
bar.add("", attr, v1, label_color=['rgba(0,0,0,0)'], is_stack=True)
bar.add("月份", attr, v2, is_label_show=True, is_stack=True, label_pos='inside')
bar.render()
```
![bar-demo](https://user-images.githubusercontent.com/19553554/35081807-34a5568e-fc51-11e7-8199-3c3f8f43ba98.png)

**Fat histogram example**
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

**Double histograms**
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

**Extra text label**
```python
from pyecharts import Bar

bar = Bar("柱状图", extra_html_text_label=["bar_extra_html_text_label", "color:red"])
bar.add("商家A", CLOTHES, clothes_v1, is_stack=True)
bar.add("商家B", CLOTHES, clothes_v2, is_stack=True)
bar.render()
```
![bar-demo](https://user-images.githubusercontent.com/19553554/43812932-31f22e0a-9af6-11e8-8fbe-c62b65daec41.png)

**Control X/Y axis line color and width**
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

**Two or more adds are made, one of the data is missing and can be filled with 0**
```python
bar = Bar("折线图示例")
bar.add("商家A", CLOTHES, clothes_v1)
bar.add("商家B", CLOTHES, [55, 60, 16, 20, 0, 0])
bar.render()
```
![bar-demo](https://user-images.githubusercontent.com/19553554/44008022-e3708900-9ed0-11e8-94c5-68c8d96ebe60.png)

## Bar3D
Bar3D.add() signatures
```python
add(name, x_axis, y_axis, data, grid3D_opacity=1, grid3D_shading='color', **kwargs)
```
* name -> str  
    chart name

* x_axis -> str    
    xAxis data, need to be a category axis, in another word, it cannot be a numeric value

* y_axis -> str  
    yAxis data, need to be a category axis, in another word, it cannot be a numeric value

* data -> [[], []]
    zAxis data, it is represented by a two-dimension array.

* grid3D_opacity -> float  
    default -> 1  
    opacity of gird3D item bar

* grid3D_shading -> str  
    3D graphics coloring effect  
    * 'color': Only show color, not affected by lighting and other factors.
    * 'lambert': Through the classic lambert coloring to show the light and shade.
    * 'realistic': Realistic rendering. With `light.ambientCubemap` and `postEffect` to improve the quality of the display.  
    ECharts GL uses physics-based rendering (PBR) to represent realistic materials

```python
from pyecharts import Bar3D

bar3d = Bar3D("3D 柱状图示例", width=1200, height=600)
x_axis = ["12a", "1a", "2a", "3a", "4a", "5a", "6a", "7a", "8a", "9a", "10a", "11a",
          "12p", "1p", "2p", "3p", "4p", "5p", "6p", "7p", "8p", "9p", "10p", "11p"]
y_axis = ["Saturday", "Friday", "Thursday", "Wednesday", "Tuesday", "Monday", "Sunday"]
data = [[0, 0, 5], [0, 1, 1], [0, 2, 0], [0, 3, 0], [0, 4, 0], [0, 5, 0], [0, 6, 0], [0, 7, 0],
        [0, 8, 0],[0, 9, 0], [0, 10, 0], [0, 11, 2], [0, 12, 4], [0, 13, 1], [0, 14, 1], [0, 15, 3],
        [0, 16, 4], [0, 17, 6], [0, 18, 4], [0, 19, 4], [0, 20, 3], [0, 21, 3], [0, 22, 2], [0, 23, 5],
        [1, 0, 7], [1, 1, 0], [1, 2, 0], [1, 3, 0], [1, 4, 0], [1, 5, 0], [1, 6, 0], [1, 7, 0], [1, 8, 0],
        [1, 9, 0], [1, 10, 5], [1, 11, 2], [1, 12, 2], [1, 13, 6], [1, 14, 9], [1, 15, 11], [1, 16, 6], [1, 17, 7],
        [1, 18, 8], [1, 19, 12], [1, 20, 5], [1, 21, 5], [1, 22, 7], [1, 23, 2], [2, 0, 1], [2, 1, 1],
        [2, 2, 0], [2, 3, 0], [2, 4, 0], [2, 5, 0], [2, 6, 0], [2, 7, 0], [2, 8, 0], [2, 9, 0], [2, 10, 3],
        [2, 11, 2], [2, 12, 1], [2, 13, 9], [2, 14, 8], [2, 15, 10], [2, 16, 6], [2, 17, 5], [2, 18, 5],
        [2, 19, 5], [2, 20, 7], [2, 21, 4], [2, 22, 2], [2, 23, 4], [3, 0, 7], [3, 1, 3], [3, 2, 0], [3, 3, 0],
        [3, 4, 0], [3, 5, 0], [3, 6, 0], [3, 7, 0], [3, 8, 1], [3, 9, 0], [3, 10, 5], [3, 11, 4], [3, 12, 7],
        [3, 13, 14], [3, 14, 13], [3, 15, 12], [3, 16, 9], [3, 17, 5], [3, 18, 5], [3, 19, 10], [3, 20, 6],
        [3, 21, 4], [3, 22, 4], [3, 23, 1], [4, 0, 1], [4, 1, 3], [4, 2, 0], [4, 3, 0], [4, 4, 0], [4, 5, 1],
        [4, 6, 0], [4, 7, 0], [4, 8, 0], [4, 9, 2], [4, 10, 4], [4, 11, 4], [4, 12, 2], [4, 13, 4], [4, 14, 4],
        [4, 15, 14], [4, 16, 12], [4, 17, 1], [4, 18, 8], [4, 19, 5], [4, 20, 3], [4, 21, 7], [4, 22, 3],
        [4, 23, 0], [5, 0, 2], [5, 1, 1], [5, 2, 0], [5, 3, 3], [5, 4, 0], [5, 5, 0], [5, 6, 0], [5, 7, 0],
        [5, 8, 2], [5, 9, 0], [5, 10, 4], [5, 11, 1], [5, 12, 5], [5, 13, 10], [5, 14, 5], [5, 15, 7], [5, 16, 11],
        [5, 17, 6], [5, 18, 0], [5, 19, 5], [5, 20, 3], [5, 21, 4], [5, 22, 2], [5, 23, 0], [6, 0, 1], [6, 1, 0],
        [6, 2, 0], [6, 3, 0], [6, 4, 0], [6, 5, 0], [6, 6, 0], [6, 7, 0], [6, 8, 0], [6, 9, 0], [6, 10, 1],
        [6, 11, 0], [6, 12, 2], [6, 13, 1], [6, 14, 3], [6, 15, 4], [6, 16, 0], [6, 17, 0], [6, 18, 0], [6, 19, 0],
        [6, 20, 1], [6, 21, 2], [6, 22, 2], [6, 23, 6]]
range_color = ['#313695', '#4575b4', '#74add1', '#abd9e9', '#e0f3f8', '#ffffbf',
               '#fee090', '#fdae61', '#f46d43', '#d73027', '#a50026']
bar3d.add("", x_axis, y_axis, [[d[1], d[0], d[2]] for d in data], 
    is_visualmap=True, visual_range=[0, 20], visual_range_color=range_color, 
    grid3D_width=200, grid3D_depth=80)
bar3d.render()
```
![bar3d-demo](https://user-images.githubusercontent.com/19553554/35081629-36a8e046-fc50-11e7-8910-e02bf24008d9.gif)

In data, such as [1, 2, 3], the index of the x-axis is 1 ("1a"); the index of the y-axis is 2 ("Thursday"); the value of the z-axis is 3.

**Set `grid3D_shading` could make bar look more real**  
```python
bar3d = Bar3D("3D 柱状图示例", width=1200, height=600)
bar3d.add("", x_axis, y_axis, [[d[1], d[0], d[2]] for d in data], is_visualmap=True,
          visual_range=[0, 20], visual_range_color=range_color, grid3D_width=200, grid3D_depth=80,
          grid3D_shading='lambert')
bar3d.show_config()
bar3d.render()
```

![bar3d-demo](https://user-images.githubusercontent.com/19553554/35081631-38a0cb02-fc50-11e7-9f74-3d487bd98a3a.gif)

**Set```is_grid3D_rotate``` could let it rotate automatically**
```python
bar3d = Bar3D("3D 柱状图示例", width=1200, height=600)
bar3d.add("", x_axis, y_axis, [[d[1], d[0], d[2]] for d in data], is_visualmap=True,
          visual_range=[0, 20], visual_range_color=range_color, grid3D_width=200, grid3D_depth=80,
          is_grid3D_rotate=True)
bar3d.show_config()
bar3d.render()
```
![bar3d-demo](https://user-images.githubusercontent.com/19553554/35081703-a70b544a-fc50-11e7-838a-53445cd8d203.gif)

set ``` grid3D_rotate_speed``` to adjust the rotation speed  
```python
bar3d = Bar3D("3D 柱状图示例", width=1200, height=600)
bar3d.add("", x_axis, y_axis, [[d[1], d[0], d[2]] for d in data], is_visualmap=True,
          visual_range=[0, 20], visual_range_color=range_color, grid3D_width=200, grid3D_depth=80,
          is_grid3D_rotate=True, grid3D_rotate_speed=180)
bar3d.render()
```
![bar3d-demo](https://user-images.githubusercontent.com/19553554/35081705-a92a878c-fc50-11e7-8427-9066456db54c.gif)

**Note：** more details about gird3D，please refer to **Chart Configuration**
**Note：** Can be used with axis3D configuration

## Boxplot
> Boxplot is a chart used to display a set of dispersion data. It can display the maximum, minimum, median, lower quartile and upper quartile.

Boxplot.add() signatures
```python
add(name, x_axis, y_axis, **kwargs)
```
* name -> str    
    Chart name

* x_axis -> list    
    x axis data

* y_axis -> list
    y axis data, each row data of the two-dimensional array (each row in the following example) is rendering a box containing five magnitudes, in order:  
    [[min,  Q1,  median (or Q2),  Q3,  max], ...]

You can calculate the required five values by ​​yourself. Or you can convert them by the built-in `prepare_data()`, which converts the input list data into [[min, Q1, median (or Q2), Q3, max], ...], as shown below:
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
_yaxis = boxplot.prepare_data(y_axis)       # transform data
boxplot.add("boxplot", x_axis, _yaxis)
boxplot.render()
```
![boxplot-demo](https://user-images.githubusercontent.com/19553554/35082364-4f4e98f8-fc54-11e7-9e53-1d6a66b67e46.png)

**Or convert directly in add()**
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


## EffectScatter
> The scatter graph with ripple animation. The special animation effect can visually highlights some data.

EffectScatter.add() signatures
```python
add(name, x_value, y_value, symbol_size=10, **kwargs)
```
* name -> str  
    Series name used for displaying in tooltip and filtering with legend,or updaing data and configuration with setOption.

* x_axis -> list  
    data of xAxis

* y_axis -> list  
    data of yAxis  

* symbol_size -> int   
    default -> 10  
    symbol size

```python
from pyecharts import EffectScatter

v1 = [10, 20, 30, 40, 50, 60]
v2 = [25, 20, 15, 10, 60, 33]
es = EffectScatter("动态散点图示例")
es.add("effectScatter", v1, v2)
es.render()
```
![effectscatter-0](https://user-images.githubusercontent.com/19553554/35090528-e4c9a04c-fc74-11e7-938a-d348bb1fdbf8.gif)

**Effect scatter charts of various symbols**
```python
es = EffectScatter("动态散点图各种图形示例")
es.add("", [10], [10], symbol_size=20, effect_scale=3.5, effect_period=3, symbol="pin")
es.add("", [20], [20], symbol_size=12, effect_scale=4.5, effect_period=4,symbol="rect")
es.add("", [30], [30], symbol_size=30, effect_scale=5.5, effect_period=5,symbol="roundRect")
es.add("", [40], [40], symbol_size=10, effect_scale=6.5, effect_brushtype='fill',symbol="diamond")
es.add("", [50], [50], symbol_size=16, effect_scale=5.5, effect_period=3,symbol="arrow")
es.add("", [60], [60], symbol_size=6, effect_scale=2.5, effect_period=3,symbol="triangle")
es.render()
```
![effectscatter-1](https://user-images.githubusercontent.com/19553554/35090533-e7330076-fc74-11e7-9ba0-7cc4ff80e030.gif)


* symbol -> str  
    symbol shape, it can be 'rect', 'roundRect', 'triangle', 'diamond', 'pin', 'arrow'

* effect_brushtype -> str   
    default -> 'stroke'  
    The brush type for ripples. options: 'stroke' and 'fill'.

* effect_scale -> float  
    default -> 2.5  
    The maximum zooming scale of ripples in animation.

* effect_period -> float  
    default -> 4(s)  
    The duration of animation.


## Funnel
Funnel.add() signatures
```python
add(name, attr, value,
    funnel_sort="ascending", funnel_gap=0, **kwargs)
```
* name -> str  
    Series name used for displaying in tooltip and filtering with legend,or updaing data and configuration with setOption.

* attr -> list  
    name of attribute

* value -> list  
    value of attribute

* funnel_sort -> str/func
    Sort the data, you can take 'ascending', 'descending', 'none' (in origin order of the data, not sorted).

* funnel_gap- > int
    Data pattern spacing. Default is 0.

**The label is displayed inside**  
```python
from pyecharts import Funnel

attr = ["衬衫", "羊毛衫", "雪纺衫", "裤子", "高跟鞋", "袜子"]
value = [20, 40, 60, 80, 100, 120]
funnel = Funnel("漏斗图示例")
funnel.add("商品", attr, value, is_label_show=True, label_pos="inside", label_text_color="#fff")
funnel.render()
```
![funnel-demo](https://user-images.githubusercontent.com/19553554/35090181-d6b0e886-fc73-11e7-8e00-dec8ac38c415.gif)

**The label is displayed outside**  
```python
funnel = Funnel("漏斗图示例", width=600, height=400, title_pos='center')
funnel.add("商品", attr, value, is_label_show=True, label_pos="outside", legend_orient='vertical',
           legend_pos='left')
funnel.show_config()
funnel.render()
```
![funnel-demo](https://user-images.githubusercontent.com/19553554/35090186-d8f50db6-fc73-11e7-9b7e-947580a621de.png)

**Ascending data**
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

**No sorted data**
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

**Specify graphics interval**
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


## Gauge
Gauge.add() signatures
```python
add(name, attr, value, scale_range=None, angle_range=None, **kwargs)
```
* name -> str  
    Series name used for displaying in tooltip and filtering with legend,or updaing data and configuration with setOption.

* attr -> list  
    name of attribute

* value -> list  
    value of attribute

* scale_range -> list  
    default -> [0, 100]  
    data range of guage

* angle_range -> list  
    default -> [225, -45]  
    angle range of guage.The direct right side of circle center is 0 degree,the right above it is 90 degree, the direct left side of it is 180 degree.

```python
from pyecharts import Gauge

gauge = Gauge("仪表盘示例")
gauge.add("业务指标", "完成率", 66.66)
gauge.render()
```
![gauge-demo](https://user-images.githubusercontent.com/19553554/35090190-daa33eee-fc73-11e7-9710-7844b12d3e6b.png)

```python
gauge = Gauge("仪表盘示例")
gauge.add("业务指标", "完成率", 166.66, angle_range=[180, 0], scale_range=[0, 200], is_legend_show=False)
gauge.render()
```
![gauge-demo](https://user-images.githubusercontent.com/19553554/35090193-dc199d22-fc73-11e7-8f4d-22477a3a22be.png)


## Geo
> Geographic coordinate system component. Geographic coordinate system component is used to draw maps, which also supports scatter series, and line series.

Geo.add() signatures
```python
add(name, attr, value, 
    type="scatter", 
    maptype='china', 
    symbol_size=12, b
    order_color="#111",
    geo_normal_color="#323c48", 
    geo_emphasis_color="#2a333d", 
    geo_cities_coords=None, 
    is_roam=True, **kwargs)
```
* name -> str  
    Series name used for displaying in tooltip and filtering with legend,or updaing data and configuration with setOption.

* attr -> list  
    Name of attribute

* value -> list  
    Value of attribute

* type -> str  
    default -> 'scatter'  
    Chart type, it can be 'scatter', 'effectscatter', 'heatmap'

* maptype -> str  
    Type of map. Since v0.3.2+, the map has become an extension package, supporting maps of provinces, cities, national districts, and countries around the world. For details, please refer to [Map Customization](en-us/customize_map)

* coordinate_region -> str   
    Which the city coordinates belong to the country. Introduced from v0.5.7, looking for the location of international cities. The default is `China`. The detail country mapping table refers to [countries_regions_db.json](https://github.com/pyecharts/pyecharts/blob/master/pyecharts/datasets/countries_regions_db.json). More geographic coordinates information can be referred to [Geography & Map](/en-us/datasets)

* symbol_size -> int  
    default -> 12  
    symbol size

* border_color -> str  
    default -> '#111'  
    color of map border

* geo_normal_color -> str  
    default -> '#323c48'  
    The color of the map area in normal state

* geo_emphasis_color -> str  
    default -> '#2a333d'  
    The color of the map area in emphasis state

* geo_cities_coords -> dict  
    User-defined regional latitude and longitude, similar to the dictionary such as {'Acheng': [126.58, 45.32],}.

* is_roam -> bool  
    Whether to enable mouse zoom and pan roaming. Default is True
    If you only want to turn on zoom or pan, you can set it to 'scale' or 'move'. Set to True to turn on

**Scatter type (Continuous)**
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

geo = Geo("全国主要城市空气质量", "data from pm2.5", title_color="#fff", title_pos="center",
width=1200, height=600, background_color='#404a59')
attr, value = geo.cast(data)
geo.add("", attr, value, visual_range=[0, 200], visual_text_color="#fff", symbol_size=15, is_visualmap=True)
geo.render()
```
![geo-demo](https://user-images.githubusercontent.com/19553554/35089650-7f06172e-fc72-11e7-9d4b-14437fb0d8fe.gif)

**Note：** Please use it with Visualmap

**Scatter type (Segmented)**
```python
geo = Geo("全国主要城市空气质量", "data from pm2.5", title_color="#fff",
          title_pos="center", width=1200,
          height=600, background_color='#404a59')
attr, value = geo.cast(data)
geo.add("", attr, value, visual_range=[0, 200], visual_text_color="#fff",
        symbol_size=15, is_visualmap=True, is_piecewise=True, visual_split_number=6)
geo.render()
```
![geo-demo](https://user-images.githubusercontent.com/19553554/35089651-80d259a0-fc72-11e7-8af9-d96df53c0d49.gif)

**HeatMap type**
```python
geo = Geo("全国主要城市空气质量", "data from pm2.5", title_color="#fff",
          title_pos="center", width=1200,
          height=600, background_color='#404a59')
attr, value = geo.cast(data)
geo.add("", attr, value, type="heatmap", is_visualmap=True, visual_range=[0, 300],
        visual_text_color='#fff')
geo.render()
```
![geo-demo](https://user-images.githubusercontent.com/19553554/35089653-82498f88-fc72-11e7-9811-2aceccd4ed68.gif)


**EffectScatter on China map**
```python
from pyecharts import Geo

data = [
    ("海门", 9), ("鄂尔多斯", 12), ("招远", 12),
    ("舟山", 12), ("齐齐哈尔", 14), ("盐城", 15)
    ]
geo = Geo("全国主要城市空气质量", "data from pm2.5", title_color="#fff",
          title_pos="center", width=1200,
          height=600, background_color='#404a59')
attr, value = geo.cast(data)
geo.add("", attr, value, type="effectScatter", is_random=True, effect_scale=5)
geo.render()
```
![geo-demo](https://user-images.githubusercontent.com/19553554/35089655-844c8902-fc72-11e7-8d1b-a0920ad5baa8.gif)

**EffectScatter on my home province, Canton**
```python
from pyecharts import Geo

data =[
    ('汕头市', 50), ('汕尾市', 60), ('揭阳市', 35),
    ('阳江市', 44), ('肇庆市', 72)
    ]
geo = Geo("广东城市空气质量", "data from pm2.5", title_color="#fff",
          title_pos="center", width=1200,
          height=600, background_color='#404a59')
attr, value = geo.cast(data)
geo.add("", attr, value, maptype='广东', type="effectScatter",
        is_random=True, effect_scale=5, is_legend_show=False)
geo.render()
```
![geo-demo](https://user-images.githubusercontent.com/19553554/35089657-85d0b7bc-fc72-11e7-8b3d-8127dbe8f780.gif)

**Use coordinate_region to specify the country which to retrieve coordinates**
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
    # Use coordinate_region to specify the coordinates of the UK range, such as Oxford above.
    # default is China
    coordinate_region="英国",
    visual_range=[0, 200],
    visual_text_color="#fff",
    symbol_size=15,
    is_visualmap=True,
)
geo.render()
```
![geo-demo](https://user-images.githubusercontent.com/19553554/43998653-23b21a78-9e2d-11e8-8273-52fbeaacc6e8.png)


## GeoLines
> It is used for drawing line data with start and end point information, mainly for the route on the map and the route visualization.

GeoLines.add() signatures
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
    Chart name

* data -> [list]
    Data item, each row is a "data item", and each column is one "dimension". Each row contains two or three data, such as ["Guangzhou", "Beijing"] or ["Guangzhou", "Beijing", 100], which is designated from Guangzhou to Beijing. The third value is used to represent the value of the line, which can be omitted.

* maptype -> str  
    Map type. Since v0.3.2+, the map has become an extension package, supporting maps of provinces, cities, national districts, and countries around the world. For details, please refer to [Map Customization] (en-us/customize_map)

* coordinate_region -> str  
    The country of which the city coordinates belongs to. From v0.5.7, looking for the location of international cities. Default is `China`. The specific country mapping table refers to [countries_regions_db.json](https://github.com/pyecharts/pyecharts/blob/master/pyecharts/datasets/countries_regions_db.json). More geographic coordinates information can be referred to [dataset articles](/en-us/datasets)

* symbol -> str  
    The symbol type at both ends of the line. It could be either an array specifying two ends, or a single unified designation.

* symbol_size -> int  
    The symbol size at both ends of the line. It could be an array specified at both ends, or a single unified designation.

* border_color -> str  
    Map border color. Default is '#111'

* geo_normal_color -> str   
    The color of the map area under normal mode. Default is '#323c48'

* geo_emphasis_color -> str   
    The color of the map area under highlighted mode. Default is '#2a333d'

* geo_cities_coords -> dict   
    Custom regional latitude and longitude, similar to the dictionary such as {'Acheng': [126.58, 45.32],}.

* geo_effect_period -> int/float  
    Effect animation time, the unit is s. Ddefault is 6s

* geo_effect_traillength -> float   
    The special effect trail length. Range from 0 to 1, the larger the value, the longer the trail. Default is 0

* geo_effect_color -> str  
    The color of the effect tag. The default is '#fff'

* geo_effect_symbol -> str  
    The symbol of the special effect graphic. There are 'circle', 'rect', 'roundRect', 'triangle', 'diamond', 'pin', 'arrow', 'plane' optional.

* geo_effect_symbolsize -> int/list  
    The size of the effect tag. It could be set to a single number such as 10, or divided into high and wide by an array. For example, [20, 10] means the tag width is 20 and the height is 10.

* is_geo_effect_show -> bool  
    Whether to display special effects.

* is_roam -> bool  
    Whether to enable mouse zoom and move roaming. Default is True.  
    If you only want to turn on zoom or move, you can set it to 'scale' or 'move'. Set to True means to turn on both.  

**Default effect**
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

**Configured more parameters**
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

**Specify value**
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

**Multiple case mode**
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

**Single selected mode, specified `legend_selectedmode="single"`**
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
    legend_selectedmode="single", #set to single selected mode
)
geolines = GeoLines("GeoLines 示例", **style.init_style)
geolines.add("从广州出发", data_guangzhou, **style_geo)
geolines.add("从北京出发", data_beijing, **style_geo)
geolines.render()
```
![geolines-demo](https://user-images.githubusercontent.com/19553554/35082105-00885b92-fc53-11e7-8803-adc054037285.gif)

## Graph
> Graph is a diagram to represent nodes and the links connecting nodes.

Graph.add() signatures
```python
add(name, nodes, links, categories=None, is_focusnode=True, is_roam=True, is_rotatelabel=False,
    layout="force", edge_length=50, gravity=0.2, repulsion=50, **kwargs)
```
* name -> str  
    Series name used for displaying in tooltip and filtering with legend,or updaing data and configuration with setOption.

* nodes -> dict  
    Relational nodes data
    * name：Name of data item.     # required！！
    * x：x value of node position.
    * y：y value of node position.
    * value：value of data item.
    * category：Index of category which the data item belongs to.
    * symbol：Symbol of node of this category.Includes 'circle', 'rect', 'roundRect', 'triangle', 'diamond', 'pin', 'arrow'
    * symbolSize：symbol size

* links -> dict  
    Relational data between nodes
    * source：name of source node on edge      # required！！
    * target：name of target node on edge      # required！！
    * vaule：value of edge,It can be used in the force layout to map to the length of the edge

* categories -> list  
    Name of category, which is used to correspond with legend and the content of tooltip.

* is_focusnode -> bool  
    defalut -> True  
    Whether to focus/highlight the hover node and it's adjacencies.

* is_roam -> bool/str  
    default -> True  
    Whether to enable mouse zooming and translating.  
    If either zooming or translating is wanted,it can be set to 'scale' or 'move'. Otherwise, set it to be true to enable both.

* is_rotatelabel -> bool  
    default -> False  
    Whether to rotate the label automatically.

* graph_layout -> str  
    Graph layout.  
    default -> 'force'  
    * none：No any layout, use x, y provided in node as the position of node.
    * circular：Adopt circular layout, see the example Les Miserables.
    * force：Adopt force-directed layout, see the example Force,the detail about configrations of layout are in graph.force

* graph_edge_length -> int  
    default -> 50  
    The distance between 2 nodes on edge. This distance is also affected by `repulsion`.  
    It can be an array to represent the range of edge length. In this case, edge with larger value will be shorter, which means two nodes are closer. And edge with smaller value will be longer.

* graph_gravity -> int/float  
    default -> 0.2  
    The gravity factor enforcing nodes approach to the center.The nodes will be closer to the center as the value becomes larger.

* graph_repulsion -> int  
    default -> 50  
    The repulsion factor between nodes. The repulsion will be stronger and the distance between 2 nodes becomes further as this value becomes larger.  
    It can be an array to represent the range of repulsion.  
    In this case, larger value have larger repulsion and smaller value will have smaller repulsion.

* graph_edge_symbol -> str/list
    The symbol type at both ends of the edge. It can be an array specifying the two ends, or a single unified designation. Symbols are not displayed by default, and common option can be set to arrows, as follows: edgeSymbol: ['circle', 'arrow']

* graph_edge_symbolsize -> int/list
    The size of the symbol at both ends of the edge. It can be an array to specify the two ends, or a single unified designation.
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
graph.show_config()
graph.render()

```
![graph-demo](https://user-images.githubusercontent.com/19553554/35082109-05240854-fc53-11e7-9e92-dd9437c55383.png)


```python
graph = Graph("关系图-环形布局示例")
graph.add("", nodes, links, is_label_show=True, repulsion=8000, layout='circular', label_text_color=None)
graph.show_config()
graph.render()
```
![graph-demo](https://user-images.githubusercontent.com/19553554/35082112-07074726-fc53-11e7-9f28-2d3b39c5e162.png)

```python
from pyecharts import Graph

import json
with open("data\weibo.json", "r", encoding="utf-8") as f:
    j = json.load(f)
    nodes, links, categories, cont, mid, userl = j
graph = Graph("微博转发关系图", width=1200, height=600)
graph.add("", nodes, links, categories, label_pos="right", repulsion=50, is_legend_show=False,
          line_curve=0.2, label_text_color=None)
graph.show_config()
graph.render()
```
![graph-demo](https://user-images.githubusercontent.com/19553554/35081908-bb313aba-fc51-11e7-8ef5-df20be445d72.gif)

**Note：** **lineStyle** parameter is configurable

## HeatMap type  
> The heat map mainly uses color to represent the size of the value and must be used with the visualMap component. Two category axes must be used on a Cartesian coordinate system.

HeatMap.add() method signature
```python
Add(*args, **kwargs)
```
If `is_calendar_heatmap` is specified (use the calendar heat map) is True, the parameter is
* name -> str  
    chart name

* data -> [list]  
    Data item, in the data, each row is a "data item", and each column belongs is a "dimension"

* calendar_date_range -> str/list  
    The date of the calendar heat map, "2016" means 2016, ["2016-5-5", "2017-5-5"] means May 5, 2016 to May 5, 2017

* calendar_cell_size -> list  
    The size of each calendar frame could be set to a single value or an array. The first element is wide. The second element is high. Support to set the adaptive "auto". Default is ["auto", 20]

Default is not specified, the parameter is
* name -> str  
    chart name

* x_axis -> str  
    x axis data. Need to be the category axis, that is, it cannot be a numeric value.

* y_axis -> str  
    y axis data. Need to be the category axis, that is, it cannot be a numeric value.

* data -> [list]   
    Data item, in the data, each row is a "data item", and each column belongs to a "dimension"

**By default, not specified `is_calendar_heatmap`**
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

**Use the calendar heat map to specify `is_calendar_heatmap` is True**
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

**Note：** The heat map must be used with VisualMap in the common configuration item.


## Kline/Candlestick
> Kline chart use red to imply increasing with red and decreasing with blue

Kline.add() signatures
```python
add(name, x_axis, y_axis, **kwargs)
```
* name -> str  
    Series name used for displaying in tooltip and filtering with legend,or updaing data and configuration with setOption.

* x_axis -> list  
    data of xAxis

* y_axis -> [[], []]  
    data pf yAxis.Data should be the two-dimensional array shown as follow.  
    Every data item (each line in the example above) represents a box, which contains 4 values. They are: [open, close, lowest, highest]  (namely: [opening value, closing value, lowest value, highest value])

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
kline.add("日K", ["2017/7/{}".format(i + 1) for i in range(31)], v1, mark_point=["max"], is_datazoom_show=True)
kline.render()
```
![kline-demo](https://user-images.githubusercontent.com/19553554/35090072-9b6ca404-fc73-11e7-8abe-e5576d35c57a.gif)

**dataZoom effect is added to the ordinate axis**
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

**Specify markLine to be on the open or close**
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

## Line
> Broken line chart relates all the data points symbol by broken lines,
> which is used to show the trend of data changing. It could be used in both rectangular coordinate and polar coordinate.

Line.add() signatures
```python
add(name, x_axis, y_axis, is_symbol_show=True, is_smooth=False, is_stack=False,
    is_step=False, **kwargs)
```
* name -> str  
    Series name used for displaying in tooltip and filtering with legend,or updaing data and configuration with setOption.

* x_axis -> list  
    data of xAxis

* y_axis -> list  
    data of yAxis

* is_symbol_show -> bool  
    default -> True  
    It specifies whether to show the symbol.

* is_smooth -> bool
    default -> False
    Whether to show as smooth curve.

* is_stack -> bool  
    default -> Flase  
    It specifies whether to stack category axis.

* is_step -> bool/str  
    default -> False  
    Whether to show as a step line.It can be true, false. Or 'start', 'middle', 'end'.Which will configure the turn point of step line.

```python
from pyecharts import Line

attr = ["衬衫", "羊毛衫", "雪纺衫", "裤子", "高跟鞋", "袜子"]
v1 = [5, 20, 36, 10, 10, 100]
v2 = [55, 60, 16, 20, 15, 80]
line = Line("折线图示例")
line.add("商家A", attr, v1, mark_point=["average"])
line.add("商家B", attr, v2, is_smooth=True, mark_line=["max", "average"])
line.show_config()
line.render()
```
![line-demo](https://user-images.githubusercontent.com/19553554/35089953-4865fe2c-fc73-11e7-8c47-e917332d061c.gif)

**Other Configurations Of Marker Point**
```python
line = Line("折线图示例")
line.add("商家A", attr, v1, mark_point=["average", "max", "min"],
         mark_point_symbol='diamond', mark_point_textcolor='#40ff27')
line.add("商家B", attr, v2, mark_point=["average", "max", "min"],
         mark_point_symbol='arrow', mark_point_symbolsize=40)
line.render()
```
![line-demo](https://user-images.githubusercontent.com/19553554/35089954-49784dd8-fc73-11e7-8a5b-d9163857c4b1.png)

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

**area_opacity：** Opacity of the component. Supports value from 0 to 1, and the component will not be drawn when set to 0.
```python
line = Line("折线图-面积图示例")
line.add("商家A", attr, v1, is_fill=True, line_opacity=0.2, area_opacity=0.4, symbol=None)
line.add("商家B", attr, v2, is_fill=True, area_color='#000', area_opacity=0.3, is_smooth=True)
line.render()
```
![line-demo](https://user-images.githubusercontent.com/19553554/35089973-53868fd8-fc73-11e7-8ff6-bfb452954267.png)

* area_opacity -> float  
    Opacity of the component. Supports value from 0 to 1, and the component will not be drawn when set to 0.

* area_color -> str  
    Fill color.

**Note：** **lineStyle** Parameter is Configurable
**Note：** Setting line color by `label_color`, like ['#eee', '#000'], all type of chart can revise label color by `label_color`.

**If it is logarithmic data, we recommended to use the ```yaxis_type``` parameter to set the y coordinate axis to logarithmic axis.**
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

**The lowest and highest temperature line chart of certain place**
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


## Line3D
Line3D.add() signatures
```python
add(name, data, grid3D_opacity=1, **kwargs)
```
* name -> str
    Series name used for displaying in tooltip and filtering with legend,or updaing data and configuration with setOption.

* data -> [[], []]  
    data of line3D

* grid3D_opacity -> float  
    default -> 1  
    opacity of gird3D item

**Draw a spring**
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
range_color = ['#313695', '#4575b4', '#74add1', '#abd9e9', '#e0f3f8', '#ffffbf',
               '#fee090', '#fdae61', '#f46d43', '#d73027', '#a50026']
line3d = Line3D("3D 折线图示例", width=1200, height=600)
line3d.add("", _data, is_visualmap=True, visual_range_color=range_color, visual_range=[0, 30],
           grid3D_rotate_sensitivity=5)
line3d.render()
```
![line3d-demo](https://user-images.githubusercontent.com/19553554/35081902-b0bed8c6-fc51-11e7-9b3a-1d138c4eba13.gif)

**rotating spring**
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
range_color = ['#313695', '#4575b4', '#74add1', '#abd9e9', '#e0f3f8', '#ffffbf',
               '#fee090', '#fdae61', '#f46d43', '#d73027', '#a50026']
line3d = Line3D("3D 折线图示例", width=1200, height=600)
line3d.add("", _data, is_visualmap=True, visual_range_color=range_color, visual_range=[0, 30],
           is_grid3D_rotate=True, grid3D_rotate_speed=180)
line3d.render()
```
![line3d-demo](https://user-images.githubusercontent.com/19553554/35081903-b3a4eada-fc51-11e7-97b1-33f1dd6ed79e.gif)

**Note：** more details aboutt gird3D，please refer to [Chart Configuration](en-us/charts_configure)
**Note：** Can be used with axis3D common configuration items


## Liquid
> Liquid chart is usually used to represent data in percentage.

Liquid.add() signatures
```python
add(name, data, shape='circle', liquid_color=None, is_liquid_animation=True,
    is_liquid_outline_show=True, **kwargs)
```
* name -> str  
    Series name used for displaying in tooltip and filtering with legend,or updaing data and configuration with setOption.

* data -> list  
    data of liquid,[0.6, 0.5, 0.4, 0.3] -> This creates a chart wit waves at position of 60%, 50%, 40%, and 30%.

* shape -> str  
    Shape of water fill chart.It can be one of the default symbols: 'circle', 'rect', 'roundRect', 'triangle', 'diamond', 'pin', 'arrow'

* liquid_color -> list  
    default -> ['#294D99', '#156ACF', '#1598ED', '#45BDFF']  
    To set colors for liquid fill chart series, set color to be an array of colors.

* is_liquid_animation -> bool  
    default -> True  
    Whether disable animation.

* is_liquid_outline_show -> bool  
    default -> True  
    whether show the outline

```python
from pyecharts import Liquid

liquid = Liquid("水球图示例")
liquid.add("Liquid", [0.6])
liquid.show_config()
liquid.render()
```
![liquid-demo](https://user-images.githubusercontent.com/19553554/35082172-536178a8-fc53-11e7-8c8b-1fa1312c8854.gif)

```python
from pyecharts import Liquid

liquid = Liquid("水球图示例")
liquid.add("Liquid", [0.6, 0.5, 0.4, 0.3], is_liquid_outline_show=False)
liquid.show_config()
liquid.render()
```
![liquid-demo](https://user-images.githubusercontent.com/19553554/35082175-55337000-fc53-11e7-9e5b-24cd47288e8d.gif)

```python
from pyecharts import Liquid

liquid = Liquid("水球图示例")
liquid.add("Liquid", [0.6, 0.5, 0.4, 0.3], is_liquid_animation=False, shape='diamond')
liquid.show_config()
liquid.render()
```
![liquid-demo](https://user-images.githubusercontent.com/19553554/35082178-567d2db6-fc53-11e7-965a-d60e72ab6bf4.png)

**Custom SVG route**
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


## Map
> Map is maily used in the visulization of geographic area data, which can be used with visualMap component to visualize the datas such as population distribution density in diffrent areas.

Map.add() signatures
```python
add(name, attr, value, is_roam=True, maptype='china', **kwargs)
```
* name -> str  
    Series name used for displaying in tooltip and filtering with legend,or updaing data and configuration with setOption.

* attr -> list  
    name of attribute

* value -> list  
    value of attribute

* maptype -> str  
   type of map, it supports chinese geographical names, such as "安徽, 澳门, 北京, 重庆, 福建, 福建, 甘肃, 广东，广西, 广州, 海南, 河北, 黑龙江, 河南, 湖北, 湖南, 江苏, 江西, 吉林, 辽宁, 内蒙古, 宁夏, 青海, 山东, 上海, 陕西, 四川, 台湾, 天津, 香港, 新疆, 西藏, 云南, 浙江" and [363 provincial cities](https://github.com/chfw/echarts-china-cities-js#featuring-citiesor-for-single-download).

* is_roam -> bool/str  
    default -> True  
    Whether to enable mouse zooming and translating.If either zooming or translating is wanted,it can be set to 'scale' or 'move'. Otherwise, set it to be true to enable both.

* is_map_symbol_show -> bool    
    Whether to display the map marker red dot, default is True.

* name_map -> dict  
    [Use a custom map name](http://echarts.baidu.com/option.html#series-map.nameMap). Some maps provide administrative area codes, and `name_map` can help convert them to user-friendly place names. For example, the British constituency map, the administrative area code of the London constituency is E14000639, and converting it into a readable place name requires such a dictionary:  
    ```
    name_map = {"E14000639": "Cities of London and Westminster"}
    ```

    By analogy, to convert all the names of the UK constituencies, you need a [larger dictionary](https://github.com/chfw/echarts-united-kingdom-pypkg/blob/master/echarts_united_kingdom_pypkg/constants.py#L1)

```python
from pyecharts import Map

value = [155, 10, 66, 78]
attr = ["福建", "山东", "北京", "上海"]
map = Map("全国地图示例", width=1200, height=600)
map.add("", attr, value, maptype='china')
map.show_config()
map.render()
```
![map-demo](https://user-images.githubusercontent.com/19553554/35082377-718385f0-fc54-11e7-88c2-bd1df8bf112b.gif)

**Show each area name**
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
attr = ["福建", "山东", "北京", "上海", "甘肃", "新疆", "河南", "广西", "西藏"]
map = Map("Map 结合 VisualMap 示例", width=1200, height=600)
map.add("", attr, value, maptype='china', is_visualmap=True, visual_text_color='#000')
map.show_config()
map.render()
```
![map-demo](https://user-images.githubusercontent.com/19553554/35082380-75e1b89c-fc54-11e7-8169-75884ffb67fb.gif)

**Note：** Settings can combine with visualMap component.

```python
from pyecharts import Map

value = [20, 190, 253, 77, 65]
attr = ['汕头市', '汕尾市', '揭阳市', '阳江市', '肇庆市']
map = Map("广东地图示例", width=1200, height=600)
map.add("", attr, value, maptype='广东', is_visualmap=True, visual_text_color='#000')
map.show_config()
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


**Set `is_map_symbol_show=False` to cancel display symbol red point**
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

**Set `name_map` to use custom map name**
Original version ： 
![map-demo](https://user-images.githubusercontent.com/4280312/36720467-16fb0a66-1ba0-11e8-8cbd-453d8f2462d3.png)
    
After `name_map` changed ： 

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

This is convenient for drawing, because many data and area numbers are directly linked, and it is also easy to localize.

Set the `pieces` custom visualMap component tag
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


## Parallel
> Parallel Coordinates is a common way of visualizing high-dimensional geometry and analyzing multivariate data.

Parallel.add() signatures
```python
add(name, data, **kwargs)
```
* name -> str  
    Series name used for displaying in tooltip and filtering with legend,or updaing data and configuration with setOption.

* data -> [[],[]]  
    data array of series, it is represented by a two-dimension array.

Parallel.set_schema() / Parallel.config() method signatures  
```python
set_schema(schema=None, c_schema=None)
config(schema=None, c_schema=None)
```

> Since v0.5.9, the original `config` method was deprecated and the set_schema method is recommended.

* schema  
    Dimension index of coordinate axis.  
    a axis name list, like ['apple', 'orange', 'watermelon']

* c_schema  
    User customize coordinate axis for parallel coordinate.
    
    * dim -> int  
        Dimension index of coordinate axis.
    
    * name > str  
        Name of axis.
    
    * type -> str  
        Type of axis  
        value：Numerical axis, suitable for continuous data.  
        category：Category axis, suitable for discrete category data.Data should only be set via data for this type.
    
    * min -> int  
        The minimun value of axis.
    
    * max -> int  
        The maximum value of axis.
    
    * inverse - bool  
        default -> False  
        Whether axis is inversed.
    
    * nameLocation -> str  
        Location of axis name. it can be 'start', 'middle', 'end'.

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
    "type": "category", "data": ['优', '良', '轻度污染', '中度污染', '重度污染', '严重污染']}
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

**Note：** **lineStyle** Parameter is Configurable


## Pie
> The pie chart is mainly used for showing proportion of different categories.Each arc length represents the proportion of data quantity.

Pie.add() signatures
```python
add(name, attr, value, radius=None, center=None, rosetype=None, **kwargs)
```
* name -> str  
    Series name used for displaying in tooltip and filtering with legend, or updaing data and configuration with setOption.

* attr -> list  
    name of attribute
* value -> list  
    value of attribute

* radius -> list  
    default -> [0, 75]  
    Radius of Pie chart, the first of which is inner radius, and the second is outer radius.  
    Percentage is supported. When set in percentage, it's relative to the smaller size between height and width of the container.

* center -> list
    default -> [50, 50]  
    Center position of Pie chart, the first of which is the horizontal position,and the second is the vertical position.  
    Percentage is supported. When set in percentage, the item is relative to the container width, and the second item to the height.

* rosetype -> str  
    default -> 'radius'  
    Whether to show as Nightingale chart, which distinguishs data through radius. There are 2 optional modes:
    * radius：Use central angle to show the percentage of data, radius to show data size.
    * area：All the sectors will share the same central angle, the data size is shown only through radiuses.

```python
from pyecharts import Pie

attr = ["衬衫", "羊毛衫", "雪纺衫", "裤子", "高跟鞋", "袜子"]
v1 = [11, 12, 13, 10, 10, 10]
pie = Pie("饼图示例")
pie.add("", attr, v1, is_label_show=True)
pie.render()
```
![pie-0](https://user-images.githubusercontent.com/19553554/35089599-5eed1ef6-fc72-11e7-8740-601880be9e16.gif)

```python
from pyecharts import Pie

attr = ["衬衫", "羊毛衫", "雪纺衫", "裤子", "高跟鞋", "袜子"]
v1 = [11, 12, 13, 10, 10, 10]
pie = Pie("饼图-圆环图示例", title_pos='center')
pie.add("", attr, v1, radius=[40, 75], label_text_color=None, is_label_show=True,
        legend_orient='vertical', legend_pos='left')
pie.render()
```
![pie-1](https://user-images.githubusercontent.com/19553554/35089631-70b6e7de-fc72-11e7-838d-f8b238bbc03f.png)

```python
from pyecharts import Pie

attr = ["衬衫", "羊毛衫", "雪纺衫", "裤子", "高跟鞋", "袜子"]
v1 = [11, 12, 13, 10, 10, 10]
v2 = [19, 21, 32, 20, 20, 33]
pie = Pie("饼图-玫瑰图示例", title_pos='center', width=900)
pie.add("商品A", attr, v1, center=[25, 50], is_random=True, radius=[30, 75], rosetype='radius')
pie.add("商品B", attr, v2, center=[75, 50], is_random=True, radius=[30, 75], rosetype='area',
        is_legend_show=False, is_label_show=True)
pie.show_config()
pie.render()
```
![pie-2](https://user-images.githubusercontent.com/19553554/35089635-72585da2-fc72-11e7-835d-c9b64750d19d.png)

**Pie in Pie**
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

**Multiple pie drawings in one chart**
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


## Polar
> Polar coordinate can be used in scatter and line chart. Every polar coordinate has an angleAxis and a radiusAxis.

Polar.add() signatures
```python
add(name, data, angle_data=None, radius_data=None, type='line', symbol_size=4, start_angle=90,
    rotate_step=0, boundary_gap=True, clockwise=True, **kwargs)
```
* name -> str  
    Series name used for displaying in tooltip and filtering with legend,or updaing data and configuration with setOption.

* data -> [[],[]]  
    data of polar, [Polar radius, Polar angle,it is represented by a two-dimension array.

* angle_data -> list  
    Category data for angle, available in type: 'category' axis.

* radius_data -> list  
    Category data for radius, available in type: 'category' axis.

* type -> str  
    default -> 'line'  
    chart type，it can be 'scatter', 'effectScatter', 'barAngle', 'barRadius'

* symbol_size -> int  
    default -> 4  
    symbol size

* start_angle -> int  
    default -> 90  
    Starting angle of axis.standing for top position of center.0 degree stands for right position of center.

* rotate_step -> int  
    default -> 0  
    Rotation degree of axis label, which is especially useful when there is no enough space for category axis.
    Rotation degree is from -90 to 90.

* boundary_gap -> bool  
    default -> True  
    The boundary gap on both sides of a coordinate axis.  
    The setting and behavior of category axes and non-category axes are different.  
    The boundaryGap of category axis can be set to either true or false.  
    Default value is set to be true, in which case axisTick is served only as a separation line,and labels and data appear only in the center part of two axis ticks, which is called band.

* clockwise -> bool  
    default -> True  
    Whether the positive position of axis is in clockwise. True for clockwise by default.

* is_stack -> bool  
    It specifies whether to stack category axis.

* axis_range -> list  
    default -> [None, None]  
    axis scale range

* is_angleaxis_show -> bool  
    default -> True  
    whether show angle axis.

* is_radiusaxis_show -> bool  
    default -> True  
    whether show radius axis.

* radiusaxis_z_index -> int
    Radius axis z-index, default is 50

* angleaxis_z_index -> int
    Angle axis z-index, default is 50

* is_radiusaxis_show -> bool  
    Whether to display the radial axis of the polar coordinate system, default is True

* render_item -> function  
    The developer provides the logic of the graphics rendering. This rendering logic is generally name [render_item](http://echarts.baidu.com/option.html#series-custom.renderItem)，refer to [Advance Topics](en-us/advanced)

```python
from pyecharts import Polar

import random
data = [(i, random.randint(1, 100)) for i in range(101)]
polar = Polar("极坐标系-散点图示例")
polar.add("", data, boundary_gap=False, type='scatter', is_splitline_show=False,
          area_color=None, is_axisline_show=True)
polar.render()
```
![polar-0](https://user-images.githubusercontent.com/19553554/35090448-aaf0d5a2-fc74-11e7-83c4-7b2f55090e98.png)

* is_splitline_show -> bool  
    default -> True  
    It specifies whether to show split line.

* is_axisline_show -> bool  
    default -> True  
    It specifies whether to show axis line.

* area_opacity -> float  
    Opacity of the component. Supports value from 0 to 1, and the component will not be drawn when set to 0.

* area_color -> str  
    Fill color.

**Note：** **lineStyle** Parameter is Configurable

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
![polar-1](https://user-images.githubusercontent.com/19553554/35090451-abf708e0-fc74-11e7-8814-25ba5e72f542.png)

```python
from pyecharts import Polar

import random
data = [(i, random.randint(1, 100)) for i in range(10)]
polar = Polar("极坐标系-动态散点图示例", width=1200, height=600)
polar.add("", data, type='effectScatter', effect_scale=10, effect_period=5)
polar.render()
```
![polar-2](https://user-images.githubusercontent.com/19553554/35090453-ad2b4d52-fc74-11e7-8ecd-cb64546d0d40.gif)

```python
from pyecharts import Polar

radius = ['周一', '周二', '周三', '周四', '周五', '周六', '周日']
polar = Polar("极坐标系-堆叠柱状图示例", width=1200, height=600)
polar.add("A", [1, 2, 3, 4, 3, 5, 1], radius_data=radius, type='barRadius', is_stack=True)
polar.add("B", [2, 4, 6, 1, 2, 3, 1], radius_data=radius, type='barRadius', is_stack=True)
polar.add("C", [1, 2, 3, 4, 1, 2, 5], radius_data=radius, type='barRadius', is_stack=True)
polar.render()
```
![polar-3](https://user-images.githubusercontent.com/19553554/35090457-afc0658e-fc74-11e7-9c58-24c780436287.gif)

```python
from pyecharts import Polar

radius = ['周一', '周二', '周三', '周四', '周五', '周六', '周日']
polar = Polar("极坐标系-堆叠柱状图示例", width=1200, height=600)
polar.add("", [1, 2, 3, 4, 3, 5, 1], radius_data=radius, type='barAngle', is_stack=True)
polar.add("", [2, 4, 6, 1, 2, 3, 1], radius_data=radius, type='barAngle', is_stack=True)
polar.add("", [1, 2, 3, 4, 1, 2, 5], radius_data=radius, type='barAngle', is_stack=True)
polar.render()
```
![polar-4](https://user-images.githubusercontent.com/19553554/35090460-b11ab380-fc74-11e7-836c-2e8197e32723.png)


**Custom rendering logic example**
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


## Radar
> Radar chart is mainly used to show multi-variable data,such as the analysis of a football player's varied attributes. It relies radar component.

Radar.add() signatures
```python
add(name, value, item_color=None, **kwargs)
```
* name -> list  
    Series name used for displaying in tooltip and filtering with legend,or updaing data and configuration with setOption.

* value -> [[],[]]  
    data array of series, it is represented by a two-dimension array.

* item_color -> str  
    Specify a single legend color

Radar.set_radar_component() /Radar.config() signatures
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

> As of v0.5.9, the original `config` is deprecated. The `set_radar_component` method is recommended.

* schema -> list  
    The default radar map indicator, used to specify multiple dimensions in the radar map,will process the data into a dictionary of {name: xx, value: xx}

* c_schema -> dict  
    Indicator of radar chart, which is used to assign multiple variables(dimensions) in radar chart.
    
    * name: Indicator's name.
    
    * min: The maximum value of indicator. It is an optional configuration, but we recommend to set it manually.
    
    * max: The maximum value of indicator. It is an optional configuration, but we recommend to set it manually.

* shape -> str  
    Radar render type, in which 'polygon' and 'circle' are supported.

* rader_text_color -> str  
    default -> '#000'  
    Radar chart data item font color

* radar_text_size -> int
    Radar chart data item font size, default is 12

```python
from pyecharts import Radar

schema = [
    ("销售", 6500), ("管理", 16000), ("信息技术", 30000), ("客服", 38000), ("研发", 52000), ("市场", 25000)]
v1 = [[4300, 10000, 28000, 35000, 50000, 19000]]
v2 = [[5000, 14000, 28000, 31000, 42000, 21000]]
radar = Radar()
radar.config(schema)
radar.add("预算分配", v1, is_splitline=True, is_axisline_show=True)
radar.add("实际开销", v2, label_color=["#4e79a7"], is_area_show=False)
radar.render()
```
![radar-demo](https://user-images.githubusercontent.com/19553554/35082333-20046172-fc54-11e7-944a-b6e25bf5dd2a.gif)

* is_area_show -> bool  
    It specifies whether to show split area.

* area_opacity -> float  
    Opacity of the component. Supports value from 0 to 1, and the component will not be drawn when set to 0.

* area_color -> str  
    Fill color.

* is_splitline_show  -> bool  
    default -> True
    It specifies whether to show split line.

* is_axisline_show -> bool  
    default -> True  
    It specifies whether to show axis line.

**Note：** **lineStyle** Parameter is Configurable

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
radar.add("上海", value_sh, item_color="#b3e4a1", symbol=None)
radar.render()
```
![radar-demo](https://user-images.githubusercontent.com/19553554/35082335-224c23ca-fc54-11e7-910a-0914699ac06e.gif)

**Tip：** symblo=None make marked graphic hiden(small circle)


**Multiple charts mode**
```python
radar = Radar()
radar.config(c_schema=c_schema, shape='circle')
radar.add("北京", value_bj, item_color="#f9713c", symbol=None)
radar.add("上海", value_sh, item_color="#b3e4a1", symbol=None)
radar.render()
```
![radar-demo](https://user-images.githubusercontent.com/19553554/35082343-269d9440-fc54-11e7-9675-4c125bbca75d.gif)


## Sankey
> Sankey is a special flow diagram, which is mainly used to indicate how raw materials, energy, etc. are processed and transformed from the initial form to the final form through the intermediate process.

Sankey.add() signatures
```python
add(name, nodes, links,
    sankey_node_width=20,
    sankey_node_gap=8, **kwargs)
```
* name -> str    
     chart name

* nodes -> list  
    The data items that must be included in the Sankey chart node are:
    * name: data item name
    * value: data item value

* links -> list  
    Sankey node link relation
    * source：The source node name of the edge ( required! )
    * target：Target node name of the edge ( required! )
    * value：The value of the edge determines the width of the edge

 * sankey_node_width -> int  
    The width of each rectangular node in the chart. Default is 20

 * sankey_node_gap -> int  
    The interval between any two rectangular nodes in each column of the chart. Default is 8

**Simple example**
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

**Use json data from official**
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


## Scatter
> The scatter chart in rectangular coordinate could be used to present the relation between x and y.
> If data have multiple dimensions, the values of the other dimensions can be visualized through symbol with various sizes and colors, which becomes a bubble chart. These can be done by using with geo component.

Scatter.add() signatures
```python
add(name, x_axis, y_axis, extra_data=None, symbol_size=10, **kwargs)
```
* name -> str  
    Series name used for displaying in tooltip and filtering with legend,or updaing data and configuration with setOption.

* x_axis -> list  
    data of xAxis

* y_axis -> list  
    data of yAxis

* extra_data -> list[int]  
    The third dimension data, the x-axis is the first dimension and the y-axis is the second dimension. (View elements can be mapped to a third dimension in a visualmap)

* extra_name -> list[str]  
    The name of the extra data item. You can specify a name for each data point.

* symbol_size -> int  
    default -> 10  
    symbol size

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

**Realize color mapping values using Visualmap component**
```python
scatter = Scatter("散点图示例")
scatter.add("A", v1, v2)
scatter.add("B", v1[::-1], v2, is_visualmap=True)
scatter.render()
```
![scatter-demo](https://user-images.githubusercontent.com/19553554/35090355-60bc82b0-fc74-11e7-8cc2-4f10c1c8193e.gif)

**Map values ​​with chart point size using the Visualmap component**
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

**Map to the third dimension data using Visualmap components**
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

**Give each coordinate point a name that can be used for tooltip display**
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

**Note：** Please use the Visualmap in the common configuration.

**The default axis of the scatter chart is value axis. If you want to implement the category axis, you can modify it by `xaxis_type`**
```python
scatter = Scatter("散点图示例")
scatter.add("A", ["a", "b", "c", "d", "e", "f"], v2)
scatter.add("B", ["a", "b", "c", "d", "e", "f"], v1[::-1], xaxis_type="category")
scatter.render()
```
![scatter-demo](https://user-images.githubusercontent.com/19553554/35090414-916add4e-fc74-11e7-83c1-d428387e8101.png)

**Scatter also have built-in draw method**
```python
draw(path, color=None)
```
convert pixels on the image into array ,when colour is （255,255,255）only retain non white pixels' coordinate information. output two k_lst, v_lst list can just as the data item of scatter plot.

```
* path -> str  
    path of Image that want to draw

* color -> str  
    select a color to exclude, (225, 225, 225) means Keep only white pixel information.

First of all ,you need to prepare a picture,like

![pyecharts-0](https://user-images.githubusercontent.com/19553554/35104421-c25a02f2-fca3-11e7-868d-d70bd86fdd76.png)

```python
from pyecharts import Scatter

scatter = Scatter("散点图示例")
v1, v2 = scatter.draw("../images/pyecharts-0.png")
scatter.add("pyecharts", v1, v2, is_random=True)
scatter.render()
```
![pyecharts-1](https://user-images.githubusercontent.com/19553554/35104426-c4ac81ce-fca3-11e7-9b46-7fd729ec3ece.png)


## Scatter3D
Scatter3D.add() signatures
```python
add(name, data, grid3D_opacity=1, **kwargs)
```
* name -> str
    Series name used for displaying in tooltip and filtering with legend,or updaing data and configuration with setOption.

* data -> [[], []]  
    data of line3D

* grid3D_opacity -> float  
    default -> 1  
    opacity of gird3D item

```python
from pyecharts import Scatter3D

import random
data = [[random.randint(0, 100), random.randint(0, 100), random.randint(0, 100)] for _ in range(80)]
range_color = ['#313695', '#4575b4', '#74add1', '#abd9e9', '#e0f3f8', '#ffffbf',
               '#fee090', '#fdae61', '#f46d43', '#d73027', '#a50026']
scatter3D = Scatter3D("3D 散点图示例", width=1200, height=600)
scatter3D.add("", data, is_visualmap=True, visual_range_color=range_color)
scatter3D.render()
```
![scatter3d-demo](https://user-images.githubusercontent.com/19553554/35081974-1ece83ca-fc52-11e7-86d7-bec5c4d3e2c8.gif)

**Note：** more details aboutt gird3D，please refer to [Chart Configuration](en-us/charts_configure)
**Note:** this can be used with axis3D common configuration

## Surface3D
Surface3D.add() signatures
```python
add(name, data,
    grid3d_opacity=1, **kwargs)
```
* name -> str  
    Series name used for displaying in tooltip and filtering with legend,or updaing data and configuration with setOption.

* data -> [list]/ndarray 
    data item，1 row is a data unit，1 column is a field data

* grid3d_opacity -> int  
    default is 1(opacity)

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

**Surface3D wave chart**
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

**Note：** more details aboutt gird3D，please refer to [Chart Configuration](en-us/charts_configure)
**Note:** this can be used with axis3D common configuration

## ThemeRiver
> The ThemeRiver chart is a special flow chart that is mainly used to indicate changes in events or topics over a period of time.

ThemeRiver.add() signatures
```python
add(name, data)
```
* name -> list  
    The chart name must be of type list, and each value in list is the kind of data.

* data -> [list] / [[], []]  
    Data item. In the data, each row is a "data item", and each column belongs to a "dimension". Each data item requires at least three dimensions, such as ['2015/11/08', 10, 'DQ'], respectively [time, value, type (legend name)]

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

**Note：** It can be seen that the third value in each data item is the type of the item, and the type can be specified in the first parameter of `add()`.


## Tree
> The tree chart is mainly used to visualize tree data structure. It is a special hierarchical type with a unique root node, a left subtree, and a right subtree.

Tree.add() signatures
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
    The name of the series, used for the display of the tooltip and filtering the legend.

* data -> list  
    The data of the tree chart is **a tree**, each node includes `value` (optional), `name`, `children` (also tree, optional) as shown below :   
    ```
    [
        {
            value: 1212,    # value
            # child node
            children: [
                {
                    # child node value
                    value: 2323,
                    # child node name
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
    Default -> `"orthogonal"`.   
    The layout of the tree diagram has two types: `orthogonal` and `radial`.   
    The `orthogonal` layout here is what we usually call the horizontal and vertical directions, and the corresponding parameter value is `'orthogonal'`.   
    The `radial` layout refers to the layout where the root node is the center, each layer is a ring, the layers are diverged outward. The corresponding parameter takes the value is `'radial'`. 

* tree_symbol -> str  
    Default -> "emptyCircle"
    Symbol graphics. The types of tags provided by ECharts include 'emptyCircle', 'circle', 'rect', 'roundRect', 'triangle', 'diamond', 'pin', 'arrow', 'none'. 

* tree_symbol_size -> int/list   
    Default -> 7
    The size of the symbol. It can be set to a single number such as 10 or expressed as an array with width and height. For example, [20, 10] means the mark width is 20 and the height is 10. 

* tree_orient -> str   
    Default -> "LR"
    The direction of the orthogonal layout in the tree chart. The configuration item only takes effect when layout = 'orthogonal'.   
    Corresponding to the horizontal direction from left to right, from right to left;  
    The vertical from top to bottom, bottom to top.   
    The values ​​are 'LR', 'RL', 'TB', 'BT'. Note that the previous configuration item value 'horizontal' is equivalent to 'LR' and 'vertical' is equivalent to 'TB'. 

* tree_top -> str   
    Default -> "12%"   
    The distance from the top of the container to the tree component. It can be a specific pixel value like 20, which can be a percentage like '20%' relative to the height and width of the container. 

* tree_left -> str   
    Default -> "12%"   
    The distance from the left of the container to the tree component. It can be a specific pixel value like 20, which can be a percentage like '20%' relative to the height and width of the container. 

* tree_bottom -> str  
    Default -> "12%"
    The distance from the bottom of the container to the tree component. It can be a specific pixel value like 20, which can be a percentage like '20%' relative to the height and width of the container. 

* tree_right -> str  
    Default -> "12%"
    The distance from the right of the container to the tree component. It can be a specific pixel value like 20, which can be a percentage like '20%' relative to the height and width of the container. 

* tree_collapse_interval -> int   
    Default -> 0
    Folding node interval. When the node is too much, it can solve the node display messy interval.

* tree_label_position -> str/list  
    The position of the label. Default is "left"
    ```
    * [x, y]
    The position of the label relative to the upper left corner of the chart bounding box. It is represented by a relative percentage or absolute pixel value. Example:
    // Absolute pixel value
    position: [10, 10],
    // Relative pixel value
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
    The label of parent node is vertically aligned and default is automatic. Optional: 'top', 'middle', 'bottom'

* tree_label_align -> str  
    The label of parent node is horizontally aligned and default is automatic. Optional：'left'，'center'，'right'

* tree_label_text_size -> int  
    The label font size of parent node

* tree_label_rotate -> int   
    Default -> 0
    Rotate the parent node label. From -90 degrees to 90 degrees. Positive values ​​are counterclockwise. 

* tree_leaves_position -> str  
    The distance between the chart elements. Valid when position is a character description value (such as 'top', 'insideRight'). Cooperate with tree_label_position

* tree_leaves_vertical_align -> str  
    The label of leaf node is vertically aligned and default is automatic. Optional: 'top', 'middle', 'bottom'

* tree_leaves_align -> str  
    The label of leaf node is horizontally aligned and default is automatic. Optional：'left'，'center'，'right'

* tree_leaves_text_size -> int  
    The label font size of leaf node

* tree_leaves_rotate -> int  
    Default is 0  
    Rotate the leaf node label. From -90 degrees to 90 degrees. Positive values ​​are counterclockwise. 


**Simple example**

First, suppose you have a data that requires generating tree chart, which is probably like this:  
```

     |----B     |----E----|----I
     |          |
     |----C-----|----F         |----J
A----|                         |
     |----D-----|----G----|----|----K
                |
                |----H
```
You need to write JSON data, the nodes are recursive nesting mode based on {name, children}, as follows:  
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
Generate Tree chart
```python
from pyecharts import Tree

tree = Tree("树图示例")
tree.add("", data)
tree.render()
```
![tree-demo](https://user-images.githubusercontent.com/19553554/44004354-fc603b0a-9e93-11e8-9437-778a1e4a3001.png)

**Use tree_collapse_interva to control node spacing**

When there are too many nodes, the node can be found to display messy intervals. Take the `flare.json` data from offical as an example. When `tree_collapse_interval` is 0 (indicating that all nodes are not collapsed), the text is crowded together.
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

Set tree_collapse_interval equals to 2 (means interval folding nodes), and then looks better
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

**Specify direction, right to left**
```python
tree = Tree(width=1200, height=800)
tree.add("", data, tree_orient="RL", tree_collapse_interval=2)
tree.render()
```
![tree-demo](https://user-images.githubusercontent.com/19553554/44004607-8cd0ff3c-9e97-11e8-97b1-c4bd343ce49c.png)

**Specify direction, from top to bottom**
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

**Specify layout** 
```python
tree = Tree(width=1200, height=800)
tree.add("", data, tree_collapse_interval=2, tree_layout="radial")
tree.render()
```
![tree-demo](https://user-images.githubusercontent.com/19553554/44004643-15e284ee-9e98-11e8-93f6-8103c3af42f4.png)

**Control container layout**
```python
tree = Tree(width=1200, height=800)
tree.add("", data, tree_collapse_interval=2, tree_top="15%", tree_right="20%")
tree.render()
```
![tree-demo](https://user-images.githubusercontent.com/19553554/44004651-399e4ab2-9e98-11e8-93b5-8ab6e9926408.png)


## TreeMap
> A rectangular tree chart is a common form of visualization that expresses "hierarchical data" and "tree data." It mainly uses the area method to highlight the important nodes in each level of the "tree".

TreeMap.add() signatures
```python
add(name, attr, value,
    shape="circle",
    word_gap=20,
    word_size_range=None,
    rotate_step=45)
```
* name -> str  
    chart name

* data -> list  
    The data item of the rectangle tree diagram is **a tree**, each node includes `value`, `name` (optional), `children` (also tree, optional) as shown below :  
    ```
    [
        {
            value: 1212,    # value
            # 子节点
            children: [
                {
                    # child node value
                    value: 2323,
                    # child node name
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
    leafDepth represents "show several layers", and nodes of deeper levels are hidden. With the leafDepth set, the drill down function is turned on. The drill down function displays the sub-levels after clicking. For example, if leafDepth is set to 1, it means that one layer of nodes is displayed.

* treemap_drilldown_icon -> str  
    The prompt when the node can drill down. Can only be characters. Default is '▶'

* treemap_visible_min -> int  
    If the area of ​​a node's rectangle is less than this value (unit: px square), this node is not displayed.

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


## WordCloud
WordCloud.add() signatures
```python
add(name, attr, value, shape="circle", word_gap=20, word_size_range=None, rotate_step=45)
```
* name -> str  
    Series name used for displaying in tooltip and filtering with legend,or updaing data and configuration with setOption.

* attr -> list  
    name of attribute

* value -> list  
    value of attribute

* shape -> list  
    shape of wordcloud.It can be 'circle', 'cardioid', 'diamond', 'triangle-forward', 'triangle', 'pentagon', 'star'

* word_gap -> int  
    default -> 20  
    Gap of word.size of the grid in pixels for marking the availability of the canvas,the larger the grid size, the bigger the gap between words.

* word_size_range -> list  
    default -> [12, 60]  
    Text size range which the value in data will be mapped to.

* rotate_step -> int  
    default -> 45  
    Text rotation range and step in degree. Text will be rotated randomly in range [-90, 90].

```python
from pyecharts import WordCloud

name = ['Sam S Club', 'Macys', 'Amy Schumer', 'Jurassic World', 'Charter Communications',
        'Chick Fil A', 'Planet Fitness', 'Pitch Perfect', 'Express', 'Home', 'Johnny Depp',
        'Lena Dunham', 'Lewis Hamilton', 'KXAN', 'Mary Ellen Mark', 'Farrah Abraham',
        'Rita Ora', 'Serena Williams', 'NCAA baseball tournament', 'Point Break']
value = [10000, 6181, 4386, 4055, 2467, 2244, 1898, 1484, 1112, 965, 847, 582, 555,
         550, 462, 366, 360, 282, 273, 265]
wordcloud = WordCloud(width=1300, height=620)
wordcloud.add("", name, value, word_size_range=[20, 100])
wordcloud.render()
```
![wordcloud-demo](https://user-images.githubusercontent.com/19553554/35081546-cfe57770-fc4f-11e7-878a-e76d274afcbd.png)

```python
wordcloud = WordCloud(width=1300, height=620)
wordcloud.add("", name, value, word_size_range=[30, 100], shape='diamond')
wordcloud.render()
```
![wordcloud-demo](https://user-images.githubusercontent.com/19553554/35081549-d2bde37e-fc4f-11e7-98b2-4cdc019433b1.png)

**Note：** if and only if shape is default 'circle' the rotate_step parameter will take effect.
**If you have read this document, you can read further [Custom Charts](en-us/charts_custom)**
