> Charts Customization : This document is a pyecharts custom chart detail document.

**Basic chart class please refer to [Chart Basic](en-us/charts_base)**


* Custom chart class
    * Grid class : display multiple charts parallel
    * Overlap class : combine different types of chart overlays on the same image
    * Page class : displays multiple images in sequence on the same page 
    * Timeline class : provide timeline carousel multiple images


### Grid : display multiple charts parallel
> Users can customize the combination of Line/Bar/Kline/Scatter/EffectScatter/Pie/HeatMap/Boxplot charts to draw different types of charts on multiple images. The first image needs to be a graph with an x/y axis, that means it cannot be a Pie, and the other positions are in any order.

Grid class usage：
1. Introduce `Grid` class, `from pyecharts import Grid`
2. Instance Grid class，`grid = Grid()`, you can specify `page_title`, `width`, `height`, `jhost` parameters。
3. Use `add()` to add chart to `grid`. You should set one of `grid_top`, `grid_bottom`, `grid_left`, `grid_right` at least. `grid_width` and `grid_height` do not need to be set generally, the default is ok.
4. Use `render()` generate ".html" file.

**Note：** `Overlap` class can be put into the `Grid` class, but there is a premise that `Overlap` cannot be multiple x or y axes, otherwise the axis index confusion will occur.

Other methods in the Grid class：
* `render_embed()`：could be used for rendering in Flask&Django
* `show_config()`：print all config items
* `chart`：chart attribute, return chart instance
* Display the chart directly by calling the Grid instance in the Jupyter-notebook

Grid.add() signature  
```python
add(chart,
    grid_width=None,
    grid_height=None,
    grid_top=None,
    grid_bottom=None,
    grid_left=None,
    grid_right=None)
```
* chart -> chart instance  
    Chart instance.

* grid_width -> str/int   
    default -> adaptive    
    The width of grid component.

* grid_height -> str/int  
    default -> adaptive  
    The height of grid component.

* grid_top -> str/int   
    default -> None    
    The distance of the grid component from the top of the container. There are 'top', 'center', 'middle' optional. It can also be a percentage or an integer.

* grid_bottom -> str/int  
    default -> None    
    The distance of the grid component from the bottom of the container. There are 'top', 'center', 'middle' optional. It can also be a percentage or an integer.

* grid_left -> str/int  
    default -> None    
    The distance of the grid component from the left of the container. There are 'left', 'center', 'right' optional. It can also be a percentage or an integer.

* grid_right -> str/int  
    default -> None    
    The distance of the grid component from the right of the container. There are 'left', 'center', 'right' optional. It can also be a percentage or an integer.


**Up and down type，Bar + Line**
```python
from pyecharts import Bar, Line, Grid

attr = ["衬衫", "羊毛衫", "雪纺衫", "裤子", "高跟鞋", "袜子"]
v1 = [5, 20, 36, 10, 75, 90]
v2 = [10, 25, 8, 60, 20, 80]
bar = Bar("柱状图示例", height=720)
bar.add("商家A", attr, v1, is_stack=True)
bar.add("商家B", attr, v2, is_stack=True)
line = Line("折线图示例", title_top="50%")
attr = ["周一", "周二", "周三", "周四", "周五", "周六", "周日"]
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
    legend_top="50%",
)

grid = Grid()
grid.add(bar, grid_bottom="60%")
grid.add(line, grid_top="60%")
grid.render()
```
![grid-demo](https://user-images.githubusercontent.com/19553554/35089722-c80f84fa-fc72-11e7-93b0-4fff14a371a5.gif)

**Left and right type，Scatter + EffectScatter**
```python
from pyecharts import Scatter, EffectScatter, Grid

v1 = [5, 20, 36, 10, 75, 90]
v2 = [10, 25, 8, 60, 20, 80]
scatter = Scatter(width=1200)
scatter.add("散点图示例", v1, v2, legend_pos="70%")
es = EffectScatter()
es.add(
    "动态散点图示例",
    [11, 11, 15, 13, 12, 13, 10],
    [1, -2, 2, 5, 3, 2, 0],
    effect_scale=6,
    legend_pos="20%",
)

grid = Grid()
grid.add(scatter, grid_left="60%")
grid.add(es, grid_right="60%")
grid.render()
```
![grid-demo](https://user-images.githubusercontent.com/19553554/35089730-ca173c70-fc72-11e7-915e-34ce5c79ead7.gif)

**Up, down, left and right type, Bar + Line + Scatter + EffectScatter**
```python
from pyecharts import Bar, Line, Scatter, EffectScatter, Grid

attr = ["衬衫", "羊毛衫", "雪纺衫", "裤子", "高跟鞋", "袜子"]
v1 = [5, 20, 36, 10, 75, 90]
v2 = [10, 25, 8, 60, 20, 80]
bar = Bar("柱状图示例", title_pos="65%")
bar.add("商家A", attr, v1, is_stack=True)
bar.add("商家B", attr, v2, is_stack=True, legend_pos="80%")
line = Line("折线图示例")
attr = ["周一", "周二", "周三", "周四", "周五", "周六", "周日"]
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
    legend_pos="20%",
)
v1 = [5, 20, 36, 10, 75, 90]
v2 = [10, 25, 8, 60, 20, 80]
scatter = Scatter("散点图示例", title_top="50%", title_pos="65%")
scatter.add("scatter", v1, v2, legend_top="50%", legend_pos="80%")
es = EffectScatter("动态散点图示例", title_top="50%")
es.add(
    "es",
    [11, 11, 15, 13, 12, 13, 10],
    [1, -2, 2, 5, 3, 2, 0],
    effect_scale=6,
    legend_top="50%",
    legend_pos="20%",
)

grid = Grid(height=720, width=1200)
grid.add(bar, grid_bottom="60%", grid_left="60%")
grid.add(line, grid_bottom="60%", grid_right="60%")
grid.add(scatter, grid_top="60%", grid_left="60%")
grid.add(es, grid_top="60%", grid_right="60%")
grid.render()
```
![grid-demo](https://user-images.githubusercontent.com/19553554/35089731-cb044614-fc72-11e7-930c-be269b1f1589.gif)

**Line + Pie**
```python
from pyecharts import Line, Pie, Grid

line = Line("折线图示例")
attr = ["周一", "周二", "周三", "周四", "周五", "周六", "周日"]
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
    legend_pos="20%",
)
attr = ["衬衫", "羊毛衫", "雪纺衫", "裤子", "高跟鞋", "袜子"]
v1 = [11, 12, 13, 10, 10, 10]
pie = Pie("饼图示例", title_pos="55%")
pie.add(
    "",
    attr,
    v1,
    radius=[45, 65],
    center=[65, 50],
    legend_pos="80%",
    legend_orient="vertical",
)

grid = Grid(width=1200)
grid.add(line, grid_right="55%")
grid.add(pie, grid_left="60%")
grid.render()
```
![grid-demo](https://user-images.githubusercontent.com/19553554/35089737-ccc1c01c-fc72-11e7-874d-8ba8b89572eb.png)

**Note：** You can change the position of the Pie chart by setting the `center` parameter, such as [v1, v2], requiring v1 > v2.

**Line + Kline**
```python
from pyecharts import Line, Kline, Grid

line = Line("折线图示例")
attr = ["周一", "周二", "周三", "周四", "周五", "周六", "周日"]
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
    legend_pos="20%",
)
v1 = [
    [2320.26, 2320.26, 2287.3, 2362.94],
    [2300, 2291.3, 2288.26, 2308.38],
    [2295.35, 2346.5, 2295.35, 2345.92],
    [2347.22, 2358.98, 2337.35, 2363.8],
    [2360.75, 2382.48, 2347.89, 2383.76],
    [2383.43, 2385.42, 2371.23, 2391.82],
    [2377.41, 2419.02, 2369.57, 2421.15],
    [2425.92, 2428.15, 2417.58, 2440.38],
    [2411, 2433.13, 2403.3, 2437.42],
    [2432.68, 2334.48, 2427.7, 2441.73],
    [2430.69, 2418.53, 2394.22, 2433.89],
    [2416.62, 2432.4, 2414.4, 2443.03],
    [2441.91, 2421.56, 2418.43, 2444.8],
    [2420.26, 2382.91, 2373.53, 2427.07],
    [2383.49, 2397.18, 2370.61, 2397.94],
    [2378.82, 2325.95, 2309.17, 2378.82],
    [2322.94, 2314.16, 2308.76, 2330.88],
    [2320.62, 2325.82, 2315.01, 2338.78],
    [2313.74, 2293.34, 2289.89, 2340.71],
    [2297.77, 2313.22, 2292.03, 2324.63],
    [2322.32, 2365.59, 2308.92, 2366.16],
    [2364.54, 2359.51, 2330.86, 2369.65],
    [2332.08, 2273.4, 2259.25, 2333.54],
    [2274.81, 2326.31, 2270.1, 2328.14],
    [2333.61, 2347.18, 2321.6, 2351.44],
    [2340.44, 2324.29, 2304.27, 2352.02],
    [2326.42, 2318.61, 2314.59, 2333.67],
    [2314.68, 2310.59, 2296.58, 2320.96],
    [2309.16, 2286.6, 2264.83, 2333.29],
    [2282.17, 2263.97, 2253.25, 2286.33],
    [2255.77, 2270.28, 2253.31, 2276.22],
]
kline = Kline("K 线图示例", title_pos="60%")
kline.add(
    "日K", ["2017/7/{}".format(i + 1) for i in range(31)], v1, legend_pos="80%"
)

grid = Grid(width=1200)
grid.add(line, grid_right="60%")
grid.add(kline, grid_left="55%")
grid.render()
```
![grid-demo](https://user-images.githubusercontent.com/19553554/35089740-ce510c6c-fc72-11e7-84eb-6ae3dddece76.png)

**HeatMap + Bar**
```python
import random

from pyecharts import HeatMap, Bar, Grid

x_axis = [
    "12a", "1a", "2a", "3a", "4a", "5a", "6a",
    "7a", "8a", "9a", "10a", "11a", "12p", "1p",
    "2p", "3p", "4p", "5p", "6p", "7p", "8p", "9p",
    "10p", "11p",
]
y_axis = [
    "Saturday",
    "Friday",
    "Thursday",
    "Wednesday",
    "Tuesday",
    "Monday",
    "Sunday",
]
data = [[i, j, random.randint(0, 50)] for i in range(24) for j in range(7)]
heatmap = HeatMap("热力图示例")
heatmap.add(
    "热力图直角坐标系",
    x_axis,
    y_axis,
    data,
    is_visualmap=True,
    visual_top="45%",
    visual_text_color="#000",
    visual_orient="horizontal",
)
attr = ["衬衫", "羊毛衫", "雪纺衫", "裤子", "高跟鞋", "袜子"]
v1 = [5, 20, 36, 10, 75, 90]
v2 = [10, 25, 8, 60, 20, 80]
bar = Bar("柱状图示例", title_top="52%")
bar.add("商家A", attr, v1, is_stack=True)
bar.add("商家B", attr, v2, is_stack=True, legend_top="50%")

grid = Grid(height=700)
grid.add(heatmap, grid_bottom="60%")
grid.add(bar, grid_top="60%")
grid.render()
```
![grid-demo](https://user-images.githubusercontent.com/19553554/35089741-cfca19bc-fc72-11e7-8c3b-2f20d054d3fc.gif)  
Bar is affected by HeatMap, very interesting.

**Use Grid to solve dataZoom overlapping with X-axis labels problem**
```python
from pyecharts imoprt Bar, Grid

x = [
    "名字很长的x轴1",
    "名字很长的x轴2",
    "名字很长的x轴3",
    "名字很长的x轴4",
    "名字很长的x轴5",
    "名字很长的x轴6",
    "名字很长的x轴7",
    "名字很长的x轴8",
    "名字很长的x轴9",
]
y = [10, 20, 30, 40, 50, 60, 70, 80, 90]

grid = Grid()
bar = Bar("利用 Grid 解决 dataZoom 与 X 轴标签重叠问题")
bar.add("", x, y, is_datazoom_show=True, xaxis_interval=0, xaxis_rotate=30)
# Add bar to the grid and adjust the grid_bottom parameter appropriately to move the bar chart up
grid.add(bar, grid_bottom="25%")
grid.render()
```
![grid-demo](https://user-images.githubusercontent.com/19553554/43446550-c3756fde-94db-11e8-81fd-b7c202306858.gif)

**datazoom component controls multiple charts simultaneously**
```python
from pyecharts import Line, Kline, Grid

line = Line("折线图示例")
attr = ["周一", "周二", "周三", "周四", "周五", "周六", "周日"]
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
    legend_top="50%",
    mark_line=["average"],
    # set dataZoom control index to [0,1], which means the first and second x axis
    is_datazoom_show=True,
    datazoom_xaxis_index=[0, 1],
)

v1 = [
    [2320.26, 2320.26, 2287.3, 2362.94],
    [2300, 2291.3, 2288.26, 2308.38],
    [2295.35, 2346.5, 2295.35, 2345.92],
    [2347.22, 2358.98, 2337.35, 2363.8],
    [2360.75, 2382.48, 2347.89, 2383.76],
    [2383.43, 2385.42, 2371.23, 2391.82],
    [2377.41, 2419.02, 2369.57, 2421.15],
    [2425.92, 2428.15, 2417.58, 2440.38],
    [2411, 2433.13, 2403.3, 2437.42],
    [2432.68, 2334.48, 2427.7, 2441.73],
    [2430.69, 2418.53, 2394.22, 2433.89],
    [2416.62, 2432.4, 2414.4, 2443.03],
    [2441.91, 2421.56, 2418.43, 2444.8],
    [2420.26, 2382.91, 2373.53, 2427.07],
    [2383.49, 2397.18, 2370.61, 2397.94],
    [2378.82, 2325.95, 2309.17, 2378.82],
    [2322.94, 2314.16, 2308.76, 2330.88],
    [2320.62, 2325.82, 2315.01, 2338.78],
    [2313.74, 2293.34, 2289.89, 2340.71],
    [2297.77, 2313.22, 2292.03, 2324.63],
    [2322.32, 2365.59, 2308.92, 2366.16],
    [2364.54, 2359.51, 2330.86, 2369.65],
    [2332.08, 2273.4, 2259.25, 2333.54],
    [2274.81, 2326.31, 2270.1, 2328.14],
    [2333.61, 2347.18, 2321.6, 2351.44],
    [2340.44, 2324.29, 2304.27, 2352.02],
    [2326.42, 2318.61, 2314.59, 2333.67],
    [2314.68, 2310.59, 2296.58, 2320.96],
    [2309.16, 2286.6, 2264.83, 2333.29],
    [2282.17, 2263.97, 2253.25, 2286.33],
    [2255.77, 2270.28, 2253.31, 2276.22],
]
kline = Kline("K 线图示例", title_top="50%")
kline.add(
    "日K",
    ["2017/7/{}".format(i + 1) for i in range(31)],
    v1,
    is_datazoom_show=True,
)

grid = Grid(width=1200, height=700)
grid.add(line, grid_top="60%")
grid.add(kline, grid_bottom="60%")
grid.render()
```
![grid-demo](https://user-images.githubusercontent.com/19553554/35089743-d13a3502-fc72-11e7-9c6a-21aeb7415c2b.gif)  

**Reflected coordinate system**
```python
from pyecharts import Line, Grid

import random

attr = ["{}天".format(i) for i in range(1, 31)]
line_top = Line("折线图示例")
line_top.add(
    "最高气温",
    attr,
    [random.randint(20, 100) for i in range(30)],
    mark_point=["max", "min"],
    mark_line=["average"],
    legend_pos="38%",
)
line_bottom = Line()
line_bottom.add(
    "最低气温",
    attr,
    [random.randint(20, 100) for i in range(30)],
    mark_point=["max", "min"],
    mark_line=["average"],
    is_yaxis_inverse=True,
    xaxis_pos="top",
)

grid = Grid(width=1200, height=700)
grid.add(line_top, grid_bottom="60%")
grid.add(line_bottom, grid_top="50%")
grid.render()
```
![grid-demo](https://user-images.githubusercontent.com/19553554/35089748-d2952178-fc72-11e7-9e1f-105733f793b9.gif)  

**Grid + Overlap**
```python
from pyecharts import Overlap, Bar, Line, Grid

grid = Grid()

attr = ["{}月".format(i) for i in range(1, 13)]
v1 = [2.0, 4.9, 7.0, 23.2, 25.6, 76.7, 135.6, 162.2, 32.6, 20.0, 6.4, 3.3]
v2 = [2.6, 5.9, 9.0, 26.4, 28.7, 70.7, 175.6, 182.2, 48.7, 18.8, 6.0, 2.3]
v3 = [2.0, 2.2, 3.3, 4.5, 6.3, 10.2, 20.3, 23.4, 23.0, 16.5, 12.0, 6.2]

bar = Bar(title="Overlap+Grid 示例", title_pos="40%")
bar.add("蒸发量", attr, v1)
bar.add(
    "降水量",
    attr,
    v2,
    yaxis_formatter=" ml",
    yaxis_max=250,
    legend_pos="85%",
    legend_orient="vertical",
    legend_top="45%",
)
line = Line()
line.add("平均温度", attr, v3, yaxis_formatter=" °C")
overlap = Overlap(width=1200, height=600)
overlap.add(bar)
overlap.add(line, is_add_yaxis=True, yaxis_index=1)

grid.add(overlap, grid_right="20%")
grid.render()
```
![grid-demo](https://user-images.githubusercontent.com/19553554/35089754-d62726c4-fc72-11e7-836b-c8cd597e2b71.png)  

**Note：** Put `Overlap` in `Grid` that can adjust the layout with its grid. For example, the above chart will put the legend on the right. This is useful when the legend name is too long.


### Overlap : Combine different types of charts overlay on the same image
> Users can customize the Line/Bar/Kline, Scatter/EffectScatter charts to draw different types of charts on a single chart. Based on the first chart, the next data will be drawn on the first chart.   

Overlap class usage：
1. Introduce `Overlap` class, `from pyecharts import Overlap`;
2. Instance `Overlap` class, `overlap = Overlap()`, you can specify `page_title`, `width`, `height`, `jhost` parameters;
3. Use `add()` to add charts to `overlap`;
4. Use `render()` generate ".html" file.

Overlap.add() signature    
```python
add(chart,
    xaxis_index=0,
    yaxis_index=0,
    is_add_xaxis=False,
    is_add_yaxis=False)
```
* chart -> chart instance  
    Chart instance

* xaxis_index -> int  
    default -> 0  
    x axis index

* yaxis_index -> int  
    default -> 0  
    y axis index

* is_add_xaxis -> bool  
    default -> False  
    Whether to add an x ​​axis

* is_add_yaxis -> bool  
    default -> False  
    Whether to add a y axis

Other methods in the Overlap class:
* `render_embed()` : use this method to render in Flask&Django
* `show_config()` : print all config items
* `chart` : return chart instance
* Display the chart in Jupyter-notebook by calling the Overlap instance directly

**Line + Bar**
```python
from pyecharts import Bar, Line, Overlap

attr = ['A', 'B', 'C', 'D', 'E', 'F']
v1 = [10, 20, 30, 40, 50, 60]
v2 = [38, 28, 58, 48, 78, 68]
bar = Bar("Line - Bar 示例")
bar.add("bar", attr, v1)
line = Line()
line.add("line", attr, v2)

overlap = Overlap()
overlap.add(bar)
overlap.add(line)
overlap.render()
```
![overlap-demo](https://user-images.githubusercontent.com/19553554/35090251-0b4c6390-fc74-11e7-829c-079c9cd8c3e5.gif)

**Scatter + EffectScatter**
```python
from pyecharts import Scatter, EffectScatter, Overlap

v1 = [10, 20, 30, 40, 50, 60]
v2 = [30, 30, 30, 30, 30, 30]
v3 = [50, 50, 50, 50, 50, 50]
v4 = [10, 10, 10, 10, 10, 10]
es = EffectScatter("Scatter - EffectScatter 示例")
es.add("es", v1, v2)
scatter = Scatter()
scatter.add("scatter", v1, v3)
es_1 = EffectScatter()
es_1.add("es_1", v1, v4, symbol='pin', effect_scale=5)

overlap = Overlap()
overlap.add(es)
overlap.add(scatter)
overlap.add(es_1)
overlap.render()
```
![overlap-demo](https://user-images.githubusercontent.com/19553554/35090256-0c49bf54-fc74-11e7-9422-da3296f842e4.gif)

**Kline + Line**
```python
import random
from pyecharts import Line, Kline, Overlap

v1 = [[2320.26, 2320.26, 2287.3, 2362.94],
      [2300, 2291.3, 2288.26, 2308.38],
      [2295.35, 2346.5, 2295.35, 2345.92],
      [2347.22, 2358.98, 2337.35, 2363.8],
      [2360.75, 2382.48, 2347.89, 2383.76],
      [2383.43, 2385.42, 2371.23, 2391.82],
      [2377.41, 2419.02, 2369.57, 2421.15],
      [2425.92, 2428.15, 2417.58, 2440.38],
      [2411, 2433.13, 2403.3, 2437.42],
      [2432.68, 2334.48, 2427.7, 2441.73],
      [2430.69, 2418.53, 2394.22, 2433.89],
      [2416.62, 2432.4, 2414.4, 2443.03],
      [2441.91, 2421.56, 2418.43, 2444.8],
      [2420.26, 2382.91, 2373.53, 2427.07],
      [2383.49, 2397.18, 2370.61, 2397.94],
      [2378.82, 2325.95, 2309.17, 2378.82],
      [2322.94, 2314.16, 2308.76, 2330.88],
      [2320.62, 2325.82, 2315.01, 2338.78],
      [2313.74, 2293.34, 2289.89, 2340.71],
      [2297.77, 2313.22, 2292.03, 2324.63],
      [2322.32, 2365.59, 2308.92, 2366.16],
      [2364.54, 2359.51, 2330.86, 2369.65],
      [2332.08, 2273.4, 2259.25, 2333.54],
      [2274.81, 2326.31, 2270.1, 2328.14],
      [2333.61, 2347.18, 2321.6, 2351.44],
      [2340.44, 2324.29, 2304.27, 2352.02],
      [2326.42, 2318.61, 2314.59, 2333.67],
      [2314.68, 2310.59, 2296.58, 2320.96],
      [2309.16, 2286.6, 2264.83, 2333.29],
      [2282.17, 2263.97, 2253.25, 2286.33],
      [2255.77, 2270.28, 2253.31, 2276.22]]
attr = ["2017/7/{}".format(i + 1) for i in range(31)]
kline = Kline("Kline - Line 示例")
kline.add("日K", attr, v1)
line_1 = Line()
line_1.add("line-1", attr, [random.randint(2400, 2500) for _ in range(31)])
line_2 = Line()
line_2.add("line-2", attr, [random.randint(2400, 2500) for _ in range(31)])

overlap = Overlap()
overlap.add(kline)
overlap.add(line_1)
overlap.add(line_2)
overlap.render()
```
![overlap-demo](https://user-images.githubusercontent.com/19553554/35090261-0e00e804-fc74-11e7-9cae-213f7ea73bd9.png)

**Line + EffectScatter**
```python
from pyecharts import Line, EffectScatter, Overlap

attr = ["衬衫", "羊毛衫", "雪纺衫", "裤子", "高跟鞋", "袜子"]
v1 = [5, 20, 36, 10, 10, 100]
line = Line("line - es 示例")
line.add("", attr, v1, is_random=True)
es = EffectScatter()
es.add("", attr, v1, effect_scale=8)

overlap = Overlap()
overlap.add(line)
overlap.add(es)
overlap.render()
```
![overlap-demo](https://user-images.githubusercontent.com/19553554/35090267-10e673fe-fc74-11e7-981d-7c9db110fbfb.gif)

**If you want to change the axis index to have more X or more Y axes. Please look below**
```python
from pyecharts import Line, Bar, Overlap

attr = ["{}月".format(i) for i in range(1, 13)]
v1 = [2.0, 4.9, 7.0, 23.2, 25.6, 76.7, 135.6, 162.2, 32.6, 20.0, 6.4, 3.3]
v2 = [2.6, 5.9, 9.0, 26.4, 28.7, 70.7, 175.6, 182.2, 48.7, 18.8, 6.0, 2.3]
v3 = [2.0, 2.2, 3.3, 4.5, 6.3, 10.2, 20.3, 23.4, 23.0, 16.5, 12.0, 6.2]

bar = Bar()
bar.add("蒸发量", attr, v1)
bar.add("降水量", attr, v2, yaxis_formatter=" ml",
        yaxis_interval=50, yaxis_max=250)

line = Line()
line.add("平均温度", attr, v3, yaxis_formatter=" °C", yaxis_interval=5)

overlap = Overlap(width=1200, height=600)
# The x y axis is not added by default, and the index of the x y axis is 0.
overlap.add(bar)
# Add a y axis, the number of y axes is 2, and the index of the second y axis is 1 (index starts from 0). So set yaxis_index = 1
# Since the same x-axis is used, it does not need to change the x-axis part.
overlap.add(line, yaxis_index=1, is_add_yaxis=True)
overlap.render()
```
![overlap-demo](https://user-images.githubusercontent.com/19553554/35090266-0f7d7d96-fc74-11e7-9851-d56777b4114d.gif)

**Note：** For double Y-axis alignment, you can use the `yaxis_force_interval` parameter to split into the same number of scales. Here's a trick to set the y-axis maximum first. For example, if the double y axis has a maximum of 700 and a maximum of 400. Then you can set the two `yaxis_force_interval` parameters to 140 and 80 respectively, and they will all be divided into 5 equals.  

If you just want to display the charts in order in a ".html" file, it is recommended to use the ```Page()``` class.  


### Page : displays multiple charts in sequence on the same page
> Grid/Timeline/Overlap can be displayed normally in Page. You can add them as a chart to Page.

Page class usage：
1. Introduce `Page` class, `from pyecharts import Page`
2. Instance `Page` class, `page = Page()`, you can specify `page_title`, `jhost` parameters.
3. Use `add()` to add charts to `page`. It can be a single chart instance or a list of chart instances.
4. Use `render()` to generate ".html" file.

Other methods in Page class:
* `render_embed()` : this method can be used to render in Flask&Django
* `show_config()` : print all config items
* `chart`：return the chart instance
* Display the chart in Jupyter-notebook by calling the Page instance directly

```python
#coding=utf-8
from __future__ import unicode_literals

from pyecharts import Bar, Scatter3D
from pyecharts import Page


page = Page()         # step 1

# bar
attr = ["衬衫", "羊毛衫", "雪纺衫", "裤子", "高跟鞋", "袜子"]
v1 = [5, 20, 36, 10, 75, 90]
v2 = [10, 25, 8, 60, 20, 80]
bar = Bar("柱状图数据堆叠示例")
bar.add("商家A", attr, v1, is_stack=True)
bar.add("商家B", attr, v2, is_stack=True)
page.add(bar)         # step 2

# scatter3D
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
page.add(scatter3D)  # step 2

page.render()        # step 3
```
After running, you will find that render.html has shown two charts in order:

![page-demo](https://user-images.githubusercontent.com/19553554/35104303-658f9654-fca3-11e7-9a05-5e2e13d1a4c4.gif)

**Of course, more charts are also possible.**
```python
#coding=utf-8
from __future__ import unicode_literals

from pyecharts import Line, Pie, Kline, Radar
from pyecharts import Page


page = Page()

# line
attr = ['周一', '周二', '周三', '周四', '周五', '周六', '周日']
line = Line("折线图示例")
line.add("最高气温", attr, [11, 11, 15, 13, 12, 13, 10],
         mark_point=["max", "min"], mark_line=["average"])
line.add("最低气温", attr, [1, -2, 2, 5, 3, 2, 0],
         mark_point=["max", "min"], mark_line=["average"])
page.add(line)

# pie
attr = ["衬衫", "羊毛衫", "雪纺衫", "裤子", "高跟鞋", "袜子"]
v1 = [11, 12, 13, 10, 10, 10]
pie = Pie("饼图-圆环图示例", title_pos='center')
pie.add("", attr, v1, radius=[40, 75], label_text_color=None,
        is_label_show=True, legend_orient='vertical', legend_pos='left')
page.add(pie)

# kline
v1 = [[2320.26, 2320.26, 2287.3, 2362.94],
      [2300, 2291.3, 2288.26, 2308.38],
      [2295.35, 2346.5, 2295.35, 2345.92],
      [2347.22, 2358.98, 2337.35, 2363.8],
      [2360.75, 2382.48, 2347.89, 2383.76],
      [2383.43, 2385.42, 2371.23, 2391.82],
      [2377.41, 2419.02, 2369.57, 2421.15],
      [2425.92, 2428.15, 2417.58, 2440.38],
      [2411, 2433.13, 2403.3, 2437.42],
      [2432.68, 2334.48, 2427.7, 2441.73],
      [2430.69, 2418.53, 2394.22, 2433.89],
      [2416.62, 2432.4, 2414.4, 2443.03],
      [2441.91, 2421.56, 2418.43, 2444.8],
      [2420.26, 2382.91, 2373.53, 2427.07],
      [2383.49, 2397.18, 2370.61, 2397.94],
      [2378.82, 2325.95, 2309.17, 2378.82],
      [2322.94, 2314.16, 2308.76, 2330.88],
      [2320.62, 2325.82, 2315.01, 2338.78],
      [2313.74, 2293.34, 2289.89, 2340.71],
      [2297.77, 2313.22, 2292.03, 2324.63],
      [2322.32, 2365.59, 2308.92, 2366.16],
      [2364.54, 2359.51, 2330.86, 2369.65],
      [2332.08, 2273.4, 2259.25, 2333.54],
      [2274.81, 2326.31, 2270.1, 2328.14],
      [2333.61, 2347.18, 2321.6, 2351.44],
      [2340.44, 2324.29, 2304.27, 2352.02],
      [2326.42, 2318.61, 2314.59, 2333.67],
      [2314.68, 2310.59, 2296.58, 2320.96],
      [2309.16, 2286.6, 2264.83, 2333.29],
      [2282.17, 2263.97, 2253.25, 2286.33],
      [2255.77, 2270.28, 2253.31, 2276.22]]
kline = Kline("K 线图示例")
kline.add("日K", ["2017/7/{}".format(i + 1) for i in range(31)], v1)
page.add(kline)

# radar
schema = [
    ("销售", 6500), ("管理", 16000), ("信息技术", 30000),
    ("客服", 38000), ("研发", 52000), ("市场", 25000)
]
v1 = [[4300, 10000, 28000, 35000, 50000, 19000]]
v2 = [[5000, 14000, 28000, 31000, 42000, 21000]]
radar = Radar("雷达图示例")
radar.config(schema)
radar.add("预算分配", v1, is_splitline=True, is_axisline_show=True)
radar.add("实际开销", v2, label_color=["#4e79a7"], is_area_show=False,
          legend_selectedmode='single')
page.add(radar)

page.render()
```
![page-demo](https://user-images.githubusercontent.com/19553554/35104305-66f2a766-fca3-11e7-8ffd-8e85911fdea5.gif)

**Additional text labels of the Page class, carried by the charts themselves**
```python
from pyecharts import *

page = Page()
line = Line("折线图示例", extra_html_text_label=["LINE TEXT LABEL", "color:red"])
line.add(
    "最高气温",
    WEEK,
    [11, 11, 15, 13, 12, 13, 10],
    mark_point=["max", "min"],
    mark_line=["average"],
)
page.add(line)

v1 = [11, 12, 13, 10, 10, 10]
pie = Pie("饼图-圆环图示例", title_pos="center", extra_html_text_label=["PIE TEXT LABEL"])
pie.add(
    "",
    CLOTHES,
    v1,
    radius=[40, 75],
    label_text_color=None,
    is_label_show=True,
    legend_orient="vertical",
    legend_pos="left",
)
page.add(pie)

v2 = [10, 25, 8, 60, 20, 80]
bar = Bar("柱状图", extra_html_text_label=["BAR TEXT LABEL"])
bar.add("商家B", CLOTHES, v2)
page.add(bar)
page.render()
```
![page-demo](https://user-images.githubusercontent.com/19553554/44133457-71fb6448-a092-11e8-88b4-78e5c5d3b48e.png)


### Timeline：provide timeline carousel multiple images
Timeline class usage :  
1. Introduce `Timeline` class, `from pyecharts import Timeline`
2. Instance `Timeline` class
3. Use `add()` to add charts to `timeline`. For example, `add(bar, '2013')` accepts two parameters, the first is the chart instance and the second is the "time point" of the timeline.
4. Use `render()` to generate ".html" file

You can set parameters when instance the Timeline class:

* page_title -> str  
    default -> 'Echarts'  
    Generates the value of the `<title>` tag of the html file

* width -> int  
    default -> 800  
    Canvas width.

* height -> int  
    default -> 400  
    Canvas height

* jhost -> str  
    Customize the JavaScript host for each instance

* is_auto_play -> bool  
    default -> Flase  
    Whether to play automatically

* is_loop_play -> bool  
    default -> True  
    Whether to loop

* is_rewind_play -> bool  
    default is Flase  
    Whether to play backwards

* is_timeline_show -> bool  
    default -> True  
    Whether to display the timeline component. If set to false, it will not be displayed, but the function still exists.

* timeline_play_interval -> int  
    The speed of play (the interval of the jitter) in milliseconds (ms).

* timeline_symbol -> str  
    The symbol graphic type. ECharts provide the graphic type including 'circle', 'rect', 'roundRect', 'triangle', 'diamond', 'pin', 'arrow'

* timeline_symbol_size -> int/list  
    The size of the marked graphic can be set to a single number such as 10. Or it can be separated by an array to indicate the width and height. For example, [20, 10] means that the mark width is 20 and the height is 10.

* timeline_left -> int/str  
    The distance of the timeline component from the left side of the container.   
    The value of `left` can be a specific pixel value like 20. Or it can be a percentage like '20%' relative to the height and width of the container. Or it can be 'left', 'center', 'right'.   
    If the value of left is 'left', 'center', 'right', the component will automatically align according to the corresponding position.  

* timeline_right -> int/str  
    The distance of the timeline component from the right side of the container.  
    Value setting is the same as timeline_left

* timeline_top -> int/str  
    The distance of the timeline component from the top side of the container.  
    Value setting is the same as timeline_left  

* timeline_bottom -> int/str  
    The distance of the timeline component from the bottom side of the container.  
    Value setting is the same as timeline_left

Other methods in Timeline class :   
* `render_embed()`：this method can be used to render in Flask&Django  
* `show_config()`：print all config items
* `chart`：return chart instance
* Timeline have a problem in Jupyter-notebook (the animation cannot be displayed properly)

```python
from pyecharts import Bar, Timeline

attr = ["衬衫", "羊毛衫", "雪纺衫", "裤子", "高跟鞋", "袜子"]
bar_1 = Bar("2012 年销量", "数据纯属虚构")
bar_1.add("春季", attr, [randint(10, 100) for _ in range(6)])
bar_1.add("夏季", attr, [randint(10, 100) for _ in range(6)])
bar_1.add("秋季", attr, [randint(10, 100) for _ in range(6)])
bar_1.add("冬季", attr, [randint(10, 100) for _ in range(6)])

bar_2 = Bar("2013 年销量", "数据纯属虚构")
bar_2.add("春季", attr, [randint(10, 100) for _ in range(6)])
bar_2.add("夏季", attr, [randint(10, 100) for _ in range(6)])
bar_2.add("秋季", attr, [randint(10, 100) for _ in range(6)])
bar_2.add("冬季", attr, [randint(10, 100) for _ in range(6)])

bar_3 = Bar("2014 年销量", "数据纯属虚构")
bar_3.add("春季", attr, [randint(10, 100) for _ in range(6)])
bar_3.add("夏季", attr, [randint(10, 100) for _ in range(6)])
bar_3.add("秋季", attr, [randint(10, 100) for _ in range(6)])
bar_3.add("冬季", attr, [randint(10, 100) for _ in range(6)])

bar_4 = Bar("2015 年销量", "数据纯属虚构")
bar_4.add("春季", attr, [randint(10, 100) for _ in range(6)])
bar_4.add("夏季", attr, [randint(10, 100) for _ in range(6)])
bar_4.add("秋季", attr, [randint(10, 100) for _ in range(6)])
bar_4.add("冬季", attr, [randint(10, 100) for _ in range(6)])

bar_5 = Bar("2016 年销量", "数据纯属虚构")
bar_5.add("春季", attr, [randint(10, 100) for _ in range(6)])
bar_5.add("夏季", attr, [randint(10, 100) for _ in range(6)])
bar_5.add("秋季", attr, [randint(10, 100) for _ in range(6)])
bar_5.add("冬季", attr, [randint(10, 100) for _ in range(6)], is_legend_show=True)

timeline = Timeline(is_auto_play=True, timeline_bottom=0)
timeline.add(bar_1, '2012 年')
timeline.add(bar_2, '2013 年')
timeline.add(bar_3, '2014 年')
timeline.add(bar_4, '2015 年')
timeline.add(bar_5, '2016 年')
timeline.render()
```
![timeline-demo](https://user-images.githubusercontent.com/19553554/35082279-e111743c-fc53-11e7-9362-580160593715.gif)

```python
from pyecharts import Pie, Timeline

attr = ["衬衫", "羊毛衫", "雪纺衫", "裤子", "高跟鞋", "袜子"]
pie_1 = Pie("2012 年销量比例", "数据纯属虚构")
pie_1.add(
    "秋季",
    attr,
    [randint(10, 100) for _ in range(6)],
    is_label_show=True,
    radius=[30, 55],
    rosetype="radius",
)

pie_2 = Pie("2013 年销量比例", "数据纯属虚构")
pie_2.add(
    "秋季",
    attr,
    [randint(10, 100) for _ in range(6)],
    is_label_show=True,
    radius=[30, 55],
    rosetype="radius",
)

pie_3 = Pie("2014 年销量比例", "数据纯属虚构")
pie_3.add(
    "秋季",
    attr,
    [randint(10, 100) for _ in range(6)],
    is_label_show=True,
    radius=[30, 55],
    rosetype="radius",
)

pie_4 = Pie("2015 年销量比例", "数据纯属虚构")
pie_4.add(
    "秋季",
    attr,
    [randint(10, 100) for _ in range(6)],
    is_label_show=True,
    radius=[30, 55],
    rosetype="radius",
)

pie_5 = Pie("2016 年销量比例", "数据纯属虚构")
pie_5.add(
    "秋季",
    attr,
    [randint(10, 100) for _ in range(6)],
    is_label_show=True,
    radius=[30, 55],
    rosetype="radius",
)

timeline = Timeline(is_auto_play=True, timeline_bottom=0)
timeline.add(pie_1, '2012 年')
timeline.add(pie_2, '2013 年')
timeline.add(pie_3, '2014 年')
timeline.add(pie_4, '2015 年')
timeline.add(pie_5, '2016 年')
timeline.render()
```
![timeline-demo](https://user-images.githubusercontent.com/19553554/35082282-e517c842-fc53-11e7-8727-0e53686c3703.gif)

```python
from pyecharts import Bar, Line, Timeline, Overlap

attr = ["{}月".format(i) for i in range(1, 7)]
bar = Bar("1 月份数据", "数据纯属虚构")
bar.add("bar", attr, [randint(10, 50) for _ in range(6)])
line = Line()
line.add("line", attr, [randint(50, 80) for _ in range(6)])
overlap = Overlap()
overlap.add(bar)
overlap.add(line)

bar_1 = Bar("2 月份数据", "数据纯属虚构")
bar_1.add("bar", attr, [randint(10, 50) for _ in range(6)])
line_1 = Line()
line_1.add("line", attr, [randint(50, 80) for _ in range(6)])
overlap_1 = Overlap()
overlap_1.add(bar_1)
overlap_1.add(line_1)

bar_2 = Bar("3 月份数据", "数据纯属虚构")
bar_2.add("bar", attr, [randint(10, 50) for _ in range(6)])
line_2 = Line()
line_2.add("line", attr, [randint(50, 80) for _ in range(6)])
overlap_2 = Overlap()
overlap_2.add(bar_2)
overlap_2.add(line_2)

bar_3 = Bar("4 月份数据", "数据纯属虚构")
bar_3.add("bar", attr, [randint(10, 50) for _ in range(6)])
line_3 = Line()
line_3.add("line", attr, [randint(50, 80) for _ in range(6)])
overlap_3 = Overlap()
overlap_3.add(bar_3)
overlap_3.add(line_3)

bar_4 = Bar("5 月份数据", "数据纯属虚构")
bar_4.add("bar", attr, [randint(10, 50) for _ in range(6)])
line_4 = Line()
line_4.add("line", attr, [randint(50, 80) for _ in range(6)])
overlap_4 = Overlap()
overlap_4.add(bar_4)
overlap_4.add(line_4)

timeline = Timeline(timeline_bottom=0)
timeline.add(overlap.chart, '1 月')
timeline.add(overlap_1.chart, '2 月')
timeline.add(overlap_2.chart, '3 月')
timeline.add(overlap_3.chart, '4 月')
timeline.add(overlap_4.chart, '5 月')
timeline.render()
```
![timeline-demo](https://user-images.githubusercontent.com/19553554/35082284-e704cfa6-fc53-11e7-8790-f92eb6b2315f.gif)

**If you have read this document, read further [Advanced Topics](en-us/advanced)**
