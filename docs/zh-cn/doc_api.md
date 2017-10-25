# pyecharts 文档-API 篇

本文档描述了 pyecharts 库一些公开的 API，以供开发者之使用。

## 图表类

图表类是 pyecharts 库中最为核心的内容，每一个类代表了[Echarts](http://echarts.baidu.com/) 中一个图表类型。下表显示了这些图表的继承体系。

![class-relationship-diagram](https://github.com/chenjiandongx/pyecharts/blob/master/images/class-relationship-diagram.png)
### 属性

图表类和属性表如下：

| 属性/图表        | Base | Chart/FOO_CHART | Grid | Overlap | Timeline | Page |
| --------------- | ---- | --------------- | ---- | ------- | -------- | ---- |
| chart_id        | ✓    | ✓               | ✓    | ✓       | ✓        |      |
| width           | ✓    | ✓               | ✓    | ✓       | ✓        |      |
| heigth          | ✓    | ✓               | ✓    | ✓       | ✓        |      |
| options         | ✓    | ✓               | ✓    | ✓       | ✓        |      |
| js_dependencies | ✓    | ✓               | ✓    | ✓       | ✓        | ✓    |
| charts          |      |                 |      |         |          | ✓    |

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
| Base     | `add(**echarts_options)`           |
| Grid     | `add(grid_width=None, grid_height=None, grid_top=None, grid_bottom=None, grid_left=None, grid_right=None)` |
| Overlap  | `add(chart, xaix_index=0, yaix_index=0, id_add_xaxis=False, is_add_yaxis=False)` |
| Timeline | `add(chart, time_point)`           |
| Page     | `add(achart_or_charts)`            |

**get_js_dependencies()**

获取 js 依赖文件列表。和 属性 *js_dependencies* 不同， 这里的元素是包含了文件完整路径。

**render(path='render.html')**

渲染至指定的 HTML 页面，不同图表类型使用默认的模板文件。

**render_embed()**

渲染包含选项的 js 代码。

**show_config()**

打印全部 options 属性。

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