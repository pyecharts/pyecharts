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

**NOTE:** Python2.7-3.4 的用户使用时请确保系统可以联网，这点非常重要！

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

本新功能属于进阶用法，需要用户对 metapensiero.pj 和 Echarts 官方配置项有一定的了解。

### 更多示例

// TODO


## 使用 JavaScript 事件处理函数

Echarts 本身提供了 [api/events](http://echarts.baidu.com/api.html#events) 事件处理函数，主要通过 on 方式实现。

pyecharts 根据官方提供的 events 列表，提供了如下全局事件名变量，看命名其实也就大概能够猜出事件的功能了。位于 `pyecharts.echarts.events` 包中。

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
from pyecharts_javascripthon.dom import alert


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

### pyecharts_javascripthon.dom API

分别对应 JavaScript 中的 Date, Math, JSON, window, Document, console, screen 等用法
```python
from pyecharts_javascripthon.dom import Date(*_) 
from pyecharts_javascripthon.dom import Document
from pyecharts_javascripthon.dom import window
from pyecharts_javascripthon.dom import Math
from pyecharts_javascripthon.dom import JSON
from pyecharts_javascripthon.dom import console
from pyecharts_javascripthon.dom import screen
from pyecharts_javascripthon.dom import alert(msg)
```

其实整个项目的核心就是 [Python2Javascript](https://github.com/pyecharts/pyecharts-javascripthon/blob/master/pyecharts_javascripthon/compiler.py)

```python
from metapensiero.pj.api import translates


class Python2Javascript:

    @staticmethod
    def translate(obj):
        source_lines, _ = inspect.getsourcelines(obj)
        javascript, _ = translates(source_lines)
        return javascript
```

这个类引用了 metapensiero.pj 的 translates 函数，转换 Python 代码。而上面提到的 python2.7-3.4 的用户使用转换功能必须确保系统可以联网的原因就是 metapensiero.pj 只支持 Python3.5+，所以我们为项目提供了一个在线转换的代码的功能，实际上就是把代码 post 到一台支持 metapensiero.pj 运行环境的服务器，再将转换后的代码返回。[pyecharts-javascripthon-api-service](https://github.com/pyecharts/pyecharts-javascripthon-api-service) 承担了这部分的工作，现已将该项目部署到了 [Heroku](https://www.heroku.com/)，想部署到自己服务器的开发者可以参考项目给出的 [文档](https://github.com/pyecharts/pyecharts-javascripthon-api-service/blob/master/README.md) 来操作。

### 更多示例

// TODO
