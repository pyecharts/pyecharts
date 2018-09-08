> Translator 篇：pyecharts.javascripthon 的接口和原理

## 概述

> 从 v0.6.0 开始，[pyecharts-javascripthon](https://github.com/pyecharts/pyecharts-javascripthon) 将合并入主代码库，原有代码不再维护。 

pyecharts.javascripthon 封装了底层的 Python-To-Javascript 的语言翻译器。

## 翻译器

pyecharts.javascripthon 封装了一个 Python-To-Javascript 语言翻译器，定义在 `pyecharts.javascripthon.api` 模块。 


- `EChartsTranslator`  --> `TranslateResult`：公共 API 类，提供对外接口，该类本身不处理具体 translate 工作，调用两个组件 translator，并将结果进行组装。
- `JSONTranslator` --> `str`：将 Python 字典翻译成 一个JS 代码段字符串（当含有函数是不再是有效的 JSON 字符串），另外提供了一个回调接口`post_encode_func(func, func_encoded)`：用于当 json 在 encode 完一个函数对象后调用。
- `FunctionTranslator` --> `FunctionStore`：将若干个函数对象翻译成对应的 JS 代码片段。


### EChartsTranslator

该类是翻译器的核心类，包含了一个方法 `translate`。接口如下

```python
class EChartsTranslator:
    def translate(self, options: dict) -> JavascriptSnippet
        pass
```

### JavascriptSnippet & FunctionSnippet

这两个类描述了 js 代码片段的数据结构，接口定义如下：

```python
class FunctionSnippet(OrderedDict):
    def to_js_snippet(self) -> six.text_type
        pass

class JavascriptSnippet:
    def __init__(self, function_snippet: FunctionSnippet, option_snippet: six.text_type):
        pass
    def to_js_snippet(self) -> six.text_type
        pass
```

各自在展开之后代码的位置如下：

```js

var myChart_09de949b428d4e5db7782a12a7541e35 = echarts.init(document.getElementById('09de949b428d4e5db7782a12a7541e35'), null, {renderer: 'canvas'});

// FunctionSnippet 片段开始
function on_click() {
    alert("\u70b9\u51fb\u4e8b\u4ef6\u89e6\u53d1");
}
function label_formatter(params) {
    return (params.value + " [Good!]");
}
// FunctionSnippet 片段结束

var option_09de949b428d4e5db7782a12a7541e35 = {
  // 省略
}; // options_snippet 片段
myChart_09de949b428d4e5db7782a12a7541e35.setOption(option_09de949b428d4e5db7782a12a7541e35);

myChart_09de949b428d4e5db7782a12a7541e35.on("click", on_click);
```


## 模拟对象(dummy objects)

这些 API 定义了 Javascript 的一些函数和对象的适配，这些函数和对象只作声明之用。

### 使用规范

这些函数或类应当使用

- 以原名方式引入
- 以函数或类名方式引入

比如下列两种引入方式都是**错误**的。

使用了别名引用

```python
from pyecharts.javascripthon.dom import Date as JDate
```

以模块方式引入

```python
from pyecharts.javascripthon import dom
```

### DOM 对象

[Date](https://www.w3schools.com/jsref/jsref_obj_date.asp), [Math](https://www.w3schools.com/jsref/jsref_obj_math.asp), [JSON](https://www.w3schools.com/jsref/jsref_obj_json.asp), [window](https://www.w3schools.com/jsref/obj_window.asp), [Document](https://www.w3schools.com/jsref/dom_obj_document.asp), [console](https://www.w3schools.com/jsref/obj_console.asp), [screen](https://www.w3schools.com/jsref/obj_screen.asp)

``` python
from pyecharts.javascripthon.dom import window    # for window object
from pyecharts.javascripthon.dom import Document  # for Document object
from pyecharts.javascripthon.dom import Date      # for Date object
from pyecharts.javascripthon.dom import Math      # for Math module
from pyecharts.javascripthon.dom import JSON      # for JSON module
from pyecharts.javascripthon.dom import screen    # for screen object
from pyecharts.javascripthon.dom import console   # for console object
```

### 全局函数

```python
from pyecharts.javascripthon.dom import alert    # provide alert dialog to the user
```

## 在线翻译 API

项目地址 https://github.com/pyecharts/pyecharts-javascripthon-api-service

pyecharts 开发组为项目提供了一个在线转换的代码的功能，实际上就是把代码 post 到一台支持 metapensiero.pj 运行环境的服务器，再将转换后的代码返回。[pyecharts-javascripthon-api-service](https://github.com/pyecharts/pyecharts-javascripthon-api-service) 承担了这部分的工作，现已将该项目部署到了 [Heroku](https://www.heroku.com/)。

用户多了的话呢，免费资源会耗尽。如果想部署到自己服务器的开发者可以参考项目给出的 [文档](https://github.com/pyecharts/pyecharts-javascripthon-api-service/blob/master/README.md) 来操作。
