> 高级用法篇：本文档描述了 pyecharts 库的高级进阶用法。

## 概述

自 v0.5.0 开始， pyecharts 支持 *javascript 回调函数* 和 *echarts 事件处理函数* ，进一步覆盖 [ECharts](http://echarts.baidu.com/) 相关特性。为项目发展注入新的活力。

在 Python-To-Javascript 语言翻译领域，[javascripthon](https://pypi.python.org/pypi/javascripthon)  是一个简单的 Python3.5+ 到 Javascript 的语言翻译器;  [dukpy](https://github.com/amol-/dukpy) 支持 Python2.7 和 Python 3.4 的语言翻译。

基于以上事实，`pyecharts.javascripthon` 封装了以上两个不同的翻译器，并提供若干个 Javascript 数据类型适配模块。

> 从 v0.6.0 开始，原有的 [pyecharts-javascripthon](https://github.com/pyecharts/pyecharts-javascripthon) 库将合并入 pyecharts ，引用路径为 `pyecharts.javascripthon` 。

pyecharts 目前仅使用了并封装一部分的 Javascripthon 的翻译规则，主要是 **函数翻译(Function Translate)** 。使用伪代码表示如下：

```
输入：一个 Python 的函数对象
输出：一个多行的 unicode 字符串
```

比如能够将以下的 Python 函数：

```python
def add(x, y):
    return x + y
```

翻译为以下 Javascript 函数。

```js
function add(x, y) {
    return (x + y);
}
```

对于 pyecharts 使用者来说，无需了解该翻译器具体的工作原理。关于翻译器的更多内容，请移步至 [Translator 篇](zh-cn/translator)。

## 安装

### 基本安装

从 v0.6.0 开始，pyecharts 默认已经集成，无需额外安装。


### 环境限制

由于 Javascripthon 要求 Python 的版本至少为 3.5+ 而 pyecharts 用户是 python 2.7, 3.4, 3.5 和 3.6, pyecharts-javascripthon 采用了双轨制：python 3.5+ 用户直接用 Javascripthon；python 2.7 和 3.4 的用户调用网络翻译服务 (software as a service)。同时，希望大家支持这个网络服务的运营费用。

> 注意： Python2.7-3.4 的用户使用时请确保系统可以联网。


## 使用 JavaScript 回调函数

### 基本使用

pyecharts 已经封装了底层相关逻辑，对使用者是透明的。因此你可以像之前一样的使用。将回调函数对象通过 `add` 方法赋值到 echarts 配置字典中，这里的回调函数需满足以下条件之一：

- 使用 `def` 定义的命名函数

注意的是目前暂不支持 `lambda` 表达式。

例子：

```python
from pyecharts import Bar


def label_formatter(params):
    return params.value + ' [Good!]'


attr = ["Jan", "Feb"]
v1 = [2.0, 4.9]
bar = Bar("Bar chart", "precipitation and evaporation one year")
bar.add("precipitation", attr, v1, is_label_show=True, label_formatter=label_formatter)
bar.render()
```

> 回调函数格式参考自  [series[i]-bar.label.formatter](http://echarts.baidu.com/option.html#series-bar.label.formatter) 。

效果图

![bar-label-formatter-callback](https://user-images.githubusercontent.com/9875406/38666230-07c1aa66-3e71-11e8-9e9f-43fb7d707a64.png)

### Tooltip 示例

举个例子，pyecharts 用户经常会提问 Geo 图中如何在 tooltip 中只显示地图坐标名称和数值，不显示经纬度。

像这样

```python
def test_geo_shantou_city():
    data = [('澄海区', 30), ('南澳县', 40), ('龙湖区', 50), ('金平区', 60)]
    geo = Geo("汕头市地图示例", **style.init_style)
    attr, value = geo.cast(data)
    geo.add(
        "",
        attr,
        value,
        maptype="汕头",
        is_visualmap=True,
        is_legend_show=False,
        label_emphasis_textsize=15,
        label_emphasis_pos='right',
    )
    geo.render()
```
得到

![](https://user-images.githubusercontent.com/19553554/39248236-186a50ae-48ce-11e8-84eb-e58ba17eca5c.png)

而现在，你可以这么操作，先定义一个 `geo_formatter` 函数

```python
def geo_formatter(params):
    return params.name + ' : ' + params.value[2]

def test_geo_shantou_city():
    data = [('澄海区', 30), ('南澳县', 40), ('龙湖区', 50), ('金平区', 60)]
    geo = Geo("汕头市地图示例", **style.init_style)
    attr, value = geo.cast(data)
    geo.add(
        "",
        attr,
        value,
        maptype="汕头",
        is_visualmap=True,
        is_legend_show=False,
        tooltip_formatter=geo_formatter,    # 重点在这里，将函数直接传递为参数。
        label_emphasis_textsize=15,
        label_emphasis_pos='right',
    )
    geo.render()
```
就可以看到下面的效果了。

![](https://user-images.githubusercontent.com/19553554/39248244-1be6da4a-48ce-11e8-931f-059879c5dcf4.png)

### Label 示例

使用回调函数强制设置浮点数位数

```python
from pyecharts import Bar, Grid
from pyecharts.javascripthon.dom import window


def custom_formatter(params):
    return window.parseFloat(params.value).toFixed(2)


attr = ["aa", "bb", "Diabetes Mellitus Requiring Medication", "d", "e", "fff"]
v1 = [5.12, 20.85, 36.69, 10.10, 75.20, 90.36]
v2 = [10.00, 25.45, 8.23, 60.00, 20.50, 80.00]
bar = Bar("x 轴和 y 轴交换")
bar.add(
    "商家A",
    attr,
    v1,
    is_label_show=True,
    label_pos="right",
    label_formatter=custom_formatter,
)
bar.add(
    "商家B",
    attr,
    v2,
    is_convert=True,
    is_label_show=True,
    label_pos="right",
    label_formatter=custom_formatter,
)
grid = Grid()
grid.add(bar, grid_left="40%")
grid.render()
```
![](https://user-images.githubusercontent.com/19553554/44003191-5c5e7764-9e81-11e8-98f1-757a208ec337.png)


## 使用 JavaScript 事件处理函数

Echarts 本身提供了 [api/events](http://echarts.baidu.com/api.html#events) 事件处理函数，主要通过 on 方式实现。

pyecharts 根据官方提供的 events 列表，提供了如下全局事件名变量。位于 `pyecharts.echarts.events` 模块中。

``` python
# Mouse Events
MOUSE_CLICK = "click"
MOUSE_DBCLICK = "dbclick"
MOUSE_DOWN = "mousedown"
MOUSE_OVER = "mouseover"
MOUSE_GLOBALOUT = "globalout"

# Other Events
LEGEND_SELECT_CHANGED = "legendselectchanged"
LEGEND_SELECTED = "legendselected"
LEGEND_UNSELECTAED = "legendunselected"
LEGEND_SCROLL = "legendscroll"
DATA_ZOOM = "datazoom"
DATA_RANGE_SELECTED = "datarangeselected"
TIMELINE_CHANGED = "timelinechanged"
TIMELINE_PLAY_CHANGED = "timelineplaychanged"
RESTORE = "restore"
DATA_VIEW_CHANGED = "dataviewchanged"
MAGIC_TYPE_CHANGED = "magictypechanged"
GEO_SELECT_CHANGED = "geoselectchanged"
GEO_SELECTED = "geoselected"
GEO_UNSELECTED = "geounselected"
PIE_SELECT_CHANGED = "pieselectchanged"
PIE_SELECTED = "pieselected"
PIE_UNSELECTED = "pieunselected"
MAP_SELECT_CHANGED = "mapselectchanged"
MAP_SELECTED = "mapselected"
MAP_UNSELECTED = "mapunselected"
AXIS_AREA_SELECTED = "axisareaselected"
FOCUS_NODE_ADJACENCY = "focusnodeadjacency"
UNFOCUS_NODE_ADJACENCY = "unfocusnodeadjacency"
BRUSH = "brush"
BRUSH_SELECTED = "brushselected"
```

使用方式如下，
```python
#!/usr/bin/env python
# coding=utf-8
from __future__ import unicode_literals

import pyecharts.echarts.events as events
from pyecharts import Bar
from pyecharts.javascripthon.dom import alert


def on_click():
    alert("点击事件触发")


def test_mouse_click():
    bar = Bar("我的第一个图表", "这里是副标题")
    bar.add(
        "服装", ["衬衫", "羊毛衫", "雪纺衫", "裤子", "高跟鞋", "袜子"], [5, 20, 36, 10, 75, 90]
    )
    bar.on(events.MOUSE_CLICK, on_click)
    bar.render()
```
效果

![](https://user-images.githubusercontent.com/19553554/39252189-b02b5420-48d7-11e8-9c53-6f0fb6d386c0.gif)

## 注意

第一，pyecharts 并不会检查 echarts 图表配置选项是否支持回调函数，关于这一部分可参考 ECharts 文档。

这里指的是，options 参数本身是否支持回调函数，比如

```python
def my_title():
    return 'my_title'
bar.add(my_title, [], [])
```
在 pyecharts 并不会出现渲染上的错误，但不符合 Echarts 中对 title 的要求.


第二，为了提高性能，pyecharts 作了以下几点处理：

- 函数翻译的实际执行是在 `render` 函数调用时，而不是 `add` 函数。
- 对已经翻译完成的函数以 **函数名** 为索引进行缓存，避免多次渲染同名函数。

因此应当避免同一个函数名多用，以下的情况可能无法获得预期的效果。

```python
from pyecharts import Bar

def label_formatter(params):
    return params.name + ' [Good!]'

attr = ["Jan", "Feb"]
v1 = [2.0, 4.9]
bar = Bar("Bar chart", "precipitation and evaporation one year")
bar.add("precipitation", attr, v1, is_label_show=True, label_formatter=label_formatter)
bar.render()

def label_formatter(params):
    return params.name + '[OK!]'

bar2 = Bar("Bar chart", "precipitation and evaporation one year")
bar2.add("precipitation", attr, v1, is_label_show=True, label_formatter=label_formatter)
bar2.render()
```

## 编辑 _option

如果 pyecharts 的自带 options 不能满足要求的话，开发人员是可以自己插入自己的配置选项。唯一的问题是，pyecharts 不能把某选项设置为空 (null)。
从 0.5.10 起，这个问题得到了解决。

```python
from pyecharts import NULL, Kline

kline = Kline("K 线图-默认示例")
kline.add("日K", DATE, data)
kline._option['series'][0]['itemStyle']['normal']['borderColor'] = NULL
kline.render()
```
