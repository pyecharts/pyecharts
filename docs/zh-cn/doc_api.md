# pyecharts 文档-API 篇

#### [pyecharts 文档-预览篇](https://github.com/chenjiandongx/pyecharts/blob/master/docs/zh-cn/doc_prepare.md)
#### [pyecharts 文档-图形篇](https://github.com/chenjiandongx/pyecharts/blob/master/docs/zh-cn/doc_charts.md)
#### [pyecharts 文档-版本篇](https://github.com/chenjiandongx/pyecharts/blob/master/changelog.md)
#### [pyecharts 文档-画廊篇](https://github.com/chenjiandongx/pyecharts/blob/master/docs/zh-cn/doc_gallery.md)
#### [pyecharts 文档-FAQ 篇](https://github.com/chenjiandongx/pyecharts/blob/master/docs/zh-cn/doc_faq.md)

本文档描述了 pyecharts 库一些公开的 API，以供开发者之使用。

## pyecharts配置项

从v0.2.8开始，所有的配置项将统一于类 `pyecharts.conf.PyEChartsConfig` 类中。一般在使用之前需要使用模块函数 `configure` 进行设置。

```python
import pyecharts
pyecharts.configure(P1=V1, P2=V2,...)
```

### 配置列表

**echarts_template_dir**

模板文件目录，默认值：'.'（当前目录）。用于自定义模板文件，即 `render` 的template_name 参数构成全部的路径。

**jshost**

js文件仓库路径。可以设置本地或者远程地址。所有的远程地址必须以 `http://` 或者 `https://` 开头。

也可以使用 `pyecharts.online()` 函数设置此选项。

为了保持兼容性， jshost 并不是必须使用 '/' 等分隔符作为结尾。

**force_js_embed**

是否强制采用内部嵌入方式渲染js文件标签， `echarts_js_dependencies`  模板函数受此影响，具体可参考该函数。

## 图表类

图表类是 pyecharts 库中最为核心的内容，每一个类代表了[Echarts](http://echarts.baidu.com/) 中一个图表类型。下表显示了这些图表的继承体系。

![class-relationship-diagram](https://github.com/chenjiandongx/pyecharts/blob/master/images/class-relationship-diagram.png)
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

数字类型(number)。图表容器 div 的宽度，以 px 为单位。

**height**

数字类型(number)。图表容器 div 的高度，以 px 为单位。

**options**

字典类型(dict)，Echarts 图表配置。不同图表类型具有不同数据格式。具体请参考 ECharts 文档。

**js_dependencies**

集合类型(set)，js 依赖文件名称列表，元素不包含文件后缀(.js)，如 `{'echarts.min', 'fujian'}` 。

**charts**

多图表对象中源图表对象列表，每个元素均为 `pyecharts.base.Base` 的子类对象。仅用于 `pyecharts.custom.page.Page` 类。

### 方法

**add()**


添加图表配置和数据。具体请参考其子类定义。

| 图表类      | 函数签名                                     |
| -------- | ---------------------------------------- |
| Base     | `add(**echarts_options)`                 |
| Grid     | `add(grid_width=None, grid_height=None, grid_top=None, grid_bottom=None, grid_left=None, grid_right=None)` |
| Overlap  | `add(chart, xaix_index=0, yaix_index=0, id_add_xaxis=False, is_add_yaxis=False)` |
| Timeline | `add(chart, time_point)`                 |
| Page     | `add(achart_or_charts)`                  |

**get_js_dependencies()**

获取 js 依赖文件列表。和 属性 *js_dependencies* 不同， 这里的元素是包含了文件完整路径。

**render(path='render.html')**

渲染至指定的 HTML 页面，不同图表类型使用默认的模板文件。

**render_embed()**

渲染包含选项的 js 代码。

**show_config()**

打印全部 options 属性。

## 多图表

`pyecharts.custom.page.Page` 用于在同一页面显示多个图表，也拥有上述的属性和方法。

同时 `Page` 类继承自 `list` ，因此也支持长度计算(len)、迭代(iter)、索引(index)、切片(slice)、添加(append)、扩展(extend)等操作。

例子：按顺序打印page中每个图表的echarts选项字典。

```python
page = Page()
line = Line('Demo Line')
# ... Add data to line
page.add(line)
kline = KLine('Demo kline')
# ... Add data to kline
page.append(kline)

for chart in page:
    chart.show_config()
```



## 数据处理工具

以下几个方法为数据处理的类方法，

**cast**

`pyecharts.base.cast(seq)`

数据格式化处理函数，能够将源数据转化为符合 pyecharts 的数据。

例子:

```python
o_data = [('A', '34'), ('B', '45'), ('C', '12')]
x, y = Base.cast(o_data)
print(x) # ['A', 'B', 'C']
print(y) # ['34', '45', '12']
```

**json_dumps**

`pyecharts.base.json_dumps(data, indent=0)`

将 data 转换为 JSON 字符串，和默认的 `json.dumps` 方法增加了：

- 将日期和时间转化为 ISO8601 字符串
- 对于 numpy 数组，增加了类型强制转化，可参考 [astype](https://docs.scipy.org/doc/numpy/reference/generated/numpy.ndarray.astype.html) 和 [tolist](https://docs.scipy.org/doc/numpy/reference/generated/numpy.ndarray.tolist.html) .

## 图表渲染

**JINJA2_ENV**

`pyecharts.templates.JINJA2_ENV`

数据类型 `jinja2.Environment`。pyecharts 内置了一个 jinja2 的模板渲染环境对象。

- 该环境对象使用 *pyecharts/templates* 作为存放模板文件的目录，包含了 HTML 和 javascript 文件。

## 模板引擎

### 概述

pyecharts库使用 [Jinja2](http://jinja.pocoo.org/) 作为其默认模板渲染引擎，并添加了若干个 echarts 图表相关的模板函数。

> 模板函数和模板标签是同一特性的不同术语，在Django模板系统中称为标签，Jinja2模板系统中称之为函数。二者语法形式也有所不同。

### 引擎对象

**EChartsEnvironment**

`pyecharts.engine.EChartsEnvironment`

EChartsEnvironment 类继承自 `Jinja2.Environment` 表示了

### 模板函数

EChartsEnvironment 引擎提供了一些模板函数，这些函数通常接收一个或多个的 `Chart` 或 `Page` 的参数，详细的调用形式见下表。

| 标签/调用形式                       | F(chart) | F(page) | F(chart1,chart2,...)/F(*page) |
| ----------------------------- | -------- | ------- | ----------------------------- |
| echarts_js_dependencies       | ✓        | ✓       | ✓                             |
| echarts_js_dependencies_embed | ✓        | ✓       | ✓                             |
| echarts_container             | ✓        |         |                               |
| echarts_js_content            | ✓        | ✓       | ✓                             |
| echarts_js_content_wrap       | ✓        | ✓       | ✓                             |



**echarts_js_dependencies**

`pyecharts.template.echarts_js_dependencies(*args)`

渲染包含图表所需要的 js 文件的 script 一个或多个节点，采用内部嵌入或者外部链接，最终采用何种模板依据 jshost 和 force_js_embed 配置项决定的，具体可参考下表：

| jshost/force_js_embed        | True | False |
| ---------------------------- | ---- | ----- |
| 本地                           | 内嵌   | 内嵌    |
| 远程（以 http:// 或者 https:// 开头） | 内嵌   | 外链    |

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

渲染js的 script 一个或多个节点，采用内嵌方式引入。仅支持本地jshost。

**echarts_container**

`pyecharts.template.echarts_container(chart)`

渲染图表容器，为一个 `<div></div>` 元素。

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

渲染js初始化代码片段，不包含`<script></script>`

**echarts_js_content_wrap**

`pyecharts.template.echarts_js_content_wrap(*args)`

渲染js初始化代码片段，包含首尾的`<script></script>`。

### 完整的例子

使用模板函数和自定义模板的例子。

demo.py

```python
from jinja2 import FileSystemLoader
from pyecharts import Bar
from pyecharts.engine import EchartsEnvironment
from pyecharts.utils import write_utf8_html_file

attr = ["衬衫", "羊毛衫", "雪纺衫", "裤子", "高跟鞋", "袜子"]
v1 = [5, 20, 36, 10, 75, 90]
v2 = [10, 25, 8, 60, 20, 80]
bar = Bar("柱状图数据堆叠示例", jshost='	https://cdn.bootcss.com/echarts/3.6.2')
bar.add("商家A", attr, v1, is_stack=True)
bar.add("商家B", attr, v2, is_stack=True)
env = EchartsEnvironment(loader=FileSystemLoader('.'))
tpl = env.get_template('demo.html')
html = tpl.render(bar=bar)
write_utf8_html_file('demo_gen.html', html)
```

demo.html模板

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

