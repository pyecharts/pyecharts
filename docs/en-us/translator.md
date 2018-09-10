> Translator Part: Interfaces and Principles of `pyecharts.javascripthon`

## Overview

> From v0.6.0, [pyecharts-javascripthon](https://github.com/pyecharts/pyecharts-javascripthon) will merge into main code library, the original code will not be maintained. 

`pyecharts.javascripthon` encapsulates the underlying Python-To-Javascript language translator.

## Translator

pyecharts.javascripthon encapsulates a Python-To-Javascript language translator, defined in `pyecharts.javascripthon.api` module.


- `EChartsTranslator`  --> `TranslateResult`:   
    Public API class that provides an external interface that does not handle the specific translate work itself. It calls two component translators, and assembles the results.

- `JSONTranslator` --> `str`：  
    Translate a Python dictionary into a JS snippet string (when a function is no longer a valid JSON string). In addition, we provide a callback interface`post_encode_func(func, func_encoded)`, which is called when `JSONTranslator` finish encoding a function object.

- `FunctionTranslator` --> `FunctionStore`：  
    Translate several function objects into corresponding JS code snippets.


### EChartsTranslator

This class is the core class of the translator and contains a method `translate`. Interface is as follows

```python
class EChartsTranslator:
    def translate(self, options: dict) -> JavascriptSnippet
        pass
```

### JavascriptSnippet & FunctionSnippet

These two classes describe the data structure of the js code snippet. The interface is defined as follows:

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

The location of the code after each expansion is as follows:

```js

var myChart_09de949b428d4e5db7782a12a7541e35 = echarts.init(document.getElementById('09de949b428d4e5db7782a12a7541e35'), null, {renderer: 'canvas'});

// FunctionSnippet starts
function on_click() {
    alert("\u70b9\u51fb\u4e8b\u4ef6\u89e6\u53d1");
}
function label_formatter(params) {
    return (params.value + " [Good!]");
}
// FunctionSnippet ends

var option_09de949b428d4e5db7782a12a7541e35 = {
  // omit
}; // options_snippet snippet
myChart_09de949b428d4e5db7782a12a7541e35.setOption(option_09de949b428d4e5db7782a12a7541e35);

myChart_09de949b428d4e5db7782a12a7541e35.on("click", on_click);
```


## Dummy objects

These APIs define the adaptation of some of Javascript's functions and objects, which are used only for declaration purposes.

### Terms of usage

These functions or classes should be used by

- introduced in the original name
- introduced as a function or class name

For example, the following two introduction methods are all **error**.

Alias ​​introduce

```python
from pyecharts.javascripthon.dom import Date as JDate
```

Module introduce

```python
from pyecharts.javascripthon import dom
```

### DOM object

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

### Global function

```python
from pyecharts.javascripthon.dom import alert    # provide alert dialog to the user
```

## Online translator API

Project url  https://github.com/pyecharts/pyecharts-javascripthon-api-service

pyecharts development team provides the project with an online conversion code function, which is actually to post the code to a server that supports the `metapensiero.pj` running environment, and could return the converted code.  
[pyecharts-javascripthon-api-service](https://github.com/pyecharts/pyecharts-javascripthon-api-service) undertook this work. And the project has now been deployed on [Heroku](https://www.heroku.com/)。

If there are too many users, free resources will be exhausted. If you want to deploy to your own server, please refer to the [documentation](https://github.com/pyecharts/pyecharts-javascripthon-api-service/blob/master/README.md) given by the project .
