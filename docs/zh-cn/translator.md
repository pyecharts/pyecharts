> Translator 篇：支持使用 ECharts 图表配置回调函数

## 概述

[pyecharts-javascripthon](https://github.com/pyecharts/pyecharts-javascripthon) 引入了一个简单的 Python3.5+ 到 Javascript 的语言翻译器：[javascripthon](https://pypi.python.org/pypi/javascripthon)。它能够翻译 Python 中大部分的核心语义。使用 Javascription 翻译后的 Javascript 代码具有良好的可读性。

在翻译的过程中，Javascripthon 尽可能使用 ES6 构建，以保证具有更好的跨浏览器和跨平台。

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

```javascript
function add(x, y) {
    return (x + y);
}
```

## 安装

由于 Javascripthon 要求 Python 的版本至少为 3.5+ 而 pyecharts 用户是 python 2.7, 3.4, 3.5 和 3.6, pyecharts-javascripthon 采用了双轨制：python 3.5+ 用户直接用 Javascripthon；python 2.7 和 3.4 的用户调用网络翻译服务 (software as a service)。同时，希望大家支持这个网络服务的运营费用。

```shell
$ pip install pyecharts-javascripthon 
```

## 使用

pyecharts 已经封装了底层相关逻辑，对使用者是透明的。因此你可以像之前一样的使用。将回函函数对象通过 `add` 方法赋值到 echarts 配置字典中，这里的回调函数需满足以下条件之一：

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
bar.add(
    "precipitation",
    attr,
    v1,
    is_label_show=True,
    label_formatter=label_formatter
)
bar.render()

```

> 回调函数格式参考自 [series[i]-bar.label.formatter](http://echarts.baidu.com/option.html#series-bar.label.formatter) 。

效果图

![bar_with_callback](https://user-images.githubusercontent.com/9875406/38666230-07c1aa66-3e71-11e8-9e9f-43fb7d707a64.png)

##  注意

1. pyecharts 并不会检查 echarts 图表配置选项是否支持回调函数，关于这一部分可参考 ECharts 文档。

这里指的是，options 参数本身是否支持回调函数，比如
```python
def my_title():
    return 'my_title'
bar.add(my_title, [], [])
```
在 pyecharts 并不会出现渲染上的错误，但不符合 Echarts 中对 title 的要求.

2. 为了提高性能，pyecharts 作了以下几点处理：

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