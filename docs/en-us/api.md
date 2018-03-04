pyecharts API

This document describes the public API for *pyecharts* library and it will be read by users and developers.

## Total Proccess

A common proccess can be listed as the following table:

| Step                     | Code Demo                                | Remark |
| ------------------------ | ---------------------------------------- | ------ |
| 1 Create chart instance  | `bar = Bar()`                            |        |
| 2 Add data               | `bar.add(**kwargs)`                      |        |
| 3 Create config instance | `config = PyEchartsConfig(**kwargs)`     |        |
| 4 Create template engine | `engine = EchartsEnvironment(pyecharts_config=config)` |        |
| 5 Get template file      | `tpl = engine.get_template('demo_tpl.html')` |        |
| 6 Render                 | `html = tpl.render(bar=bar)`             |        |
| 7 Write to target file   | `write_utf8_html_file('my_demo_chart.html', html)` |        |



## pyecharts Config Items

pyecharts follows the principle of "Config-Use" . The class `pyecharts.conf.PyEChartsConfig`  contains all config items when using *pyecharts* library.Before building chart, you can use module function  `configure` to set all config items.

```python
import pyecharts
pyecharts.configure(P1=V1, P2=V2,...)
```

### Config Item List

**echarts_template_dir**

The diretory of template files. Default value: '.'(current diretory).

**jshost**

The repository of js dependency files.You can set it with a local host url or remote host url(starts with `http://` or `https://` ).

You can also use `pyecharts.online()`  to set this item.

WIth the compatibility, this string value do not need `/` as its ending character.

**force_js_embed**

Whether to force to insert javascript file with internal embed mode.  This item will affect the function`echarts_js_dependencies`  . 

## Charts Classes

Charts classes is the core component of this library.Each charts class represents the one kind of chart in [Echarts](http://echarts.baidu.com/) .

This pictures  the inherit tree for these charts classes.

![class-relationship-diagram](https://github.com/chenjiandongx/pyecharts/blob/master/images/class-relationship-diagram.png)

### Properties

This table list properties for these chart classes.

| Properites/Charts | Base | Chart/FOO_CHART | Grid | Overlap | Timeline | Page |
| ----------------- | ---- | --------------- | ---- | ------- | -------- | ---- |
| chart_id          | ✓    | ✓               | ✓    | ✓       | ✓        |      |
| width             | ✓    | ✓               | ✓    | ✓       | ✓        |      |
| heigth            | ✓    | ✓               | ✓    | ✓       | ✓        |      |
| options           | ✓    | ✓               | ✓    | ✓       | ✓        |      |
| js_dependencies   | ✓    | ✓               | ✓    | ✓       | ✓        | ✓    |

**chart_id**

Data type:str.The identifier string for a chart. E.g.`'d2d9dcc4e28247518186c0882d356ba8'` 。

**width**

Data type:number/str.A valid string for css length.The width(px) of div container for a chart.

**height**

Data type:number/str.A valid string for css length.The height(px) of div container for a chart.

**options**

Data type:dict.The config options for a chart。Each chart has its own format and value.Please see more detail at ECharts document。

**js_dependencies**

*Changed in v0.4*

Data type:list.The js filename collections for a chart's dependencies.Every element do not contain the filename extension(.js).E.g `{'echarts.min', 'fujian'}` .

> In previous v0.4, the js_dependencies returns a unordered set.


### Methods

**add()**

Add options and data to a chart.See the source code for more detail.

| Chart Class | Function Sign                            |
| ----------- | ---------------------------------------- |
| Base        | `add(**echarts_options)`                 |
| Grid        | `add(grid_width=None, grid_height=None, grid_top=None, grid_bottom=None, grid_left=None, grid_right=None)` |
| Overlap     | `add(chart, xaix_index=0, yaix_index=0, id_add_xaxis=False, is_add_yaxis=False)` |
| Timeline    | `add(chart, time_point)`                 |
| Page        | `add(achart_or_charts)`                  |

**get_js_dependencies()**

Gert the javascript dependencies of a chart.

**render(path='render.html')**

Render to a HTML page.

**render_embed()**

Render javascript code fragment including options.

**print_echarts_options()**

Print all options of charts.The new alias form `show_config`.

**show_config()**

Print all options of charts.From v0.3.3,this method has been deprecated and use `print_echarts_options` instead.

## Multiple Chart

`pyecharts.custom.page.Page` is used to show multiple chart in a html page,which includes properties and methods above.

Also, `Page` inherits built-in `list` and len,iter,index,splice,append,extend are supported.

Example,print the option for each chart in a page object.

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



## Data Hanlder Methods

These methods are tool methods for data handlers.

**cast**

`pyecharts.base.Base.cast(seq)`

Class method for formatting and converting data.It can convert your origin data to the corresponding data for pyecharts library.

Example:

```python
o_data = [('A', '34'), ('B', '45'), ('C', '12')]
x, y = Base.cast(o_data)
print(x) # ['A', 'B', 'C']
print(y) # ['34', '45', '12']
```

**json_dumps**

`pyecharts.utils.json_dumps(data, indent=0)`

Convert *data* to json string, and add encoding for some specified data type:

- Convert Datetime and Time objects to ISO8601 format string.
- Cast numpy arrays. See the document of  [astype](https://docs.scipy.org/doc/numpy/reference/generated/numpy.ndarray.astype.html) and [tolist](https://docs.scipy.org/doc/numpy/reference/generated/numpy.ndarray.tolist.html) .

## Template Engine

### Overview

*pyecharts* use  [Jinja2](http://jinja.pocoo.org/)  as its template engine, with some extra template functions.

> *Tempate function* and *template tag* is the same feature in the area of template engine.In Django it is called *template tag* and it is called *template function* in jinja2.

### Engine Class

`pyecharts.engine` module defines some engine class, which inherit from `jinja2.Environment`.Each class has different use case.

**BaseEnvironment**

`pyecharts.engine.BaseEnvironment`

This class is the basic engine in pyecharts,and it inherits  `jinja2.Environment` .It has the following extra features:

- Add *pyecharts_config* attribute, it is a `PyEchartsConfig` object.
- Add  `echarts_*`  template functions

This class can be used for integration with web framework.

**EChartsEnvironment**

`pyecharts.engine.EChartsEnvironment`

EChartsEnvironment class inherits  `BaseEnvironment` .And it use `pyecharts_config.echarts_template_dir` as the default value of template folder. 

This class should not be used in web integration because of overwriting the default behavior of template file loader.

**ECHAERTS_TEMPLATE_FUNCTIONS**

`pyecharts.engine.ECHAERTS_TEMPLATE_FUNCTIONS`

The dictionary containing template functions.It can be used in web integration.

### 模板函数

 pyecharts contains some template functions, which receives a or some  `Chart`  /  `Page`  objects as its parameter.See the following table.

| Function Name/Function Sign   | F(chart) | F(page) | F(chart1,chart2,...)/F(*page) |
| ----------------------------- | -------- | ------- | ----------------------------- |
| echarts_js_dependencies       | ✓        | ✓       | ✓                             |
| echarts_js_dependencies_embed | ✓        | ✓       | ✓                             |
| echarts_container             | ✓        |         |                               |
| echarts_js_content            | ✓        | ✓       | ✓                             |
| echarts_js_content_wrap       | ✓        | ✓       | ✓                             |



**echarts_js_dependencies**

`pyecharts.template.echarts_js_dependencies(*args)`

Render script html nodes with internal embed mode or enternal link.The mode will follow this table.

Internal Embed(IE)

```html
<script type="text/javascript">
    var a = 1;
    console.log(a):
</script>
```

Enternal Link(EL)

```html
<script type="text/javascript" src="/static/js/echarts.min.js"></script>
```

Which mode is used is determined by the `PyEchartsConfig.jshost` and  `PyEchartsConfig.force_js_embed` .See this table.

| Value                                    | local/remote | script mode | Use Case                  | Remark                |
| ---------------------------------------- | ------------ | ----------- | ------------------------- | --------------------- |
| `/template/js/echarts`                   | local        | IE          | Generate one file locally | Default value         |
| `'https://chfw.github.io/jupyter-echarts/echarts'` | remote       | IE          | Generate on file          | switch using `online` |
| Other Local Host (E.g. `/static/js`)                  | local        | EL          | Integrate with Web        |                       |
| Other Remote Host(E.g. `hthttps://cdn.bootcss.com/echarts/3.7.2`) | remote       | EL          | Use remote JS             |                       |

Example

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

Render script nodes in internal embed mode.Only support local host.

**echarts_container**

`pyecharts.template.echarts_container(chart)`

Render the html node of container,output  `<div></div>` element.

Example

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

Render the js initial code fragment without the  `<script></script>` .

**echarts_js_content_wrap**

`pyecharts.template.echarts_js_content_wrap(*args)`

Render the js initial code fragment with the  `<script></script>` .

### Example

This is a full example.

The pythonfile:demo.py

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

The template file:demo.html

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

