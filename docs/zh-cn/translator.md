> Translator 篇：ECharts 图表配置回调函数支持

## 概述

[javascripthon](https://pypi.python.org/pypi/javascripthon) 是一个简单的 Python3.5 到 Javascript 的语言翻译器，它能够翻译 Python 中大部分的核心语义。使用 Javascription 翻译后的 Javascript 代码具有良好的可读性。

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
function add(x, y){
    return (x + y);
}
```

## 安装

Javascripthon 要求 Python 的版本至少在 3 .5 以上，可以使用以下方式安装。

```shell
pip install Javascripthon 
```

> javascripthon 目前在 Windows  平台上可能无法正确安装。

可以使用以下代码验证当前环境是否可以使用 Function Translate 功能。

```shell
>>>from pyecharts.translator.compat import TranslatorCompatAPI
>>>TranslatorCompatAPI.check_enabled()
True
```

## 使用

pyecharts 已经封装了底层相关逻辑，对使用者是透明的。因此你可以像之前一样的使用。将回函函数对象通过 `add` 方法赋值到 echarts 配置字典中，这里的回调函数需满足以下条件之一：

- 使用 `def` 定义的命名函数
- `lambda` 表达式 

例子：

```python
from pyecharts import Bar

def label_formatter(params):
    return params.name + 'abc'

attr = ["Jan", "Feb"]
v1 = [2.0, 4.9]
bar = Bar("Bar chart", "precipitation and evaporation one year")
bar.add("precipitation", attr, v1, label_formatter=label_formatter)
bar.render()
```

如果 `TranslatorCompatAPI.check_enabled()` 无法通过，上述 `render` 函数将抛出 `FunctionTranslatorDisabled` 异常。

##  注意

第一，pyecharts 并不会检查 echarts 图表配置选项是否支持回调函数，关于这一部分可参考 ECharts 文档。

第二，为了提高性能，pyecharts 作了以下几点处理：

- 函数翻译的实际执行是在 `render` 函数调用时，而不是 `add` 函数
- 对已经翻译完成的函数以 **函数名** 为索引进行缓存。

因此应当避免同一个函数名多用，以下的情况可能无法获得预期的效果。

```python
from pyecharts import Bar

def label_formatter(params):
    return params.name + 'abc'

attr = ["Jan", "Feb"]
v1 = [2.0, 4.9]
bar = Bar("Bar chart", "precipitation and evaporation one year")
bar.add("precipitation", attr, v1, label_formatter=label_formatter)
bar.render()

def label_formatter(params):
    return params.name + 'test'

bar2 = Bar("Bar chart", "precipitation and evaporation one year")
bar2.add("precipitation", attr, v1, label_formatter=label_formatter)
bar2.render()
```





