> 自定义图表篇：本篇文档为 pyecharts 自定义图表详情文档，介绍了关于 pyecharts 各类自定义图表的细节。

**基本图表类请参考 [基本图表类篇](zh-cn/charts_base)**


* 自定义图表类
    * Grid 类：并行显示多张图
    * Overlap 类：结合不同类型图表叠加画在同张图上
    * Page 类：同一网页按顺序展示多图
    * Timeline 类：提供时间线轮播多张图


## Grid：并行显示多张图
> 用户可以自定义结合 Line/Bar/Kline/Scatter/EffectScatter/Pie/HeatMap/Boxplot 图表，将不同类型图表画在多张图上。第一个图需为 有 x/y 轴的图，即不能为 Pie，其他位置顺序任意。

Grid 类的使用：
1. 引入 `Grid` 类，`from pyecharts import Grid`
2. 实例化 Grid 类，`grid = Grid()` ，可指定 `page_title`, `width`, `height`, `jhost` 参数。
3. 使用 `add()` 向 `grid` 中添加图，至少需要设置一个 `grid_top`, `grid_bottom`, `grid_left`, `grid_right` 四个参数中的一个。`grid_width` 和 `grid_height` 一般不用设置，默认即可。
4. 使用 `render()` 渲染生成 .html 文件

**Note：** `Overlap` 类可放入 `Grid` 类中，不过有个前提，`Overlap` 不可为多 x 轴或者多 y 轴，否则会出现坐标轴索引混乱问题

Grid 类中其他方法：
* `render_embed()`：在 Flask&Django 中可以使用该方法渲染
* `show_config()`：打印输出所有配置项
* `chart`：chart 属性返回图形实例
* 在 Jupyter-notebook 中直接调用 Grid 实例即可显示图表

Grid.add() 方法签名 
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
    图表实例
* grid_width -> str/int  
    grid 组件的宽度。默认自适应。
* grid_height -> str/int  
    grid 组件的高度。默认自适应。
* grid_top -> str/int  
    grid 组件离容器顶部的距离。默认为 None, 有'top', 'center', 'middle'可选，也可以为百分数或者整数
* grid_bottom -> str/int  
    grid 组件离容器底部的距离。默认为 None, 有'top', 'center', 'middle'可选，也可以为百分数或者整数
* grid_left -> str/int  
    grid 组件离容器左侧的距离。默认为 None, 有'left', 'center', 'right'可选，也可以为百分数或者整数
* grid_right -> str/int  
    grid 组件离容器右侧的距离。默认为 None, 有'left', 'center', 'right'可选，也可以为百分数或者整数


**上下类型，Bar + Line**
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

**左右类型，Scatter + EffectScatter**
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

**上下左右类型，Bar + Line + Scatter + EffectScatter**
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

**Note：** 可以通过设置 center 参数改变 Pie 图的位置，如 [v1, v2]， 要求 v1 > v2。

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
Bar 会受 HeatMap 影响，很有趣。

**利用 Grid 解决 dataZoom 与 X 轴标签重叠问题**
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
# 把 bar 加入到 grid 中，并适当调整 grid_bottom 参数，使 bar 图整体上移
grid.add(bar, grid_bottom="25%")
grid.render()
```
![grid-demo](https://user-images.githubusercontent.com/19553554/43446550-c3756fde-94db-11e8-81fd-b7c202306858.gif)

**datazoom 组件同时控制多个图**
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
    # 设置 dataZoom 控制索引为 0,1 的 x 轴，即第一个和第二个
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

**倒映直角坐标系**
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

**Note：** `Overlap` 放入 `Grid` 可以利用其 grid 网格调整布局，例如上图将图例放在右边，这种情况在**图例名字过长**时很有用。


## Overlap：结合不同类型图表叠加画在同张图上
> 用户可以自定义结合 Line/Bar/Kline, Scatter/EffectScatter 图表，将不同类型图表画在一张图上。利用第一个图表为基础，往后的数据都将会画在第一个图表上。   
Overlap 类的使用：
1. 引入 `Overlap` 类，`from pyecharts import Overlap`
2. 实例化 `Overlap` 类，`overlap = Overlap()`  ，可指定 `page_title`, `width`, `height`, `jhost` 参数。
3. 使用 `add()` 向 `overlap` 中添加图
4. 使用 `render()` 渲染生成 .html 文件

Overlap.add() 方法签名  
```python
add(chart,
    xaxis_index=0,
    yaxis_index=0,
    is_add_xaxis=False,
    is_add_yaxis=False)
```
* chart -> chart instance  
    图表示例
* xaxis_index -> int  
    x 坐标轴索引，默认为 0
* yaxis_index -> int  
    y 坐标轴索引，默认为 0
* is_add_xaxis -> bool  
    是否新增一个 x 坐标轴，默认为 False
* is_add_yaxis -> bool  
    是否新增一个 y 坐标轴，默认为 False

Overlap 类中其他方法：
* `render_embed()`：在 Flask&Django 中可以使用该方法渲染
* `show_config()`：打印输出所有配置项
* `chart`：返回图形实例
* 在 Jupyter-notebook 中直接调用 Overlap 实例即可显示图表

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

**如果想改变轴索引，使其有多 X 轴或者多 Y 轴的话。请看下面**
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
# 默认不新增 x y 轴，并且 x y 轴的索引都为 0
overlap.add(bar)
# 新增一个 y 轴，此时 y 轴的数量为 2，第二个 y 轴的索引为 1（索引从 0 开始），所以设置 yaxis_index = 1
# 由于使用的是同一个 x 轴，所以 x 轴部分不用做出改变
overlap.add(line, yaxis_index=1, is_add_yaxis=True)
overlap.render()
```
![overlap-demo](https://user-images.githubusercontent.com/19553554/35090266-0f7d7d96-fc74-11e7-9851-d56777b4114d.gif)

**Note：** 关于双 Y 轴对齐，可以使用 `yaxis_force_interval` 参数，强制分割成相同份数的刻度。这里有个小技巧，可以先设置 y 轴最大值。举个例子，如果双 y 轴一个最大值为 700，一个最大值为 400。那你可以把两个的 `yaxis_force_interval` 参数分别设置为 140 和 80，那就会都分成均等的 5 份了。

如果只是想在单个 .html 按顺序展示图表，推荐使用 ```Page()``` 类


## Page：同一网页按顺序展示多图
> Grid/Timeline/Overlap 都可在 Page 中正常展示，把其当做一个图加入到 Page 中即可

Page 类的使用：
1. 引入 `Page` 类，`from pyecharts import Page`
2. 实例化 `Page` 类，`page = Page()`  ，可指定 `page_title`, `jhost` 参数。
3. 使用 `add()` 向 `page` 中添加图，可以是单个图实例，也可以是一个图实例列表。
4. 使用 `render()` 渲染生成 .html 文件

Page 类中其他方法：
* `render_embed()`：在 Flask&Django 中可以使用该方法渲染
* `show_config()`：打印输出所有配置项
* `chart`：chart 属性返回图形实例
* 在 Jupyter-notebook 中直接调用 Page 实例即可显示图表

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
运行之后，你会发现 render.html 已经按顺序显示了两个图:

![page-demo](https://user-images.githubusercontent.com/19553554/35104303-658f9654-fca3-11e7-9a05-5e2e13d1a4c4.gif)

**当然，更多图也是可以的**
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

**Page 类的额外的文本标签，由各图形本身携带**
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


## Timeline：提供时间线轮播多张图
Timeline 类的使用：
1. 引入 `Timeline` 类，`from pyecharts import Timeline`
2. 实例化 `Timeline` 类
3. 使用 `add()` 向 `timeline` 中添加图。如 `add(bar, '2013')` 接受两个参数，第一个为图实例，第二个为时间线的 ”时间点“。
4. 使用 `render()` 渲染生成 .html 文件

实例化 Timeline 类时接受设置参数：

* page_title -> str  
    生成 html 文件的 `<title>` 标签的值，默认为'Echarts'
* width -> int  
    画布宽度，默认为 800
* height -> int  
    画布高度，默认为 400
* jhost -> str  
    自定义每个实例的 JavaScript host
* is_auto_play -> bool  
    是否自动播放，默认为 Flase
* is_loop_play -> bool  
    是否循环播放，默认为 True
* is_rewind_play -> bool  
    是否反向播放，默认为 Flase
* is_timeline_show -> bool  
    是否显示 timeline 组件。默认为 True，如果设置为false，不会显示，但是功能还存在。
* timeline_play_interval -> int  
    播放的速度（跳动的间隔），单位毫秒（ms）。
* timeline_symbol -> str  
    标记的图形。ECharts 提供的标记类型包括 'circle', 'rect', 'roundRect', 'triangle', 'diamond', 'pin', 'arrow'
* timeline_symbol_size -> int/list  
    标记的图形大小，可以设置成诸如 10 这样单一的数字，也可以用数组分开表示宽和高，例如 [20, 10] 表示标记宽为 20，高为 10。
* timeline_left -> int/str  
    timeline 组件离容器左侧的距离。  
    left 的值可以是像 20 这样的具体像素值，可以是像 '20%' 这样相对于容器高宽的百分比，也可以是 'left', 'center', 'right'。如果 left 的值为'left', 'center', 'right'，组件会根据相应的位置自动对齐。
* timeline_right -> int/str  
    timeline 组件离容器右侧的距离。同 left
* timeline_top -> int/str  
    timeline 组件离容器顶侧的距离。同 left
* timeline_bottom -> int/str  
    timeline 组件离容器底侧的距离。同 left

Timeline 类中其他方法：
* `render_embed()`：在 Flask&Django 中可以使用该方法渲染
* `show_config()`：打印输出所有配置项
* `chart`：chart 属性返回图形实例
* Timeline 在 Jupyter-notebook 中显示有问题（无法正常显示动画）

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

**如果你已阅读完本篇文档，可以进一步阅读 [高级用法篇](zh-cn/advanced)**
