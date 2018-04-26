> Translator 篇：pyecharts-javascripthon 的接口和原理

## 概述

[pyecharts-javascripthon](https://github.com/pyecharts/pyecharts-javascripthon) 封装了底层的 Python-To-Javascript 的语言翻译器。

由于 Javascripthon 要求 Python 的版本至少为 3.5+ 而 pyecharts 用户是 python 2.7, 3.4, 3.5 和 3.6, pyecharts-javascripthon 采用了双轨制：python 3.5+ 用户直接用 Javascripthon；python 2.7 和 3.4 的用户调用网络翻译服务 (software as a service)。同时，希望大家支持这个网络服务的运营费用。

## 版本依赖



## 翻译器

翻译器定义在 `pyecharts_javascripthon.api` 模块中。

### 翻译状态机

### 结果数据结构



## 模拟对象(dummy objects)

这些 API 定义了 Javascript 的一些函数和对象的适配。

## 使用规范

这些函数或类应当使用

- 以原名方式引入
- 以函数或类名方式引入

比如下列两种引入方式都是错误的。

使用了别名引用

```python
from pyecharts_javascripthon.dom import Date as JDate
```

以模块方式引入

```python
from pyecharts_javascripthon import dom
```



### DOM 对象

[Date](https://www.w3schools.com/jsref/jsref_obj_date.asp), [Math](https://www.w3schools.com/jsref/jsref_obj_math.asp), [JSON](https://www.w3schools.com/jsref/jsref_obj_json.asp), [window](https://www.w3schools.com/jsref/obj_window.asp), [Document](https://www.w3schools.com/jsref/dom_obj_document.asp), [console](https://www.w3schools.com/jsref/obj_console.asp), [screen](https://www.w3schools.com/jsref/obj_screen.asp)

```
from pyecharts_javascripthon.dom import window    # for window object
from pyecharts_javascripthon.dom import Document  # for Document object
from pyecharts_javascripthon.dom import Date      # for Date object
```

### 全局函数

```
from pyecharts_javascripthon.dom import alert    # provide alert dialog to the user
```