> API 篇：本文档描述了 pyecharts 库一些公开的 API，以供开发者之使用。

## 总体流程

一个通用的 pyecharts 使用流程可描述如下：

| 步骤       | 简略代码                                     | 备注   |
| -------- | ---------------------------------------- | ---- |
| 1 创建图表实例 | `bar = Bar()`                            |      |
| 2 添加数据   | `bar.add(**kwargs)`                      |      |
| 3 添加事件处理   | `bar.on(event_name, handler)`             | added in v0.5.0    |
| 4 创建配置实例 | `config = PyEchartsConfig(**kwargs)`     |      |
| 5 构建模板引擎 | `engine = EchartsEnvironment(pyecharts_config=config)` |      |
| 6 获取模板文件 | `tpl = engine.get_template('demo_tpl.html')` |      |
| 7 渲染     | `html = tpl.render(bar=bar)`             |      |
| 8 写入目标文件 | `write_utf8_html_file('my_demo_chart.html', html)` |      |


## pyecharts 配置项

pyecharts 遵循 “先配置后使用” 的基本原则，所有的配置项将统一于类 `pyecharts.conf.PyEChartsConfig` 类中。

如果使用 `chart.render()` 这种渲染方式，可以通过模块函数 `configure` 进行修改 pyecharts 中默认的配置类。

```python
import pyecharts
pyecharts.configure(
    jshost=None,
    echarts_template_dir=None,
    force_js_embed=None,
    output_image=None,
    global_theme=None
)
```

* jshost
js 文件仓库路径。可以设置本地或者远程地址。所有的远程地址必须以 `http://` 或者 `https://` 开头。  
也可以使用 `pyecharts.online()` 函数设置此选项。  
为了保持兼容性， jshost 并不是必须使用 '/' 等分隔符作为结尾。

* echarts_template_dir
模板文件目录，默认值：'.'（当前目录）。用于自定义模板文件，即 `render` 的 template_name 参数构成全部的路径。

* force_js_embed
是否强制采用内部嵌入方式渲染js文件标签， `echarts_js_dependencies`  模板函数受此影响，具体可参考该函数。

* output_image
指定输出图片类型，有 'svg', 'jpeg', 'png' 可选

* global_theme
指定全局主题，目前提供的主题有 `dark`, `vintage`, `macarons`, `infographic`, `shine` 和 `roma`。


## 图表类

图表类是 pyecharts 库中最为核心的内容，每一个类代表了 [ECharts](http://echarts.baidu.com/) 中一个图表类型。下表显示了这些图表的继承体系。

![class-relationship-diagram](https://raw.githubusercontent.com/chenjiandongx/pyecharts/master/images/class-relationship-diagram.png)

### 属性

图表类和属性表如下：

| 属性/图表           | Base | Chart/FOO_CHART | Grid | Overlap | Timeline | Page |
| --------------- | ---- | --------------- | ---- | ------- | -------- | ---- |
| chart_id        | ✓    | ✓               | ✓    | ✓       | ✓        |      |
| width           | ✓    | ✓               | ✓    | ✓       | ✓        |      |
| heigth          | ✓    | ✓               | ✓    | ✓       | ✓        |      |
| options         | ✓    | ✓               | ✓    | ✓       | ✓        |      |
| js_dependencies | ✓    | ✓               | ✓    | ✓       | ✓        | ✓    |

**chart_id**

字符串类型(str)，图表唯一标识符，默认 uuid 格式的字符串，如 `'d2d9dcc4e28247518186c0882d356ba8'` 。

**width**

数字类型(number)或字符串(str)。图表容器 div 的宽度，接收一个有效 css 长度形式的字符串；如果是数字，以 px 为单位。

**height**

数字类型(number)或字符串(str)。图表容器 div 的高度，接收一个有效 css 长度形式的字符串；如果是数字，以 px 为单位。

> chart_id、width、height 三个属性均支持可写。

**options**

字典类型(dict)，ECharts 图表配置。不同图表类型具有不同数据格式。具体请参考 ECharts 文档。

**js_dependencies**

列表类型(list)，js 依赖文件名称列表，元素不包含文件后缀(.js)，如 `{'echarts.min', 'fujian'}` 。

> 从v0.4开始，pyecharts 重写了  `js_dependencies` 的生成逻辑，目前返回的是有序、元素唯一的列表对象。另外还可以通过 `pyecharts.utils.merge_js_dependencies` 函数合并若干个图表的 js 依赖文件。

### 方法

**add()**

添加图表配置和数据。具体请参考其子类定义。

| 图表类      | 函数签名                                     |
| -------- | ---------------------------------------- |
| Base     | `add(**echarts_options)`                 |
| Grid     | `add(grid_width=None, grid_height=None, grid_top=None, grid_bottom=None,grid_left=None, grid_right=None)` |
| Overlap  | `add(chart, xaix_index=0, yaix_index=0, id_add_xaxis=False, is_add_yaxis=False)` |
| Timeline | `add(chart, time_point)`                 |
| Page     | `add(achart_or_charts)`                  |

**on(event_name, handler)**

添加 [事件处理函数](http://echarts.baidu.com/api.html#events)。

* event_name：事件名称
* handler：回调函数


这是支持的所有事件

``` python
# Mouse Events

MOUSE_CLICK = 'click'
MOUSE_DBCLICK = 'dbclick'
MOUSE_DOWN = 'mousedown'
MOUSE_OVER = 'mouseover'
MOUSE_GLOBALOUT = 'globalout'

# Other Events

LEGEND_SELECT_CHANGED = 'legendselectchanged'
LEGEND_SELECTED = 'legendselected'
LEGEND_UNSELECTAED = 'legendunselected'
LEGEND_SCROLL = 'legendscroll'
DATA_ZOOM = 'datazoom'
DATA_RANGE_SELECTED = 'datarangeselected'
TIMELINE_CHANGED = 'timelinechanged'
TIMELINE_PLAY_CHANGED = 'timelineplaychanged'
RESTORE = 'restore'
DATA_VIEW_CHANGED = 'dataviewchanged'
MAGIC_TYPE_CHANGED = 'magictypechanged'
GEO_SELECT_CHANGED = 'geoselectchanged'
GEO_SELECTED = 'geoselected'
GEO_UNSELECTED = 'geounselected'
PIE_SELECT_CHANGED = 'pieselectchanged'
PIE_SELECTED = 'pieselected'
PIE_UNSELECTED = 'pieunselected'
MAP_SELECT_CHANGED = 'mapselectchanged'
MAP_SELECTED = 'mapselected'
MAP_UNSELECTED = 'mapunselected'
AXIS_AREA_SELECTED = 'axisareaselected'
FOCUS_NODE_ADJACENCY = 'focusnodeadjacency'
UNFOCUS_NODE_ADJACENCY = 'unfocusnodeadjacency'
BRUSH = 'brush'
BRUSH_SELECTED = 'brushselected'
```

事件处理函数的原型:

``` python
def handler(params):
    pass
```

此处 params 的结构与 echarts 的一模一样：

```
{
    // 当前点击的图形元素所属的组件名称，
    // 其值如 'series'、'markLine'、'markPoint'、'timeLine' 等。
    componentType: string,
    // 系列类型。值可能为：'line'、'bar'、'pie' 等。当 componentType 为 'series' 时有意义。
    seriesType: string,
    // 系列在传入的 option.series 中的 index。当 componentType 为 'series' 时有意义。
    seriesIndex: number,
    // 系列名称。当 componentType 为 'series' 时有意义。
    seriesName: string,
    // 数据名，类目名
    name: string,
    // 数据在传入的 data 数组中的 index
    dataIndex: number,
    // 传入的原始数据项
    data: Object,
    // sankey、graph 等图表同时含有 nodeData 和 edgeData 两种 data，
    // dataType 的值会是 'node' 或者 'edge'，表示当前点击在 node 还是 edge 上。
    // 其他大部分图表中只有一种 data，dataType 无意义。
    dataType: string,
    // 传入的数据值
    value: number|Array
    // 数据图形的颜色。当 componentType 为 'series' 时有意义。
    color: string
}
```

例子：

``` python
# coding=utf-8
from __future__ import unicode_literals

from pyecharts import Map
import pyecharts.events as events
from pyecharts_javascripthon.dom.functions import alert


def on_click(params):
    alert(params.name)

value = [155, 10, 66, 78]
attr = ["福建", "山东", "北京", "上海"]
map = Map("全国地图示例", width=1200, height=600)
map.add("", attr, value, maptype='china', is_label_show=True)
map.on(events.MOUSE_CLICK, on_click)
map.render()
```

![](https://user-images.githubusercontent.com/4280312/39089412-88f0436e-45be-11e8-91b1-6617d795f26e.gif)

**get_js_dependencies()**

获取 js 依赖文件列表。和 属性 *js_dependencies* 不同， 这里的元素是包含了文件完整路径。

**render(path='render.html', template_name='simple_chart.html', object_name='chart', extra_context=None)**

渲染至指定的 HTML 页面，不同图表类型使用默认的模板文件。各参数意义如下：

- path ：最终生成文件名称
- template_name: 模板文件名称，其目录可通过 `pyecharts.configure()` 全局函数进行配置
- object_name: 模板文件中，该图表类所使用变量的名称
- extra_context 额外数据字典。

**render_embed()**

渲染包含选项的 js 代码。

**print_echarts_options**

打印全部 options 属性。

**show_config()**

打印全部 options 属性。自 v0.3.3 起。已废弃，应当使用 `print_echarts_options` 。


## 多图表 Page

> 在 v0.5.4 变更，重写内部实现，新增图表命名名称。

### 基本使用

由于无论是 Jinja2 模板还是 Django 模板，均不提倡使用 `{{ charts.1 }}` 形式访问列表中的某一个元素。因此在 v0.5.4 对 Page 进行重构，新增图表命名名称。

在创建一个 `Page` 实例 page ，后，使用 `add_chart` 添加一个图表对象，可以使用 name 为之起一个引用名称。


```python

from pyecharts import Page, Line, Bar

page = Page()
line = Line('Demo Line')
# ... Add data to line
page.add_chart(line, name='line')
bar = Bar('Demo kline')
# ... Add data to bar
page.add_chart(bar)
```

图表访问方式

| 项目 | Python 代码 | 模板代码 |
| ------ | ------ | ------ |
| line 实例 | `print(page['line'])` | `{{ page.line }}` |
| bar 实例 | `print(page['c1'])` | `{{ page.c1 }}` |

### 方法列表

在创建一个 page 实例后，可以通过各种方法将现有的图表实例添加到该实例中。

> Page 不再具有 list 的全部特性，因此 切片(slice)、添加(append)、扩展(extend) 等方法不再支持。

**`__init__(page_title, **name_chart_pair)`**

构造函数，使用 `{<name>:<chart>}` 创建实例。根据 [PEP 468](https://www.python.org/dev/peps/pep-0468/)，仅在 Python 3.6+ 同时保证其顺序。

**`add_chart(chart, name=None)`**

v0.5.4 新增，可链式使用。添加一个图表对象，如果如果没有指定  `name` 参数，默认使用类似 `'c0'` ，`'c1'` 等字符串命名。

**`add(achart_or_charts)`**

可链式使用。添加一个或多个图表对象，该函数使用默认的名称。

**`cls.from_charts(*charts)`**

从一个或多个图表实例，创建一个 `Page` 实例。

### 图表方法

准确来说， `Page` 并不是 ECharts 中的图表类型，所包含的图表也并不要求具有相关性。为了方便， `Page` 也具有相关的属性方法，包括：

- `page_title`
- `js_dependencies`
- `render_embed()`
- `get_js_dependencies()`
- `_repr_html_()`

这些方法的使用方法同 `Base` 类。

## 模板引擎

### 概述

pyecharts库使用 [Jinja2](http://jinja.pocoo.org/) 作为其默认模板渲染引擎，并添加了若干个 echarts 图表相关的模板函数。

> 模板函数和模板标签是同一特性的不同术语，在 Django 模板系统中称为标签，Jinja2 模板系统中称之为函数。二者语法形式也有所不同。

### 引擎对象

`pyecharts.engine` 定义了若干个继承自 `jinja2.Environment` 的模板引擎类，每个类都有其适合的使用场景。

**BaseEnvironment**

`pyecharts.engine.BaseEnvironment`

该类是 pyecharts 基本的模板引擎类，该类直接继承 `jinja2.Environment` ，并且：

- 添加了 pyecharts_config 属性，这是一个 `PyEchartsConfig` 对象。
- 添加了 `echarts_*` 等模板函数。

该类可用于 web 框架整合。

**EChartsEnvironment**

`pyecharts.engine.EChartsEnvironment(pyecharts_config=None, **kwargs)`

EChartsEnvironment 类继承自 `BaseEnvironment` 。并在此基础上改写了模板文件加载器(loader)的行为，默认使用 `pyecharts_config.echarts_template_dir` 作为模板文件目录。

由于该类重写模板文件加载器的行为，因此不应当用于 web 整合。

**ECHAERTS_TEMPLATE_FUNCTIONS**

`pyecharts.engine.ECHAERTS_TEMPLATE_FUNCTIONS`

包含模板函数的字典。可用于 web 框架整合。

### 引擎方法

**create_default_environment(filet_ype)**

* file_type: 输出文件类型，有 'html', 'svg', 'png', 'jpeg', 'gif'，'pdf' 可选

为渲染创建一个默认配置环境


### 模板函数

pyecharts 内置的引擎提供了一些模板函数，这些函数通常接收一个或多个的 `Chart` 或 `Page` 的参数，详细的调用形式见下表。

| 标签/调用形式                       | F(chart) | F(page) | F(chart1,chart2,...)/F(*page) |
| ----------------------------- | -------- | ------- | ----------------------------- |
| echarts_js_dependencies       | ✓        | ✓       | ✓                             |
| echarts_js_dependencies_embed | ✓        | ✓       | ✓                             |
| echarts_container             | ✓        |         |                               |
| echarts_js_content            | ✓        | ✓       | ✓                             |
| echarts_js_content_wrap       | ✓        | ✓       | ✓                             |


**echarts_js_dependencies**

 `pyecharts.template.echarts_js_dependencies(*args)`  

渲染包含图表所需要的 js 文件的 script 一个或多个节点，有内部嵌入或者外部链接两种结果。

内嵌模式

 ```html
 <script type="text/javascript">
     var a = 1;
     console.log(a):
 </script>
 ```

外链模式

```html
<script type="text/javascript" src="/static/js/echarts.min.js"></script>
```

最终采用何种模板依据 PyEchartsConfig.jshost 和 PyEchartsConfig.force_js_embed 配置项决定的，具体可参考下表：

| 取值                                       | 本地/远程 | script 模式              | 使用场景          | 备注                 |
| ---------------------------------------- | ----- | ---------------------- | ------------- | ------------------ |
| `/template/js/echarts`                   | 本地    | 内嵌                     | 本地生成单一文件，直接移植 | 此为默认是设置            |
| `'https://pyecharts.github.io/jupyter-echarts/echarts'` | 远程    | 内嵌                     | 生成单一文件        | 使用 `online` 可切换到此项 |
| 其他本地模式 (如 `/static/js`)                  | 本地    | 外链，可以通过force_embed改成内嵌 | 可用于web框架整合    |                    |
| 其他远程模式（如 `https://cdn.bootcss.com/echarts/3.7.2`） | 远程    | 外链                     | 使用外部js，需依赖网络  |                    |


例子

```
# Jinja2 Context function
{{ echarts_js_dependencies('echarts') }}
# Html Output
<script type="text/javascript" src="js/echarts.js"></script>

# Python
bar = Bar('Demo Bar')
# Jinja2 Context function
{{ echarts_js_dependencies(bar) }}
# Html Output
<script type="text/javascript" src="js/echarts.js"></script>
```

**echarts_js_dependencies_embed**

`pyecharts.template.echarts.js_dependencies_embed(*args)`  

渲染 js 的 script  一个或多个节点，采用内嵌方式引入。仅支持本地 jshost 。

**echarts_container**

`pyecharts.template.echarts_container(chart)`  

渲染图表容器，为一个  `<div></div>`  元素。

例子

```
# Python Code
bar = Bar('Demo Bar')
# Jinjia2 Context Function
{{ echarts_container(bar) }}
# Html Output
<div id="d09aa82b55384f84a33055f9878c3679" style="width:800px;height:400px;"></div>
```

**echarts_js_content**

`pyecharts.template.echarts_container(*chart)`  

渲染js初始化代码片段，不包含 `<script></script>` 。

**echarts_js_content_wrap**

`pyecharts.template.echarts_js_content_wrap(*args)`  

渲染js初始化代码片段，包含首尾的 `<script></script>` 。


### 完整的例子

使用模板函数和自定义模板的例子。

demo.py
```python
from __future__ import unicode_literals

from pyecharts import Bar
from pyecharts.conf import PyEchartsConfig
from pyecharts.engine import EchartsEnvironment
from pyecharts.utils import write_utf8_html_file

attr = ["衬衫", "羊毛衫", "雪纺衫", "裤子", "高跟鞋", "袜子"]
v1 = [5, 20, 36, 10, 75, 90]
v2 = [10, 25, 8, 60, 20, 80]
bar = Bar("柱状图数据堆叠示例")
bar.add("商家A", attr, v1, is_stack=True)
bar.add("商家B", attr, v2, is_stack=True)
config = PyEchartsConfig(echarts_template_dir='my_tpl',
                         jshost=options)
env = EchartsEnvironment(pyecharts_config=config)
tpl = env.get_template('tpl_demo.html')
html = tpl.render(bar=bar)
write_utf8_html_file('my_tpl_demo2.html', html)
```

tpl_demo.html 模板

```html
<!DOCTYPE html>
<html lang="zh-CN">
<head>
    <meta charset="UTF-8">
    <title>自定义模板</title>
    {{ echarts_js_dependencies(bar) }}
</head>
<body>
    {{ echarts_container(bar) }}
    {{ echarts_js_content(bar) }}
</body>
</html>
```
