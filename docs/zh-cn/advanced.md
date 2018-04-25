> 高级用法篇：本文档描述了 pyecharts 库的高级进阶用法。

## 使用 JavaScript 回调函数

v0.5.0 引入了新的 pyecharts 扩展包 [pyecharts-javascripthon](https://github.com/pyecharts/pyecharts-javascripthon)，该包的引入为 pyecharts 注入了新的活力。pyecharts-javascripthon 使用了一个优秀的第三方 Python 库 [metapensiero.pj](https://github.com/metapensiero/metapensiero.pj)，该库的官方介绍是 *Javascript for refined palates: a Python 3 to ES6 Javascript translator*，很明显了，这是一个用于将 Python 代码转换为 Javascript 代码的工具。

下面是几个简单的示例，

python 代码

``` python
def foo(a, b, c):
    pass
```
经转换，成为 JavaScript 代码
``` js
function foo(a, b, c) {
}
```

python 代码

```python
def foo(a, b, c):
    for i in range(a, b, c):
        yield i

for i in iterable(foo(0, 5, 2)):
    print(i)
```
经转换，成为 JavaScript 代码
``` js
function* foo(a, b, c) {
    for ... { // loop control omitted for brevity
        yield i;
    }
}

for (var i of foo(0, 5, 2)) {
    console.log(i);
}
```

想对这个库做进一步了解的话，可以阅读该 [官方文档](https://github.com/metapensiero/metapensiero.pj)。

有了这个库后，从本版本开始，pyecharts 将支持在配置项中传入 Python Function 类型的参数，对应的 Function 将会在 render 时自动的被转换成 Javascript 代码写入到 html 文件中，这也解决了 pyecharts 一直以来的一个痛点，缺乏对回调函数的支持，类似 formatter 这样的配置项一直无法得到较好的支持。

**NOTE:** Python2.7-3.4 的用户使用时请确保系统可以联网。

举个例子，pyecharts 用户经常会提问 Geo 图中如何在 tooltip 中只显示地图坐标名称和数值，不显示经纬度。

像这样

![](https://user-images.githubusercontent.com/19553554/39248236-186a50ae-48ce-11e8-84eb-e58ba17eca5c.png)

而现在，你可以这么操作，先定义一个函数

```python
def geo_formatter(params):
    return params.name + ' : ' + params.value[2]
```

然后设置 `tooltip_formatter=geo_formatter`，就能得到这样的效果

![](https://user-images.githubusercontent.com/19553554/39248244-1be6da4a-48ce-11e8-931f-059879c5dcf4.png)

本新功能需要用户对 metapensiero.pj 和 Echarts 官方配置项有一定的了解。

### 更多示例

// TODO


## 使用 JavaScript 事件处理函数

Echarts 本身提供了 [api/events](http://echarts.baidu.com/api.html#events) 事件处理函数，主要通过 on 方式实现。

pyecharts 根据官方提供的 events 列表，提供了如下全局事件名变量。位于 `pyecharts.echarts.events` 包中。

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
from pyecharts_javascripthon.dom.functions import alert


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

### 更多示例

// TODO
